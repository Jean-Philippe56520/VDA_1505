from __future__ import annotations

import importlib.util
from pathlib import Path

from domain.schema import Choice, Scene


POURQUOI_MOI = """
*Aliénor ne répond pas immédiatement.*

« Tu crois que je t’ai choisie à Saint-Georges. »

*Quelque chose passe dans son regard. Presque un sourire, mais trop triste pour en être un.*

« C’est une réponse raisonnable. »

« Elle est seulement fausse. »

*Elle laisse quelques secondes s’écouler.*

« Je te connaissais bien avant que tu ne me connaisses. »

« J’ai veillé sur toi de plus loin que tu ne l’imagines. Et lorsque je suis finalement venue à toi, je savais déjà beaucoup plus de choses sur toi que tu n’en savais sur moi. »

*Aliénor détourne brièvement les yeux.*

« Alors non. Je ne t’ai pas rencontrée un soir dans un couvent en me demandant si tu méritais mon Sang. »

« Lorsque vint le moment de choisir, une partie de ce choix avait été faite depuis longtemps. »

*Elle revient à Perrine.*

« Tu veux savoir pourquoi toi ? »

*Un silence.*

« Parce que je t’avais déjà vue survivre à quelque chose qui aurait dû t’emporter. »

« Parce que je savais que ta vie n’avait jamais été aussi simple qu’elle en avait l’air. »

*Sa voix devient plus basse.*

« Et parce qu’au moment où il fallut décider si je pouvais accepter de te perdre… »

« J’avais déjà pris cette décision une première fois. »

*Aliénor la regarde sans ciller.*

« Je ne t’ai pas choisie par hasard, Perrine. »

« C’est tout ce que je te dirai. »

*Puis, avant qu’elle puisse reprendre :*

« Tu avais droit à une question. »

« Je t’ai répondu. »
""".strip()


_BASE_PATH = Path(__file__).with_name("_une_seule_question_base.py")


def _get_base_scene() -> Scene:
    spec = importlib.util.spec_from_file_location(
        "vda_private_scene_une_seule_question_base",
        _BASE_PATH,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load base scene module: {_BASE_PATH}")

    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    scene = mod.get_scene()
    if not isinstance(scene, Scene):
        raise TypeError(f"{_BASE_PATH}.get_scene() must return a domain.schema.Scene")
    return scene


def get_scene() -> Scene:
    scene = _get_base_scene()
    scene.choices.append(
        Choice(
            id="une_question_pourquoi_m_avoir_choisie",
            label="POURQUOI MOI ? — Pourquoi m’avoir choisie ?",
            answer_md=POURQUOI_MOI,
            ends_scene=True,
        )
    )
    return scene
