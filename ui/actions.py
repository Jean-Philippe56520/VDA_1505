from __future__ import annotations

from domain.engine import RunState, pick_choice, push_bot, undo_last_choice
from ui.state import get_state, set_state, Screen


def go_home() -> None:
    """Retourne a l'accueil sans detruire une scene en cours."""
    state = get_state()
    state.screen = Screen.HOME
    state.last_error = None
    set_state(state)


def go_private_scenes() -> None:
    """Ouvre le sous-menu des scenes privees sans modifier une scene suspendue."""
    state = get_state()
    state.screen = Screen.PRIVATE_SCENES
    state.last_error = None
    set_state(state)


def clear_scene() -> None:
    """Oublie explicitement la scene courante et revient a l'accueil."""
    state = get_state()
    state.screen = Screen.HOME
    state.active_scene_id = None
    state.scene_intro_md = ""
    state.run_state = None
    state.last_error = None
    set_state(state)


def resume_scene() -> None:
    state = get_state()
    if state.active_scene_id and state.run_state is not None:
        state.screen = Screen.SCENE
        state.last_error = None
    else:
        state.last_error = "Aucune scene suspendue a reprendre."
    set_state(state)


def start_scene(scene_id: str, scene: object) -> None:
    """Demarre ou recommence une scene depuis son etat initial."""
    state = get_state()
    state.screen = Screen.SCENE
    state.active_scene_id = scene_id

    intro = getattr(scene, "intro_md", "") or ""
    choices = getattr(scene, "choices", []) or []

    rs = RunState(scene_id=scene_id, active_choices=choices)
    push_bot(rs, intro)

    state.scene_intro_md = intro
    state.run_state = rs
    state.last_error = None
    set_state(state)


def restart_scene(scene_id: str, scene: object) -> None:
    start_scene(scene_id, scene)


def undo_choice() -> bool:
    state = get_state()
    rs = state.run_state
    if rs is None:
        state.last_error = "Aucune scene active."
        set_state(state)
        return False

    restored = undo_last_choice(rs)
    state.run_state = rs
    state.last_error = None if restored else "Aucun choix precedent a restaurer."
    set_state(state)
    return restored


def pick(choice_id: str) -> None:
    state = get_state()
    rs = state.run_state

    if rs is None:
        state.last_error = "Aucune scene active. Retour a l'accueil."
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
