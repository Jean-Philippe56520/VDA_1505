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
class RunState:
    scene_id: str
    active_choices: List[Choice]

    # "Conversation"
    transcript: List[Tuple[Role, str]] = field(default_factory=list)

    # Convenience fields
    last_answer_md: str = ""
    history_labels: List[str] = field(default_factory=list)
    ended: bool = False


def push_bot(state: RunState, md: str) -> None:
    md = (md or "").strip()
    if md:
        state.transcript.append(("Narrateur", md))


def push_pj(state: RunState, md: str) -> None:
    md = (md or "").strip()
    if md:
        state.transcript.append(("PJ", md))


def pick_choice(state: RunState, choice: Choice) -> None:
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
