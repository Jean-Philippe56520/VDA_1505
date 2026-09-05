from __future__ import annotations

"""Décisions MJ et projections runtime complémentaires pour la chasse.

Les identifiants techniques restent stables. Les libellés visibles sont français.
La compatibilité est un trait stable du lieu ; le danger de campagne est une
couche distincte qui ne modifie pas automatiquement la difficulté.
"""

PREDATOR_LABELS = {
    "alleycat": "Chat de gouttière",
    "bagger": "Biberonneur",
    "blood_leech": "Lamproie",
    "cleaver": "Parasite domestique",
    "consensualist": "Consensualiste",
    "farmer": "Fermier",
    "osiris": "Osiris",
    "sandman": "Marchand de sable",
    "scene_queen": "Reine de la nuit",
    "siren": "Succube",
    "roadside_killer": "Tueur de la route",
    "extortionist": "Racketteur",
    "graverobber": "Pilleur de tombes",
    "grim_reaper": "Faucheur",
    "montero": "Maître de battue",
    "pursuer": "Poursuivant",
    "trapdoor": "Chausse-trappe",
    "tithe_collector": "Collecteur de dîme",
}

# Matrice validée par le MJ le 2026-09-02.
INADAPTED_STYLES = {
    "loc_place_lices": {"alleycat", "cleaver", "extortionist", "graverobber", "grim_reaper", "sandman", "trapdoor"},
    "loc_maison_bourgeois": {"alleycat", "extortionist", "farmer", "graverobber", "grim_reaper", "montero", "roadside_killer", "trapdoor"},
    "loc_grand_comptoir": {"alleycat", "cleaver", "extortionist", "graverobber", "grim_reaper", "sandman", "trapdoor"},
    "loc_cathedrale_st_pierre": {"alleycat", "extortionist", "farmer", "montero", "roadside_killer", "siren", "trapdoor"},
    "loc_cloitre_chanoines": {"alleycat", "extortionist", "farmer", "montero", "roadside_killer", "siren", "trapdoor"},
    "loc_archives_chapitre": {"alleycat", "extortionist", "farmer", "graverobber", "grim_reaper", "montero", "roadside_killer", "trapdoor"},
    "loc_tanneries": {"cleaver", "graverobber", "grim_reaper", "osiris", "sandman", "siren", "tithe_collector"},
    "loc_caves_souterrains": {"bagger", "cleaver", "consensualist", "extortionist", "grim_reaper", "montero", "osiris", "roadside_killer", "scene_queen", "siren", "tithe_collector"},
    "loc_quartier_paroisses_populaires": set(),
    "loc_faubourg_saint_michel": set(),
    "loc_saint_georges": set(),
    "loc_abbaye_saint_georges": {"alleycat", "extortionist", "farmer", "montero", "roadside_killer", "siren", "trapdoor"},
    "loc_faubourg_saint_helier": set(),
    "loc_bourg_eveque": {"alleycat", "extortionist"},
    "loc_relais_marchands": {"cleaver", "graverobber", "grim_reaper"},
    "loc_faubourg_saint_germain": set(),
    "loc_tanneries_fleuve": {"cleaver", "graverobber", "grim_reaper", "osiris", "sandman", "siren", "tithe_collector"},
    "loc_pont_vilaine": {"bagger", "cleaver", "graverobber", "grim_reaper", "osiris", "sandman", "tithe_collector", "trapdoor"},
    "zone_lisiere_bois_saint_germain": {"bagger", "cleaver", "consensualist", "graverobber", "grim_reaper", "osiris", "sandman", "scene_queen", "siren", "tithe_collector", "trapdoor"},
    "loc_faubourg_madeleine": set(),
    "loc_saint_yves": {"alleycat", "extortionist", "farmer", "montero", "roadside_killer"},
    "loc_hopital_pelerins": {"alleycat", "extortionist", "farmer", "montero"},
    "loc_faubourg_saint_martin": set(),
    "loc_jardins_vignes": {"bagger", "graverobber", "grim_reaper", "osiris", "scene_queen", "siren", "trapdoor"},
    "loc_ferme_fortifiee": {"alleycat", "extortionist", "graverobber", "grim_reaper", "osiris", "scene_queen", "siren"},
    "loc_porte_saint_michel": {"alleycat", "cleaver", "extortionist", "graverobber", "grim_reaper", "sandman", "siren", "trapdoor"},
    "loc_porte_saint_helier": {"alleycat", "cleaver", "extortionist", "graverobber", "grim_reaper", "sandman", "siren", "trapdoor"},
    "loc_porte_saint_germain": {"alleycat", "cleaver", "extortionist", "graverobber", "grim_reaper", "sandman", "siren", "trapdoor"},
    "loc_porte_madeleine": {"alleycat", "cleaver", "extortionist", "graverobber", "grim_reaper", "sandman", "siren", "trapdoor"},
    "loc_porte_saint_martin": {"alleycat", "cleaver", "extortionist", "graverobber", "grim_reaper", "sandman", "siren", "trapdoor"},
}

FORBIDDEN_POINT_ID = "hunt_interdit_lisiere_saint_germain"

SPECIAL_POINTS = {
    "loc_porte_saint_michel": {
        "id": "loc_porte_saint_michel", "label": "Porte Saint-Michel / Porte des Abbesses",
        "zone_id": "zone_portes_rennes", "zone_label": "Portes de Rennes", "controller_ref": "cot_main_prince",
    },
    "loc_porte_saint_helier": {
        "id": "loc_porte_saint_helier", "label": "Porte Saint-Hélier / Porte du Sang Neuf",
        "zone_id": "zone_portes_rennes", "zone_label": "Portes de Rennes", "controller_ref": "cot_gardiens_sacre",
    },
    "loc_porte_saint_germain": {
        "id": "loc_porte_saint_germain", "label": "Porte Saint-Germain / Porte du Pont Noir",
        "zone_id": "zone_portes_rennes", "zone_label": "Portes de Rennes", "controller_ref": "cot_executeurs",
    },
    "loc_porte_madeleine": {
        "id": "loc_porte_madeleine", "label": "Porte Madeleine / Porte des Mourants",
        "zone_id": "zone_portes_rennes", "zone_label": "Portes de Rennes", "controller_ref": "cot_executeurs",
    },
    "loc_porte_saint_martin": {
        "id": "loc_porte_saint_martin", "label": "Porte Saint-Martin / Porte des Brumes",
        "zone_id": "zone_portes_rennes", "zone_label": "Portes de Rennes", "controller_ref": "cot_crocs_silencieux",
    },
    FORBIDDEN_POINT_ID: {
        "id": FORBIDDEN_POINT_ID, "label": "Périmètre interdit de la lisière — chasse interdite",
        "zone_id": "secteur_faubourgs_saint_germain", "zone_label": "Lisière et bois de Saint-Germain", "controller_ref": None,
    },
}

OPERATIONAL_POINTS = {
    "cot_executeurs": {
        "loc_porte_madeleine", "loc_porte_saint_germain", "loc_faubourg_saint_germain",
        "loc_tanneries_fleuve", "loc_pont_vilaine", "zone_lisiere_bois_saint_germain",
    }
}

OPERATIONAL_LABELS = {
    "cot_executeurs": "Les Exécuteurs — territoire + front opérationnel de Saint-Germain",
}

DANGER = {
    "loc_porte_saint_michel": (
        "Réservé",
        "Droit ordinaire de chasse réservé à Ysabeau des Voûtes ; tout autre chasseur doit disposer d'une permission explicite ou assume une chasse non autorisée.",
    ),
    "loc_porte_madeleine": ("Surveillé", "Seuil tenu et fortement observé."),
    "loc_porte_saint_germain": ("Tendu", "Passage vers un front où les incidents sont fréquents."),
    "loc_faubourg_saint_germain": ("Hostile", "Habitants vigilants et crise occulte active."),
    "loc_tanneries_fleuve": ("Hostile", "Activité humaine exploitable, mais logistiques clandestines et raids possibles."),
    "loc_pont_vilaine": ("Très hostile", "Nœud de passage et d'observation ; une chasse peut vite devenir poursuite ou enquête."),
    "zone_lisiere_bois_saint_germain": ("Mortel", "Bois disputés, bêtes, patrouilles et limites à ne pas franchir."),
    FORBIDDEN_POINT_ID: ("Interdit", "Chasse et nourrissage interdits."),
}

DEFAULT_CONTEXT = {
    "executeurs_front_saint_germain": ("cot_executeurs", "loc_porte_saint_germain"),
}

DEFAULT_PREDATOR = {"executeurs_front_saint_germain": "pursuer"}

TABLE_NOTES = {
    "justicier_nocturne": "Style local Justicier ; le préréglage proposé est Chat de gouttière.",
    "roi_de_la_nuit": "Style local du Trémère du Chapitre ; le préréglage proposé est Reine de la nuit.",
    "executeurs_front_saint_germain": (
        "Table préparatoire filtrée par point d'intérêt. Saint-Germain est un front opérationnel des Exécuteurs, "
        "pas une extension de leur domaine ni de leur Viandis."
    ),
}


def style_status(point_id: str, style_id: str) -> str:
    if point_id == FORBIDDEN_POINT_ID:
        return "impossible"
    if style_id in INADAPTED_STYLES.get(point_id, set()):
        return "inadapte"
    return "normal"
