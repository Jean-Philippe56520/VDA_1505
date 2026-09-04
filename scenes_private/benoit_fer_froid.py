from domain.schema import Choice, Scene


def _inspiration_rituelle() -> str:
    return """
### Inspiration rituelle
Cette branche brutale t'inspire une piste de recherche.

Si Benoît consacre plus tard le temps nécessaire à **La Fondation de Rennes** pour créer ou développer un **nouveau rituel ayant un lien réel avec le monde féerique**, ce rituel coûte **1 XP de moins**.

*Usage unique. Rien n'est acquis tant que cette branche n'a pas été effectivement jouée et confirmée par le MJ.*
""".strip()


def _echec_brutal_text() -> str:
    return f"""
Tu forces malgré l'absence de réponse claire. Bruges et Gurvan se confondent, sans information fiable.

La cicatrice située sur ton cœur s'ouvre brutalement et le sang traverse tes vêtements. Avec la douleur remonte la noirceur de ton âme maudite — peut-être seulement celle de tout vampire, peut-être aussi celle de l'hérésie et de l'horreur du rituel que l'on t'a fait subir.

**Conséquences si cette branche est jouée :**
- **+1 Soif**
- **+1 Flétrissure**
- aucune information fiable sur Gurvan

{_inspiration_rituelle()}
""".strip()


def get_scene() -> Scene:
    return Scene(
        schema_version=1,
        id="scene_privee_benoit_fer_froid",
        title="Le fer froid se souvient",
        intro_md="""
Depuis que tu es entré au **Pain Amical**, quelque chose te crispe.

Le fer est partout : clous trop épais, ferrures bâclées, crochets, chaînes réparées, métal grossier et mal travaillé. Ce n'est pas le fer froid de Bruges, pourtant ton corps le déteste sans que tu puisses l'expliquer rationnellement.

**Effet tant que Benoît reste dans l'auberge : –1 dé à toutes ses actions.**

Gurvan devrait être beaucoup plus proche de la mort. Pourtant quelque chose travaille sa chair. Lorsque tu t'approches pour l'examiner, la cicatrice située sur ton cœur commence à brûler et le souvenir de Bruges remonte : Scalla, Simon, le cercle, le fer froid, la créature captive.
""".strip(),
        choices=[
            Choice(
                id="benoit_reculer",
                label="Reculer",
                answer_md="""
Tu romps l'observation. La brûlure diminue.

Tu n'apprends rien de certain sur Gurvan. Tu sais seulement que quelque chose dans son état a réveillé la marque de Bruges.
""".strip(),
                ends_scene=True,
            ),
            Choice(
                id="benoit_forcer_sens",
                label="Forcer tes sens à regarder au-delà de la chair",
                answer_md="""
**Jet physique : Résolution + Auspex — Difficulté 2.**

Le **–1 dé du Pain Amical** s'applique. La Volonté peut être utilisée normalement.

Effectue le jet à table, puis sélectionne son résultat.
""".strip(),
                followups=[
                    Choice(
                        id="benoit_resultat_echec",
                        label="Échec",
                        answer_md="""
Tu forces trop. Bruges se superpose à Gurvan et tu ne distingues plus ce que tu perçois réellement de ce que ta cicatrice te fait revivre.

**Aucune information fiable.**

Tu peux accepter l'échec ou dépenser volontairement **1 Volonté** pour forcer la branche d'**échec brutal**.
""".strip(),
                        followups=[
                            Choice(
                                id="benoit_accepter_echec",
                                label="Accepter l'échec",
                                answer_md="Tu abandonnes l'examen. La sensation décroît lentement. **Aucune information obtenue.**",
                                ends_scene=True,
                            ),
                            Choice(
                                id="benoit_forcer_echec_brutal",
                                label="Dépenser 1 Volonté et forcer",
                                answer_md=_echec_brutal_text(),
                                ends_scene=True,
                            ),
                        ],
                    ),
                    Choice(
                        id="benoit_resultat_echec_brutal",
                        label="Échec brutal",
                        answer_md=_echec_brutal_text(),
                        ends_scene=True,
                    ),
                    Choice(
                        id="benoit_resultat_succes",
                        label="Succès",
                        answer_md="""
La confusion disparaît. Tu ne sais pas ce qui travaille Gurvan, mais quelque chose en toi reconnaît immédiatement une absence.

**Ce phénomène n'est pas féerique.**

Tu ignores comment ton Sang peut en être aussi certain.
""".strip(),
                        ends_scene=True,
                    ),
                    Choice(
                        id="benoit_resultat_critique",
                        label="Succès critique",
                        answer_md="""
La première certitude est immédiate : **ce phénomène n'est pas féerique**.

Puis ta perception va plus profond. Tu reconnais une corruption qui paraît plus radicale encore que ta propre nature vampirique.

**Informations obtenues :**
- non féerique ;
- profondément corrompu.

Tu n'en comprends ni l'origine ni le mécanisme.
""".strip(),
                        ends_scene=True,
                    ),
                    Choice(
                        id="benoit_resultat_bestial",
                        label="Succès bestial (critique)",
                        answer_md=f"""
Tu comprends successivement :

**Ce n'est pas féerique.**

**C'est profondément corrompu.**

Puis tu perçois que cette corruption ne demeure pas simplement dans Gurvan : elle cherche à passer, s'étendre, contaminer et transformer.

**Elle est infectieuse.**

Au même instant, la cicatrice située sur ton cœur s'ouvre et saigne abondamment. Avec la douleur remonte la noirceur de ton âme maudite — celle de la Bête, celle du rituel de Bruges, ou les deux mêlées.

**Conséquences si cette branche est jouée :**
- **+1 Soif**
- **+1 Flétrissure**

{_inspiration_rituelle()}
""".strip(),
                        ends_scene=True,
                    ),
                ],
            ),
        ],
    )
