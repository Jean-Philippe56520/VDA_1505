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

« Et lorsque j’ai commencé à veiller sur toi, je ne pensais pas encore à t’Étreindre. »

*Aliénor observe attentivement la réaction de Perrine.*

« Tu n’étais pas un projet d’infante. »

« Tu n’étais pas une candidate que j’évaluais depuis l’ombre. »

« Je savais seulement que je ne parvenais déjà plus à te regarder comme une étrangère. »

*Un silence.*

« Alors oui, j’ai veillé sur toi de beaucoup plus loin que tu ne l’imagines. »

« J’ai su des choses sur ta vie que tu ne pensais pas me concerner. »

« Et bien avant Saint-Georges, j’avais déjà dû prendre une décision à ton sujet. »

*Sa voix devient plus basse.*

« Te laisser vivre sans moi. »

*Elle ne précise pas ce que cette phrase signifie exactement.*

« Je l’ai fait. »

« J’ai cru que je pouvais accepter cela. »

*Un sourire très bref, sans joie.*

« J’ai même réussi pendant longtemps à appeler cela de la sagesse. »

*Aliénor détourne un instant les yeux.*

« Tu veux savoir pourquoi toi ? »

« Parce que je t’avais déjà vue survivre à quelque chose qui aurait dû t’emporter. »

« Parce que je savais que ta vie avait commencé par une fragilité que les gens autour de toi avaient appris à expliquer autrement. »

« Parce que j’avais déjà eu peur de te perdre avant même que tu sois capable de connaître mon nom. »

*Elle revient à Perrine.*

« Et parce qu’après t’avoir laissée suivre une vie qui n’était pas la mienne, je t’ai retrouvée des années plus tard à Saint-Georges. »

« Pas comme la personne que j’aurais fabriquée. »

« Comme celle que tu étais devenue sans moi. »

*Un silence plus long.*

« Ton refus de la vie que l’on voulait choisir pour toi. »

« Tes livres. »

« Ta curiosité. »

« Cette manière de chercher des monstres dans les histoires sans imaginer encore que certains te regardaient déjà depuis l’autre côté de la page. »

*Un vrai sourire apparaît, puis disparaît.*

« Je ne t’ai pas Étreinte parce que j’avais attendu quarante ans pour fabriquer une Toreador convenable. »

« Je t’ai Étreinte parce qu’au moment où je risquais de te perdre une seconde fois, j’ai découvert que la première séparation ne m’avait jamais appris à le supporter. »

*Aliénor laisse cette phrase reposer entre elles.*

« Tu es mon infante. »

*Elle reprend exactement le mot de l’ouverture.*

« C’est vrai. »

« Mais ce n’est pas là que mon attachement à toi a commencé. »

*Son regard se fait plus dur, comme si elle venait d’atteindre la limite exacte qu’elle s’était imposée.*

« Je ne te dirai pas ce qui a failli t’emporter. »

« Je ne te dirai pas comment je te connaissais alors. »

« Je ne te dirai pas non plus qui m’a aidée. »

*Un très léger silence après cette dernière phrase.*

« Pas ce soir. »

« Mais si tu veux réellement comprendre pourquoi je t’ai choisie… »

« Commence peut-être par te demander pourquoi une vampire que tu croyais avoir rencontrée en 1492 parle de la peur de te perdre avant même que tu puisses connaître son nom. »

*Aliénor ne baisse pas les yeux.*

« Tu avais droit à une question. »

« Je t’ai répondu. »
""".strip()


_BASE_PATH = Path(__file__).with_name("_perrine_une_seule_question_base.py")


def _get_base_scene() -> Scene:
    spec = importlib.util.spec_from_file_location(
        "vda_private_scene_perrine_une_seule_question_base",
        _BASE_PATH,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load base scene module: {_BASE_PATH}")

    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    scene = mod.get_scene()
    if not isinstance(scene, Scene):
        raise TypeError(f"{_BASE_PATH}.get_scene() must return a domain.schema.Scene")
    scene.id = "scene_privee_perrine_une_seule_question"
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
