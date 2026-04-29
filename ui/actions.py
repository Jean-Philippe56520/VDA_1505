from __future__ import annotations

from domain.engine import RunState, pick_choice, push_bot
from ui.state import get_state, set_state, Screen


def go_home() -> None:
    state = get_state()
    state.screen = Screen.HOME
    state.active_scene_id = None
    state.scene_intro_md = ""
    state.run_state = None
    state.last_error = None
    set_state(state)


def start_scene(scene_id: str, scene: object) -> None:
    state = get_state()
    state.screen = Screen.SCENE
    state.active_scene_id = scene_id

    intro = getattr(scene, "intro_md", "") or ""
    choices = getattr(scene, "choices", []) or []

    rs = RunState(scene_id=scene_id, active_choices=choices)
    # Start conversation with intro (one place only)
    push_bot(rs, intro)

    state.scene_intro_md = intro
    state.run_state = rs
    state.last_error = None
    set_state(state)


def pick(choice_id: str) -> None:
    state = get_state()
    rs = state.run_state

    if rs is None:
        state.last_error = "Aucune scène active. Retour à l'accueil."
        set_state(state)
        go_home()
        return

    choice = next((c for c in rs.active_choices if c.id == choice_id), None)
    if choice is None:
        state.last_error = "Choix introuvable (refresh ?)."
        set_state(state)
        return

    pick_choice(rs, choice)
    state.run_state = rs
    state.last_error = None
    set_state(state)
