from __future__ import annotations

import uuid

from domain.engine import RunState, pick_choice, push_bot, undo_last_choice
from services import runtime as runtime_service
from ui.state import Screen, get_state, set_state


def _safe_runtime(callable_obj, *args, **kwargs) -> None:
    """Runtime telemetry must never make the physical table app unusable."""
    try:
        callable_obj(*args, **kwargs)
    except Exception:
        pass


def _ensure_runtime_run(state) -> tuple[str, str]:
    if not getattr(state, "active_scene_run_id", None):
        state.active_scene_run_id = str(uuid.uuid4())
    if not getattr(state, "active_scene_started_at", None):
        state.active_scene_started_at = runtime_service.now_iso()
    return state.active_scene_run_id, state.active_scene_started_at


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
    """Oublie explicitement la scene courante et revient a l'accueil.

    Les identifiants de scènes irréversibles déjà scellées sont volontairement
    conservés pour empêcher leur relance pendant la même session.
    """
    state = get_state()
    if state.active_scene_id and state.run_state is not None:
        run_id, started_at = _ensure_runtime_run(state)
        if not state.run_state.ended:
            _safe_runtime(
                runtime_service.scene_abandoned,
                run_id=run_id,
                scene_id=state.active_scene_id,
                run_state=state.run_state,
                started_at=started_at,
            )
    state.screen = Screen.HOME
    state.active_scene_id = None
    state.scene_intro_md = ""
    state.run_state = None
    state.active_scene_run_id = None
    state.active_scene_started_at = None
    state.runtime_logged_transcript_count = 0
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


def start_scene(scene_id: str, scene: object) -> bool:
    """Demarre une scene depuis son etat initial si elle n'est pas scellée."""
    state = get_state()
    sealed_scene_ids = getattr(state, "sealed_scene_ids", set())
    if scene_id in sealed_scene_ids:
        state.last_error = "Cette scene a deja ete scellee par un choix irreversible pendant cette session."
        set_state(state)
        return False

    # Replacing an unfinished run is a runtime fact only, never a canon decision.
    if state.active_scene_id and state.run_state is not None and not state.run_state.ended:
        previous_run_id, previous_started_at = _ensure_runtime_run(state)
        _safe_runtime(
            runtime_service.scene_abandoned,
            run_id=previous_run_id,
            scene_id=state.active_scene_id,
            run_state=state.run_state,
            started_at=previous_started_at,
        )

    state.screen = Screen.SCENE
    state.active_scene_id = scene_id
    state.active_scene_run_id = str(uuid.uuid4())
    state.active_scene_started_at = runtime_service.now_iso()
    state.runtime_logged_transcript_count = 0

    intro = getattr(scene, "intro_md", "") or ""
    choices = getattr(scene, "choices", []) or []

    rs = RunState(
        scene_id=scene_id,
        active_choices=choices,
        allow_undo=bool(getattr(scene, "allow_undo", True)),
        allow_restart_after_choice=bool(getattr(scene, "allow_restart_after_choice", True)),
    )
    push_bot(rs, intro)

    state.scene_intro_md = intro
    state.run_state = rs
    state.last_error = None
    set_state(state)
    _safe_runtime(
        runtime_service.scene_opened,
        run_id=state.active_scene_run_id,
        scene=scene,
        run_state=rs,
        started_at=state.active_scene_started_at,
    )
    return True


def restart_scene(scene_id: str, scene: object) -> bool:
    state = get_state()
    rs = state.run_state
    if (
        rs is not None
        and rs.scene_id == scene_id
        and rs.history_labels
        and not getattr(rs, "allow_restart_after_choice", True)
    ):
        state.last_error = "Cette scene est irreversible depuis son premier choix et ne peut plus etre recommencee."
        state.sealed_scene_ids.add(scene_id)
        set_state(state)
        return False

    _safe_runtime(
        runtime_service.scene_restarted,
        previous_run_id=getattr(state, "active_scene_run_id", None),
        scene_id=scene_id,
    )
    return start_scene(scene_id, scene)


def undo_choice() -> bool:
    state = get_state()
    rs = state.run_state
    if rs is None:
        state.last_error = "Aucune scene active."
        set_state(state)
        return False

    if not getattr(rs, "allow_undo", True):
        state.last_error = "Cette scene ne permet pas de revenir sur un choix."
        set_state(state)
        return False

    restored = undo_last_choice(rs)
    state.run_state = rs
    state.last_error = None if restored else "Aucun choix precedent a restaurer."
    if restored:
        state.runtime_logged_transcript_count = min(
            int(getattr(state, "runtime_logged_transcript_count", 0)),
            len(getattr(rs, "transcript", []) or []),
        )
        run_id, started_at = _ensure_runtime_run(state)
        _safe_runtime(
            runtime_service.scene_choice_undone,
            run_id=run_id,
            scene_id=rs.scene_id,
            run_state=rs,
            started_at=started_at,
        )
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

    first_choice = not rs.history_labels
    pick_choice(rs, choice)

    if first_choice and not getattr(rs, "allow_restart_after_choice", True):
        state.sealed_scene_ids.add(rs.scene_id)

    run_id, started_at = _ensure_runtime_run(state)
    _safe_runtime(
        runtime_service.scene_choice_selected,
        run_id=run_id,
        scene_id=rs.scene_id,
        choice=choice,
        run_state=rs,
        started_at=started_at,
    )

    state.run_state = rs
    state.last_error = None
    set_state(state)
