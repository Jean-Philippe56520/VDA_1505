from __future__ import annotations

from typing import Dict, Optional, Tuple

import streamlit as st

from repositories.scenes import load_scenes


@st.cache_data(show_spinner=False)
def get_scenes_cached() -> Dict[str, Tuple[str, object]]:
    """Return {scene_id: (source_name, scene)} from the configured repository."""
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
