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

    # Une scène marquée irréversible est ajoutée ici dès son premier choix.
    # Ce verrou survit aux retours à l'accueil et aux changements de scène
    # pendant la session Streamlit courante.
    sealed_scene_ids: set[str] = field(default_factory=set)

    last_error: Optional[str] = None


STATE_KEY = "VDA_APP_STATE_V1"


def get_state() -> AppState:
    if STATE_KEY not in st.session_state:
        st.session_state[STATE_KEY] = AppState()
    state = st.session_state[STATE_KEY]
    # Compatibilité avec une session ouverte avant l'ajout du verrou.
    if not hasattr(state, "sealed_scene_ids"):
        state.sealed_scene_ids = set()
    return state


def set_state(state: AppState) -> None:
    st.session_state[STATE_KEY] = state
