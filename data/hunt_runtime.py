from __future__ import annotations

"""Métadonnées runtime du générateur de chasse.

Le référentiel mécanique et géographique reste le Drive canonique. Ce module
projette pour l'application les Predator Types V5, les incompatibilités stables
des points d'intérêt et quelques préréglages ergonomiques des tables locales.
Les préréglages Git ne définissent jamais le Predator Type canonique d'un PJ.
"""

from typing import Literal, TypedDict


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


LOCAL_HUNT_TABLE_NOTES: dict[str, str] = {
    "osiris_muse": "Variante locale d'Osiris centrée sur l'art et les admirateurs.",
    "rat_egouts": "Variante locale consensualiste centrée sur le barbier-chirurgien.",
    "justicier_nocturne": "Style local Justicier ; le préréglage de compatibilité proposé est Alleycat.",
    "roi_de_la_nuit": "Style local du Trémère du Chapitre ; le préréglage de compatibilité proposé est Scene Queen.",
}

# Préréglages ergonomiques uniquement. Ils sont toujours modifiables dans l'UI.
LOCAL_HUNT_TABLE_DEFAULT_PREDATOR: dict[str, str] = {
    "osiris_muse": "osiris",
    "rat_egouts": "consensualist",
    "justicier_nocturne": "alleycat",
    "roi_de_la_nuit": "scene_queen",
}

LOCAL_HUNT_TABLE_DEFAULT_CONTEXT: dict[str, tuple[str, str]] = {
    "osiris_muse": ("cot_main_prince", "loc_place_lices"),
    "rat_egouts": ("cot_gardiens_sacre", "loc_cathedrale_st_pierre"),
    "justicier_nocturne": ("cot_heritiers_alexandrie", "loc_tanneries"),
    "roi_de_la_nuit": ("cot_fondation_pierre_noire", "loc_archives_chapitre"),
}


HUNT_BASE_DIFFICULTY = 2
HUNT_DIFFICULTY_OPTIONS: dict[str, tuple[str, int]] = {
    "strong_resonance": ("Résonance puissante", 2),
    "balance_resonance": ("Chercher une résonance différente", 1),
    "known_target": ("Cibler un mortel connu", 1),
    "cautious": ("Chasse prudente", 1),
    "different_style": ("Style de prédation ponctuellement différent", 1),
    "inappropriate_point": ("Style inadapté au point d'intérêt", 2),
}

# Projection de 05_REGIONS_LIEUX_ROUTES.chasse_compatibilite_stable.
# Un style absent de la liste est normal et ne reçoit aucun bonus automatique.
HUNT_POINT_INADAPTED_STYLES: dict[str, frozenset[str]] = {
    "loc_place_lices": frozenset({"cleaver", "sandman", "graverobber", "grim_reaper", "trapdoor"}),
    "loc_maison_bourgeois": frozenset({"alleycat", "farmer", "roadside_killer", "graverobber", "grim_reaper", "montero"}),
    "loc_grand_comptoir": frozenset({"cleaver", "sandman", "graverobber", "grim_reaper", "trapdoor"}),
    "loc_cathedrale_st_pierre": frozenset({"alleycat", "farmer", "siren", "roadside_killer", "montero", "trapdoor"}),
    "loc_cloitre_chanoines": frozenset({"alleycat", "farmer", "siren", "roadside_killer", "montero", "trapdoor"}),
    "loc_archives_chapitre": frozenset({"alleycat", "farmer", "roadside_killer", "graverobber", "grim_reaper", "montero"}),
    "loc_tanneries": frozenset({"cleaver", "osiris", "sandman", "siren", "graverobber", "grim_reaper", "tithe_collector"}),
    "loc_caves_souterrains": frozenset({"bagger", "cleaver", "consensualist", "osiris", "scene_queen", "siren", "roadside_killer", "extortionist", "grim_reaper", "montero", "tithe_collector"}),
    "loc_quartier_paroisses_populaires": frozenset(),
    "loc_faubourg_saint_michel": frozenset(),
    "loc_saint_georges": frozenset(),
    "loc_abbaye_saint_georges": frozenset({"alleycat", "farmer", "siren", "roadside_killer", "montero", "trapdoor"}),
    "loc_faubourg_saint_helier": frozenset(),
    "loc_bourg_eveque": frozenset(),
    "loc_relais_marchands": frozenset({"cleaver", "graverobber", "grim_reaper"}),
    "loc_faubourg_saint_germain": frozenset(),
    "loc_tanneries_fleuve": frozenset({"cleaver", "osiris", "sandman", "siren", "graverobber", "grim_reaper", "tithe_collector"}),
    "loc_pont_vilaine": frozenset({"bagger", "cleaver", "sandman", "osiris", "graverobber", "grim_reaper", "trapdoor", "tithe_collector"}),
    "zone_lisiere_bois_saint_germain": frozenset({"bagger", "cleaver", "consensualist", "osiris", "sandman", "scene_queen", "siren", "graverobber", "grim_reaper", "trapdoor", "tithe_collector"}),
    "loc_faubourg_madeleine": frozenset(),
    "loc_saint_yves": frozenset({"alleycat", "farmer", "roadside_killer", "montero"}),
    "loc_hopital_pelerins": frozenset({"alleycat", "farmer", "montero"}),
    "loc_faubourg_saint_martin": frozenset(),
    "loc_jardins_vignes": frozenset({"bagger", "osiris", "scene_queen", "siren", "graverobber", "grim_reaper", "trapdoor"}),
    "loc_ferme_fortifiee": frozenset({"osiris", "scene_queen", "siren", "graverobber", "grim_reaper"}),
}

HUNT_IMPOSSIBLE_POINTS = frozenset({"loc_caern_lisiere_saint_germain"})

# Le Caern est un cas spécial canonique imbriqué dans la lisière. Il est montré
# dans l'outil uniquement pour rappeler l'interdit, jamais comme domaine.
HUNT_SPECIAL_POINTS: dict[str, dict[str, str | None]] = {
    "loc_caern_lisiere_saint_germain": {
        "id": "loc_caern_lisiere_saint_germain",
        "label": "Caern de la lisière de Saint-Germain — chasse interdite",
        "zone_id": "secteur_faubourgs_saint_germain",
        "zone_label": "Lisière et bois de Saint-Germain",
        "controller_ref": None,
    }
}

HuntPointStyleStatus = Literal["normal", "inadapte", "impossible"]


def predator_label(style_id: str) -> str:
    return PREDATOR_TYPES.get(style_id, {"label": style_id})["label"]


def hunt_point_style_status(point_id: str, style_id: str) -> HuntPointStyleStatus:
    if point_id in HUNT_IMPOSSIBLE_POINTS:
        return "impossible"
    if style_id in HUNT_POINT_INADAPTED_STYLES.get(point_id, frozenset()):
        return "inadapte"
    return "normal"
