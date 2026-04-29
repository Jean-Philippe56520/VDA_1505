from __future__ import annotations
import importlib
import pkgutil
from typing import Dict, Tuple, List

from domain.schema import Scene

SCENES_PKG = "scenes"

def discover_scene_modules() -> List[str]:
    pkg = importlib.import_module(SCENES_PKG)
    out = []
    for m in pkgutil.iter_modules(pkg.__path__):
        if not m.ispkg and not m.name.startswith("_"):
            out.append(f"{SCENES_PKG}.{m.name}")
    return sorted(out)

def load_scenes() -> Dict[str, Tuple[str, Scene]]:
    scenes: Dict[str, Tuple[str, Scene]] = {}
    for module_name in discover_scene_modules():
        mod = importlib.import_module(module_name)
        if not hasattr(mod, "get_scene"):
            continue
        scene = mod.get_scene()
        if not isinstance(scene, Scene):
            raise TypeError(f"{module_name}.get_scene() must return a domain.schema.Scene")
        scenes[scene.id] = (module_name, scene)
    return scenes
