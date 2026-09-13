from __future__ import annotations

import os
from datetime import datetime
from typing import Any

from repositories.runtime import ensure_campaign_session, record_event, upsert_scene_run
from domain.engine import RunSnapshot, RunState
from domain.schema import Choice


APP_VERSION = os.environ.get("VDA_APP_VERSION") or os.environ.get("GIT_COMMIT_SHA")


def now_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def _serialize_choices(choices: Any) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for choice in list(choices or []):
        if hasattr(choice, "model_dump"):
            out.append(choice.model_dump(mode="json"))
        else:
            out.append({"id": getattr(choice, "id", None), "label": getattr(choice, "label", None)})
    return out


def _serialize_snapshot(snapshot: Any) -> dict[str, Any]:
    return {
        "active_choices": _serialize_choices(getattr(snapshot, "active_choices", [])),
        "transcript": [list(item) for item in list(getattr(snapshot, "transcript", []) or [])],
        "last_answer_md": getattr(snapshot, "last_answer_md", "") or "",
        "history_labels": list(getattr(snapshot, "history_labels", []) or []),
        "ended": bool(getattr(snapshot, "ended", False)),
    }


def serialize_run_state(run_state: Any) -> dict[str, Any]:
    return {
        "active_choices": _serialize_choices(getattr(run_state, "active_choices", [])),
        "transcript": [list(item) for item in list(getattr(run_state, "transcript", []) or [])],
        "last_answer_md": getattr(run_state, "last_answer_md", "") or "",
        "history_labels": list(getattr(run_state, "history_labels", []) or []),
        "ended": bool(getattr(run_state, "ended", False)),
        "allow_undo": bool(getattr(run_state, "allow_undo", True)),
        "allow_restart_after_choice": bool(getattr(run_state, "allow_restart_after_choice", True)),
        "undo_stack": [
            _serialize_snapshot(item)
            for item in list(getattr(run_state, "undo_stack", []) or [])
        ],
    }


def _restore_choices(raw: Any) -> list[Choice]:
    return [Choice.model_validate(item) for item in list(raw or []) if isinstance(item, dict)]


def deserialize_run_state(scene_id: str, data: dict[str, Any]) -> RunState:
    rs = RunState(
        scene_id=scene_id,
        active_choices=_restore_choices(data.get("active_choices")),
        transcript=[tuple(item) for item in list(data.get("transcript") or []) if isinstance(item, (list, tuple)) and len(item) == 2],
        last_answer_md=str(data.get("last_answer_md") or ""),
        history_labels=[str(item) for item in list(data.get("history_labels") or [])],
        ended=bool(data.get("ended", False)),
        allow_undo=bool(data.get("allow_undo", True)),
        allow_restart_after_choice=bool(data.get("allow_restart_after_choice", True)),
    )
    stack: list[RunSnapshot] = []
    for item in list(data.get("undo_stack") or []):
        if not isinstance(item, dict):
            continue
        stack.append(
            RunSnapshot(
                active_choices=_restore_choices(item.get("active_choices")),
                transcript=[tuple(row) for row in list(item.get("transcript") or []) if isinstance(row, (list, tuple)) and len(row) == 2],
                last_answer_md=str(item.get("last_answer_md") or ""),
                history_labels=[str(row) for row in list(item.get("history_labels") or [])],
                ended=bool(item.get("ended", False)),
            )
        )
    rs.undo_stack = stack
    return rs


def persist_scene_run(
    *,
    run_id: str,
    scene_id: str,
    run_state: Any,
    started_at: str,
    status: str = "open",
    ended_at: str | None = None,
) -> dict[str, Any]:
    session = ensure_campaign_session(app_version=APP_VERSION)
    row = {
        "id": run_id,
        "session_id": session["id"],
        "scene_id": scene_id,
        "delivery_mode": None,
        "intended_character_ref": None,
        "started_at": started_at,
        "ended_at": ended_at,
        "status": status,
        "current_state": serialize_run_state(run_state),
        "source_app_version": APP_VERSION,
    }
    return upsert_scene_run(row)


def scene_opened(
    *,
    run_id: str,
    scene: Any,
    run_state: Any,
    started_at: str,
) -> None:
    scene_id = str(getattr(scene, "id", ""))
    title = str(getattr(scene, "title", scene_id))
    session = ensure_campaign_session(app_version=APP_VERSION)
    record_event(
        "scene_opened",
        session_id=session["id"],
        scene_ref=scene_id,
        payload={"run_id": run_id, "title": title},
        source_app_version=APP_VERSION,
    )
    persist_scene_run(
        run_id=run_id,
        scene_id=scene_id,
        run_state=run_state,
        started_at=started_at,
    )


def scene_content_shown(
    *,
    run_id: str,
    scene_id: str,
    transcript_index: int,
    content_md: str,
) -> None:
    """Persist content only after the Streamlit render path completed."""
    session = ensure_campaign_session(app_version=APP_VERSION)
    record_event(
        "scene_content_shown",
        session_id=session["id"],
        scene_ref=scene_id,
        payload={
            "run_id": run_id,
            "content_kind": "transcript_bot",
            "transcript_index": transcript_index,
            "content_md": content_md,
        },
        source_app_version=APP_VERSION,
    )


def scene_restarted(
    *,
    previous_run_id: str | None,
    scene_id: str,
) -> None:
    session = ensure_campaign_session(app_version=APP_VERSION)
    record_event(
        "scene_restarted",
        session_id=session["id"],
        scene_ref=scene_id,
        payload={"previous_run_id": previous_run_id},
        source_app_version=APP_VERSION,
    )


def scene_choice_selected(
    *,
    run_id: str,
    scene_id: str,
    choice: Any,
    run_state: Any,
    started_at: str,
) -> None:
    session = ensure_campaign_session(app_version=APP_VERSION)
    choice_id = str(getattr(choice, "id", ""))
    label = str(getattr(choice, "label", ""))
    record_event(
        "scene_choice_selected",
        session_id=session["id"],
        scene_ref=scene_id,
        payload={"run_id": run_id, "choice_id": choice_id, "label": label},
        source_app_version=APP_VERSION,
    )
    ended = bool(getattr(run_state, "ended", False))
    ended_at = now_iso() if ended else None
    persist_scene_run(
        run_id=run_id,
        scene_id=scene_id,
        run_state=run_state,
        started_at=started_at,
        status="finished" if ended else "open",
        ended_at=ended_at,
    )
    if ended:
        record_event(
            "scene_finished",
            session_id=session["id"],
            scene_ref=scene_id,
            payload={"run_id": run_id},
            source_app_version=APP_VERSION,
        )


def scene_choice_undone(
    *,
    run_id: str,
    scene_id: str,
    run_state: Any,
    started_at: str,
) -> None:
    session = ensure_campaign_session(app_version=APP_VERSION)
    record_event(
        "scene_choice_undone",
        session_id=session["id"],
        scene_ref=scene_id,
        payload={"run_id": run_id},
        source_app_version=APP_VERSION,
    )
    persist_scene_run(
        run_id=run_id,
        scene_id=scene_id,
        run_state=run_state,
        started_at=started_at,
    )


def scene_abandoned(
    *,
    run_id: str,
    scene_id: str,
    run_state: Any,
    started_at: str,
) -> None:
    session = ensure_campaign_session(app_version=APP_VERSION)
    ended_at = now_iso()
    record_event(
        "scene_abandoned",
        session_id=session["id"],
        scene_ref=scene_id,
        payload={"run_id": run_id},
        source_app_version=APP_VERSION,
    )
    persist_scene_run(
        run_id=run_id,
        scene_id=scene_id,
        run_state=run_state,
        started_at=started_at,
        status="abandoned",
        ended_at=ended_at,
    )
