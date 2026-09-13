from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, Tuple

from domain.loader import load_scenes as load_local_scenes
from domain.schema import Scene
from infrastructure.supabase_client import get_supabase_client
from repositories.runtime import RUNTIME_DIR


DEFAULT_SNAPSHOT_PATH = RUNTIME_DIR / "runtime_snapshot.json"


def scene_backend() -> str:
    backend = os.environ.get("VDA_SCENE_BACKEND", "local").strip().lower()
    return backend if backend in {"local", "supabase", "hybrid", "snapshot"} else "local"


def _snapshot_path() -> Path:
    configured = os.environ.get("VDA_RUNTIME_SNAPSHOT")
    return Path(configured) if configured else DEFAULT_SNAPSHOT_PATH


def _module_name(delivery_mode: str, scene_id: str, source: str) -> str:
    if delivery_mode == "individual":
        return f"private:{source}:{scene_id}"
    return f"{source}:{scene_id}"


def _rows_to_scenes(rows: list[dict]) -> Dict[str, Tuple[str, Scene]]:
    scenes: Dict[str, Tuple[str, Scene]] = {}
    for row in rows:
        if not isinstance(row, dict) or not row.get("scene_id"):
            continue
        payload = row.get("payload")
        if not isinstance(payload, dict):
            continue
        scene = Scene.model_validate(payload)
        scene_id = str(row["scene_id"])
        if scene.id != scene_id:
            raise ValueError(
                f"Scene id mismatch in published data: row={scene_id!r}, payload={scene.id!r}"
            )
        if scene_id in scenes:
            raise ValueError(f"Duplicate published scene id: {scene_id}")
        delivery_mode = str(row.get("delivery_mode") or "group")
        source = str(row.get("source_kind") or "runtime")
        scenes[scene_id] = (_module_name(delivery_mode, scene_id, source), scene)
    return scenes


def load_supabase_scenes() -> Dict[str, Tuple[str, Scene]]:
    client = get_supabase_client()
    if client is None:
        return {}
    response = (
        client.table("published_scenes")
        .select("scene_id,title,delivery_mode,payload,source_kind,enabled")
        .eq("enabled", True)
        .execute()
    )
    rows = list(getattr(response, "data", None) or [])
    return _rows_to_scenes(rows)


def load_snapshot_scenes() -> Dict[str, Tuple[str, Scene]]:
    path = _snapshot_path()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return {}
    rows = data.get("scenes", []) if isinstance(data, dict) else []
    return _rows_to_scenes(rows if isinstance(rows, list) else [])


def load_scenes() -> Dict[str, Tuple[str, Scene]]:
    """Load scenes without making connectivity a table-session dependency.

    local is the default until the migration is explicitly activated. When
    Supabase is selected, failure falls back to the last snapshot and finally
    to the existing Python modules so a physical session can continue offline.
    """
    backend = scene_backend()
    if backend == "local":
        return load_local_scenes()
    if backend == "snapshot":
        return load_snapshot_scenes() or load_local_scenes()
    if backend == "hybrid":
        combined = load_local_scenes()
        try:
            combined.update(load_supabase_scenes())
        except Exception:
            pass
        return combined

    try:
        remote = load_supabase_scenes()
        if remote:
            return remote
    except Exception:
        pass

    snapshot = load_snapshot_scenes()
    if snapshot:
        return snapshot
    return load_local_scenes()


def export_snapshot(
    scenes: Dict[str, Tuple[str, Scene]] | None = None,
    *,
    git_sha: str | None = None,
    destination: Path | None = None,
) -> Path:
    scenes = scenes or load_local_scenes()
    rows = []
    for scene_id, (module_name, scene) in sorted(scenes.items()):
        individual = str(module_name).startswith("private:")
        rows.append(
            {
                "scene_id": scene_id,
                "title": scene.title,
                "delivery_mode": "individual" if individual else "group",
                "intended_character_ref": None,
                "schema_version": scene.schema_version,
                "payload": scene.model_dump(mode="json"),
                "source_kind": "git",
                "legacy_source_path": module_name,
                "source_git_sha": git_sha,
                "enabled": True,
            }
        )
    document = {
        "schema_version": 1,
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "git_sha": git_sha,
        "scenes": rows,
    }
    path = destination or _snapshot_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temp.replace(path)
    return path


def publish_local_scenes(*, git_sha: str | None = None) -> int:
    client = get_supabase_client()
    if client is None:
        raise RuntimeError("Supabase is not configured")
    scenes = load_local_scenes()
    rows = []
    now = datetime.now().astimezone().isoformat(timespec="seconds")
    for scene_id, (module_name, scene) in sorted(scenes.items()):
        rows.append(
            {
                "scene_id": scene_id,
                "title": scene.title,
                "delivery_mode": (
                    "individual" if str(module_name).startswith("private:") else "group"
                ),
                "intended_character_ref": None,
                "schema_version": scene.schema_version,
                "payload": scene.model_dump(mode="json"),
                "source_kind": "git",
                "legacy_source_path": module_name,
                "source_git_sha": git_sha,
                "published_at": now,
                "enabled": True,
            }
        )
    if rows:
        client.table("published_scenes").upsert(rows, on_conflict="scene_id").execute()
    export_snapshot(scenes, git_sha=git_sha)
    return len(rows)
