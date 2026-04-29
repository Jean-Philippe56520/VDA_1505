from domain.schema import Scene, Choice


# =========================================================
# Helpers
# =========================================================
def _hub_choices() -> list[Choice]:
    """
    Hub central : choisir un PNJ à approcher.

    IMPORTANT :
    Le moteur valide l'arbre de choix en parcourant récursivement `followups`.
    Il faut donc un arbre *acyclique* : on ne peut pas "revenir au hub" en
    ré-injectant `_hub_choices()` dans un followup (sinon récursion infinie).

    Note :
    Cette scène fonctionne en "chapitres" : une interaction = une fin de scène,
    puis on relance la scène si on veut parler à quelqu’un d’autre.
    """
    return [
        Choice(id="pick_ronan", label="Approcher Ronan l’Ébréché (Brujah)", answer_md="", followups=_ronan_entry()),
        Choice(id="pick_ysoria", label="Approcher Ysoria la Silencieuse (Tremere)", answer_md="", followups=_ysoria_entry()),
        Choice(id="pick_maloch", label="Approcher Frère Maloch l’Insondable (Malkavien)", answer_md="", followups=_maloch_entry()),
        Choice(id="pick_ysabeau", label="Approcher Ysabeau des Voûtes (Nosferatu)", answer_md="", followups=_ysabeau_entry()),
        Choice(id="pick_maela", label="Approcher Maëla la Veilleuse (Gangrel)", answer_md="", followups=_maela_entry()),
        Choice(id="pick_aodren", label="Approcher Aodren Croc-Fendu (Gangrel)", answer_md="", followups=_aodren_entry()),
        Choice(id="pick_heloise", label="Approcher Héloïse de Fougères (Ventrue)", answer_md="", followups=_heloise_entry()),
        Choice(id="pick_jehanne", label="Croiser Jehanne, goule de la garde", answer_md="", followups=_jehanne()),
        Choice(
            id="end_night",
            label="Se retirer et clore la nuit",
            answer_md=(
                "Vous vous écartez des cercles de parole, gagnant une zone d’ombre entre deux arcades.\n\n"
                "Les voix demeurent basses et serrées, comme si chaque syllabe devait payer sa dîme.\n\n"
                "Vous avez assez vu. Ce soir, la cour n’offrira rien de plus que des présages.\n\n"
                "**Fin du chapitre I.**"
            ),
            ends_scene=True,
        ),
    ]


def _back_to_hub(label: str = "Revenir parmi les groupes") -> Choice:
    """
    Retour "sûr" : termine proprement l'échange (pas de boucle dans followups).
    """
    return Choice(
        id=f"back_{_slug(label)}",
        label=label,
        answer_md=(
            "Vous rompez l’échange sans éclat. Dans cette cour, savoir quand se taire "
            "vaut parfois mieux que savoir parler."
        ),
        followups=[],
        ends_scene=True,
    )


def _slug(s: str) -> str:
    return "".join(ch.lower() for ch in s if ch.isalnum() or ch == "_")[:32] or "x"


def _roll_gate_md(difficulty: int, target: str) -> str:
    """
    Texte standard à afficher AVANT les boutons Réussite/Échec.

    Ici, le *premier* jet social sert surtout à obtenir un **aparté** (un échange
    discret) : une approche correcte, une formule juste, le bon moment, le bon
    angle pour s’isoler du cercle.

    Le MJ choisit ensuite l'issue.
    """
    return (
        f"**Test d’Étiquette (MJ)** — Difficulté {difficulty}\n\n"
        "Objectif : obtenir un **aparté** avec "
        f"{target} (quelques pas à l’écart, voix basse, hors des oreilles immédiates).\n\n"
        "**Avant de trancher Réussite / Échec :**\n"
        "le personnage peut, s’il le souhaite, **promettre une faveur mineure** "
        "(un service simple, plus tard) pour **réduire la difficulté de 1**.\n\n"
        f"👉 MJ : choisis l’issue pour {target}."
    )


# =========================================================
# Ronan (Brujah) — version inchangée sur le fond, juste ajout d’un “entry”
# =========================================================
def _ronan_entry() -> list[Choice]:
    return [
        Choice(
            id="ronan_setup",
            label="Prendre la parole (tenter un aparté) et tenter d’ouvrir l’échange",
            answer_md=(
                "Ronan ne se cache pas. Il ne chuchote pas. Il **assume** sa présence.\n\n"
                "Tu mesures les regards, le rang, les oreilles. Quelques mots convenus, puis tu tentes d’obtenir **un aparté** à l’écart.\n\n"
                + _roll_gate_md(3, "Ronan")
            ),
            followups=_ronan_t1(),
        )
    ]


def _ronan_t1() -> list[Choice]:
    return [
        Choice(
            id="ronan_t1_fail",
            label="Résultat : Échec",
            answer_md=(
                "Ronan plisse les yeux. "
                "« Trop de mots. On dirait un serment appris par cœur. »"
            ),
            followups=[_back_to_hub("S’éloigner (Ronan se ferme)")],
        ),
        Choice(
            id="ronan_t1_success",
            label="Résultat : Réussite",
            answer_md=(
                "« Ici, chacun a son histoire prête à servir. "
                "Celles-là sont faites pour endormir. »\n\n"
                "*Indice idéologique (incertain) : Ambigu.*"
            ),
            followups=_ronan_t2(),
        ),
        Choice(
            id="ronan_t1_crit",
            label="Résultat : Réussite critique",
            answer_md=(
                "« Tu n’as pas l’odeur des courtisans. "
                "Écoute : certains préfèrent qu’on regarde ailleurs. »\n\n"
                "*Indice idéologique (incertain) : Ambigu.*"
            ),
            followups=_ronan_t2(),
        ),
    ]



def _ronan_t2() -> list[Choice]:
    return [
        Choice(
            id="ronan_t2_fail",
            label="Approfondir : Échec",
            answer_md="« Ça suffit. Tu attires l’œil… et l’œil attire le couperet. »",
            followups=[_back_to_hub("Revenir (Ronan coupe court)")],
        ),
        Choice(
            id="ronan_t2_success",
            label="Approfondir : Réussite",
            answer_md=(
                "« Ceux qu’on fait disparaître ne sont pas les plus dangereux. "
                "Ce sont ceux qui croient encore… et qui le montrent. »\n\n"
                "*Indice idéologique : Ambigu (confirmé).*"
            ),
            followups=[_back_to_hub()],
        ),
        Choice(
            id="ronan_t2_crit",
            label="Approfondir : Réussite critique",
            answer_md=(
                "« On ne teste pas la force. On teste l’obéissance. Et la moitié plie avant même qu’on pousse. »\n\n"
                "*Indice idéologique : Ambigu (confirmé).*"
            ),
            followups=[_back_to_hub()],
        ),
    ]


# =========================================================
# Ysoria (Tremere) — entry ajouté
# =========================================================
def _ysoria_entry() -> list[Choice]:
    return [
        Choice(
            id="ysoria_setup",
            label="Approcher avec Étiquette (aparté, voix mesurée)",
            answer_md=(
                "Ysoria est immobile, comme si l’air avait peur de la déranger.\n\n"
                "Tu appliques l’étiquette : salut, distance, formule. Puis tu cherches le moment pour obtenir **un aparté**, à voix basse.\n\n"
                + _roll_gate_md(3, "Ysoria")
            ),
            followups=_ysoria_t1(),
        )
    ]


def _ysoria_t1() -> list[Choice]:
    return [
        Choice(
            id="ysoria_t1_fail",
            label="Résultat : Échec",
            answer_md="« Votre manière manque de rigueur. » Son regard devient glacial, sans appel.",
            followups=[_back_to_hub("S’éloigner (froideur ouverte)")],
        ),
        Choice(
            id="ysoria_t1_success",
            label="Résultat : Réussite",
            answer_md=(
                "« La cité endure parce qu’elle accepte ce qui doit être sacrifié. »\n\n"
                "*Indice idéologique (trouble) : Camarilla loyale.*"
            ),
            followups=_ysoria_t2(),
        ),
        Choice(
            id="ysoria_t1_crit",
            label="Résultat : Réussite critique",
            answer_md=(
                "« Vous observez sans trembler. C’est… utile. »\n\n"
                "*Indice idéologique (trouble) : Camarilla loyale.*"
            ),
            followups=_ysoria_t2(),
        ),
    ]


def _ysoria_t2() -> list[Choice]:
    return [
        Choice(
            id="ysoria_t2_fail",
            label="Approfondir : Échec",
            answer_md="« Cette conversation n’aurait jamais dû commencer. »",
            followups=[_back_to_hub("Revenir (porte close)")],
        ),
        Choice(
            id="ysoria_t2_success",
            label="Approfondir : Réussite",
            answer_md=(
                "« La loyauté est une matière. Ceux qui la croient de pierre découvrent qu’elle se brise. »\n\n"
                "*Indice idéologique : Camarilla pragmatique.*"
            ),
            followups=[_back_to_hub()],
        ),
        Choice(
            id="ysoria_t2_crit",
            label="Approfondir : Réussite critique",
            answer_md=(
                "Elle baisse la voix, comme on ferme une serrure.\n\n"
                "« La foi n’est qu’un outil. Et les outils s’usent… ou se remplacent. »\n\n"
                "*Indice idéologique : Camarilla hypocrite (clair).*"
            ),
            followups=[_back_to_hub()],
        ),
    ]


# =========================================================
# Maloch (Malkavien) — enrichi pour “déclamation loyale au Prince” + message au Prince
# =========================================================
def _maloch_entry() -> list[Choice]:
    return [
        Choice(
            id="maloch_setup",
            label="Approcher Maloch (tenter un aparté) et tenter d’être entendu sans se perdre",
            answer_md=(
                "Frère Maloch est là comme une fissure dans le décor.\n\n"
                "Tu avances prudemment. Avec Maloch, la première victoire est d’être **accepté** assez près pour un aparté — sans attirer d’yeux.\n\n"
                + _roll_gate_md(4, "Maloch")
            ),
            followups=_maloch_t1(),
        )
    ]


def _maloch_t1() -> list[Choice]:
    return [
        Choice(
            id="maloch_t1_fail",
            label="Résultat : Échec",
            answer_md="« Tu cherches des réponses. Moi, je n’ai que des plaies ouvertes. »",
            followups=[_back_to_hub("Reculer (présence malsaine)")],
        ),
        Choice(
            id="maloch_t1_success",
            label="Résultat : Réussite",
            answer_md=(
                "« Les plus fervents tombent d’abord. Comme appelés… comme aspirés. »\n\n"
                "*Indice idéologique (confus) : Camarilla loyale.*"
            ),
            followups=_maloch_t2(),
        ),
        Choice(
            id="maloch_t1_crit",
            label="Résultat : Réussite critique",
            answer_md=(
                "« Tu entends le silence derrière les sourires. Peu savent l’écouter sans s’y perdre. »\n\n"
                "*Indice idéologique (confus) : Camarilla loyale.*"
            ),
            followups=_maloch_t2(),
        ),
    ]


def _maloch_t2() -> list[Choice]:
    return [
        Choice(
            id="maloch_t2_fail",
            label="Approfondir : Échec",
            answer_md="« Pas ce soir. Ton sang fait trop de bruit. »",
            followups=[_back_to_hub("Revenir (les mots meurent)")],
        ),
        Choice(
            id="maloch_t2_success",
            label="Approfondir : Réussite",
            answer_md=(
                "« On ne teste pas les crocs. On teste la foi. Et beaucoup choisissent de vivre… "
                "quitte à se renier. »\n\n"
                "*Indice idéologique : Camarilla loyale.*\n\n"
                "Maloch ne promet rien. Il ne transmet rien. "
                "Il te laisse seulement avec une vérité qui gratte sous la peau."
            ),
            followups=[_back_to_hub("Revenir (un goût de cendre)")],
        ),
        Choice(
            id="maloch_t2_crit",
            label="Approfondir : Réussite critique",
            answer_md=(
                "« Quand il n’y aura plus de croyants… il ne restera qu’une cage. "
                "Et dans une cage, tout le monde finit par mordre les barreaux. »\n\n"
                "*Indice idéologique : Camarilla loyale.*\n\n"
                "Son regard s’attarde, lourd, puis s’éloigne. "
                "Pas de promesse. Pas de relais. Juste un avertissement."
            ),
            followups=[_back_to_hub("Revenir (avertissement reçu)")],
        ),
    ]


# =========================================================
# Ysabeau (Nosferatu) — enrichi pour “déclamation loyale au Prince” + message au Prince
# =========================================================
def _ysabeau_entry() -> list[Choice]:
    return [
        Choice(
            id="ysabeau_setup",
            label="Approcher Ysabeau (tenter un aparté) sans donner l’impression de ‘prendre’",
            answer_md=(
                "Ysabeau est là où les ombres semblent plus épaisses.\n\n"
                "Tu ne réclames rien. Tu cherches d’abord à être **toléré**, puis à obtenir un aparté — un coin d’ombre, deux pas de côté.\n\n"
                + _roll_gate_md(4, "Ysabeau")
            ),
            followups=_ysabeau_t1(),
        )
    ]


def _ysabeau_t1() -> list[Choice]:
    return [
        Choice(
            id="ysabeau_t1_fail",
            label="Résultat : Échec",
            answer_md="« Tu regardes trop. Ici, regarder, c’est déjà prendre. »",
            followups=[_back_to_hub("Revenir (ombre fuyante)")],
        ),
        Choice(
            id="ysabeau_t1_success",
            label="Résultat : Réussite",
            answer_md=(
                "« Les absences parlent plus fort que les présents. Et ce soir, il manque du monde. »\n\n"
                "*Indice idéologique (incertain) : Ambigu.*"
            ),
            followups=_ysabeau_t2(),
        ),
        Choice(
            id="ysabeau_t1_crit",
            label="Résultat : Réussite critique",
            answer_md=(
                "Elle esquisse un sourire qui n’a rien d’aimable.\n\n"
                "« Tu sais te faire petit. C’est une vertu rare, ici. »\n\n"
                "*Indice idéologique (incertain) : Ambigu.*"
            ),
            followups=_ysabeau_t2(),
        ),
    ]


def _ysabeau_t2() -> list[Choice]:
    return [
        Choice(
            id="ysabeau_t2_fail",
            label="Approfondir : Échec",
            answer_md="« Non. Tu n’es pas un secret sûr. »",
            followups=[_back_to_hub("Revenir (porte close)")],
        ),
        Choice(
            id="ysabeau_t2_success",
            label="Approfondir : Réussite",
            answer_md=(
                "« Les récits tiennent parce que certains les tiennent… à deux mains. "
                "Et ces mains-là ne sont pas celles des humbles. »\n\n"
                "*Indice idéologique : Ambigu (confirmé).*\n\n"
                "Tu peux t’arrêter… ou tenter une **déclamation publique loyale au Prince** "
                "en montrant une loyauté qui n’efface pas la vérité."
            ),
            followups=_ysabeau_declame_gate(),
        ),
        Choice(
            id="ysabeau_t2_crit",
            label="Approfondir : Réussite critique",
            answer_md=(
                "« Il y en a qui ‘servent’ l’ordre en étouffant la vérité. "
                "Ce n’est pas de la loyauté. C’est du confort. »\n\n"
                "*Indice : hypocrisie possible chez des figures ‘respectables’.*\n\n"
                "Moment tendu. Si tu le veux, tu peux répondre par une **déclamation publique** :\n"
                "montrer ton attachement au Prince sans réclamer de secrets, et sans salir qui que ce soit."
            ),
            followups=_ysabeau_declame_gate(),
        ),
    ]


def _ysabeau_declame_gate() -> list[Choice]:
    return [
        Choice(
            id="ysabeau_declame_setup",
            label="Faire une déclamation publique pro-Prince (sans quémander de secrets)",
            answer_md=(
                "Tu prends la parole **à haute voix**. Tu ne demandes rien.\n\n"
                "Tu dis :\n"
                "« Je ne viens pas acheter des vérités. Je viens montrer que je fais confiance au Prince, "
                "comme je fais confiance à mon Sire : parce que l’ordre a un prix… et que quelqu’un le paie. »\n\n"
                + _roll_gate_md(4, "la déclamation devant Ysabeau")
            ),
            followups=[
                Choice(
                    id="ysabeau_declame_fail",
                    label="Déclamation : Échec",
                    answer_md=(
                        "Ysabeau laisse un silence trop long.\n\n"
                        "« Beau. Trop beau. »\n\n"
                        "Elle te jauge : « Ici, les belles phrases servent souvent à cacher un besoin. »\n\n"
                        "Tu n’es pas humilié… mais tu n’es pas validé."
                    ),
                    followups=[_back_to_hub("Revenir (elle reste insaisissable)")],
                ),
                Choice(
                    id="ysabeau_declame_success",
                    label="Déclamation : Réussite",
                    answer_md=(
                        "Ysabeau incline à peine la tête. C’est déjà beaucoup.\n\n"
                        "« Tu n’as pas essayé de me voler. Tu as parlé pour être vu… mais pas pour prendre. »\n\n"
                        "Puis, devant témoins :\n"
                        "**« Très bien. J’en toucherai deux mots au Prince. »**"
                    ),
                    followups=[_back_to_hub("Revenir (le Prince saura)")],
                ),
                Choice(
                    id="ysabeau_declame_crit",
                    label="Déclamation : Réussite critique",
                    answer_md=(
                        "Une approbation discrète circule : pas des sourires, des regards.\n\n"
                        "Ysabeau tranche : « Tu as compris la seule politesse qui compte ici : "
                        "ne pas prendre ce qui n’est pas offert. »\n\n"
                        "Et elle prononce, calmement, la phrase qui change ton statut :\n"
                        "**« Très bien. J’en toucherai deux mots au Prince. »**\n\n"
                        "Ce n’est pas une promesse : c’est une mise en circulation."
                    ),
                    followups=[_back_to_hub("Revenir (meilleure impression)")],
                ),
            ],
        ),
        _back_to_hub("S’arrêter là (ne pas faire de déclamation)"),
    ]


# =========================================================
# Maëla (Gangrel) — entry ajouté
# =========================================================
def _maela_entry() -> list[Choice]:
    return [
        Choice(
            id="maela_setup",
            label="Approcher Maëla (tenter un aparté) sans ‘politique de salon’",
            answer_md=(
                "Maëla te jauge comme on jauge un terrain.\n\n"
                "Tu évites les politesses de salon. Quelques mots francs, puis tu tentes un aparté, loin des cercles.\n\n"
                + _roll_gate_md(3, "Maëla")
            ),
            followups=_maela_t1(),
        )
    ]


def _maela_t1() -> list[Choice]:
    return [
        Choice(
            id="maela_t1_fail",
            label="Résultat : Échec",
            answer_md="« Les cours me donnent la nausée. Garde tes politesses. »",
            followups=[_back_to_hub("Revenir (distance)")],
        ),
        Choice(
            id="maela_t1_success",
            label="Résultat : Réussite",
            answer_md=(
                "« La lisière est nerveuse. Trop de pas, trop de chiens, trop de prières dites de travers. »\n\n"
                "*Indice idéologique (incertain) : Ambigu.*"
            ),
            followups=_maela_t2(),
        ),
        Choice(
            id="maela_t1_crit",
            label="Résultat : Réussite critique",
            answer_md=(
                "« Tu ne sens pas la terre. Mais tu sens la peur. Ça suffit parfois. »\n\n"
                "*Indice idéologique (incertain) : Ambigu.*"
            ),
            followups=_maela_t2(),
        ),
    ]


def _maela_t2() -> list[Choice]:
    return [
        Choice(
            id="maela_t2_fail",
            label="Approfondir : Échec",
            answer_md="« Non. Pas ici. Les murs ont des oreilles, et les oreilles ont des maîtres. »",
            followups=[_back_to_hub("Revenir (silence)")],
        ),
        Choice(
            id="maela_t2_success",
            label="Approfondir : Réussite",
            answer_md=(
                "« Les loups ne font pas tout. Il y avait autre chose… une vieille faim, plus ancienne que leurs crocs. »\n\n"
                "*Indice idéologique : Ambigu (confirmé).*"
            ),
            followups=[_back_to_hub()],
        ),
        Choice(
            id="maela_t2_crit",
            label="Approfondir : Réussite critique",
            answer_md=(
                "« Si on recule, on ne ‘gagne’ pas la paix. On ouvre la porte. Et ce qui entrera ne négociera pas. »\n\n"
                "*Indice idéologique : Ambigu (confirmé).*"
            ),
            followups=[_back_to_hub()],
        ),
    ]


# =========================================================
# Aodren (Gangrel) — entry ajouté
# =========================================================
def _aodren_entry() -> list[Choice]:
    return [
        Choice(
            id="aodren_setup",
            label="Approcher Aodren (tenter un aparté) malgré l’hostilité",
            answer_md=(
                "Aodren ne joue pas la cour. Il la subit.\n\n"
                "Tu t’approches sans provoquer. Tu attends une faille dans la tension, puis tu tentes d’obtenir un aparté.\n\n"
                + _roll_gate_md(3, "Aodren")
            ),
            followups=_aodren_t1(),
        )
    ]


def _aodren_t1() -> list[Choice]:
    return [
        Choice(
            id="aodren_t1_fail",
            label="Résultat : Échec",
            answer_md="« Je n’ai rien pour toi. Va nourrir ton orgueil ailleurs. »",
            followups=[_back_to_hub("Revenir (hostilité)")],
        ),
        Choice(
            id="aodren_t1_success",
            label="Résultat : Réussite",
            answer_md=(
                "« Vous appelez ça l’ordre. Moi j’appelle ça une cage qui rétrécit à chaque lune. »\n\n"
                "*Indice idéologique (incertain) : Indépendant.*"
            ),
            followups=_aodren_t2(),
        ),
        Choice(
            id="aodren_t1_crit",
            label="Résultat : Réussite critique",
            answer_md=(
                "Il vous jauge, puis crache presque les mots.\n\n"
                "« Une phrase : ils vont faire du vide. Et ils diront que c’est pour notre bien. »\n\n"
                "*Indice idéologique (incertain) : Ambigu.*"
            ),
            followups=_aodren_t2(),
        ),
    ]


def _aodren_t2() -> list[Choice]:
    return [
        Choice(
            id="aodren_t2_fail",
            label="Approfondir : Échec",
            answer_md="« Assez. Je t’ai trop parlé. »",
            followups=[_back_to_hub("Revenir (coupure nette)")],
        ),
        Choice(
            id="aodren_t2_success",
            label="Approfondir : Réussite",
            answer_md=(
                "« Réduire nos terres, c’est inviter le pire. Un no man’s land, ça n’existe pas : "
                "quelqu’un finit toujours par s’y installer. »\n\n"
                "*Indice idéologique : Indépendant (confirmé).*"
            ),
            followups=[_back_to_hub()],
        ),
        Choice(
            id="aodren_t2_crit",
            label="Approfondir : Réussite critique",
            answer_md=(
                "« Quand l’Elysium ne sera plus qu’un mot, vous comprendrez. "
                "Ce qui viendra après ne respectera aucune loi. »\n\n"
                "*Indice idéologique : Indépendant (confirmé).*"
            ),
            followups=[_back_to_hub()],
        ),
    ]


# =========================================================
# Héloïse (Ventrue) — enrichi pour “déclamation loyale au Prince” + message au Prince
# =========================================================
def _heloise_entry() -> list[Choice]:
    return [
        Choice(
            id="heloise_setup",
            label="Approcher Héloïse (tenter un aparté) avec tenue et loyauté affichée",
            answer_md=(
                "Héloïse est une Ventrue : la forme n’est pas un décor, c’est une armure.\n\n"
                "Tu respectes la forme, puis tu tentes d’obtenir un aparté : un échange bref, discret, sans offrir un spectacle.\n\n"
                + _roll_gate_md(3, "Héloïse")
            ),
            followups=_heloise_t1(),
        )
    ]


def _heloise_t1() -> list[Choice]:
    return [
        Choice(
            id="heloise_t1_fail",
            label="Résultat : Échec",
            answer_md="« Je ne puis me permettre ce genre de propos. » Elle se détourne sans hâte.",
            followups=[_back_to_hub("Revenir (prudence)")],
        ),
        Choice(
            id="heloise_t1_success",
            label="Résultat : Réussite",
            answer_md=(
                "« L’ordre protège la cité… du moins, c’est ce qu’on nous a appris. »\n\n"
                "*Indice idéologique (incertain) : Camarilla loyale.*"
            ),
            followups=_heloise_t2(),
        ),
        Choice(
            id="heloise_t1_crit",
            label="Résultat : Réussite critique",
            answer_md=(
                "Elle hésite.\n\n"
                "« J’ai… des doutes. Mais ici, les doutes se paient. »\n\n"
                "*Indice idéologique (incertain) : Ambigu.*"
            ),
            followups=_heloise_t2(),
        ),
    ]


def _heloise_t2() -> list[Choice]:
    return [
        Choice(
            id="heloise_t2_fail",
            label="Approfondir : Échec",
            answer_md="« Non. Pardon. Je dois rester prudente. »",
            followups=[_back_to_hub("Revenir (elle se ferme)")],
        ),
        Choice(
            id="heloise_t2_success",
            label="Approfondir : Réussite",
            answer_md=(
                "« Je n’ai jamais vu autant de silence. Comme si la loyauté elle-même était devenue dangereuse. »\n\n"
                "*Indice idéologique : Camarilla loyale (confirmé).*\n\n"
                "Tu peux maintenant, si tu le souhaites, tenter une **déclamation publique** :\n"
                "dire du bien du Prince (actions passées, tenue, coût payé), et montrer ta confiance "
                "comme envers ton Sire — pour obtenir la meilleure impression."
            ),
            followups=_heloise_declame_gate(),
        ),
        Choice(
            id="heloise_t2_crit",
            label="Approfondir : Réussite critique",
            answer_md=(
                "« Certains portent la Camarilla comme un manteau… pour cacher le couteau. "
                "Ce n’est pas la loyauté. C’est l’ambition. »\n\n"
                "*Indice : hypocrisie possible chez des figures ‘respectables’.*\n\n"
                "Moment fort. Si tu le veux, tu peux répondre par une **déclamation pro-Prince** "
                "à haute voix, sans flatterie grossière, juste un témoignage propre."
            ),
            followups=_heloise_declame_gate(),
        ),
    ]


def _heloise_declame_gate() -> list[Choice]:
    return [
        Choice(
            id="heloise_declame_setup",
            label="Faire une déclamation publique pro-Prince (loyauté visible, tenue Ventrue)",
            answer_md=(
                "Tu prends la parole **à haute voix**.\n\n"
                "Tu évoques un geste du Prince : arbitrage, sanction, protection, coût politique.\n"
                "Tu poses une phrase simple, stable :\n"
                "« Je lui fais confiance comme à mon Sire : parce qu’il tient l’ordre quand d’autres hésitent. »\n\n"
                + _roll_gate_md(3, "la déclamation devant Héloïse")
            ),
            followups=[
                Choice(
                    id="heloise_declame_fail",
                    label="Déclamation : Échec",
                    answer_md=(
                        "Héloïse garde son masque.\n\n"
                        "« Bien dit… mais trop exposé. »\n\n"
                        "Elle te protège d’un geste : « Ne te fais pas remarquer pour de mauvaises raisons. »\n\n"
                        "Tu n’as pas humilié, mais tu n’as pas gagné de recommandation."
                    ),
                    followups=[_back_to_hub("Revenir (correct, sans plus)")],
                ),
                Choice(
                    id="heloise_declame_success",
                    label="Déclamation : Réussite",
                    answer_md=(
                        "Héloïse te regarde, puis acquiesce : sobre, public, net.\n\n"
                        "« C’est une loyauté qui comprend la structure. »\n\n"
                        "Et elle prononce, devant témoins :\n"
                        "**« Très bien. J’en toucherai deux mots au Prince. »**"
                    ),
                    followups=[_back_to_hub("Revenir (appui obtenu)")],
                ),
                Choice(
                    id="heloise_declame_crit",
                    label="Déclamation : Réussite critique",
                    answer_md=(
                        "Un léger mouvement dans les cercles de parole : on a entendu.\n\n"
                        "Héloïse te valide sans t’écraser :\n"
                        "« Tu as parlé comme un nouveau-né… qui a déjà compris ce que coûte l’ordre. »\n\n"
                        "Puis, clairement :\n"
                        "**« Très bien. J’en toucherai deux mots au Prince. »**\n\n"
                        "C’est une recommandation. Et une mise à l’épreuve future."
                    ),
                    followups=[_back_to_hub("Revenir (meilleure impression)")],
                ),
            ],
        ),
        _back_to_hub("S’arrêter là (ne pas faire de déclamation)"),
    ]


# =========================================================
# Jehanne (goule de la garde) — inchangé
# =========================================================
def _jehanne() -> list[Choice]:
    return [
        Choice(
            id="jehanne_warn",
            label="Soutenir son regard",
            answer_md=(
                "Jehanne ne sourit pas.\n\n"
                "« Aucun pouvoir. Aucun geste inutile. Les règles ne protègent pas : elles condamnent. »\n\n"
                "Son regard pèse comme une main sur la nuque."
            ),
            followups=[_back_to_hub()],
        ),
        Choice(
            id="jehanne_avoid",
            label="Baisser les yeux",
            answer_md="Elle te laisse passer. Son regard, lui, ne te quitte pas.",
            followups=[_back_to_hub()],
        ),
        Choice(
            id="jehanne_call",
            label="Insister",
            answer_md=(
                "Elle avance d’un pas, et la cour semble retenir son souffle.\n\n"
                "« Je puis appeler la Gardienne. Je n’hésiterai pas. »\n\n"
                "Autour de vous, les paroles meurent."
            ),
            followups=[_back_to_hub("Revenir (malaise palpable)")],
        ),
    ]


# =========================================================
# Scene
# =========================================================
def get_scene() -> Scene:
    return Scene(
        id="s01_cour_inferieure",
        title="Cour inférieure — murmures, déclamations et impressions",
        intro_md=(
            "La cour inférieure est noyée d’ombres et de chuchotements.\n\n"
            "Sous les arcades, les non-morts se croisent sans jamais se heurter. "
            "Chaque regard pèse, chaque silence est un calcul.\n\n"
            "La pierre suinte l’humidité, les torches fument, et l’on jurerait que la nuit "
            "a des oreilles.\n\n"
            "Ici, les paroles sont des lames : trop franches, elles coupent leur porteur.\n\n"
            "**Rappel pour la table** :\n"
            "- Les approches visent d’abord un **aparté** : quelques pas à l’écart, voix basse.\n"
            "- Le MJ tranche les issues (Échec / Réussite / Critique).\n"
            "- Avant de trancher, le personnage peut promettre une **faveur mineure** pour **réduire la difficulté de 1**.\n"
            "- Les **déclamations** (si proposées) sont, elles, à **haute voix** et avec témoins.\n\n"
            "Choisis qui tu oses approcher."
        ),
        choices=_hub_choices(),
    )
