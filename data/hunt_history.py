from __future__ import annotations

"""Historique local des rencontres de chasse explicitement marquées « Jouée ».

Le fichier local reste le fallback de table et ne remplace jamais 04A. Quand
Supabase est configuré, la même trace est synchronisée comme donnée runtime ;
elle reste non canonique jusqu'à confirmation et consolidation par le MJ.
"""

import json
import os
from pathlib import Path
from typing import Any

from repositories.runtime import ensure_campaign_session, record_event, upsert_hunt_run


RUNTIME_DIR = Path(os.environ.get("VDA_1505_RUNTIME_DIR", Path.home() / ".vda_1505"))
HUNT_HISTORY_PATH = RUNTIME_DIR / "hunt_played.json"
APP_VERSION = os.environ.get("VDA_APP_VERSION") or os.environ.get("GIT_COMMIT_SHA")


def load_played_hunts() -> list[dict[str, Any]]:
    try:
        raw = HUNT_HISTORY_PATH.read_text(encoding="utf-8")
        data = json.loads(raw)
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return []
    if not isinstance(data, list):
        return []
    return [item for item in data if isinstance(item, dict)]


def _sync_runtime(record: dict[str, Any]) -> None:
    try:
        session = ensure_campaign_session(app_version=APP_VERSION)
        run = {
            "session_id": session["id"],
            "draw_id": str(record.get("draw_id")),
            "generated_at": record.get("generated_at"),
            "played_at": record.get("played_at"),
            "play_status": "unconfirmed",
            "payload": record,
            "source_app_version": APP_VERSION,
        }
        upsert_hunt_run(run)
        record_event(
            "hunt_marked_played",
            session_id=session["id"],
            payload=record,
            source_app_version=APP_VERSION,
            play_status="unconfirmed",
        )
    except Exception:
        # The physical session must continue even if remote persistence fails.
        pass


def record_played_hunt(record: dict[str, Any]) -> bool:
    """Persiste une scène une seule fois par draw_id. Retourne True si ajoutée."""
    draw_id = str(record.get("draw_id") or "").strip()
    if not draw_id:
        return False

    history = load_played_hunts()
    if any(str(item.get("draw_id")) == draw_id for item in history):
        return False

    RUNTIME_DIR.mkdir(parents=True, exist_ok=True)
    history.append(record)
    temp_path = HUNT_HISTORY_PATH.with_suffix(".tmp")
    temp_path.write_text(
        json.dumps(history, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    temp_path.replace(HUNT_HISTORY_PATH)
    _sync_runtime(record)
    return True


def is_draw_played(history: list[dict[str, Any]], draw_id: str | None) -> bool:
    if not draw_id:
        return False
    return any(str(item.get("draw_id")) == str(draw_id) for item in history)


def played_count_for_encounter(
    history: list[dict[str, Any]],
    table_id: str,
    point_id: str,
    rencontre: str,
) -> int:
    return sum(
        1
        for item in history
        if item.get("table_id") == table_id
        and item.get("point_id") == point_id
        and item.get("rencontre") == rencontre
    )
