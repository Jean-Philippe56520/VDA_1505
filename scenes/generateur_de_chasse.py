"""Scène-outil : générateur de chasse express pour le MJ.

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
        title="Générateur de chasse express — Rennes 1505 (MJ)",
        intro_md=(
            "Outil MJ dérivé du canon actif du Drive, conçu pour enchaîner rapidement plusieurs chasses à la table.\n\n"
            "Sélectionne une ou plusieurs **tables de rencontre**, puis choisis pour chacune le **style utilisé**, "
            "le **territoire / la coterie sur lequel la chasse a lieu** et le **point d'intérêt canonique**. "
            "L'outil affiche seulement un mémo compact : contrôle, Viandis du territoire, surveillance éventuelle, "
            "style inadapté (+2 difficulté) ou interdiction.\n\n"
            "La qualification automatique **style × point d'intérêt** utilise actuellement une matrice préparatoire "
            "dérivée des descriptions de lieux de 05 : elle sert d'aide MJ et reste à valider comme canon exact.\n\n"
            "Les rencontres sélectionnées peuvent être générées ensemble et restent visibles dans des "
            "**bulles indépendantes**, chacune relançable séparément. Les dés et la décision du résultat restent physiques.\n\n"
            "Rappel : succès = difficulté donne une **Victoire à la Pyrrhus** ; une **Victoire critique prime**. "
            "Résonance, tempérament et effet spécial peuvent être affichés avant le jet comme mémo MJ, mais ne sont "
            "acquis que si la chasse réussit.\n\n"
            "Les préréglages de style du Git sont ergonomiques et modifiables : ils ne définissent pas le Predator Type "
            "canonique d'un PJ. Un tirage ou un clic dans cet outil reste une préparation et ne constitue ni scène jouée, "
            "ni événement canonique, ni connaissance acquise par un PJ."
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
