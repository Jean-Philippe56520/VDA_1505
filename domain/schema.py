from __future__ import annotations
from typing import List, Literal
from pydantic import BaseModel, Field

SchemaVersion = Literal[1]


class Choice(BaseModel):
    id: str
    label: str
    answer_md: str = ""
    followups: List["Choice"] = Field(default_factory=list)
    ends_scene: bool = False  # si True, fin même si followups vides (optionnel)


class Scene(BaseModel):
    schema_version: SchemaVersion = 1
    id: str
    title: str
    intro_md: str
    choices: List[Choice] = Field(default_factory=list)
    # Contrôles génériques pour les décisions irréversibles. Les anciennes scènes
    # conservent exactement leur comportement par défaut.
    allow_undo: bool = True
    allow_restart_after_choice: bool = True
