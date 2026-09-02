from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Tuple, Literal

from domain.schema import Scene, Choice


class SceneValidationError(Exception):
    pass


Role = Literal["BOT", "PJ"]


def _validate_choice_tree(path: str, choices: List[Choice], ids_seen: set) -> List[str]:
    warnings: List[str] = []
    for ch in choices:
        if not ch.id:
            raise SceneValidationError(f"Choice with empty id at {path}")
        if ch.id in ids_seen:
            warnings.append(f"Duplicate choice id '{ch.id}' (path: {path}). Prefer unique ids.")
        ids_seen.add(ch.id)

        # If ends_scene True but followups exist, we warn (allowed but weird)
        if ch.ends_scene and ch.followups:
            warnings.append(f"Choice '{ch.id}' ends_scene=True but has followups (they will be ignored by engine).")

        if ch.followups:
            warnings.extend(_validate_choice_tree(f"{path}/{ch.id}", ch.followups, ids_seen))
    return warnings


def validate_scene(scene: Scene) -> List[str]:
    if not scene.choices:
        raise SceneValidationError("Scene has no choices.")
    ids_seen: set = set()
    return _validate_choice_tree(f"scene:{scene.id}", scene.choices, ids_seen)


@dataclass
class RunSnapshot:
    """Etat minimal permettant d'annuler proprement un choix joueur."""

    active_choices: List[Choice]
    transcript: List[Tuple[Role, str]]
    last_answer_md: str
    history_labels: List[str]
    ended: bool


@dataclass
class RunState:
    scene_id: str
    active_choices: List[Choice]

    # "Conversation"
    transcript: List[Tuple[Role, str]] = field(default_factory=list)

    # Convenience fields
    last_answer_md: str = ""
    history_labels: List[str] = field(default_factory=list)
    ended: bool = False

    # Une copie de l'etat est empilee avant chaque choix.
    # Cela permet un vrai "Choix precedent" sans reconstruire la scene.
    undo_stack: List[RunSnapshot] = field(default_factory=list)


def push_bot(state: RunState, md: str) -> None:
    md = (md or "").strip()
    if md:
        state.transcript.append(("Narrateur", md))


def push_pj(state: RunState, md: str) -> None:
    md = (md or "").strip()
    if md:
        state.transcript.append(("PJ", md))


def _snapshot(state: RunState) -> RunSnapshot:
    return RunSnapshot(
        active_choices=list(state.active_choices),
        transcript=list(state.transcript),
        last_answer_md=state.last_answer_md,
        history_labels=list(state.history_labels),
        ended=state.ended,
    )


def _undo_stack(state: RunState) -> List[RunSnapshot]:
    """Compatibilite avec les RunState deja presents dans une session Streamlit ouverte."""
    stack = getattr(state, "undo_stack", None)
    if stack is None:
        stack = []
        setattr(state, "undo_stack", stack)
    return stack


def can_undo_choice(state: RunState) -> bool:
    return bool(_undo_stack(state))


def undo_last_choice(state: RunState) -> bool:
    """Restaure l'etat juste avant le dernier choix. Retourne False si rien a annuler."""
    stack = _undo_stack(state)
    if not stack:
        return False

    previous = stack.pop()
    state.active_choices = list(previous.active_choices)
    state.transcript = list(previous.transcript)
    state.last_answer_md = previous.last_answer_md
    state.history_labels = list(previous.history_labels)
    state.ended = previous.ended
    return True


def pick_choice(state: RunState, choice: Choice) -> None:
    # Sauvegarde l'etat avant toute mutation pour permettre un retour fiable.
    _undo_stack(state).append(_snapshot(state))

    # Record player choice
    state.history_labels.append(choice.label)
    push_pj(state, choice.label)

    # Record bot answer
    state.last_answer_md = (choice.answer_md or "").strip()
    push_bot(state, state.last_answer_md)

    # Ends now?
    if choice.ends_scene or not choice.followups:
        state.active_choices = []
        state.ended = True
        return

    # Escalation continues
    state.active_choices = choice.followups
    state.ended = False


def find_choice_by_id(choices: List[Choice], choice_id: str) -> Optional[Choice]:
    for ch in choices:
        if ch.id == choice_id:
            return ch
    return None
