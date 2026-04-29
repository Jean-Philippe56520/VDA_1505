from __future__ import annotations
from typing import List, Literal, Optional
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
