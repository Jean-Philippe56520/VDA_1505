from __future__ import annotations

import streamlit as st

from ui.components import apply_theme
from ui.data import get_scenes_cached, get_scene_by_id
from ui.state import get_state, Screen
from ui.pages import page_home, page_private_scenes, page_scene
from ui.actions import go_home

APP_TITLE = "Vampire: Dark Ages — Secret Kiosk"


def main() -> None:
    st.set_page_config(page_title=APP_TITLE, layout="centered")

    apply_theme()

    scenes = get_scenes_cached()
    if not scenes:
        st.error(
            "Aucune scène trouvée dans /scenes ou /scenes_private "
            "(fichiers .py avec get_scene())."
        )
        return

    state = get_state()

    if state.screen == Screen.HOME:
        page_home(scenes)
        return

    if state.screen == Screen.PRIVATE_SCENES:
        page_private_scenes(scenes)
        return

    # Screen.SCENE
    scene = get_scene_by_id(scenes, state.active_scene_id)
    if scene is None:
        st.error("Scène introuvable. Retour à l'accueil.")
        go_home()
        st.rerun()
        return

    page_scene(scene)


if __name__ == "__main__":
    main()
