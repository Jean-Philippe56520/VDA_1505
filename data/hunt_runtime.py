from __future__ import annotations

"""Métadonnées runtime du générateur de chasse.

Le référentiel mécanique reste le Drive canonique. Ce module fournit à
l'application une projection compacte des styles de prédation V5 et des
modificateurs validés pour Rennes 1505. Il ne canonise aucun événement et ne
remplace pas les fiches PJ.
"""

from typing import TypedDict


class PredatorType(TypedDict):
    label: str
    medieval_reading: str
    source: str


PREDATOR_TYPES: dict[str, PredatorType] = {
    "alleycat": {
        "label": "Alleycat",
        "medieval_reading": "Prédation par force, intimidation ou embuscade dans les rues et passages isolés.",
        "source": "V5 Corebook",
    },
    "bagger": {
        "label": "Bagger",
        "medieval_reading": "Sang obtenu indirectement : saignées, barbiers-chirurgiens, réserves médicales ou autres prélèvements.",
        "source": "V5 Corebook",
    },
    "blood_leech": {
        "label": "Blood Leech",
        "medieval_reading": "Se nourrit sur d'autres vampires plutôt que sur des mortels.",
        "source": "V5 Corebook",
    },
    "cleaver": {
        "label": "Cleaver",
        "medieval_reading": "Maintient une famille, une maisonnée ou un cercle domestique comme source de sang.",
        "source": "V5 Corebook",
    },
    "consensualist": {
        "label": "Consensualist",
        "medieval_reading": "Obtient un consentement réel ou ritualisé avant le prélèvement.",
        "source": "V5 Corebook",
    },
    "farmer": {
        "label": "Farmer",
        "medieval_reading": "Se nourrit principalement sur des animaux.",
        "source": "V5 Corebook",
    },
    "osiris": {
        "label": "Osiris",
        "medieval_reading": "Se nourrit parmi ses fidèles, admirateurs, clients, adeptes ou dévots.",
        "source": "V5 Corebook",
    },
    "sandman": {
        "label": "Sandman",
        "medieval_reading": "Prélève sur des victimes endormies ou inconscientes.",
        "source": "V5 Corebook",
    },
    "scene_queen": {
        "label": "Scene Queen",
        "medieval_reading": "Chasse dans un milieu social ou une sous-culture dont le vampire est un membre reconnu.",
        "source": "V5 Corebook",
    },
    "siren": {
        "label": "Siren",
        "medieval_reading": "Mêle séduction, intimité et nourrissage.",
        "source": "V5 Corebook",
    },
    "roadside_killer": {
        "label": "Roadside Killer",
        "medieval_reading": "Cible voyageurs, pèlerins, marchands et population de passage sur les routes et relais.",
        "source": "Let the Streets Run Red",
    },
    "extortionist": {
        "label": "Extortionist",
        "medieval_reading": "Obtient du sang par protection, dette, racket, chantage ou contrainte organisée.",
        "source": "Cults of the Blood Gods",
    },
    "graverobber": {
        "label": "Graverobber",
        "medieval_reading": "Fréquente morts, mourants, cimetières, charniers, hospices et lieux funéraires.",
        "source": "Cults of the Blood Gods",
    },
    "grim_reaper": {
        "label": "Grim Reaper",
        "medieval_reading": "Cible ceux qui sont proches de la mort : malades graves, blessés ou agonisants.",
        "source": "V5 Player's Guide",
    },
    "montero": {
        "label": "Montero",
        "medieval_reading": "Organise une chasse avec rabatteurs, serviteurs, hommes de main ou auxiliaires.",
        "source": "V5 Player's Guide",
    },
    "pursuer": {
        "label": "Pursuer",
        "medieval_reading": "Étudie une proie particulière, ses habitudes et ses déplacements avant de la traquer.",
        "source": "V5 Player's Guide",
    },
    "trapdoor": {
        "label": "Trapdoor",
        "medieval_reading": "Attire la proie dans un lieu qu'il contrôle : demeure, atelier, auberge, cave ou autre piège social.",
        "source": "V5 Player's Guide",
    },
    "tithe_collector": {
        "label": "Tithe Collector",
        "medieval_reading": "Reçoit des victimes ou du sang comme tribut grâce à son statut, son droit ou une obligation féodale.",
        "source": "In Memoriam",
    },
}


# Tables narratives locales déjà présentes dans data/hunt_tables.py. Elles ne
# redéfinissent pas les Predator Types officiels : certaines sont des variantes
# adaptées à un PJ ou à une fonction de la chronique.
LOCAL_HUNT_TABLE_NOTES: dict[str, str] = {
    "osiris_muse": "Variante locale d'Osiris centrée sur l'art et les admirateurs.",
    "rat_egouts": "Variante locale consensualiste centrée sur le barbier-chirurgien.",
    "justicier_nocturne": "Style local Justicier ; ne pas le présenter comme un Predator Type officiel distinct.",
    "roi_de_la_nuit": "Style local du Trémère du Chapitre ; ne pas l'assimiler automatiquement à un Predator Type officiel.",
}


HUNT_BASE_DIFFICULTY = 2
HUNT_DIFFICULTY_OPTIONS: dict[str, tuple[str, int]] = {
    "strong_resonance": ("Résonance puissante", 2),
    "balance_resonance": ("Chercher une résonance différente", 1),
    "known_target": ("Cibler un mortel connu", 1),
    "cautious": ("Chasse prudente", 1),
    # Canon local courant. Une préférence MJ pour -1 dé a été évoquée mais
    # n'a pas encore remplacé explicitement cette règle dans le Drive.
    "different_style": ("Style de prédation ponctuellement différent", 1),
    "inappropriate_point": ("Style inadapté au point d'intérêt", 2),
}


def predator_label(style_id: str) -> str:
    return PREDATOR_TYPES.get(style_id, {"label": style_id})["label"]
