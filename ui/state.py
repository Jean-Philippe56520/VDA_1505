from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

import streamlit as st

from domain.engine import RunState


class Screen(str, Enum):
    HOME = "HOME"
    PRIVATE_SCENES = "PRIVATE_SCENES"
    SCENE = "SCENE"


@dataclass
class AppState:
    screen: Screen = Screen.HOME

    active_scene_id: Optional[str] = None
    scene_intro_md: str = ""
    run_state: Optional[RunState] = None

    # Runtime identifiers are operational only. They never make an event canon.
    active_scene_run_id: Optional[str] = None
    active_scene_started_at: Optional[str] = None
    runtime_logged_transcript_count: int = 0

    # Une scène marquée irréversible est ajoutée ici dès son premier choix.
    # Ce verrou survit aux retours à l'accueil et aux changements de scène
    # pendant la session Streamlit courante.
    sealed_scene_ids: set[str] = field(default_factory=set)

    last_error: Optional[str] = None


STATE_KEY = "VDA_APP_STATE_V2"
LEGACY_STATE_KEY = "VDA_APP_STATE_V1"


def get_state() -> AppState:
    if STATE_KEY not in st.session_state:
        legacy = st.session_state.get(LEGACY_STATE_KEY)
        if legacy is not None:
            # Preserve an already-open Streamlit session while adding V2 fields.
            if not hasattr(legacy, "active_scene_run_id"):
                setattr(legacy, "active_scene_run_id", None)
            if not hasattr(legacy, "active_scene_started_at"):
                setattr(legacy, "active_scene_started_at", None)
            if not hasattr(legacy, "runtime_logged_transcript_count"):
                setattr(legacy, "runtime_logged_transcript_count", 0)
            st.session_state[STATE_KEY] = legacy
        else:
            restored = AppState()
            try:
                from repositories.runtime import (
                    current_campaign_session,
                    latest_open_scene_run,
                    logged_transcript_count_for_run,
                    sealed_scene_ids_for_session,
                )
                from services.runtime import deserialize_run_state

                session = current_campaign_session()
                if session is not None:
                    session_id = str(session["id"])
                    restored.sealed_scene_ids = sealed_scene_ids_for_session(session_id)
                    row = latest_open_scene_run(session_id)
                    if row is not None and isinstance(row.get("current_state"), dict):
                        scene_id = str(row.get("scene_id") or "")
                        run_id = str(row.get("id") or "")
                        if scene_id and run_id:
                            restored.active_scene_id = scene_id
                            restored.active_scene_run_id = run_id
                            restored.active_scene_started_at = str(row.get("started_at") or "") or None
                            restored.run_state = deserialize_run_state(scene_id, row["current_state"])
                            restored.runtime_logged_transcript_count = logged_transcript_count_for_run(
                                session_id, run_id
                            )
            except Exception:
                # Local recovery is best-effort; an unreadable runtime journal must
                # never prevent the table application from starting.
                restored = AppState()
            st.session_state[STATE_KEY] = restored
    state = st.session_state[STATE_KEY]
    if not hasattr(state, "sealed_scene_ids"):
        state.sealed_scene_ids = set()
    if not hasattr(state, "active_scene_run_id"):
        state.active_scene_run_id = None
    if not hasattr(state, "active_scene_started_at"):
        state.active_scene_started_at = None
    if not hasattr(state, "runtime_logged_transcript_count"):
        state.runtime_logged_transcript_count = 0
    return state


def set_state(state: AppState) -> None:
    st.session_state[STATE_KEY] = state
