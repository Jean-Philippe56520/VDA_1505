from __future__ import annotations

import json
import os
import tempfile
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any

from infrastructure.supabase_client import get_supabase_client, supabase_enabled


RUNTIME_DIR = Path(os.environ.get("VDA_1505_RUNTIME_DIR", Path.home() / ".vda_1505"))
SESSIONS_PATH = RUNTIME_DIR / "campaign_sessions.json"
ACTIVE_SESSION_PATH = RUNTIME_DIR / "active_campaign_session.json"
EVENTS_PATH = RUNTIME_DIR / "runtime_events.ndjson"
SCENE_RUNS_PATH = RUNTIME_DIR / "scene_runs.json"
PENDING_REMOTE_PATH = RUNTIME_DIR / "pending_remote_ops.json"


def _now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def _ensure_runtime_dir() -> None:
    RUNTIME_DIR.mkdir(parents=True, exist_ok=True)


def _read_json(path: Path, default: Any) -> Any:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return default


def _atomic_write_json(path: Path, data: Any) -> None:
    _ensure_runtime_dir()
    fd, temp_name = tempfile.mkstemp(prefix=path.name, suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(data, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        os.replace(temp_name, path)
    except Exception:
        try:
            os.unlink(temp_name)
        except OSError:
            pass
        raise


def _append_ndjson(path: Path, record: dict[str, Any]) -> None:
    _ensure_runtime_dir()
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")))
        handle.write("\n")


def _upsert_local_list(path: Path, record: dict[str, Any], key: str) -> None:
    rows = _read_json(path, [])
    if not isinstance(rows, list):
        rows = []
    target = record.get(key)
    replaced = False
    for index, row in enumerate(rows):
        if isinstance(row, dict) and row.get(key) == target:
            rows[index] = record
            replaced = True
            break
    if not replaced:
        rows.append(record)
    _atomic_write_json(path, rows)


def _upsert_local_map(path: Path, record: dict[str, Any], key: str) -> None:
    rows = _read_json(path, {})
    if not isinstance(rows, dict):
        rows = {}
    target = str(record[key])
    rows[target] = record
    _atomic_write_json(path, rows)


def _queue_remote(table: str, payload: dict[str, Any], on_conflict: str) -> None:
    queue = _read_json(PENDING_REMOTE_PATH, [])
    if not isinstance(queue, list):
        queue = []

    # Stable primary keys make every operation idempotent. Replace an existing
    # pending operation for the same row rather than growing the queue forever.
    identity = payload.get(on_conflict)
    replacement = {
        "table": table,
        "payload": payload,
        "on_conflict": on_conflict,
        "queued_at": _now(),
    }
    for index, item in enumerate(queue):
        if (
            isinstance(item, dict)
            and item.get("table") == table
            and item.get("on_conflict") == on_conflict
            and isinstance(item.get("payload"), dict)
            and item["payload"].get(on_conflict) == identity
        ):
            queue[index] = replacement
            break
    else:
        queue.append(replacement)
    _atomic_write_json(PENDING_REMOTE_PATH, queue)


def _remote_upsert(table: str, payload: dict[str, Any], on_conflict: str) -> bool:
    client = get_supabase_client()
    if client is None:
        raise RuntimeError("Supabase is enabled but the server client is unavailable")
    client.table(table).upsert(payload, on_conflict=on_conflict).execute()
    return True


def _write_remote_best_effort(table: str, payload: dict[str, Any], on_conflict: str) -> bool:
    if not supabase_enabled():
        return False
    try:
        return _remote_upsert(table, payload, on_conflict)
    except Exception:
        _queue_remote(table, payload, on_conflict)
        return False


def flush_pending_remote() -> dict[str, int]:
    """Replay offline writes. The local runtime remains authoritative for V1."""
    queue = _read_json(PENDING_REMOTE_PATH, [])
    if not isinstance(queue, list) or not queue:
        return {"synced": 0, "remaining": 0}
    if not supabase_enabled() or get_supabase_client() is None:
        return {"synced": 0, "remaining": len(queue)}

    remaining: list[dict[str, Any]] = []
    synced = 0
    for item in queue:
        try:
            _remote_upsert(
                str(item["table"]),
                dict(item["payload"]),
                str(item["on_conflict"]),
            )
            synced += 1
        except Exception:
            remaining.append(item)
    _atomic_write_json(PENDING_REMOTE_PATH, remaining)
    return {"synced": synced, "remaining": len(remaining)}


def current_campaign_session() -> dict[str, Any] | None:
    session = _read_json(ACTIVE_SESSION_PATH, None)
    if isinstance(session, dict) and session.get("status") == "open" and session.get("id"):
        return session
    return None


def start_campaign_session(
    *,
    title: str | None = None,
    app_version: str | None = None,
) -> dict[str, Any]:
    current = current_campaign_session()
    if current is not None:
        return current

    session = {
        "id": str(uuid.uuid4()),
        "title": (title or "Séance VDA").strip() or "Séance VDA",
        "status": "open",
        "started_at": _now(),
        "ended_at": None,
        "app_version": app_version,
        "metadata": {},
    }
    _upsert_local_list(SESSIONS_PATH, session, "id")
    _atomic_write_json(ACTIVE_SESSION_PATH, session)
    _write_remote_best_effort("campaign_sessions", session, "id")
    record_event(
        "session_started",
        session_id=session["id"],
        payload={"title": session["title"]},
        source_app_version=app_version,
    )
    return session


def ensure_campaign_session(*, app_version: str | None = None) -> dict[str, Any]:
    current = current_campaign_session()
    if current is not None:
        return current
    return start_campaign_session(app_version=app_version)


def close_campaign_session(*, app_version: str | None = None) -> dict[str, Any] | None:
    session = current_campaign_session()
    if session is None:
        return None
    session = dict(session)
    session["status"] = "closed"
    session["ended_at"] = _now()
    _upsert_local_list(SESSIONS_PATH, session, "id")
    _write_remote_best_effort("campaign_sessions", session, "id")
    record_event(
        "session_closed",
        session_id=session["id"],
        payload={},
        source_app_version=app_version,
    )
    try:
        ACTIVE_SESSION_PATH.unlink()
    except FileNotFoundError:
        pass
    return session


def record_event(
    event_type: str,
    *,
    session_id: str | None = None,
    actor_ref: str | None = None,
    scene_ref: str | None = None,
    payload: dict[str, Any] | None = None,
    source_app_version: str | None = None,
    play_status: str = "unconfirmed",
    consolidation_status: str = "pending",
    event_id: str | None = None,
) -> dict[str, Any]:
    if session_id is None:
        session_id = ensure_campaign_session(app_version=source_app_version)["id"]
    event = {
        "id": event_id or str(uuid.uuid4()),
        "session_id": session_id,
        "event_type": event_type,
        "occurred_at": _now(),
        "actor_ref": actor_ref,
        "scene_ref": scene_ref,
        "payload": payload or {},
        "source_app_version": source_app_version,
        "play_status": play_status,
        "consolidation_status": consolidation_status,
    }
    _append_ndjson(EVENTS_PATH, event)
    _write_remote_best_effort("runtime_events", event, "id")
    return event


def latest_open_scene_run(session_id: str) -> dict[str, Any] | None:
    rows = _read_json(SCENE_RUNS_PATH, {})
    if not isinstance(rows, dict):
        return None
    candidates = [
        row
        for row in rows.values()
        if isinstance(row, dict)
        and row.get("session_id") == session_id
        and row.get("status") == "open"
        and row.get("id")
    ]
    if not candidates:
        return None
    candidates.sort(key=lambda row: str(row.get("started_at") or ""), reverse=True)
    return candidates[0]


def sealed_scene_ids_for_session(session_id: str) -> set[str]:
    rows = _read_json(SCENE_RUNS_PATH, {})
    if not isinstance(rows, dict):
        return set()
    sealed: set[str] = set()
    for row in rows.values():
        if not isinstance(row, dict) or row.get("session_id") != session_id:
            continue
        state = row.get("current_state")
        if not isinstance(state, dict):
            continue
        if state.get("allow_restart_after_choice") is False and state.get("history_labels"):
            scene_id = str(row.get("scene_id") or "").strip()
            if scene_id:
                sealed.add(scene_id)
    return sealed


def logged_transcript_count_for_run(session_id: str, run_id: str) -> int:
    try:
        lines = EVENTS_PATH.read_text(encoding="utf-8").splitlines()
    except OSError:
        return 0
    highest = -1
    for line in lines:
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(event, dict):
            continue
        if event.get("session_id") != session_id or event.get("event_type") != "scene_content_shown":
            continue
        payload = event.get("payload")
        if not isinstance(payload, dict) or payload.get("run_id") != run_id:
            continue
        index = payload.get("transcript_index")
        if isinstance(index, int):
            highest = max(highest, index)
    return highest + 1


def upsert_scene_run(
    run: dict[str, Any],
) -> dict[str, Any]:
    _upsert_local_map(SCENE_RUNS_PATH, run, "id")
    _write_remote_best_effort("scene_runs", run, "id")
    return run


def upsert_hunt_run(run: dict[str, Any]) -> dict[str, Any]:
    _write_remote_best_effort("hunt_runs", run, "draw_id")
    return run
