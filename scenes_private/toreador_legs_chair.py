from domain.schema import Choice, Scene


RECTO = """
### L'œuvre
Aliénor est représentée nue, mais son corps n'est plus entièrement humain.

Des ailes membraneuses naissent dans son dos. Des structures osseuses suivent ses flancs avec une élégance presque architecturale. Certaines excroissances pourraient éventrer un homme. Ses mains sont longues, fines, prédatrices. Son visage demeure parfaitement reconnaissable, mais ses pommettes sont plus hautes, ses lignes plus cruelles, ses proportions presque irréelles.

Chaque transformation monstrueuse semble obéir à la même règle : ne jamais sacrifier la beauté à l'efficacité lorsque les deux peuvent être obtenues ensemble. Des pigments subtils donnent même les teintes de la chair, des membranes et des reliefs osseux.

L'auteur connaît le corps d'Aliénor avec une précision intime.

**Effet immédiat si cette découverte est effectivement jouée : +1 Flétrissure et 1 dégât superficiel de Volonté.**

### Les mots
**Aliénor,**

La nature t'a presque achevée.  
Elle a eu peur au dernier instant.

Moi non.

Je me souviens de ta chair sous mes doigts et de ton Sang lorsqu'il cessait enfin de résister.

Tu pourrais commander.  
Tu as pourtant toujours préféré qu'une autre volonté te dise où mordre.

Avec moi, je l'acceptais.  
Avec les autres, c'est une faiblesse.

Je ne veux plus que tu offres la gorge.  
Je veux que l'on s'agenouille devant tes crocs.

Tes pommettes peuvent apprendre le mépris.  
Tes mains peuvent apprendre à posséder.

Ta beauté n'a jamais été faite pour être contemplée.  
Elle est faite pour soumettre.

Ne commence pas sur toi.  
Tu es trop précieuse pour porter tes premières erreurs.

Prends de la matière qui ne compte pas.  
Apprends sur elle.

Et lorsque tes mains ne trembleront plus, reprends possession de ta propre chair.
""".strip()

REVERSE = """
Le revers n'est plus une œuvre : ce sont des études techniques.

Les pommettes sont reprises en plusieurs étapes. Puis viennent les mains : chair ouverte, doigts progressivement allongés et affinés, blessures répétées puis régénérées avec le Sang. La méthode semble destinée à quelqu'un qui ne sait pas encore ordonner directement à la chair de changer.

Des silhouettes humaines anonymes servent de matière d'entraînement.

> **Le Sang restaure ce qu'il croit être toi. Force-le assez souvent à voir autre chose, et même lui finit par apprendre.**

> **N'apprends jamais une erreur sur toi lorsque quelqu'un d'autre peut la porter.**

> **Je sais ce que tu es lorsque personne ne choisit pour toi. C'est précisément pour cela que je veux t'apprendre à choisir pour les autres.**

**Effet si cette lecture est effectivement jouée : le dégât de Volonté de la découverte devient aggravé au lieu de superficiel. Il ne s'agit pas d'un second dégât. La Flétrissure reste à +1.**
""".strip()


def _apres_acceptation() -> list[Choice]:
    return [
        Choice(
            id="legs_preserver_direct",
            label="Préserver le sceau",
            answer_md="Tu conserves l'étui intact. Son contenu reste destiné à Aliénor. La suite dépendra de ce que tu décideras réellement de faire de l'objet.",
            ends_scene=True,
        ),
        Choice(
            id="legs_examiner_sceau",
            label="Examiner le sceau",
            answer_md="""
**Jet physique facultatif : Intelligence + Occultisme — Difficulté 4.**

Effectue le jet à table, puis sélectionne le résultat.
""".strip(),
            followups=[
                Choice(
                    id="legs_sceau_echec",
                    label="Échec",
                    answer_md="Tu n'identifies que des symboles anciens, païens et manifestement hérétiques.",
                    followups=[
                        Choice(
                            id="legs_sceau_echec_preserver",
                            label="Préserver le sceau",
                            answer_md="Tu conserves l'étui fermé et intact.",
                            ends_scene=True,
                        ),
                        Choice(
                            id="legs_sceau_echec_ouvrir",
                            label="Rompre le sceau et ouvrir",
                            answer_md=RECTO,
                            followups=_apres_recto(),
                        ),
                    ],
                ),
                Choice(
                    id="legs_sceau_succes",
                    label="Succès",
                    answer_md="""
Ce n'est pas une simple fantaisie hérétique. Le sceau appartenait à une **ancienne lignée noble disparue depuis plusieurs siècles**, associée à des traditions préchrétiennes et à une forme de **paganisme celtique**.

Le nom exact de cette lignée ne t'est pas donné.
""".strip(),
                    followups=[
                        Choice(
                            id="legs_sceau_succes_preserver",
                            label="Préserver le sceau",
                            answer_md="Tu conserves l'étui fermé et intact.",
                            ends_scene=True,
                        ),
                        Choice(
                            id="legs_sceau_succes_ouvrir",
                            label="Rompre le sceau et ouvrir",
                            answer_md=RECTO,
                            followups=_apres_recto(),
                        ),
                    ],
                ),
            ],
        ),
        Choice(
            id="legs_ouvrir_direct",
            label="Rompre le sceau et ouvrir",
            answer_md=RECTO,
            followups=_apres_recto(),
        ),
    ]


def _apres_recto() -> list[Choice]:
    return [
        Choice(
            id="legs_arreter_recto",
            label="T'arrêter là",
            answer_md="Tu as déjà vu suffisamment pour comprendre que l'auteur connaît intimement Aliénor, son corps, son Sang et une part de sa nature. Le sceau est brisé.",
            ends_scene=True,
        ),
        Choice(
            id="legs_lire_revers",
            label="Lire le revers",
            answer_md=REVERSE,
            ends_scene=True,
        ),
    ]


def _refus_text() -> str:
    return """
Maël reprend simplement l'étui.

« Comme vous voudrez. »

Il s'éloigne. Cette rencontre ne t'apporte aucune **preuve nouvelle** sur l'identité de l'expéditeur. Ce que tu en déduis reste entièrement fondé sur les informations que tu possèdes déjà.
""".strip()


def get_scene() -> Scene:
    return Scene(
        schema_version=1,
        id="scene_privee_toreador_legs_chair",
        title="Le legs de chair",
        intro_md="""
Saint-Germain commence à rester derrière vous et le chemin ramène vers Rennes.

À l'écart, **Maël** t'attend. Il tient un long étui de cuir sombre, fermé par un sceau ancien.

« Pour la dame de Dinan. De votre main à la sienne. »

*Cette version suppose Maël vivant, libre et disponible. Si ce n'est pas le cas en jeu, le MJ remplace simplement le porteur par un fidèle discret du Vieux Qui Écoute sans modifier le contenu de la scène.*
""".strip(),
        choices=[
            Choice(
                id="legs_accepter_immediat",
                label="Prendre l'étui",
                answer_md="Maël te remet l'étui. « De votre main à la sienne. » Puis il s'éloigne.",
                followups=_apres_acceptation(),
            ),
            Choice(
                id="legs_refuser_immediat",
                label="Refuser",
                answer_md=_refus_text(),
                ends_scene=True,
            ),
            Choice(
                id="legs_questions",
                label="« Attendez. J'ai des questions. »",
                answer_md="""
Tu lui demandes qui l'envoie, pourquoi toi et ce que contient l'étui.

Maël répond sans impatience :

« Celui qui l'envoie ne souhaite pas venir jusqu'à Rennes. »

« Vous, parce qu'elle vous laissera approcher. »

Il regarde l'étui.

« Je ne l'ai pas ouvert. Je n'étais pas celui à qui l'on demandait de décider s'il devait le rester. »

Il n'en dira pas davantage.
""".strip(),
                followups=[
                    Choice(
                        id="legs_questions_accepter",
                        label="Accepter l'étui",
                        answer_md="Maël te remet l'étui et s'éloigne.",
                        followups=_apres_acceptation(),
                    ),
                    Choice(
                        id="legs_questions_refuser",
                        label="Refuser",
                        answer_md=_refus_text(),
                        ends_scene=True,
                    ),
                ],
            ),
        ],
    )
