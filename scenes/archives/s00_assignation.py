from domain.schema import Scene, Choice


def get_scene() -> Scene:
    return Scene(
        id="s00_assignation",
        title="L’Assignation",
        intro_md=(
    "Cette nuit, **quelque chose change**.\n\n"
    "Vous n’êtes pas à l’Élysium.\n"
    "Pas sous ses voûtes.\n"
    "Pas exposé aux regards.\n\n"
    "Mais vous le savez désormais :\n"
    "**c’est un lieu que vous devrez fréquenter.**\n"
    "**Avec tout ce que cela implique.**\n\n"
    "**Votre Sire vous a convoqué dans son domaine.**\n"
    "Pas pour une faveur.\n"
    "Pas pour un entretien.\n\n"
    "**Pour une obligation.**\n\n"
    "**À partir de cette nuit, il n’y a plus d’ambiguïté :**\n"
    "**vous êtes un Infant.**\n"
    "**Rien de plus.**\n\n"
    "À ce titre,\n"
    "**vous porterez ce que l’on vous donne.**\n"
    "**Vous parlerez quand on vous autorise.**\n"
    "**Vous vous tairez quand on l’exige.**\n\n"
    "**Votre survie ne vous appartient plus entièrement.**\n\n"
    "Des devoirs.\n"
    "Des attentes.\n"
    "**Des charges qui ne se refusent pas.**\n\n"
    "L’Élysium, que vous allez bientôt découvrir n’est pas un refuge.\n"
    "**C’est l’Élysium du Prince Amaury.**\n"
    "**Ce lieu est prêt à broyer tout ce qui ne plie pas sous son joug.**\n\n"
    "**Le Conseil des Primogènes observe.**\n"
    "**Le Prince tranche.**\n"
    "**La Camarilla exécute.**\n\n"
    "Votre Sire le sait.\n"
    "Et vous le comprenez à votre tour :\n\n"
    "**Qu’il soit exigeant, distant, brutal, protecteur ou calculateur,**\n"
    "**votre Sire est votre maître.**\n\n"
    "Mais il est aussi autre chose.\n\n"
    "**Il est ce qui se tient entre vous et le Conseil des Primogènes.**\n"
    "**Entre vous et le Prince.**\n\n"
    "Sans lui,\n"
    "**vous seriez broyé avant même d’être entendu.**\n\n"
    "**Ces responsabilités ne s’allègeront jamais.**\n"
    "**Elles ne feront que changer de forme.**\n"
),
        choices=[

            # ==================================================
            # ALIÉNOR — TOREADOR — GARDIENNE D’ELYSIUM
            # ==================================================
            Choice(
                id="choose_alienor",
                label="Répondre à l’appel d’Aliénor, Gardienne d’Elysium.",
                answer_md=(
                    "Aliénor vous reçoit comme une enfant que l’on expose.\n\n"
                    "Elle lisse votre tenue, lentement.\n"
                    "Un geste tendre.\n"
                    "Un geste qui ne vous appartient pas.\n\n"
                    "« **Cette nuit, tu ne seras pas seule.** »\n\n"
                    "« **Trois autres Infants seront à la Cour inférieure avec toi.** »\n\n"
                    "Elle les énumère comme des curiosités.\n\n"
                    "« **Un Brujah.** L’iconoclaste, pas l'idéaliste.\n"
                    "La colère avant la pensée.\n"
                    "Il confond encore la rue et la justice. »\n\n"
                    "« **Un Ventrue.** Le mâle.\n"
                    "Le plus jeune.\n"
                    "Il croit que l’obéissance est une vertu personnelle. »\n\n"
                    "« **Un Tremere.** Le moins incommodant\n"
                    "Il parle comme un livre qu’on a trop annoté. »\n\n"
                    "Elle relève votre menton.\n\n"
                    "« **Vous coopérerez.** »\n"
                    "« **Vous mettrez en commun ce que vous aurez entendu.** »\n"
                    "« **Sans commentaires. Sans bravade.** »\n\n"
                ),
                followups=[
                    Choice(
                        id="alienor_main",
                        label="Recevoir la mission principale.",
                        answer_md=(
                            "« **Tu vas observer la Cour inférieure.** »\n\n"
                            "« **Non pas leurs querelles. Pas leurs nostalgies.** »\n"
                            "« **Les Décrets.** »\n\n"
                            "« **Je veux savoir comment les autres vampires les portent en bouche.** »\n"
                            "« **Comment ils disent les appliquer.** »\n"
                            "« **Ce qu’ils prétendent en comprendre.** »\n"
                            "« **Ce qu’ils évitent soigneusement de dire.** »\n\n"
                            "« **Tu ne remets jamais un Décret en cause.** »\n"
                            "« **Tu demandes seulement :** comment bien faire, comment être conforme, à qui s’adresser. »\n\n"
                            "« **Tu notes mot pour mot.** »\n"
                            "« **Tu racontes des scènes.** »\n"
                            "« **Tu n’interprètes pas.** »\n"
                            "« **Tu ne juges pas.** »"
                        ),
                        followups=[
                            Choice(
                                id="alienor_leave",
                                label="Prendre congé.",
                                answer_md=(
                                    "Aliénor vous embrasse le front.\n\n"
                                    "« **Va.** »\n\n"
                                    "Vous baissez le regard et prenez congé."
                                ),
                                followups=[
                                    Choice(
                                        id="alienor_secondary",
                                        label="(Aliénor ajoute.)",
                                        answer_md=(
                                            "« **Une dernière chose.** »\n\n"
                                            "« **Dans ce pacte ponctuel, tu observeras aussi tes alliés.** »\n"
                                            "« **Leur tenue. Leur retenue. Leurs failles d’étiquette.** »\n\n"
                                            "« **Pas pour les trahir.** »\n"
                                            "« **Pour savoir ce que je tiens… et ce que je risque.** »\n\n"
                                            "« **Tu notes leurs formulations quand les Décrets apparaissent.** »\n"
                                            "« **Leurs réflexes. Leurs silences.** »\n"
                                            "« **Sans jamais leur demander directement.** »\n\n"
                                            "« **Jehanne t’aidera.** »\n"
                                            "« **J’ai mis, entre autre, à sa disposition un calice qui devrait plaire au mâle Ventrue.** »\n"
                                            "« **Sers-t’en à bon escient, pour qu’il ne s’arrête pas de parler. Tu ne pourras pas suffisament tous les observer, choisis bien tes cibles** »"
                                        ),
                                        followups=[
                                            Choice(
                                                id="alienor_accept",
                                                label="Accepter sans discuter.",
                                                answer_md=(
                                                    "Aliénor sourit.\n\n"
                                                    "« **Parfait. Va, mon enfant** »"
                                                ),
                                                ends_scene=True,
                                            ),
                                            Choice(
                                                id="alienor_question",
                                                label="Demander jusqu’où aller.",
                                                answer_md=(
                                                    "« **Jusqu’à ce qu’ils oublient que tu écoutes.** »\n\n"
                                                    "« **Mais tu ne franchis jamais la ligne.** »"
                                                ),
                                                ends_scene=True,
                                            ),
                                        ],
                                    )
                                ],
                            )
                        ],
                    )
                ],
            ),

            # ==================================================
            # GWILHERM — BRUJAH — PRIMOGÈNE
            # ==================================================
            Choice(
                id="choose_gwilherm",
                label="Répondre à l’appel de Gwilherm le Rouge, Primogène Brujah.",
                answer_md=(
                    "Gwilherm ne vous fait pas asseoir.\n\n"
                    "« **Bonsoir mon garçon. Cette nuit, tu seras avec trois autres rejetons.** »\n\n"
                    "Il les désigne d’un geste vague.\n\n"
                    "« **Une Toreador.** La poupée bien gardée.\n"
                    "Elle écoute mieux qu’elle ne parle. »\n\n"
                    "« **Un Ventrue.** Le plus jeune.\n"
                    "Il appelle ça le devoir pour ne pas dire la peur. »\n\n"
                    "« **Un Tremere.** Le seul nouveau-né du clan.\n"
                    "Il croit que noter suffit à comprendre. »\n\n"
                    "Il vous fixe.\n\n"
                    "« **J'ai un accord avec leurs sires.** »\n"
                    "« **Vous, les enfants, vous coopérez, vous mettez en commun.** »\n"
                    "« **Et après, chacun retourne à sa laisse.** »"
                ),
                followups=[
                    Choice(
                        id="gwilherm_main",
                        label="Recevoir la mission principale.",
                        answer_md=(
                            "« **Tu observes les autres vampires de la Cour inférieure.** »\n\n"
                            "« **Ce qu’ils disent des Décrets.** »\n"
                            "« **Comment ils les appliquent.** »\n"
                            "« **Comment ils s’en servent.** »\n\n"
                            "« **Je veux des mots exacts.** »\n"
                            "« **Des scènes.** »\n"
                            "« **Pas ton jugement.** »\n\n"
                            "« **Et tu compares tes notes avec les trois autres.** »\n"
                            "« **Sans débat.** »\n"
                            "« **Sans leçon.** »"
                        ),
                        followups=[
                            Choice(
                                id="gwilherm_leave",
                                label="Continuer.",
                                answer_md=(
                                    "« **Va, mon garçon. Cette nuit tu n'auras pas l'occasion d'honnorer ton clan, mais je te demande de ne pas le déshonorer.** »\n\n"
                                    "Vous pensez que c’est fini."
                                ),
                                followups=[
                                    Choice(
                                        id="gwilherm_secondary",
                                        label="(Gwilherm ajoute.)",
                                        answer_md=(
                                            "« **Dernière chose.** »\n\n"
                                            "« **Fais en sorte que tes frères, surtout Guillaume, ne soient pas trop observés par tes alliés.** »\n"
                                            "« **Si cela doit arriver, je le saurais.**\n"
                                        ),
                                        followups=[
                                            Choice(
                                                id="gwilherm_accept",
                                                label="Accepter sans broncher.",
                                                answer_md=(
                                                    "Un rictus.\n\n"
                                                    "« **Bien. Allons retrouver tes frères, je vous accompagne jusqu'à l'Elysium** »"
                                                ),
                                                ends_scene=True,
                                            ),
                                            Choice(
                                                id="gwilherm_question",
                                                label="Demander ce qu’il se passera sinon.",
                                                answer_md=(
                                                    "« **C’est comme ça que ça a commencé la dernière fois.** »\n\n"
                                                    "Il marque une pause.\n\n"
                                                    "« **Allons retrouver tes frères.** »\n"
                                                    "« **Je vous accompagne jusqu’à l’Élysium.** »\n"
)
,
                                                ends_scene=True,
                                            ),
                                        ],
                                    )
                                ],
                            )
                        ],
                    )
                ],
            ),

            # ==================================================
            # SIMON — TRÉMÈRE — PRIMOGÈNE
            # ==================================================
            Choice(
                id="choose_simon",
                label="Répondre à l’appel de Simon, Primogène Trémère.",
                answer_md=(
                    "Simon vous attend déjà.\n\n"
                    "« **Mon jeune apprenti. Cette nuit, tu vas coopérer avec d'autres Caïnites.** »\n\n"
                    "« **Trois Infants :** »\n\n"
                    "« **Une Toreador.** Sous tutelle.\n"
                    "Conditionnée à appeler cela protection. »\n\n"
                    "« **Un Brujah.** Celui qui semble suivre le chemin du frère le plus instable.\n"
                    "Utile tant qu’il est observé. »\n\n"
                    "« **Un Ventrue.** Le plus jeune.\n"
                    "Il croit que la hiérarchie est une prière. »\n\n"
                    "« **Vous recueillerez un même type d’information.** »\n"
                    "« **Vous la mettrez en commun** »\n\n"
                    "« **Et vous ne confondrez pas collecte et opinion.** »"
                ),
                followups=[
                    Choice(
                        id="simon_main",
                        label="Recevoir la mission principale.",
                        answer_md=(
                            "« **Vous allez observer les autres vampires de la Cour inférieure.** »\n\n"
                            "« **Je veux ce qu’ils disent des Décrets.** »\n"
                            "« **Les passages qu’ils citent.** »\n"
                            "« **Les mots qu’ils choisissent pour paraître conformes.** »\n"
                            "« **Les silences quand le texte devient tranchant.** »\n\n"
                            "« **Tu notes.** »\n"
                            "« **Mot pour mot.** »\n"
                            "« **Aucune hypothèse.** »"
                        ),
                        followups=[
                            Choice(
                                id="simon_leave",
                                label="Continuer",
                                answer_md=(
                                    "« **Tu peux disposer.** »\n\n"
                                   
                                ),
                                followups=[
                                    Choice(
                                        id="simon_secondary",
                                        label="Prendre congé",
                                        answer_md=(
                                            "« **Une dernière chose.** »\n\n"
                                            "« **Yosria et Maloch, surtout Ysoria ne doivent pas faire l'objet d'un récit que les sires de tes alliés pourraient exploiter un jour contre nous. J'espère que nous nous sommes bien compris.** »\n"
                                        ), 
                                        followups=[
                                            Choice(
                                                id="simon_accept",
                                                label="Accepter sans poser de question.",
                                                answer_md=(
                                                    "« **Bien. Maintenant, tu peux disposer, apprenti** »"
                                                ),
                                                ends_scene=True,
                                            ),
                                            Choice(
                                                id="simon_question",
                                                label="Demander comment les en empêcher.",
                                                answer_md=(
                                                    "« **Chaque problème a plusieurs équations. A toi d'appliquer la meilleure. Cette fois, tu peux disposer.** »"
                                                ),
                                                ends_scene=True,
                                            ),
                                        ],
                                    )
                                ],
                            )
                        ],
                    )
                ],
            ),

            # ==================================================
            # ODON — VENTRUE — DOCTRINE DE L’ÉLU
            # ==================================================
            Choice(
                id="choose_odon",
                label="Répondre à l’appel d’Odon, Primogène Ventrue.",
                answer_md=(
                    "Odon vous reçoit sans décor.\n\n"
                    "« **Mon enfant. Cette nuit, tu ne seras pas seul.** »\n\n"
                    "« **Trois autres Infants.** »\n\n"
                    "« **Une Toreador.** Façonnée pour plaire. »\n\n"
                    "« **Un Brujah.** Le plus jeune des 3, façonné pour rompre. »\n\n"
                    "« **Le Tremere.** Celui qui est façonné pour obéir à des formules. »\n\n"
                    "Il vous regarde.\n\n"
                    "« **Nous avons un accord entre sirs.** »\n"
                    "« **Cette nuit, vous coopérerez.** »\n"
                    "« **Vous mettrez en commun ce que vous aurez entendu.** »\n\n"
                    "« **Mais souviens-toi : tu n’es pas leur égal. Toi tu sers les desseins de Dieu.** »"
                ),
                followups=[
                    Choice(
                        id="odon_main",
                        label="Recevoir la mission principale.",
                        answer_md=(
                            "« **Vous observerez la Cour inférieure.** »\n\n"
                            "« **Comment les autres vampires appliquent les Décrets.** »\n"
                            "« **Comment ils parlent des domaines, des portes, des charges.** »\n"
                            "« **Comment ils justifient leur présence là où ils se tiennent.** »\n\n"
                            "« **Tu me rapportes des récits.** »\n"
                            "« **Des mots.** »\n"
                            "« **Pas ta pensée.** »\n\n"
                            "« **Et tu compares tes notes avec les autres Infants, sans bavardage.** »"
                        ),
                        followups=[
                            Choice(
                                id="odon_leave",
                                label="Prendre congé.",
                                answer_md=(
                                    "« **Va, mon enfant.** »\n\n"
                                    "Vous pensez que c’est fini."
                                ),
                                followups=[
                                    Choice(
                                        id="odon_secondary",
                                        label="(Odon ajoute.)",
                                        answer_md=(
                                            "« **Une dernière chose.** »\n\n"
                                            "« **Nos alliés de circonstance ne sont pas moins dangereux que les autres. Fais en sorte que ta soeur ne fasse pas l'objet d'un récit utile à leurs yeux\n"
                                            "Si leur récit permet à leur sire d'interprêter des faits qui saurait la compromettre :\n"
                                            "Tu échoues.** »\n\n"
                                        ),
                                        followups=[
                                            Choice(
                                                id="odon_accept",
                                                label="Accepter.",
                                                answer_md=(
                                                    "Odon incline la tête.\n\n"
                                                    "« **Mes prières t'accompagnent** »"
                                                ),
                                                ends_scene=True,
                                            ),
                                            Choice(
                                                id="odon_question",
                                                label="Demander si Héloïse à sa confiance .",
                                                answer_md=(
                                                    "« **Elle sert les desseins de Dieu, tout comme toi. Tu peux douter d'elle, mais ne la trahis pas, ce serait trahir Dieu.** »"
                                                ),
                                                ends_scene=True,
                                            ),
                                        ],
                                    )
                                ],
                            )
                        ],
                    )
                ],
            ),
        ],
    )
