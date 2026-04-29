"""Scène-outil : générateur de rencontres de chasse (MJ).

⚠️ Cette scène est un *outil* : le résultat final est un tableau.
Le moteur de scène "choix -> transcript" n'est pas utilisé ici.

Pour rester compatible avec la validation (une scène doit avoir au moins 1 choix),
on fournit un choix "Retour accueil" qui termine immédiatement la scène.
L'UI détecte l'ID de scène et affiche l'outil dédié.

Tables (placeholders ou contenu réel) : data/hunt_tables.py
"""

from __future__ import annotations

from domain.schema import Scene, Choice


SCENE_ID = "generateur_de_chasse"


def get_scene() -> Scene:
    return Scene(
        id=SCENE_ID,
        title="Générateur de chasse (MJ)",
        intro_md=(
            "Outil MJ : génère des rencontres de chasse aléatoires.\n\n"
            "**ID : generateur_de_chasse**\n\n"
            "Sélectionne un ou plusieurs styles de prédation, puis génère un tableau.\n"
            "Les textes sont pré-écrits dans les tables (placeholders tant que tu ne les as pas remplis)."
        ),
        # Choix minimal uniquement pour satisfaire la validation/compatibilité du moteur.
        choices=[
            Choice(
                id="retour_accueil",
                label="Retour accueil",
                answer_md="",
                followups=[],
                ends_scene=True,
            )
        ],
    )
