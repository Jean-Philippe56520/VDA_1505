from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional

import streamlit as st

from domain.engine import RunState


class Screen(str, Enum):
    HOME = "HOME"
    SCENE = "SCENE"


@dataclass
class AppState:
    screen: Screen = Screen.HOME

    active_scene_id: Optional[str] = None
    scene_intro_md: str = ""
    run_state: Optional[RunState] = None

    last_error: Optional[str] = None


STATE_KEY = "VDA_APP_STATE_V1"


def get_state() -> AppState:
    if STATE_KEY not in st.session_state:
        st.session_state[STATE_KEY] = AppState()
    return st.session_state[STATE_KEY]


def set_state(state: AppState) -> None:
    st.session_state[STATE_KEY] = state
