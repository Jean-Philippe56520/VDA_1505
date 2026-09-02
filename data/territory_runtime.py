from __future__ import annotations

"""Projection Git du canon territorial actif.

Source de vérité : Drive CORPUS_ACTIF, principalement 05/07/07A.
Ce module est un cache runtime pour l'application de table : il n'est pas une
source canonique et doit être resynchronisé après toute modification du Drive.
"""

from typing import TypedDict


class PointHunt(TypedDict, total=False):
    id: str
    label: str
    controller_ref: str | None


class HuntZone(TypedDict, total=False):
    id: str
    label: str
    points: list[PointHunt]
    difficulty_modifier: int
    difficulty_origin: str


COTERIE_DOMAINS: dict[str, dict] = {
    "cot_main_prince": {
        "label": "La Main du Prince",
        "faction": "Camarilla",
        "type": "Régence (+1 Viandis)",
        "domain": "Cœur Bourgeois et Porte Saint-Michel",
        "totals": {"viandis": 5, "servage": 4, "rempart": 3},
        "components": [
            ("Place des Lices", "+2 Viandis"),
            ("Maison des Bourgeois", "+2 Servage, +1 Rempart"),
            ("Grand Comptoir des Marchands", "+2 Viandis, +1 Servage"),
            ("Contrôle complet du Cœur Bourgeois", "+1 Servage"),
            ("Porte Saint-Michel", "+1 Servage, +1 Rempart"),
        ],
        "modifiers": [
            ("Régence", "+1 Viandis"),
            ("Investissement de répression", "-1 Servage — pression et surveillance sur la Madeleine et les Anarchs"),
            ("Tribut des Gardiens du Sacré", "+1 Rempart"),
        ],
        "summary": "Pouvoir central, abondance de sang et leviers bourgeois. Son Rempart effectif inclut le tribut ventrue ; son Servage est réduit par l'investissement permanent de répression à la Madeleine.",
    },
    "cot_gardiens_sacre": {
        "label": "Les Gardiens du Sacré",
        "faction": "Camarilla",
        "type": "Firme (+1 Servage)",
        "domain": "Cathédrale Saint-Pierre, Cloître des Chanoines et Porte Saint-Hélier",
        "totals": {"viandis": 1, "servage": 3, "rempart": 4},
        "components": [
            ("Cathédrale Saint-Pierre", "+1 Servage, +2 Rempart"),
            ("Cloître des Chanoines", "+2 Rempart"),
            ("Porte Saint-Hélier", "+1 Servage, +1 Rempart"),
        ],
        "modifiers": [
            ("Firme", "+1 Servage"),
            ("Tribut reçu des Héritiers d'Alexandrie", "+1 Viandis"),
            ("Tribut versé à la Main du Prince", "-1 Rempart"),
        ],
        "summary": "Contrôle religieux très défensif. Les Archives du Chapitre ne leur appartiennent pas : elles restent à la Fondation, donc aucun bonus de contrôle complet de la Ceinture Sacrée n'est appliqué.",
    },
    "cot_fondation_pierre_noire": {
        "label": "La Fondation",
        "faction": "Camarilla",
        "type": "Fondation précaire",
        "domain": "Archives du Chapitre",
        "totals": {"viandis": 1, "servage": 1, "rempart": 0},
        "components": [
            ("Archives du Chapitre", "+1 Viandis, +1 Servage"),
        ],
        "modifiers": [],
        "summary": "Ancrage territorial minimal mais stratégique. La Fondation tient un point précis de la Ceinture Sacrée, pas la zone entière.",
    },
    "cot_heritiers_alexandrie": {
        "label": "Les Héritiers d'Alexandrie",
        "faction": "Camarilla",
        "type": "Bande de Crocs (+1 Viandis)",
        "domain": "Ombres des Rues / Bas-quartiers",
        "totals": {"viandis": 3, "servage": 2, "rempart": 1},
        "components": [
            ("Tanneries", "+2 Viandis"),
            ("Caves, ruines et souterrains", "+1 Rempart"),
            ("Quartier des paroisses populaires", "+1 Viandis, +1 Servage, +1 Rempart"),
            ("Contrôle complet des Ombres des Rues", "+1 Servage"),
        ],
        "modifiers": [
            ("Bande de Crocs", "+1 Viandis"),
            ("Tribut versé aux Gardiens du Sacré", "-1 Viandis"),
            ("Tribut versé aux Exécuteurs", "-1 Rempart"),
        ],
        "summary": "Le territoire produit beaucoup de sang, mais les deux tributs réduisent directement les ressources effectivement mobilisables de la coterie.",
    },
    "cot_crocs_silencieux": {
        "label": "Les Crocs Silencieux",
        "faction": "Camarilla",
        "type": "Sentinelles (+1 Rempart)",
        "domain": "Faubourgs Saint-Martin et Porte Saint-Martin",
        "totals": {"viandis": 2, "servage": 2, "rempart": 3},
        "components": [
            ("Saint-Martin", "+1 Viandis"),
            ("Jardins et Vignes", "+1 Viandis"),
            ("Ferme Fortifiée", "+1 Rempart"),
            ("Contrôle complet de Saint-Martin", "+1 Servage"),
            ("Porte Saint-Martin", "+1 Servage, +1 Rempart"),
        ],
        "modifiers": [
            ("Sentinelles", "+1 Rempart"),
        ],
        "summary": "Domaine de frontière équilibré et défensif. La mission juridique vers Saint-Germain ne transforme pas automatiquement Saint-Germain en domaine contrôlé ni en Viandis mobilisable.",
    },
    "cot_executeurs": {
        "label": "Les Exécuteurs",
        "faction": "Camarilla",
        "type": "Instrument de coercition",
        "domain": "Porte Madeleine et Porte Saint-Germain",
        "totals": {"viandis": 0, "servage": 2, "rempart": 3},
        "components": [
            ("Porte Madeleine", "+1 Servage, +1 Rempart"),
            ("Porte Saint-Germain", "+1 Servage, +1 Rempart"),
        ],
        "modifiers": [
            ("Tribut reçu des Héritiers d'Alexandrie", "+1 Rempart"),
        ],
        "summary": "Les Exécuteurs contrôlent des seuils et des moyens de coercition, pas un terrain nourricier. Leur Rempart effectif inclut le tribut Brujah.",
    },
    "cot_fracture": {
        "label": "La Fracture",
        "faction": "Anarchs",
        "type": "Saboteur (+1 Rempart)",
        "domain": "Faubourgs de la Madeleine",
        "totals": {"viandis": 2, "servage": 2, "rempart": 1},
        "components": [
            ("La Madeleine", "+1 Viandis"),
            ("Saint-Yves / Hospices", "+1 Viandis"),
            ("Hôpital des Pèlerins", "+1 Servage"),
            ("Contrôle complet de la Madeleine", "+1 Servage"),
        ],
        "modifiers": [
            ("Saboteur", "+1 Rempart"),
            ("Surveillance princière", "+1 difficulté aux chasses dans la Madeleine"),
            ("Action hostile ordinaire", "-1 dé à l'acteur"),
            ("Exception : Main du Prince ou autorité légale de Rennes", "+1 dé à l'acteur à la place de -1 dé"),
        ],
        "summary": "La répression princière complique la chasse. Le Rempart Saboteur reste dans le score effectif ; son modificateur d'action est inversé au bénéfice de la Main du Prince et de l'autorité mortelle légale de Rennes.",
    },
}


HUNT_ZONES: dict[str, HuntZone] = {
    "zone_coeur_bourgeois": {
        "id": "zone_coeur_bourgeois",
        "label": "Cœur Bourgeois",
        "points": [
            {"id": "loc_place_lices", "label": "Place des Lices", "controller_ref": "cot_main_prince"},
            {"id": "loc_maison_bourgeois", "label": "Maison des Bourgeois", "controller_ref": "cot_main_prince"},
            {"id": "loc_grand_comptoir", "label": "Grand Comptoir des Marchands", "controller_ref": "cot_main_prince"},
        ],
    },
    "zone_ceinture_sacree": {
        "id": "zone_ceinture_sacree",
        "label": "Ceinture Sacrée",
        "points": [
            {"id": "loc_cathedrale_st_pierre", "label": "Cathédrale Saint-Pierre", "controller_ref": "cot_gardiens_sacre"},
            {"id": "loc_cloitre_chanoines", "label": "Cloître des Chanoines", "controller_ref": "cot_gardiens_sacre"},
            {"id": "loc_archives_chapitre", "label": "Archives du Chapitre", "controller_ref": "cot_fondation_pierre_noire"},
        ],
    },
    "zone_ombres_rues": {
        "id": "zone_ombres_rues",
        "label": "Ombres des Rues / Bas-quartiers",
        "points": [
            {"id": "loc_tanneries", "label": "Tanneries", "controller_ref": "cot_heritiers_alexandrie"},
            {"id": "loc_caves_souterrains", "label": "Caves, ruines et souterrains", "controller_ref": "cot_heritiers_alexandrie"},
            {"id": "loc_quartier_paroisses_populaires", "label": "Quartier des paroisses populaires", "controller_ref": "cot_heritiers_alexandrie"},
        ],
    },
    "secteur_faubourgs_saint_michel": {
        "id": "secteur_faubourgs_saint_michel",
        "label": "Faubourgs Saint-Michel",
        "points": [
            {"id": "loc_faubourg_saint_michel", "label": "Saint-Michel", "controller_ref": None},
            {"id": "loc_saint_georges", "label": "Saint-Georges", "controller_ref": None},
            {"id": "loc_abbaye_saint_georges", "label": "Abbaye Saint-Georges", "controller_ref": None},
        ],
    },
    "secteur_faubourgs_saint_helier": {
        "id": "secteur_faubourgs_saint_helier",
        "label": "Faubourgs Saint-Hélier",
        "points": [
            {"id": "loc_faubourg_saint_helier", "label": "Saint-Hélier", "controller_ref": None},
            {"id": "loc_bourg_eveque", "label": "Bourg-l’Évêque", "controller_ref": None},
            {"id": "loc_relais_marchands", "label": "Relais des Marchands", "controller_ref": None},
        ],
    },
    "secteur_faubourgs_saint_germain": {
        "id": "secteur_faubourgs_saint_germain",
        "label": "Faubourgs Saint-Germain",
        "points": [
            {"id": "loc_faubourg_saint_germain", "label": "Saint-Germain", "controller_ref": None},
            {"id": "loc_tanneries_fleuve", "label": "Tanneries du Fleuve", "controller_ref": None},
            {"id": "loc_pont_vilaine", "label": "Pont de la Vilaine", "controller_ref": None},
            {"id": "zone_lisiere_bois_saint_germain", "label": "Lisière et bois de Saint-Germain", "controller_ref": None},
        ],
    },
    "secteur_faubourgs_madeleine": {
        "id": "secteur_faubourgs_madeleine",
        "label": "Faubourgs de la Madeleine",
        "difficulty_modifier": 1,
        "difficulty_origin": "Surveillance princière de la Madeleine",
        "points": [
            {"id": "loc_faubourg_madeleine", "label": "La Madeleine", "controller_ref": "cot_fracture"},
            {"id": "loc_saint_yves", "label": "Saint-Yves / Hospices", "controller_ref": "cot_fracture"},
            {"id": "loc_hopital_pelerins", "label": "Hôpital des Pèlerins", "controller_ref": "cot_fracture"},
        ],
    },
    "secteur_faubourgs_saint_martin": {
        "id": "secteur_faubourgs_saint_martin",
        "label": "Faubourgs Saint-Martin",
        "points": [
            {"id": "loc_faubourg_saint_martin", "label": "Saint-Martin", "controller_ref": "cot_crocs_silencieux"},
            {"id": "loc_jardins_vignes", "label": "Jardins et Vignes", "controller_ref": "cot_crocs_silencieux"},
            {"id": "loc_ferme_fortifiee", "label": "Ferme Fortifiée", "controller_ref": "cot_crocs_silencieux"},
        ],
    },
}


def effective_viandis_for_hunt(coterie_ref: str | None, point: PointHunt) -> int:
    """Retourne le Viandis mobilisable sans inventer de contrôle territorial.

    Le score effectif vient de 07. Il n'est appliqué que si le point choisi est
    actuellement contrôlé par cette coterie dans cette projection runtime.
    """
    if not coterie_ref or point.get("controller_ref") != coterie_ref:
        return 0
    domain = COTERIE_DOMAINS.get(coterie_ref)
    if not domain:
        return 0
    return int(domain["totals"]["viandis"])


def coterie_label(coterie_ref: str | None) -> str:
    if not coterie_ref:
        return "Aucun domaine reconnu"
    return str(COTERIE_DOMAINS.get(coterie_ref, {}).get("label", coterie_ref))
