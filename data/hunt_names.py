from __future__ import annotations

"""Noms de circonstance pour les rencontres de chasse enrichies.

Ces noms sont de la préparation MJ non canonique. Ils deviennent des identités
persistantes seulement si la rencontre est effectivement jouée puis consolidée
dans le propriétaire PNJ approprié.
"""

PREPARED_HUNT_NAMES: dict[str, list[tuple[str, str]]] = {
    "osiris_muse": [
        ("Une noble mariée te demande un poème", "Dame Perrine de Keravel"),
        ("Un cercle d’art fermé débat de ton œuvre", "Maître Colin Le Saux — hôte du cercle"),
        ("Banquet chez un marchand influent", "Jehan Le Berre — marchand et hôte"),
        ("Dans un salon feutré, un homme te demande un poème", "Mathurin Le Guern"),
    ],
    "rat_egouts": [
        ("Un jeune noble exige une saignée tardive", "Gilles de Kerbrat"),
        ("Un noble du cœur bourgeois intra-muros est saigné", "Raoul de Penhoët — patient ; Martin Le Floch — domestique"),
        ("Un magistrat influent souffre de migraines", "Maître Alain Rivoal"),
        ("Un professeur de droit canon vient pour une saignée discrète", "Maître Étienne Le Borgne"),
        ("Un blessé amené en urgence suite à une impressionante entaille", "Hervé Le Veyer — blessé ; Aélis Lannur — accompagnatrice"),
    ],
    "justicier_nocturne": [
        ("Un usurier manipule les comptes des artisans", "Colin Boterel — usurier"),
        ("Un réseau protégé par la garde opère en silence", "Sergent Gautier Rivel — premier relais visible"),
        ("Un réseau d’enlèvements organisé opère sous la tannerie", "Robin Tesson — chef local présumé"),
        ("Un maître tortionnaire organise enlèvements et supplices", "Gautier Malherbe — maître du nœud local"),
        ("Un sorcier exalté enlève des pauvres", "Maël Kergoat — sorcier de la cellule locale"),
    ],
    "roi_de_la_nuit": [
        ("Un jeune noble rennais sollicite une annulation discrète", "Gilles de Kervadec"),
        ("Une veuve influente cherche l’appui du Chapitre", "Dame Alix de Brézal"),
        ("Une maison rennaise aux ambitions croissantes veut que le Chapitre", "Maître Alain Bréhand — représentant de la maison"),
        ("Un dossier évoque indirectement le pouvoir ducal", "Maître Guillaume Le Mézec — porteur du dossier"),
        ("Un arrangement matrimonial, présenté comme canonique", "Hervé de Kerlouët — négociateur principal"),
        ("Le Gardien du Tribunal Canonique vous convoque", "Maître Olivier de Kergoët — Gardien du Tribunal"),
        ("Un Inquisiteur ‘de passage’ (Frère Séverin d’Angers)", "Frère Séverin d’Angers"),
    ],
}


def find_hunt_prepared_name(table_id: str, rencontre: str | None) -> str | None:
    if not rencontre:
        return None
    folded = rencontre.casefold()
    for match, name in PREPARED_HUNT_NAMES.get(table_id, []):
        if match.casefold() in folded:
            return name
    return None
