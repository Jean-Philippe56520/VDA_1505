from __future__ import annotations

"""Enrichissements préparatoires des rencontres de chasse.

Le Drive canonique (01 pour les règles, 11 pour la procédure) reste autoritaire.
Ce fichier n'est qu'une projection runtime MJ : un tirage, un affichage ou un clic
ne crée ni événement joué, ni connaissance PJ, ni PNJ canonique.

Les crochets majeurs sont volontairement formulés comme pistes/questions : le
répertoire étant public, ce fichier ne doit pas ajouter de résolution secrète MJ.
"""

from typing import Literal, TypedDict


HuntImportance = Literal["courante", "notable", "majeure"]


class HuntEnrichment(TypedDict):
    match: str
    importance: HuntImportance
    identite: str
    description: str
    ouverture: str
    consequence_contextuelle: str
    crochet: str
    supplement_reussite: str
    supplement_echec: str
    supplement_critique: str
    supplement_pyrrhus: str
    supplement_reussite_bestiale: str
    supplement_echec_bestial: str


def _entry(
    match: str,
    importance: HuntImportance,
    identite: str,
    description: str,
    ouverture: str,
    consequence_contextuelle: str = "",
    crochet: str = "",
    supplement_reussite: str = "",
    supplement_echec: str = "",
    supplement_critique: str = "",
    supplement_pyrrhus: str = "",
    supplement_reussite_bestiale: str = "",
    supplement_echec_bestial: str = "",
) -> HuntEnrichment:
    return {
        "match": match,
        "importance": importance,
        "identite": identite,
        "description": description,
        "ouverture": ouverture,
        "consequence_contextuelle": consequence_contextuelle,
        "crochet": crochet,
        "supplement_reussite": supplement_reussite,
        "supplement_echec": supplement_echec,
        "supplement_critique": supplement_critique,
        "supplement_pyrrhus": supplement_pyrrhus,
        "supplement_reussite_bestiale": supplement_reussite_bestiale,
        "supplement_echec_bestial": supplement_echec_bestial,
    }


HUNT_ENRICHMENTS: dict[str, list[HuntEnrichment]] = {
    "osiris_muse": [
        _entry(
            "Une noble mariée te demande un poème",
            "notable",
            "Une dame de la noblesse rennaise ; son nom peut être obtenu au cours de l'échange.",
            "Élégante, entourée mais momentanément seule, elle veut transformer une faveur artistique en intimité privilégiée.",
            "Lui demander son nom, sa maison, qui l'a invitée ou ce qu'elle attend réellement du poème ; observer bijoux, livrée et sceau.",
            "Une relation mondaine peut devenir un accès, un contact ou une opportunité de projet liée à l'Influence/Contacts nobles.",
            supplement_reussite="Nom et maison obtenus, avec une invitation ou un moyen crédible de la recontacter.",
            supplement_echec="Elle se retire sans scandale ; aucun bénéfice mécanique, mais son identité peut rester partiellement connue si l'échange a eu lieu.",
            supplement_critique="Opportunité RP — noblesse : -1 difficulté au prochain projet pertinent visant à améliorer un Historique directement lié à ce milieu ; usage unique.",
            supplement_pyrrhus="Le contact est acquis, mais avec une attente sociale, une promesse ou une surveillance conjugale à gérer.",
            supplement_reussite_bestiale="L'accès demeure possible, mais la dame devient imprudente ou dépendante ; -1 dé au prochain jet social visant à préserver la discrétion avec son entourage.",
            supplement_echec_bestial="Le cercle mondain se ferme temporairement : -1 dé au prochain jet directement lié à cette maison ou à ses proches.",
        ),
        _entry(
            "Un cercle d’art fermé débat de ton œuvre",
            "notable",
            "Un cercle artistique fermé ; l'hôte ou le membre dominant peut être identifié pendant la discussion.",
            "Quelques mécènes, lettrés et artistes évaluent qui mérite d'entrer dans leur réseau.",
            "Prendre la parole, demander qui tranche, repérer qui finance qui, offrir une dédicace ou obtenir une prochaine invitation.",
            "Accès social, contact de mécène ou opportunité de projet liée à l'Influence, aux Contacts ou aux Ressources selon la fiction.",
            supplement_reussite="Un nom utile, une invitation ou un relais social précis est obtenu.",
            supplement_echec="Le cercle reste fermé ; aucun malus automatique si le PJ se retire proprement.",
            supplement_critique="Opportunité RP : -1 difficulté au prochain projet pertinent d'Historique directement lié à ce cercle ; usage unique.",
            supplement_pyrrhus="Accès obtenu contre une prestation, une promesse ou une dette sociale clairement formulée.",
            supplement_reussite_bestiale="Le PJ gagne une place mais écrase un rival : +1 dé au premier jet pour exploiter l'accès, puis le rival devient une complication active.",
            supplement_echec_bestial="Réputation écornée : -1 dé au prochain jet social dans ce cercle précis.",
        ),
        _entry(
            "Banquet chez un marchand influent",
            "notable",
            "Un marchand influent ; son nom et son enseigne peuvent être obtenus sans difficulté si le PJ échange avec lui.",
            "Banquet d'affaires où contrats, protections et recommandations circulent davantage que le sang.",
            "Demander qui cherche un artiste, qui finance une maison, qui a besoin d'une faveur ; offrir une prestation future ou recueillir une confidence commerciale.",
            "Contact marchand, information économique ou opportunité RP liée à Ressources/Influence/Contacts si l'issue le justifie.",
            supplement_reussite="Un contact ou une information exploitable est acquis, sans bonus automatique supplémentaire.",
            supplement_echec="Le marchand reste cordial mais ne s'engage pas.",
            supplement_critique="Opportunité RP : -1 difficulté au prochain projet pertinent visant un Historique directement relié à ce réseau marchand ; usage unique.",
            supplement_pyrrhus="Le bénéfice existe, mais le marchand attend une prestation ou une faveur identifiable.",
            supplement_reussite_bestiale="Le réseau s'ouvre mais un convive est humilié : la prochaine exploitation du contact se fait avec une complication sociale.",
            supplement_echec_bestial="Le marchand ferme ses portes : -1 dé au prochain jet directement lié à son réseau.",
        ),
        _entry(
            "Dans un salon feutré, un homme te demande un poème",
            "majeure",
            "Un dévot cultivé à la présence anormalement sacrée ; son identité civile n'est pas donnée d'office et peut être obtenue.",
            "Calme, poli, sincèrement religieux. Sa proximité provoque un malaise surnaturel avant même que le PJ comprenne pourquoi.",
            "Lui demander son nom, sa paroisse, qui lui a parlé de l'artiste ou pourquoi il est venu ; observer symbole, accent, lettre, sceau ou formule répétée.",
            "La rencontre peut livrer une piste, un nom, un symbole ou un avantage ponctuel de suivi. Elle ne résout jamais ce qui l'a conduit ici.",
            "Pourquoi cet homme a-t-il précisément cherché le PJ, et d'où vient l'orientation qui l'a mené jusqu'à ce salon ?",
            supplement_reussite="Le PJ obtient un élément concret mais incomplet : nom, provenance, phrase ou objet permettant une première enquête.",
            supplement_echec="L'arc s'ouvre défavorablement : l'homme repart avec une impression forte du PJ, tandis que celui-ci ne conserve qu'un indice faible.",
            supplement_critique="Indice concret + avantage ponctuel : +1 dé au premier jet directement consacré à remonter cette piste. Aucun accès à la vérité complète.",
            supplement_pyrrhus="Un nom ou symbole exploitable est obtenu, mais l'homme reviendra ou attirera une attention extérieure.",
            supplement_reussite_bestiale="Une piste nette subsiste, mais le PJ s'est rendu mémorable ; le premier suivi adverse est facilité par la scène.",
            supplement_echec_bestial="Le PJ fuit ou rompt brutalement ; l'arc peut désormais progresser contre lui. Aucun jet de chasse ne permet de clore la menace.",
        ),
    ],
    "rat_egouts": [
        _entry(
            "Un jeune noble exige une saignée tardive",
            "notable",
            "Un jeune noble venu discrètement ; son nom, sa maison et son écuyer peuvent être obtenus dans le cadre du soin.",
            "Nerveux de sa réputation mais flatté par le traitement privé, il veut que personne ne sache qu'il est venu.",
            "Demander son nom complet, qui l'a recommandé, quel service il attend, ou obtenir l'identité de son écuyer.",
            "Contact noble potentiel ; peut devenir une opportunité RP d'Influence/Contacts nobles si l'interaction se déroule exceptionnellement bien.",
            supplement_reussite="Le PJ obtient un contact discret et un moyen crédible de le revoir.",
            supplement_echec="Le noble ne revient pas ; aucun malus automatique si la discrétion est préservée.",
            supplement_critique="Opportunité RP — noblesse : -1 difficulté au prochain projet pertinent visant un Historique lié à ce milieu ; usage unique.",
            supplement_pyrrhus="Le contact existe, mais l'écuyer ou la maison surveille désormais davantage les visites.",
            supplement_reussite_bestiale="Le noble devient trop attaché : accès facilité, mais -1 dé au prochain jet visant à maintenir une distance discrète avec lui.",
            supplement_echec_bestial="Rumeur possible dans sa maison : -1 dé au prochain jet directement lié à ce contact.",
        ),
        _entry(
            "Un noble du cœur bourgeois intra-muros est saigné",
            "notable",
            "Un noble du Cœur Bourgeois et un domestique mandaté par sa maison.",
            "Le soin est accepté, mais le domestique observe quantités, gestes et horaires comme un comptable de la réputation familiale.",
            "Obtenir le nom de la maison, demander qui a ordonné la visite, tester la loyauté du domestique, relever une livrée ou un sceau.",
            "Accès à une maison noble, information domestique ou opportunité RP liée à l'Influence/Contacts nobles.",
            supplement_reussite="Un nom de maison, un contact ou une invitation exploitable est obtenu.",
            supplement_echec="La maison se referme sans nécessairement devenir hostile.",
            supplement_critique="Opportunité RP — noblesse : -1 difficulté au prochain projet pertinent d'Historique lié à cette maison ; usage unique.",
            supplement_pyrrhus="Le service est acquis mais sous contrôle : le domestique devient un observateur récurrent.",
            supplement_reussite_bestiale="Le patient est fasciné mais le domestique devient soupçonneux ; le prochain jet social avec la maison subit -1 dé.",
            supplement_echec_bestial="La maison coupe l'accès : -1 dé au prochain jet visant spécifiquement à rétablir ce contact.",
        ),
        _entry(
            "Un magistrat influent souffre de migraines",
            "notable",
            "Un magistrat influent venu sous couvert de discrétion médicale.",
            "Contrôlé, exigeant et attentif au secret professionnel ; il connaît procédures, officiers et querelles de juridiction.",
            "Lui demander qui l'a recommandé, solliciter un éclairage juridique ou obtenir une présentation future sans formuler de faveur illégitime.",
            "Contact juridique, accès à une information procédurale ou avantage ponctuel sur une démarche directement liée.",
            supplement_reussite="Un renseignement juridique précis ou un moyen de reprendre contact est obtenu.",
            supplement_echec="Il repart sans s'engager et reste neutre.",
            supplement_critique="Avantage ponctuel : +1 dé au prochain jet directement lié au renseignement ou à l'introduction obtenue.",
            supplement_pyrrhus="L'information est utile mais le magistrat attend une discrétion ou un retour de faveur.",
            supplement_reussite_bestiale="Le magistrat reste accessible mais soupçonne une influence excessive : -1 dé au prochain jet social avec lui.",
            supplement_echec_bestial="Il coupe le contact et peut faire circuler une mise en garde informelle.",
        ),
        _entry(
            "Un professeur de droit canon vient pour une saignée discrète",
            "notable",
            "Un professeur de droit canon, froid et méthodique.",
            "Il remarque les imprécisions, connaît les tensions du Chapitre et traite toute faveur comme un précédent possible.",
            "Le faire parler d'un point de jurisprudence, d'une querelle interne ou d'un texte ; demander quelle autorité tranche réellement.",
            "Indice juridique, contact érudit ou avantage ponctuel pour une enquête/procédure directement reliée.",
            supplement_reussite="Une information utilisable sur le droit canon ou le Chapitre est obtenue.",
            supplement_echec="Il reste distant ; aucun bénéfice mécanique.",
            supplement_critique="Avantage ponctuel : +1 dé au prochain jet de recherche, droit ou influence directement fondé sur cette information.",
            supplement_pyrrhus="L'information est vraie mais incomplète ou assortie d'une mise en garde qui limite son usage.",
            supplement_reussite_bestiale="Le professeur comprend qu'il intéresse particulièrement le PJ et devient plus prudent.",
            supplement_echec_bestial="Le professeur se retire du réseau ; -1 dé au prochain jet visant à obtenir son aide.",
        ),
        _entry(
            "Un blessé amené en urgence suite à une impressionante entaille",
            "majeure",
            "Un blessé sans identité établie et la jeune femme qui l'accompagne ; leurs noms peuvent être obtenus avant que la situation ne dégénère.",
            "Entaille profonde déjà purulente, exigence étrange d'amputation immédiate, accompagnatrice très investie dans le contrôle de la douleur.",
            "Demander noms, origine de la blessure et raison de l'amputation ; examiner la plaie, les vêtements et les réactions du couple ; conserver un indice matériel si la fiction le permet.",
            "La scène peut fournir un échantillon, un détail médical ou une piste occulte. La nature exacte et la cause de l'anomalie ne sont jamais résolues par le seul jet de chasse.",
            "Pourquoi cette blessure ne suit-elle pas l'évolution attendue, et qu'est-ce qui a réellement causé l'entaille ?",
            supplement_reussite="Le PJ repart avec une observation concrète et une question exploitable ; un échantillon n'existe que s'il a réellement été obtenu en scène.",
            supplement_echec="La rencontre s'interrompt ou devient hostile ; le PJ conserve au mieux un détail visuel ou un nom partiel.",
            supplement_critique="Indice médical concret +1 dé au premier jet de Médecine ou d'Occultisme directement consacré à l'anomalie. Aucun diagnostic d'arc automatique.",
            supplement_pyrrhus="Le PJ obtient un indice exploitable mais la paire sait désormais qu'elle a été observée ou reconnue.",
            supplement_reussite_bestiale="Une trace ou un échantillon peut être acquis, mais la scène devient mémorable et dangereuse ; la piste est réciproque.",
            supplement_echec_bestial="La chasse s'inverse et l'arc s'ouvre contre le PJ : fuite, blessure ou poursuite possible selon la scène, sans résolution automatique.",
        ),
    ],
    "justicier_nocturne": [
        _entry(
            "Un usurier manipule les comptes des artisans",
            "notable",
            "Un usurier local et son réseau de débiteurs ; son registre ou ses commis peuvent permettre de l'identifier complètement.",
            "Il contrôle les artisans par des écritures, faux calculs et dettes entretenues plutôt que par la violence directe.",
            "Demander qui tient les livres, subtiliser/copier une page, suivre un commis ou faire nommer un créancier plus haut placé.",
            "Indice matériel possible : registre, reçu, sceau ou nom de complice. Peut donner +1 dé au prochain jet directement destiné à exploiter cette preuve.",
            supplement_reussite="Une preuve partielle ou un nom de complice est obtenu.",
            supplement_echec="Le réseau reste actif ; pas de pénalité automatique si le PJ n'est pas identifié.",
            supplement_critique="Preuve exploitable +1 dé au prochain jet directement lié à l'exposition ou au démantèlement de ce réseau local.",
            supplement_pyrrhus="La preuve est obtenue, mais un débiteur ou commis est compromis et peut subir des représailles.",
            supplement_reussite_bestiale="L'usurier cède une information mais sait qu'il est visé ; il commence à effacer ses traces.",
            supplement_echec_bestial="Le réseau est alerté : -1 dé au prochain jet de discrétion/infiltration visant ces mêmes comptes.",
        ),
        _entry(
            "Un réseau protégé par la garde opère en silence",
            "majeure",
            "Un réseau criminel bénéficiant d'une protection dans la garde ; aucun commanditaire supérieur n'est donné d'office.",
            "Les exécutants semblent trop sereins face aux patrouilles, et certains itinéraires sont manifestement laissés libres.",
            "Identifier un officier, suivre un messager, obtenir un signe de reconnaissance ou conserver une preuve de paiement/protection.",
            "Crochet de corruption : le jet peut donner un officier, une preuve ou un accès, jamais cartographier tout le réseau.",
            "Jusqu'où remonte la protection, et qui ferme les yeux au-dessus des exécutants visibles ?",
            supplement_reussite="Un officier, trajet ou signe de protection est identifié comme première piste.",
            supplement_echec="Le PJ comprend qu'une protection existe mais ne peut pas encore la rattacher à une personne fiable.",
            supplement_critique="Indice concret +1 dé au premier jet directement consacré à remonter la chaîne de protection.",
            supplement_pyrrhus="Un nom ou une preuve sort, mais le réseau apprend qu'une enquête informelle est en cours.",
            supplement_reussite_bestiale="Un exécutant parle sous la peur ; l'information est utile mais la garde devient plus méfiante dans le secteur.",
            supplement_echec_bestial="La protection se resserre : -1 dé au prochain jet visant à infiltrer ou surprendre ce réseau précis.",
        ),
        _entry(
            "Un réseau d’enlèvements organisé opère sous la tannerie",
            "majeure",
            "Une cellule organisée d'enleveurs sous la tannerie ; un chef local ou un intermédiaire peut être identifié.",
            "Réseau plus structuré qu'une bande de rue : passages, gardes, lieux de rétention et relais semblent coordonnés.",
            "Sauver une victime, capturer un intermédiaire, relever un symbole, récupérer une liste ou suivre une voie de sortie.",
            "La chasse peut briser une cellule locale et fournir une piste ; elle ne révèle ni ne détruit automatiquement l'organisation au-delà.",
            "Qui fournit les cibles, et où les victimes qui quittent la tannerie sont-elles conduites ?",
            supplement_reussite="Une victime, un intermédiaire ou un document livre une première direction exploitable.",
            supplement_echec="La cellule se replie ; un détail de trajet ou de méthode peut toutefois survivre à l'échec.",
            supplement_critique="Cellule locale neutralisée + indice concret +1 dé au premier jet de suivi vers l'échelon suivant.",
            supplement_pyrrhus="Une piste nette est obtenue, mais un chef ou messager échappe au PJ et peut prévenir l'étage supérieur.",
            supplement_reussite_bestiale="Le PJ obtient une information sous la violence ; elle est exploitable, mais les survivants savent exactement qui les a frappés.",
            supplement_echec_bestial="Le réseau disparaît du secteur immédiat et peut agir contre un témoin ou le PJ avant d'être retrouvé.",
        ),
        _entry(
            "Un maître tortionnaire organise enlèvements et supplices",
            "majeure",
            "Un maître tortionnaire protégé par des relais corrompus ; ses soutiens ne sont pas tous identifiés.",
            "Il dispose de lieux, d'hommes et d'une impunité qui dépassent la simple brutalité individuelle.",
            "Le faire nommer un protecteur, récupérer une clé/lettre/registre, libérer un témoin ou suivre l'évacuation d'un complice.",
            "La chute du tortionnaire peut créer une preuve, un témoin ou un vide de pouvoir ; elle ne détruit pas automatiquement ses protections.",
            "Qui lui garantissait l'impunité, et qui cherchera à récupérer son réseau après sa chute ?",
            supplement_reussite="Un témoin ou une preuve survit et pointe vers un relais précis.",
            supplement_echec="Le tortionnaire ou un complice s'échappe ; le PJ sait désormais qu'une protection structurée existe.",
            supplement_critique="Le nœud local tombe et un indice exploitable donne +1 dé au premier jet visant ses protecteurs. L'arc reste ouvert.",
            supplement_pyrrhus="Le nœud local tombe, mais le scandale attire garde, rivaux ou protecteurs avant que toutes les preuves soient sécurisées.",
            supplement_reussite_bestiale="Le PJ gagne la scène par la terreur ; une preuve subsiste, mais un témoin devient difficile à utiliser proprement.",
            supplement_echec_bestial="Le tortionnaire marque le PJ comme cible et peut déplacer ses opérations ; -1 dé au prochain jet de traque directe contre lui.",
        ),
        _entry(
            "Un sorcier exalté enlève des pauvres",
            "majeure",
            "Un sorcier fanatique dirigeant une petite cellule locale ; son commanditaire occulte n'est pas établi par cette rencontre.",
            "Il parle en signes, prophéties et fragments de rituel, avec des victimes préparées comme offrandes.",
            "Le capturer avant qu'il ne meure, lui faire nommer un lieu ou un intermédiaire, récupérer un symbole, un texte, une substance ou un objet rituel.",
            "Objet/indice de quête possible : fragment rituel, symbole ou provenance. Même une victoire critique ne révèle ni n'atteint automatiquement le commanditaire.",
            "À qui ou à quoi cette cellule adresse-t-elle réellement ses offrandes, et comment communique-t-elle avec l'échelon supérieur ?",
            supplement_reussite="Un symbole, un lieu ou un nom partiel constitue une piste concrète.",
            supplement_echec="La cellule s'éparpille ; le PJ conserve au mieux un fragment rituel ou un témoignage incomplet.",
            supplement_critique="Cellule locale neutralisée + objet/indice concret +1 dé au premier jet d'Occultisme ou d'enquête directement consacré à la piste. Aucun commanditaire révélé automatiquement.",
            supplement_pyrrhus="La cellule tombe mais un relais extérieur apprend l'intervention du PJ.",
            supplement_reussite_bestiale="Le sorcier lâche une piste sous la terreur ; elle est exploitable mais peut être mêlée de fanatisme et doit être vérifiée.",
            supplement_echec_bestial="Le sorcier s'échappe ou laisse un signe destiné à ses alliés : l'arc peut progresser contre le PJ.",
        ),
    ],
    "roi_de_la_nuit": [
        _entry(
            "Un jeune noble rennais sollicite une annulation discrète",
            "notable",
            "Un jeune noble rennais demandeur d'une annulation canonique ; son nom et sa maison sont disponibles dans le dossier.",
            "Il veut une solution juridique discrète, mais la véritable valeur de la rencontre est l'accès à son réseau familial.",
            "Lire le nom de maison, demander qui l'a conseillé, identifier le juriste adverse ou proposer une future audience.",
            "Contact noble/ecclésiastique et opportunité RP possible pour Influence/Contacts nobles ou religieux.",
            supplement_reussite="Le PJ obtient un contact ou une introduction utilisable.",
            supplement_echec="Le dossier stagne ; aucun malus automatique si l'avis reste professionnel.",
            supplement_critique="Opportunité RP : -1 difficulté au prochain projet pertinent visant un Historique directement lié à cette maison ou au réseau canonique mobilisé ; usage unique.",
            supplement_pyrrhus="L'accès est réel mais l'affaire comporte une contrepartie civile ou familiale qui reviendra plus tard.",
            supplement_reussite_bestiale="Le demandeur devient trop dépendant : -1 dé au prochain jet visant à lui imposer une limite ou une distance.",
            supplement_echec_bestial="Le dossier se retourne contre le PJ : -1 dé au prochain jet social directement lié à cette maison.",
        ),
        _entry(
            "Une veuve influente cherche l’appui du Chapitre",
            "notable",
            "Une veuve influente et l'héritier qu'elle cherche à protéger.",
            "Elle comprend les rapports de force et cherche un appui canonique assez solide pour devenir protection sociale.",
            "Demander qui menace l'héritage, quel notaire ou parent conteste, obtenir une lettre ou une présentation familiale.",
            "Contact de maison, accès à une querelle successorale ou opportunité RP d'Influence/Contacts.",
            supplement_reussite="Une introduction familiale ou une information successorale exploitable est obtenue.",
            supplement_echec="La veuve cherche une autre voie ; pas de pénalité automatique si le secret est préservé.",
            supplement_critique="Opportunité RP : -1 difficulté au prochain projet pertinent d'Historique lié à cette maison ; usage unique.",
            supplement_pyrrhus="La relation est acquise, mais une autre branche familiale considère le PJ comme partie prenante.",
            supplement_reussite_bestiale="La gratitude publique facilite le contact mais attire une jalousie ; le prochain usage du réseau comporte une complication sociale.",
            supplement_echec_bestial="La famille associe le PJ à l'échec : -1 dé au prochain jet visant spécifiquement ce réseau.",
        ),
        _entry(
            "Une maison rennaise aux ambitions croissantes veut que le Chapitre",
            "notable",
            "Une maison rennaise en ascension ; le représentant et la maison sont identifiables dans la demande.",
            "Elle cherche à transformer une validation canonique en levier de pouvoir urbain.",
            "Demander qui bénéficiera réellement de la décision, relever les autres signataires, exiger un écrit ou obtenir l'identité du relais civil.",
            "Information politique, contact ou opportunité RP d'Influence si le PJ transforme correctement l'accès en projet ultérieur.",
            supplement_reussite="Un relais civil ou une information de coalition est obtenu.",
            supplement_echec="La maison cherche un autre intermédiaire ; aucun malus automatique hors conséquence fictionnelle.",
            supplement_critique="Opportunité RP : -1 difficulté au prochain projet pertinent d'Historique lié à cette maison ou à son milieu ; usage unique.",
            supplement_pyrrhus="Le contact est acquis mais le PJ est désormais compté parmi les appuis possibles de la maison.",
            supplement_reussite_bestiale="Le poids du PJ devient trop visible : +1 dé au premier usage immédiat du contact, mais une faction rivale le remarque.",
            supplement_echec_bestial="La maison se braque et cherche une autre voie : -1 dé au prochain jet directement lié à sa coopération.",
        ),
        _entry(
            "Un dossier évoque indirectement le pouvoir ducal",
            "majeure",
            "Un dossier canonique dont les conséquences peuvent remonter au pouvoir ducal ; les signataires et relais doivent être lus dans le dossier, pas inventés par le tirage.",
            "La formulation religieuse masque un enjeu politique plus large que le Chapitre et potentiellement plus large que Rennes.",
            "Identifier qui a déposé le dossier, qui doit le recevoir ensuite, quelles maisons y gagnent, et quelles mentions relient l'affaire à Nantes.",
            "Indice politique, chaîne documentaire ou accès à un relais. Le jet n'établit jamais à lui seul l'intention du pouvoir ducal.",
            "Qui cherche à faire remonter cette affaire au niveau ducal, et dans quel intérêt ?",
            supplement_reussite="Une signature, un relais ou une étape de transmission est isolé comme piste.",
            supplement_echec="Le dossier change de main ou se referme ; le PJ sait qu'il dépasse Rennes mais manque encore d'un relais fiable.",
            supplement_critique="Indice documentaire précis +1 dé au premier jet directement consacré à remonter la chaîne politique. Aucun acteur supérieur n'est déclaré coupable automatiquement.",
            supplement_pyrrhus="Une piste est obtenue mais le nom du PJ peut remonter avec le dossier.",
            supplement_reussite_bestiale="Le PJ force la lecture ou la décision : l'information sort, mais son intérêt pour le dossier devient visible.",
            supplement_echec_bestial="Le dossier lui échappe et l'arc peut progresser hors de son contrôle ; -1 dé au prochain jet visant à reprendre cette chaîne documentaire.",
        ),
        _entry(
            "Un arrangement matrimonial, présenté comme canonique",
            "majeure",
            "Les représentants de deux maisons et un arrangement matrimonial dont la portée dépasse le simple droit canon.",
            "La négociation emploie le langage de l'Église pour déplacer un équilibre de pouvoir ; Nantes est évoquée sans que son rôle soit établi.",
            "Demander qui a proposé l'union, qui s'y oppose, qui garantit la dot, ou obtenir un exemplaire/nom de messager lié à Nantes.",
            "Contact politique ou indice de circulation entre Rennes et Nantes ; aucune alliance supérieure n'est canonisée par le tirage.",
            "Qui pousse réellement cette union, et quel équilibre cherche-t-on à déplacer ?",
            supplement_reussite="Un nom de relais ou une pièce de la négociation devient exploitable.",
            supplement_echec="L'accord échoue ou se déplace ailleurs ; le PJ conserve une compréhension partielle des intérêts en présence.",
            supplement_critique="Indice précis + opportunité RP : -1 difficulté au prochain projet pertinent d'Influence/Contacts directement fondé sur ce réseau ; usage unique.",
            supplement_pyrrhus="Le contact est acquis mais le PJ devient partie visible d'une négociation qui dépasse son territoire habituel.",
            supplement_reussite_bestiale="L'accord avance sous pression ; +1 dé au premier jet pour exploiter l'ouverture, mais une maison rivale identifie le PJ comme acteur.",
            supplement_echec_bestial="Les parties cherchent un responsable : -1 dé au prochain jet social directement lié à cette négociation.",
        ),
        _entry(
            "Le Gardien du Tribunal Canonique vous convoque",
            "notable",
            "Le Gardien du Tribunal Canonique, autorité de procédure et de mémoire institutionnelle.",
            "Il teste moins un dossier qu'une méthode : précision, retenue, connaissance des formes et capacité à ne pas trop expliquer.",
            "Lui demander quelle pratique il juge fragile, quel texte il recommande, ou obtenir l'autorisation de consulter une ressource normalement peu accessible.",
            "Accès institutionnel, contact ou avantage ponctuel de droit canon.",
            supplement_reussite="Un conseil ou un accès limité est obtenu.",
            supplement_echec="Le Gardien reste neutre et n'ouvre aucune porte supplémentaire.",
            supplement_critique="Avantage ponctuel : +1 dé au prochain jet de droit canon/procédure directement fondé sur son conseil ou son accès.",
            supplement_pyrrhus="L'accès est obtenu mais laisse une trace administrative ou une attente de conformité.",
            supplement_reussite_bestiale="Le Gardien respecte la force du PJ mais note son aplomb ; bénéfice immédiat sans gain durable automatique.",
            supplement_echec_bestial="Surveillance accrue : -1 dé au prochain jet visant à contourner ou accélérer une procédure sous son regard.",
        ),
        _entry(
            "Un Inquisiteur ‘de passage’ (Frère Séverin d’Angers)",
            "majeure",
            "Frère Séverin d'Angers, Inquisiteur de passage ; cordial, cultivé et méthodiquement attentif.",
            "Il demande archives et scribes avec une politesse qui rend chaque question plus dangereuse qu'une accusation ouverte.",
            "Lui demander son mandat, qui l'a recommandé, ce qu'il cherche exactement, quels noms/dates l'intéressent ; lui proposer un parcours contrôlé et observer ce qu'il refuse de consulter.",
            "La rencontre peut donner une question précise, un détail de mandat, un contact ecclésiastique ou un avantage ponctuel pour comprendre sa recherche. Elle ne résout jamais ses motifs en un jet.",
            "Pourquoi Séverin est-il venu maintenant, qui l'a orienté, et quelle incohérence cherche-t-il réellement ?",
            supplement_reussite="Le PJ circonscrit une partie de son intérêt : une date, un type de dossier, un nom ou une méthode de recherche.",
            supplement_echec="Séverin obtient l'initiative : il reste, revient ou choisit lui-même le prochain angle d'enquête.",
            supplement_critique="Piste précise +1 dé au premier jet directement destiné à comprendre son mandat, suivre ses contacts ou préparer sa prochaine visite. Aucun arc résolu.",
            supplement_pyrrhus="Le PJ détourne une partie de l'attention, mais Séverin prolonge son séjour ou conserve une question non résolue.",
            supplement_reussite_bestiale="Séverin perçoit qu'il est jaugé : une information peut être gagnée, mais -1 dé au prochain jet social direct avec lui.",
            supplement_echec_bestial="Séverin repart avec un détail exploitable et l'arc progresse contre le PJ ; aucune conclusion automatique n'est tirée à sa place.",
        ),
    ],
}


def find_hunt_enrichment(table_id: str, rencontre: str | None) -> HuntEnrichment | None:
    if not rencontre:
        return None
    folded = rencontre.casefold()
    for enrichment in HUNT_ENRICHMENTS.get(table_id, []):
        if enrichment["match"].casefold() in folded:
            return enrichment
    return None
