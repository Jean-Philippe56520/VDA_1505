from __future__ import annotations

import importlib
import importlib.util
import pkgutil
from pathlib import Path
from typing import Dict, List, Tuple

from domain.schema import Scene

SCENES_PKG = "scenes"
ROOT_DIR = Path(__file__).resolve().parents[1]
PRIVATE_SCENES_DIR = ROOT_DIR / "scenes_private"
LOCAL_PRIVATE_SCENES_DIR = ROOT_DIR / "runtime_local_private"


def discover_scene_modules() -> List[str]:
    pkg = importlib.import_module(SCENES_PKG)
    out = []
    for m in pkgutil.iter_modules(pkg.__path__):
        if not m.ispkg and not m.name.startswith("_"):
            out.append(f"{SCENES_PKG}.{m.name}")
    return sorted(out)


def _discover_python_files(directory: Path) -> List[Path]:
    if not directory.is_dir():
        return []
    return sorted(
        path
        for path in directory.glob("*.py")
        if path.is_file() and not path.name.startswith("_")
    )


def discover_private_scene_files() -> List[Tuple[str, Path]]:
    """Retourne les scènes du sous-menu privé.

    `scenes_private/` reste un dossier versionnable : son contenu doit donc être
    considéré comme potentiellement public. `runtime_local_private/` est au
    contraire ignoré par Git et sert aux scènes MJ réellement sensibles.
    """
    out: List[Tuple[str, Path]] = []
    out.extend(("public", path) for path in _discover_python_files(PRIVATE_SCENES_DIR))
    out.extend(("local", path) for path in _discover_python_files(LOCAL_PRIVATE_SCENES_DIR))
    return sorted(out, key=lambda item: (item[0], item[1].name))


def _load_private_scene(source: str, path: Path) -> Tuple[str, Scene] | None:
    module_name = f"vda_private_scene_{source}_{path.stem}"
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load private scene module: {path}")

    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if not hasattr(mod, "get_scene"):
        return None

    scene = mod.get_scene()
    if not isinstance(scene, Scene):
        raise TypeError(f"{path}.get_scene() must return a domain.schema.Scene")
    # Le préfixe `private:` suffit à conserver le regroupement UI existant ;
    # le sous-type précise seulement la provenance technique.
    return f"private:{source}:{path.name}", scene


def load_scenes() -> Dict[str, Tuple[str, Scene]]:
    scenes: Dict[str, Tuple[str, Scene]] = {}

    for module_name in discover_scene_modules():
        mod = importlib.import_module(module_name)
        if not hasattr(mod, "get_scene"):
            continue
        scene = mod.get_scene()
        if not isinstance(scene, Scene):
            raise TypeError(f"{module_name}.get_scene() must return a domain.schema.Scene")
        if scene.id in scenes:
            raise ValueError(f"Duplicate scene id: {scene.id}")
        scenes[scene.id] = (module_name, scene)

    for source, path in discover_private_scene_files():
        loaded = _load_private_scene(source, path)
        if loaded is None:
            continue
        module_name, scene = loaded
        if scene.id in scenes:
            raise ValueError(
                f"Private scene id '{scene.id}' conflicts with an existing scene. "
                "Rename one of the scenes instead of overriding it."
            )
        scenes[scene.id] = (module_name, scene)

    return scenes
