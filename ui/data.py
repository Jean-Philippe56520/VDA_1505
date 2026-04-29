from __future__ import annotations

from typing import Dict, Tuple, Optional

import streamlit as st

from domain.loader import load_scenes


@st.cache_data(show_spinner=False)
def get_scenes_cached() -> Dict[str, Tuple[str, object]]:
    """
    Retourne {scene_id: (module_name, scene)}
    """
    return load_scenes()


def get_scene_by_id(
    scenes: Dict[str, Tuple[str, object]],
    scene_id: Optional[str],
) -> Optional[object]:
    if not scene_id:
        return None
    if scene_id not in scenes:
        return None
    _, scene = scenes[scene_id]
    return scene
