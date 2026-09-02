"""Scène-outil : assistant de chasse pour le MJ.

Le moteur narratif standard n'est pas utilisé pour résoudre la chasse : l'UI
reconnaît cet ID et affiche l'outil dédié. Le choix minimal existe uniquement
pour satisfaire la validation générale des scènes.
"""

from __future__ import annotations

from domain.schema import Choice, Scene


SCENE_ID = "generateur_de_chasse"


def get_scene() -> Scene:
    return Scene(
        id=SCENE_ID,
        title="Assistant de chasse — Rennes 1505 (MJ)",
        intro_md=(
            "Outil MJ dérivé du canon actif du Drive.\n\n"
            "Il croise la **coterie**, le **Predator Type habituel**, le **style utilisé cette nuit**, "
            "la **zone** et le **point d'intérêt canonique**. Il affiche ensuite les modificateurs de "
            "Viandis et la difficulté de chasse à appliquer au **jet physique**.\n\n"
            "Les 18 Predator Types V5 servent de référentiel. Les grandes tables déjà écrites dans le dépôt "
            "restent disponibles comme **tables narratives locales optionnelles**.\n\n"
            "Un tirage ou un clic dans cet outil reste une préparation : il ne constitue ni une scène jouée, "
            "ni un événement canonique, ni une connaissance acquise par un PJ."
        ),
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
