from domain.schema import Choice, Scene


INTRO = """
**Aliénor — Une seule question**

*Aliénor la regarde longtemps avant de parler.*

« Je me souviens de la nuit où je t’ai Étreinte. De ce que tu étais… et de ce que j’ai choisi de **garder**. »

*Elle effleure sa joue.*

« Depuis, tu poses des questions. Sur moi. Sur notre sang. Sur nos morts. Sur tout ce que je préférerais parfois laisser **enterré**. »

*Un faible sourire.*

« Tu es mon infante. Ce qui m’a façonnée finira toujours par t’atteindre. »

*Sa main demeure un instant contre son visage.*

« Alors, ce soir, je t’accorde **une question**. Une seule. Sur moi, notre lignée, ou ceux qui nous ont précédées. »

*Elle marque une pause.*

« Je ne te promets pas toute la vérité. Je te promets une réponse **réelle**, et suffisamment complète selon mon propre jugement. »

*Son regard se durcit légèrement.*

« Si je refuse de répondre, je te devrai une **faveur mineure**. Elle sera inscrite au registre de la Gardienne de l’Élysium. »

*Puis un sourire presque amusé.*

« Je doute que la Gardienne conteste ma parole. »

*Elle retire enfin sa main.*

« Mais choisis bien. Tu ne fouilles pas seulement dans ton histoire. Tu fouilles dans la **mienne**. »

*Un silence.*

« Certaines réponses peuvent te mettre en colère contre moi. Je peux le supporter. »

*Son regard ne quitte pas le sien.*

« Je suis moins certaine de supporter qu’elles te fassent **cesser de m’aimer**. »

*Puis, simplement :*

« **Demande.** »
""".strip()


REPONSES = {
    "attente_alienor": """
*Le faible sourire d’Aliénor disparaît presque.*

« Que tu survives. D’abord. C’est une attente moins élégante que toutes celles que tu imagines, mais elle précède les autres. »

« Je veux qu’un jour tu n’aies plus besoin de ma permission pour être dangereuse. Que tu reconnaisses les mensonges des Anciens sans devenir l’esclave de leur cynisme. Que tu saches ce que vaut notre Sang sans croire que sa gloire suffit à tout justifier. »

*Elle l’observe un moment.*

« Je ne veux pas une seconde Aliénor. Si je voulais un miroir, j’aurais choisi quelque chose de plus docile. »

« Je veux que tu sois capable de me désobéir intelligemment, sans avoir besoin de me haïr pour cela. Que tu deviennes assez forte pour pouvoir me quitter sans te perdre. Et assez libre pour que, si tu demeures près de moi, ce ne soit plus parce que tu ne sais pas faire autrement. »

*Sa voix baisse.*

« Voilà ce que j’attends de toi. »

*Puis, après un silence :*

« Et que tu **restes**. »
""".strip(),
    "verite_1493": """
*Aliénor reste silencieuse assez longtemps pour que la réponse cesse de ressembler à un récit.*

« Plusieurs guerres. C’est la première chose que tu dois comprendre. Ceux qui racontent 1493 comme une seule guerre mentent ou simplifient. »

« Les Brujah se battaient contre le Prince et contre nous. La Main du Prince frappait les Lasombra. Les Gangrel et la Main combattaient les Tzimisce. Chacun croyait régler sa propre dette pendant que Rennes recevait tous les coups à la fois. »

« Et les mortels étaient au milieu. Ils ont payé pour nos rancunes, nos territoires, nos fidélités et notre orgueil. »

*Son regard se durcit.*

« Ne commets pas l’erreur de croire que les Toreador furent seulement des victimes. Avant de tomber, notre ancien ordre avait lui aussi fait énormément de mal aux Brujah. Mikolai et moi y avons pris notre part. Ensemble, nous pouvions être… particulièrement efficaces. »

« Guillaume a vaincu Mikolai en combat singulier à la **Porte de la Madeleine** et l’a décapité. Ailleurs, la guerre contre les Tzimisce a entraîné la destruction de la grande tour de Saint-Germain. »

« Puis l’Inquisition a frappé une ville que nous avions déjà suffisamment exposée. Elle n’a pas été appelée à Rennes par un vampire. Elle avait vu trop de morts, trop de disparitions, trop de choses qui ne pouvaient plus être expliquées proprement. »

*Elle détourne brièvement les yeux.*

« Voilà ce qui s’est passé en 1493 : pas un plan parfait. Une accumulation de guerres, de fautes et d’occasions saisies par ceux qui avaient encore la force de le faire. »

**Conséquence si cette réponse est effectivement jouée : +1 Flétrissure.**
""".strip(),
    "mikolai": """
« Mon frère. »

*Aliénor ne corrige pas le mot.*

« Isabelle nous avait faits tous les deux. Il était mon aîné dans le Sang, et pendant très longtemps j’ai mesuré une partie de ce que j’étais à ce qu’il était devenu. »

« Mikolai croyait que la plus grande œuvre n’était pas nécessairement celle que l’on enferme dans une chapelle ou un coffre. Une œuvre pouvait marcher, parler, enseigner, engendrer à son tour. Il voulait que ce que nous créions survive à nos personnes. »

*Un sourire sans joie.*

« Je l’admirais. Je le trouvais insupportable. Je l’aimais. Je l’enviais. »

« Contre les Brujah, nous avons parfois été terribles ensemble. Lui avec sa manière de transformer chaque victoire en leçon. Moi avec une conception beaucoup moins patiente de la pédagogie. »

*Elle soutient le regard de son infante.*

« Je voulais sa place. Il y eut même des nuits où je souhaitais simplement qu’il ne soit plus là pour l’occuper. Cela ne signifie pas que sa mort m’a laissée intacte. Les sentiments des morts ne deviennent pas simples parce qu’ils sont morts. »

**Conséquence si cette réponse est effectivement jouée : +1 Flétrissure.**
""".strip(),
    "isabelle_identite": """
« Ma sire. Ma Princesse. Ma première loi. »

*Aliénor prononce chaque titre séparément.*

« Isabelle pouvait être d’une beauté qui faisait paraître la flatterie inutile. Elle était intelligente, cultivée, et possédait cette courtoisie cruelle qui vous permet de comprendre que vous avez été condamné avant même qu’elle ait élevé la voix. »

« Elle savait donner de l’affection sans cesser de posséder ce qu’elle aimait. Avec elle, les deux choses n’étaient pas opposées. »

*Un silence.*

« J’ai longtemps considéré comme naturel que mes volontés viennent après les siennes. Elle m’avait choisie. Elle m’avait faite. À mes yeux, cela créait une dette qu’aucune durée ne pouvait entièrement dissoudre. »

« Je pourrais aujourd’hui te réciter toutes ses fautes. Cela ne changerait pas ce qu’elle fut pour moi. »

*Aliénor relève légèrement le menton.*

« Je l’ai servie. Je l’ai crainte. Je l’ai aimée. »
""".strip(),
    "isabelle_mort": """
*Pour la première fois, Aliénor semble regretter d’avoir offert la question.*

« En 1362, la Bretagne était encore en guerre. Les Penthièvre perdaient du terrain, les Montfort en gagnaient, et notre guerre nocturne suivait sa propre logique sous la guerre des mortels. »

« Kerzu et les guerriers venus avec lui des landes reculées de Cornouaille avaient déjà été vaincus. Son Primogène Gangrel n’était pas encore mort, mais son camp ne pouvait plus sauver Isabelle. Odon avait reconnu l’autorité d’Amaury. Willem dirigeait alors les Lasombra de Rennes. »

*Sa voix devient parfaitement égale.*

« Willem a torturé Isabelle pendant qu’Amaury exigeait des réponses. Je l’ai vue. »

« Ensuite ils l’ont empalée à Saint-Pierre. Ils ne l’ont pas détruite immédiatement. Ils l’ont laissée là, incapable de fuir, jusqu’au lever du jour. »

*Aliénor ne détourne pas les yeux.*

« La grande tour de Saint-Germain existait encore. L’exposition n’était pas seulement une exécution. Elle devait être vue. Elle était un message adressé à Zvonimir : la guerre était perdue, et ceux qui poursuivraient le combat sauraient ce qu’Amaury était prêt à faire. »

« J’ai vu ma sire être torturée. J’ai vu le pieu la maintenir. Et j’ai attendu avec elle jusqu’à ce que le soleil accomplisse ce que ses ennemis avaient décidé. »

**Conséquence si cette réponse est effectivement jouée : 1 dégât aggravé de Volonté.**
""".strip(),
    "zvonimir": """
*Aliénor réfléchit avant de répondre.*

« Si je te réponds “un amant”, je te mens par insuffisance. »

« J’ai passé une grande partie de ma non-vie à commander. À décider. À tenir les autres assez près pour qu’ils me servent et assez loin pour qu’ils ne puissent pas me posséder. »

« Avec Zvonimir, j’ai découvert le luxe de déposer ma volonté entre les mains de quelqu’un d’autre. Je ne l’ai pas vécu comme une humiliation. À l’époque, cela me paraissait presque… exaltant. Une intensité que peu d’êtres étaient capables de supporter ou de rendre. »

*Son expression se ferme légèrement.*

« Ce qui avait commencé comme un choix est devenu une dépendance plus profonde que ma prudence ne l’aurait permis. Il le savait. Il l’encourageait. Et il savait très bien utiliser cette place que je lui avais donnée. »

« Il m’a aussi appris à regarder la chair autrement : non comme une forme terminée, mais comme une matière qui pouvait encore être corrigée, prolongée, transformée. »

*Un temps.*

« Je l’ai aimé, sans doute. Mais ne confonds pas l’amour avec l’innocence. »
""".strip(),
    "seigneur_kermorvan_1493": """
« Il a choisi. Mais il n’a pas choisi le jeu. »

« Le seigneur de Kermorvan était un chevalier de sang noble et un mandataire d’Anne. Lorsque l’Inquisition a commencé à regarder Rennes, cette position lui permettait de protéger certaines personnes. Pas toutes. »

« Amaury a compris immédiatement l’utilité de son mandat. Des dossiers lui ont été remis par les gens du Prince. Une partie des renseignements qui avaient permis de les construire venait de moi. »

*Aliénor laisse passer un silence.*

« Kermorvan a dû décider qui pouvait être soustrait à l’orage et qui ne le pouvait pas. Une partie de la noblesse a été protégée. D’autres, dans la haute bourgeoisie et la petite noblesse, ont été abandonnés à l’enquête, aux arrestations et à leurs conséquences. Ses choix ont tué des gens. »

« Mais rien de ce que je sais n’établit qu’il comprenait le mécanisme vampirique caché derrière les dossiers qu’on lui remettait. Il servait son mandat, avec les informations qu’on lui donnait. »

*Son regard devient dur.*

« Il a choisi quels hommes retirer de l’eau. D’autres avaient déjà choisi le bassin dans lequel ils se noieraient. »
""".strip(),
    "silence_alienor": """
*Aliénor sourit presque immédiatement.*

« Parce que tu poses beaucoup trop de questions. »

*Le sourire demeure une seconde, puis disparaît.*

« Et parce que certaines réponses tuent. Chez nous, savoir pourquoi un Ancien hait un autre, qui doit une dette, qui a trahi qui, ou quel mort aurait dû rester oublié peut suffire à faire de toi une cible avant même que tu comprennes la valeur de ce que tu sais. »

« Une partie de mon silence te protège donc réellement. »

*Elle incline légèrement la tête.*

« Une autre partie me protège, moi. »

« Je sais parfaitement qu’il existe des vérités sur mon passé qui modifieront la manière dont tu me regardes. Et je suis assez égoïste pour vouloir choisir le moment où elles entrent entre nous. »

« Enfin, je suis ta sire. Je crois avoir le droit de décider du rythme auquel je te livre certaines choses. Tu appelleras peut-être cela du contrôle. Tu n’auras pas entièrement tort. »

*Sa voix se fait plus douce.*

« Je veux que tu grandisses. Je n’ai jamais prétendu vouloir que tu le fasses loin de ma main. »
""".strip(),
    "secret_amour": """
*Aliénor reste parfaitement immobile.*

« Je voulais la place de Mikolai. Et il y eut une nuit où je voulus aussi sa mort. »

*Elle ne cherche pas à adoucir la phrase.*

« Je n’ai pas appelé l’Inquisition à Rennes. Elle était déjà là, attirée par ce que nos guerres avaient fait aux mortels et à la Mascarade. Mais j’ai vu cette menace et j’ai décidé de l’utiliser. »

« Je suis allée trouver Amaury. Je voulais que Mikolai soit désigné de manière à ce que l’Inquisition l’atteigne. J’ai posé une condition : aucun autre Toreador ne devait payer pour cela. »

« Guillaume l’a tué à la **Porte de la Madeleine** avant que le dispositif d’Amaury ne puisse l’atteindre. J’aurais obtenu sa place de toute manière. Cela aurait dû arrêter les choses. »

*Ses doigts se referment lentement.*

« Cela ne les a pas arrêtées. Des artistes, des bourgeois, des gens qui n’étaient pas Mikolai ont été pris. J’ai exigé qu’Amaury mette fin à ce que nous avions commencé. »

« La nuit où la succession devait se décider, j’ai essayé de rejoindre la Maison des Lumières. Une attaque de mortels m’en a empêchée. Les hommes du Prince sont arrivés au moment opportun pour me tirer de là et me maintenir loin de ce qui se passait ailleurs. Je n’ai compris que trop tard à quel point Amaury avait veillé à ce que je sois vue comme celle qu’il sauvait plutôt que comme celle qui aurait pu intervenir. »

*Aliénor soutient le regard de son infante.*

« Je n’ai pas voulu l’anéantissement de notre clan. Je n’ai pas voulu les morts qui ont suivi. Mais je ne vais pas me cacher derrière ce que je n’avais pas prévu. »

« Si tu veux savoir quelle vérité sur moi pourrait te faire cesser de m’aimer, la voici : lorsque notre monde s’est brisé, je n’étais pas seulement parmi ceux qui essayaient d’en ramasser les morceaux. »

*Un silence.*

« Cette nuit-là, j’avais aussi tenu le marteau. »

**Conséquences si cette réponse est effectivement jouée : +1 Flétrissure et 1 dégât aggravé de Volonté.**
""".strip(),
}


def get_scene() -> Scene:
    return Scene(
        schema_version=1,
        id="scene_privee_toreador_une_seule_question",
        title="Une seule question",
        intro_md=INTRO,
        choices=[
            Choice(
                id="une_question_secret_amour",
                label="Quelle vérité sur toi pourrait me faire cesser de t'aimer ?",
                answer_md=REPONSES["secret_amour"],
                ends_scene=True,
            ),
            Choice(
                id="une_question_verite_1493",
                label="Que s'est-il réellement passé en 1493 ?",
                answer_md=REPONSES["verite_1493"],
                ends_scene=True,
            ),
            Choice(
                id="une_question_kermorvan_1493",
                label="Qu'a réellement fait le seigneur de Kermorvan en 1493 ?",
                answer_md=REPONSES["seigneur_kermorvan_1493"],
                ends_scene=True,
            ),
            Choice(
                id="une_question_mikolai",
                label="Qu'était réellement Mikolai pour toi ?",
                answer_md=REPONSES["mikolai"],
                ends_scene=True,
            ),
            Choice(
                id="une_question_isabelle_mort",
                label="Comment Isabelle est-elle réellement morte ?",
                answer_md=REPONSES["isabelle_mort"],
                ends_scene=True,
            ),
            Choice(
                id="une_question_zvonimir",
                label="Qu'était Zvonimir pour toi ?",
                answer_md=REPONSES["zvonimir"],
                ends_scene=True,
            ),
            Choice(
                id="une_question_isabelle_identite",
                label="Qui était vraiment Isabelle ?",
                answer_md=REPONSES["isabelle_identite"],
                ends_scene=True,
            ),
            Choice(
                id="une_question_silence_alienor",
                label="Pourquoi me caches-tu autant de choses ?",
                answer_md=REPONSES["silence_alienor"],
                ends_scene=True,
            ),
            Choice(
                id="une_question_attente_alienor",
                label="Qu'attends-tu réellement de moi ?",
                answer_md=REPONSES["attente_alienor"],
                ends_scene=True,
            ),
        ],
        allow_undo=False,
        allow_restart_after_choice=False,
    )
