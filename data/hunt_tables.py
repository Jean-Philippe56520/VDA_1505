# hunt_tables.py — tables de chasse

from __future__ import annotations
from typing import Dict, List, TypedDict


class HuntEntry(TypedDict):
    rencontre: str
    res_temp: str
    effet: str
    victoire_critique: str
    victoire_pyrrhus: str
    reussite_bestiale: str
    echec_bestial: str


class HuntTable(TypedDict):
    label: str
    entries: List[HuntEntry]


HUNT_TABLES: Dict[str, HuntTable] = {'osiris_muse': {'label': 'Osiris — Artiste',
                 'entries': [{'rencontre': 'Après une déclamation au théâtre, un admirateur te suit en coulisses. Un '
                                           'sourire, un mot, et il croit obtenir un privilège : quelques minutes seul '
                                           'avec toi.',
                              'res_temp': 'Sanguine (Fugace)',
                              'effet': 'Tu l’emmènes à l’écart, et la morsure devient un baiser. Il repart persuadé '
                                       'd’avoir été choisi.',
                              'victoire_critique': 'Il en ressort exalté mais intact : il deviendra ton meilleur '
                                                   'propagandiste dans les salons.',
                              'victoire_pyrrhus': 'Tu le laisses un peu trop marqué : il cherche à te revoir dès le '
                                                  'lendemain, insistant.',
                              'reussite_bestiale': 'Ta Bête savoure l’adoration : tu le rends dépendant, presque '
                                                   'fanatique.',
                              'echec_bestial': 'Un sursaut de peur : il te repousse, crie, et l’ombre des coulisses '
                                               'devient un danger.'},
                             {'rencontre': 'Un rival artistique te provoque en public. Après le duel verbal, un de ses '
                                           'proches, bouleversé, te réclame un entretien privé… pour « comprendre ton '
                                           'génie ».',
                              'res_temp': 'Sanguine (Fugace)',
                              'effet': 'La tension nourrit ton charme : tu transformes la humiliation en fascination '
                                       'intime.',
                              'victoire_critique': 'Tu retournes la scène : le rival perd son influence, et toi tu '
                                                   'gagnes un nouveau cercle d’admirateurs.',
                              'victoire_pyrrhus': 'Tu réussis, mais l’émotion déborde : l’admirateur sort trop pâle et '
                                                  'trop heureux, ce qui attire les questions.',
                              'reussite_bestiale': 'Tu prends trop, grisée : la proie s’effondre et le théâtre '
                                                   's’agite.',
                              'echec_bestial': 'Ta Bête te fait humilier quelqu’un de trop ; la scène devient '
                                               'scandale.'},
                             {'rencontre': 'En coulisses, une habilleuse jalouse te surveille. Elle fouille les '
                                           'costumes, écoute les murmures, et cherche une faille.',
                              'res_temp': 'Aucune',
                              'effet': 'Tu joues la normalité : pas de nourrissage, seulement contrôle social.',
                              'victoire_critique': 'Tu la retournes par une promesse ou une faveur : elle devient un '
                                                   'écran utile.',
                              'victoire_pyrrhus': 'Tu la calmes, mais elle garde une rancune silencieuse.',
                              'reussite_bestiale': 'Ta Bête la menace : elle se met à parler en secret.',
                              'echec_bestial': 'Tu perds ton masque : elle te surprend au mauvais moment et la rumeur '
                                               'démarre.'},
                             {'rencontre': 'Le directeur du théâtre, pragmatique, t’invite dans son bureau. Il veut '
                                           't’attacher à l’affiche. Il croit que tu as besoin de lui ; tu sais qu’il a '
                                           'besoin de toi.',
                              'res_temp': 'Aucune',
                              'effet': 'Tu fais de la négociation une danse. Un contact, un souffle, et il se rend '
                                       'disponible.',
                              'victoire_critique': 'Contrat parfait, discrétion assurée : tu tiens une scène stable '
                                                   'dans ton territoire.',
                              'victoire_pyrrhus': 'Tu réussis, mais il devient possessif : il réclame ton exclusivité.',
                              'reussite_bestiale': 'Tu le domines trop : il te craint, et la peur attire les ragots.',
                              'echec_bestial': 'Il se braque : il tente de te nuire par orgueil.'},
                             {'rencontre': 'Un jeune disciple te récite tes propres vers, tremblant. Il te supplie de '
                                           'le corriger « en privé ». Il est prêt à tout pour ton regard.',
                              'res_temp': 'Sanguine (Fugace)',
                              'effet': 'Tu le nourris comme on signe un autographe : un moment unique qu’il idolâtre.',
                              'victoire_critique': 'Il repart illuminé, et sa loyauté devient un fil facile à tirer.',
                              'victoire_pyrrhus': 'Tu réussis, mais il s’accroche : il rôde près de chez toi.',
                              'reussite_bestiale': 'Ta Bête le marque trop : obsession en germe.',
                              'echec_bestial': 'Il panique au dernier instant : il fuit et parle trop.'},
                             {'rencontre': 'Soir de triomphe. Après les applaudissements, un mécène te fait ouvrir un '
                                           'petit salon derrière la scène. Les regards sont partout, mais la porte se '
                                           'ferme.',
                              'res_temp': 'Flegmatique (Intense)',
                              'effet': 'Tu choisis une proie parmi les admirateurs, et tu fais de la morsure une '
                                       'consécration.',
                              'victoire_critique': 'Tu ressors renforcée et intangible : personne ne remet en cause ta '
                                                   'place.',
                              'victoire_pyrrhus': 'Tu réussis, mais une silhouette a vu l’entrée dans la pièce et s’en '
                                                  'souviendra.',
                              'reussite_bestiale': 'Tu t’abandonnes : un corps vacille, on appelle à l’aide, et ta '
                                                   'nuit se fissure.',
                              'echec_bestial': 'Ta Bête fait du théâtre : trop de domination, trop de traces.'},
                             {'rencontre': 'Dans un salon privé du cœur bourgeois, un mécène te présente comme sa '
                                           'perle. Il te prête une pièce pour « te reposer ». Une proie s’y glisse '
                                           'd’elle-même.',
                              'res_temp': 'Aucune',
                              'effet': 'Tu te nourris dans le velours, sans bruit, en gardant le contrôle de la '
                                       'soirée.',
                              'victoire_critique': 'Le mécène se croit honoré : il ouvre davantage son réseau et te '
                                                   'protège des rumeurs.',
                              'victoire_pyrrhus': 'Tu réussis, mais le mécène sent ta prise d’ascendant et tente de '
                                                  'resserrer sa cage.',
                              'reussite_bestiale': 'Tu prends trop par défi : la proie ressort chancelante et la '
                                                   'soirée s’alourdit.',
                              'echec_bestial': 'Ta Bête humilie quelqu’un : le cercle se retourne contre toi.'},
                             {'rencontre': 'Une noble mariée te demande un poème « rien que pour elle ». Elle t’invite '
                                           'à l’écart, certaine d’être unique.',
                              'res_temp': 'Sanguine (Fugace)',
                              'effet': 'Un baiser suffit. Elle repart brûlante, confuse, persuadée d’avoir vécu une '
                                       'révélation.',
                              'victoire_critique': 'Elle protège ton nom, et ses invitations deviennent des portes '
                                                   'dorées.',
                              'victoire_pyrrhus': 'Tu réussis, mais son mari remarque un changement et se met à '
                                                  'surveiller.',
                              'reussite_bestiale': 'Ta Bête la rend imprudente : elle parle, elle écrit, elle '
                                                   's’expose.',
                              'echec_bestial': 'Elle panique et te maudit : scandale possible.'},
                             {'rencontre': 'Un cercle d’art fermé débat de ton œuvre. On te jauge, on te classe, on te '
                                           'compare. Ici, nourrir serait une erreur : il faut gagner.',
                              'res_temp': 'Aucune',
                              'effet': 'Tu joues la stratégie, pas la faim : tu plantes des idées, des alliances, des '
                                       'dettes.',
                              'victoire_critique': 'Tu sors de là intouchable : le cercle te consacre, et ton '
                                                   'territoire social s’élargit.',
                              'victoire_pyrrhus': 'Tu gagnes, mais au prix d’une promesse : on attend de toi une '
                                                  'prestation risquée.',
                              'reussite_bestiale': 'Ta Bête te fait écraser un rival : il prépare sa vengeance.',
                              'echec_bestial': 'Tu perds la face : l’assemblée te rejette et la rumeur se fixe.'},
                             {'rencontre': 'Un mécène possessif t’invite à un banquet privé. Il veut te garder près de '
                                           'lui, comme un objet rare. Il ne te laisse pas respirer.',
                              'res_temp': 'Flegmatique (Intense)',
                              'effet': 'Tu transformes la possession en piège : tu choisis un admirateur, pas le '
                                       'mécène.',
                              'victoire_critique': 'Le mécène reste persuadé de te tenir, tandis que tu t’en sers '
                                                   'comme couverture parfaite.',
                              'victoire_pyrrhus': 'Tu réussis, mais le mécène devient jaloux : il te réclame un prix.',
                              'reussite_bestiale': 'Ta Bête répond à l’emprise : tu marques quelqu’un trop fort, et la '
                                                   'scène devient dangereuse.',
                              'echec_bestial': 'Tu t’emportes contre le mécène : il peut devenir un ennemi puissant.'},
                             {'rencontre': 'À la fin d’un banquet, un convive te propose de te raccompagner. Dans la '
                                           'voiture, dans l’ombre, il croit obtenir un instant volé.',
                              'res_temp': 'Aucune',
                              'effet': 'Tu fais de l’instant une offrande : il repart persuadé d’avoir touché la Muse.',
                              'victoire_critique': 'Il devient un relais enthousiaste : invitations, cadeaux, '
                                                   'informations.',
                              'victoire_pyrrhus': 'Tu réussis, mais il se vante à demi-mots : trop de gens devinent '
                                                  'qu’il t’a vue seule.',
                              'reussite_bestiale': 'Ta Bête veut recommencer : tu le rends dépendant.',
                              'echec_bestial': 'Un témoin surgit : tu dois couper court.'},
                             {'rencontre': 'Un collectionneur d’art t’adore. Il te suit de rue en rue et t’offre une '
                                           'pièce « plus calme » pour écrire. Il te pousse subtilement à sortir de ton '
                                           'circuit habituel.',
                              'res_temp': 'Aucune',
                              'effet': 'Tu peux refuser et rester dans ton territoire : ce soir, c’est le contrôle qui '
                                       'nourrit.',
                              'victoire_critique': 'Tu le maintiens à distance tout en gardant ses ressources : il '
                                                   'continue à financer sans posséder.',
                              'victoire_pyrrhus': 'Tu réussis, mais tu acceptes de le suivre « pour une minute ». '
                                                  'Emportée par l’élan (ou par l’admirateur), ⚠️ tu franchis la limite '
                                                  'de ton territoire du cœur bourgeois intra-muros : erreur politique '
                                                  'et dangereuse.',
                              'reussite_bestiale': 'Ta Bête se délecte de l’emprise : tu le terrorises, et il devient '
                                                   'dangereux.',
                              'echec_bestial': 'Il te voit différemment : peur, soupçon, et obsession noire.'},
                             {'rencontre': 'Dans la rue, ta déclamation attire une foule élégante. Un admirateur '
                                           't’offre une rose et demande un mot « juste pour lui ».',
                              'res_temp': 'Aucune',
                              'effet': 'Tu l’emmènes sous une arcade : un baiser, une morsure, et il repart enivré.',
                              'victoire_critique': 'La foule ne remarque rien : ta légende grandit sans incident.',
                              'victoire_pyrrhus': 'Tu réussis, mais un témoin croit reconnaître un geste trop intime.',
                              'reussite_bestiale': 'Ta Bête te pousse : tu vas trop loin, trop vite, et le risque '
                                                   'public explose.',
                              'echec_bestial': 'Tu perds le contrôle : cris, fuite, et une patrouille se rapproche.'},
                             {'rencontre': 'La foule devient trop dense après un succès. On te touche, on t’entoure, '
                                           'on t’appelle. C’est le moment où nourrir serait une erreur.',
                              'res_temp': 'Aucune',
                              'effet': 'Tu te retires avec grâce, sans incident, en gardant ton mystère.',
                              'victoire_critique': 'Tu transformes la cohue en adoration organisée : ton nom circule '
                                                   'comme une prière.',
                              'victoire_pyrrhus': 'Tu t’en sors, mais on t’attend désormais à chaque coin de rue : '
                                                  'pression constante.',
                              'reussite_bestiale': 'Ta Bête veut choisir une proie dans la foule : c’est presque un '
                                                   'désastre.',
                              'echec_bestial': 'Tu craques et la scène devient publique : danger de Mascarade.'},
                             {'rencontre': 'Un admirateur fanatique te parle comme d’une sainte de l’art. Il demande '
                                           'une confession intime. Il ne veut pas ton corps : il veut ta présence.',
                              'res_temp': 'Aucune',
                              'effet': 'Tu le nourris sans le briser : tu le gardes utile, stable, discret.',
                              'victoire_critique': 'Il devient un gardien de ta réputation, prêt à étouffer les '
                                                   'rumeurs.',
                              'victoire_pyrrhus': 'Tu réussis, mais il veut te voir plus souvent : le fanatisme '
                                                  'grignote la discrétion.',
                              'reussite_bestiale': 'Ta Bête se moque de sa foi : il se retourne contre toi.',
                              'echec_bestial': 'Il panique, prie, et court parler à un prêtre.'},
                             {'rencontre': 'Un duel artistique improvisé attire des nobles. Après ta victoire, un '
                                           'admirateur exalté veut te suivre « jusqu’à l’aube ». Il insiste, te tire '
                                           'vers des ruelles moins sûres.',
                              'res_temp': 'Sanguine (Fugace)',
                              'effet': 'L’adrénaline rend la prise facile, mais chaque pas compte : tu es visible.',
                              'victoire_critique': 'Tu te nourris et disparais, laissant la foule avec ton mythe, pas '
                                                   'avec ton ombre.',
                              'victoire_pyrrhus': 'Tu réussis, mais la poursuite t’emporte. Emportée par l’élan (ou '
                                                  'par l’admirateur), ⚠️ tu franchis la limite de ton territoire du '
                                                  'cœur bourgeois intra-muros : erreur politique et dangereuse.',
                              'reussite_bestiale': 'Ta Bête répond à l’exaltation : tu marques trop et déclenches un '
                                                   'scandale.',
                              'echec_bestial': 'Tu te fais surprendre : une patrouille intervient.'},
                             {'rencontre': 'Poème nocturne sous les arcades du cœur bourgeois. Deux couples '
                                           's’arrêtent, fascinés. Une proie possible… mais trop de regards.',
                              'res_temp': 'Aucune',
                              'effet': 'Tu choisis de ne pas chasser : tu récoltes admiration et informations.',
                              'victoire_critique': 'Tu obtiens une invitation dans un salon très fermé, en échange '
                                                   'd’un texte dédié.',
                              'victoire_pyrrhus': 'Tu restes sur la retenue, mais la faim monte : frustration.',
                              'reussite_bestiale': 'Ta Bête veut choisir maintenant : tu frôles l’incident.',
                              'echec_bestial': 'Tu fais peur : les couples s’éloignent et parlent d’une ‘présence '
                                               'glacée’.'},
                             {'rencontre': 'Une patrouille rôde près d’un théâtre. Un admirateur te propose un passage '
                                           '‘plus sûr’… qui s’approche dangereusement de la limite de ton territoire.',
                              'res_temp': 'Flegmatique (Fugace)',
                              'effet': 'Tu te nourris à la marge, puis tu reviens dans la zone sûre sans bruit.',
                              'victoire_critique': 'Tu manœuvres la patrouille par des détours et préserves ta scène '
                                                   'comme un sanctuaire.',
                              'victoire_pyrrhus': 'Tu réussis, mais tu suis le passage trop loin. Emportée par l’élan '
                                                  '(ou par l’admirateur), ⚠️ tu franchis la limite de ton territoire '
                                                  'du cœur bourgeois intra-muros : erreur politique et dangereuse.',
                              'reussite_bestiale': 'Ta Bête s’agace : tu deviens brusque et suspecte.',
                              'echec_bestial': 'La patrouille vous arrête : contrôle, questions, risque.'},
                             {'rencontre': 'Invitation dans un hôtel particulier du cœur bourgeois. On te demande une '
                                           'lecture privée pour quelques invités triés.',
                              'res_temp': 'Flegmatique (Fugace)',
                              'effet': 'Tu choisis une proie parmi les admirateurs, et tu la conduis à l’écart avec '
                                       'une élégance implacable.',
                              'victoire_critique': 'Tout le monde ressort conquis : ton réseau social s’épaissit.',
                              'victoire_pyrrhus': 'Tu réussis, mais une servante te voit disparaître avec quelqu’un.',
                              'reussite_bestiale': 'Ta Bête veut prolonger : tu affaiblis trop et la soirée se fige.',
                              'echec_bestial': 'Tu fais un geste de trop : quelqu’un comprend qu’il ne s’agit pas que '
                                               'd’art.'},
                             {'rencontre': 'Un mécène te propose de lire tes vers dans une résidence « tout près ». '
                                           'C’est encore intra-muros… mais pas dans ton cœur bourgeois habituel.',
                              'res_temp': 'Sanguine (Fugace)',
                              'effet': 'Tu joues l’intimité : un baiser suffit à obtenir ce que tu veux.',
                              'victoire_critique': 'Le mécène se croit honoré : il finance davantage et protège ta '
                                                   'liberté.',
                              'victoire_pyrrhus': 'Tu réussis, mais la soirée se prolonge et on t’entraîne hors de ta '
                                                  'zone. Emportée par l’élan (ou par l’admirateur), ⚠️ tu franchis la '
                                                  'limite de ton territoire du cœur bourgeois intra-muros : erreur '
                                                  'politique et dangereuse.',
                              'reussite_bestiale': 'Ta Bête se grise : tu te montres trop possessive.',
                              'echec_bestial': 'Tu perds le contrôle : témoin, rumeur, risque immédiat.'},
                             {'rencontre': 'Banquet chez un marchand influent. On t’admire, on te jauge, on te propose '
                                           'des contrats. Ici, la chasse est secondaire : la politique prime.',
                              'res_temp': 'Aucune',
                              'effet': 'Tu engranges des dettes et des promesses. Tu chasses plus tard.',
                              'victoire_critique': 'Tu obtiens une protection discrète et une salle pour tes salons '
                                                   'futurs.',
                              'victoire_pyrrhus': 'Tu gagnes, mais on attend de toi une prestation risquée en public.',
                              'reussite_bestiale': 'Ta Bête te pousse à humilier un convive : erreur sociale.',
                              'echec_bestial': 'Tu fais peur : le marchand ferme ses portes.'},
                             {'rencontre': 'Un disciple amoureux devient jaloux. Il te réclame ‘un vrai moment’ et '
                                           't’entraîne hors des rues familières, juste pour te prouver qu’il est le '
                                           'seul.',
                              'res_temp': 'Sanguine (Fugace)',
                              'effet': 'Tu peux le calmer par un baiser et le nourrir pour reprendre l’ascendant.',
                              'victoire_critique': 'Il se calme et redevient docile, persuadé d’avoir été choisi.',
                              'victoire_pyrrhus': 'Tu réussis, mais tu le suis trop loin, prise par le jeu. Emportée '
                                                  'par l’élan (ou par l’admirateur), ⚠️ tu franchis la limite de ton '
                                                  'territoire du cœur bourgeois intra-muros : erreur politique et '
                                                  'dangereuse.',
                              'reussite_bestiale': 'Ta Bête le domine : il se brise et devient dangereux.',
                              'echec_bestial': 'Il te fuit et te hait : il cherchera à te nuire.'},
                             {'rencontre': 'Après un spectacle, un admirateur plus âgé te confie une honte. Il demande '
                                           'une confession, pas une étreinte. Il est prêt à ‘payer’ d’une intimité.',
                              'res_temp': 'Flegmatique (Fugace)',
                              'effet': 'Tu le nourris doucement, comme une absolution. Il repart apaisé, loyal.',
                              'victoire_critique': 'Il devient un protecteur discret : il étouffe les rumeurs avant '
                                                   'qu’elles naissent.',
                              'victoire_pyrrhus': 'Tu réussis, mais il veut te revoir régulièrement : la dépendance '
                                                  's’installe.',
                              'reussite_bestiale': 'Ta Bête se moque de sa faiblesse : il se retourne, blessé.',
                              'echec_bestial': 'Il parle trop, trop vite : la confidence devient poison.'},
                             {'rencontre': 'Un noble veut te ‘posséder’. Il exige un tête-à-tête comme une dette. Le '
                                           'consentement est social, contraint, mais réel dans le jeu des apparences.',
                              'res_temp': 'Flegmatique (Intense)',
                              'effet': 'Tu reprends le contrôle en faisant de son désir une laisse autour de son cou.',
                              'victoire_critique': 'Tu le rends docile sans scandale : il devient une protection, pas '
                                                   'un maître.',
                              'victoire_pyrrhus': 'Tu réussis, mais il sort humilié : il cherchera à reprendre '
                                                  'l’avantage.',
                              'reussite_bestiale': 'Ta Bête écrase : tu le brises trop, et la vengeance commence.',
                              'echec_bestial': 'Tu perds ton masque : la scène devient dangereuse politiquement.'},
                             {'rencontre': 'Un admirateur régulier revient avec des fleurs et des lettres. Il veut '
                                           'juste te voir. Nourrir ici serait facile… mais risqué à force.',
                              'res_temp': 'Aucune',
                              'effet': 'Tu gères la distance : tu nourris ailleurs et tu gardes celui-ci comme réserve '
                                       'sociale.',
                              'victoire_critique': 'Il reste fidèle sans devenir obsessionnel : équilibre parfait.',
                              'victoire_pyrrhus': 'Tu temporises, mais il devient impatient : il cherche à te suivre.',
                              'reussite_bestiale': 'Ta Bête veut le prendre maintenant : danger de répétition.',
                              'echec_bestial': 'Il comprend qu’il n’est qu’un jouet : il se retourne.'},
                             {'rencontre': 'Une rumeur circule : ‘les hommes qui l’approchent tombent pâles’. Rien de '
                                           'prouvé, mais ton nom devient une inquiétude mondaine.',
                              'res_temp': 'Aucune',
                              'effet': 'Tu réduis la fréquence et changes de profils : tu protèges ton territoire '
                                       'social.',
                              'victoire_critique': 'La rumeur s’éteint : tu ressors plus légitime que jamais.',
                              'victoire_pyrrhus': 'Tu stabilises, mais au prix de plusieurs nuits de retenue.',
                              'reussite_bestiale': 'Ta Bête veut compenser : tu fais une erreur visible.',
                              'echec_bestial': 'Incident public : la rumeur devient enquête.'},
                             {'rencontre': 'Un artiste concurrent humilié te défie. Un de ses admirateurs, fasciné par '
                                           'ta cruauté, vient te chercher après la scène.',
                              'res_temp': 'Sanguine (Fugace)',
                              'effet': 'Tu fais de la fascination un dîner : il repart exalté, marqué par ton aura.',
                              'victoire_critique': 'Le concurrent perd du terrain : ton ascendant s’étend.',
                              'victoire_pyrrhus': 'Tu réussis, mais le concurrent comprend qu’on te suit : il enquête.',
                              'reussite_bestiale': 'Ta Bête se repaît de la victoire : tu laisses trop de traces.',
                              'echec_bestial': 'Tu déclenches une revanche organisée.'},
                             {'rencontre': 'Un critique littéraire influent te demande une lecture privée pour juger '
                                           '‘la vérité’ de ton art. Il consent à l’intimité comme à une méthode.',
                              'res_temp': 'Flegmatique (Fugace)',
                              'effet': 'Tu le nourris en même temps que tu le convaincs : jugement et désir '
                                       's’entremêlent.',
                              'victoire_critique': 'Sa critique te consacre : ton territoire devient intouchable.',
                              'victoire_pyrrhus': 'Tu réussis, mais il devient possessif intellectuellement : il veut '
                                                  'te façonner.',
                              'reussite_bestiale': 'Ta Bête se rebiffe : tu l’humilies et il se venge par l’écrit.',
                              'echec_bestial': 'Il devine trop : il commence à relier des indices.'},
                             {'rencontre': 'Tes performances attirent presque un culte : des admirateurs se réunissent '
                                           'pour te voir passer. C’est flatteur… et dangereux.',
                              'res_temp': 'Aucune',
                              'effet': 'Tu organises la distance : tu restes icône, pas proie de la foule.',
                              'victoire_critique': 'Tu canalises le culte en salons contrôlés : sécurité accrue.',
                              'victoire_pyrrhus': 'Tu gardes le contrôle, mais tu sens l’étau social se resserrer.',
                              'reussite_bestiale': 'Ta Bête veut se nourrir de la foule : catastrophe proche.',
                              'echec_bestial': 'Une scène éclate : tu dois disparaître immédiatement.'},
                             {'rencontre': 'Performance transcendante dans un salon du cœur bourgeois. La salle est en '
                                           'extase, et un admirateur ‘parfait’ se livre à toi comme à une divinité.',
                              'res_temp': 'Flegmatique (Vive)',
                              'effet': 'Son sang a une intensité rare : il goûte l’art, le désir, l’abandon total. '
                                       'C’est dangereux par sa pureté.',
                              'victoire_critique': 'Tu canalises la vague sans laisser de trace : tu ressors plus '
                                                   'forte et plus lucide.',
                              'victoire_pyrrhus': 'Tu réussis, mais la tentation de recommencer devient une obsession '
                                                  'pour toi aussi.',
                              'reussite_bestiale': 'Tu dépasses la mesure : la proie vacille et la soirée se brise.',
                              'echec_bestial': 'Tu laisses une marque visible : quelqu’un comprend que ce n’est pas '
                                               'qu’un jeu.'},
                             {'rencontre': 'Dans un salon feutré, un homme te demande un poème « pour la gloire de '
                                           'Dieu ». Sa présence brûle la peau et glace le sang : il porte la Foi '
                                           'Véritable. Il ne sait pas ce que tu es, mais quelque chose en lui refuse '
                                           'ton masque. Et derrière lui, hors de ta vue, une influence plus noire le '
                                           'guide : un ancien Lasombra le pousse à se rapprocher de toi.',
                              'res_temp': 'Flegmatique (Vive)',
                              'effet': 'Le danger n’est pas l’admirateur : c’est le reflet qu’il te renvoie. Ta faim '
                                       'se heurte à une barrière sacrée, et tu comprends que cette rencontre peut te '
                                       'marquer durablement.',
                              'victoire_critique': 'Tu le quittes sans le heurter et sans te trahir. Tu ressors avec '
                                                   'un indice subtil : un nom, un symbole, une phrase qui trahit la '
                                                   'main du Lasombra.',
                              'victoire_pyrrhus': 'Tu t’éloignes, mais il te fixe comme s’il t’avait déjà vue en rêve. '
                                                  'Il priera pour te « sauver »… et reviendra, entraînant avec lui '
                                                  'l’ombre qui le manipule.',
                              'reussite_bestiale': 'Ta Bête se cabre contre la Foi : tu réagis violemment, et sa '
                                                   'présence te brûle. Tu fuis en laissant une impression terrifiante '
                                                   'et une piste facile à suivre.',
                              'echec_bestial': 'Tu t’approches trop : la Foi te heurte de plein fouet. Panique, '
                                               'douleur, fuite… et tu comprends que quelqu’un t’a mise sur une '
                                               'trajectoire.'}]},
 'rat_egouts': {'label': 'Consensualiste — Barbier-chirurgien',
                'entries': [{'rencontre': 'Dans les murs, un bourgeois fidèle vient pour sa saignée mensuelle et te '
                                          'traite comme une évidence du lieu. Il accepte que tu restes « à portée » '
                                          'pendant l’opération.',
                             'res_temp': 'Aucune',
                             'effet': 'Tu te nourris discrètement sans perturber le geste du barbier. La routine '
                                      'protège tout le monde.',
                             'victoire_critique': 'Le client repart étonnamment bien : il parle de la « main sûre » du '
                                                  'maître barbier et renforce la réputation de l’échoppe.',
                             'victoire_pyrrhus': 'Tu réussis, mais il ressort un peu trop pâle : l’entourage remarque '
                                                 'une faiblesse inhabituelle.',
                             'reussite_bestiale': 'Tu prends trop : malaise sur le fauteuil, agitation, et l’apprenti '
                                                  'garde l’image en tête.',
                             'echec_bestial': 'Ta Bête te trahit : ton attitude devient prédatrice et le client exige '
                                              'qu’on te tienne à distance.'},
                            {'rencontre': 'Après une saignée, le maître barbier met de côté un bol de sang encore '
                                          'chaud pour « lire les humeurs ». Le patient a consenti au prélèvement '
                                          'médical.',
                             'res_temp': 'Flegmatique (Fugace)',
                             'effet': 'Tu prélèves ta part sans nourrissage direct. C’est propre, clinique, presque '
                                      'invisible.',
                             'victoire_critique': 'Tu ajustes la quantité au millimètre : personne ne soupçonne quoi '
                                                  'que ce soit et l’assistant te traite en allié discret.',
                             'victoire_pyrrhus': 'Tu réussis, mais le barbier fronce les sourcils : « étrange, on '
                                                 'dirait moins qu’à l’habitude ».',
                             'reussite_bestiale': 'Tu t’attardes : une trace sur ta manche, un apprenti remarque, et '
                                                  'une question naît.',
                             'echec_bestial': 'Un geste maladroit renverse le bol : on nettoie, on parle, on te '
                                              'regarde trop.'},
                            {'rencontre': 'En arrière-salle, le maître barbier évoque ses dettes : outils à acheter, '
                                          'loyers, pressions de notables. Il sollicite ton aide sans savoir qui tu es.',
                             'res_temp': 'Aucune',
                             'effet': 'Tu consolides ta main sur le réseau. L’accès aux murs et aux horaires devient '
                                      'plus simple.',
                             'victoire_critique': 'Tu poses des termes élégants : il te devra un service clair, '
                                                  'durable, sans rancœur.',
                             'victoire_pyrrhus': 'Tu obtiens ce que tu veux, mais il commence à se demander d’où vient '
                                                 'ton aisance et ton influence.',
                             'reussite_bestiale': 'Tu appuies trop : il cède, mais la crainte attire les langues et '
                                                  'les prières.',
                             'echec_bestial': 'Il se braque : la relation se fissure, et le réseau devient moins '
                                              'fiable.'},
                            {'rencontre': 'Un jeune noble exige une saignée tardive pour éviter les regards. Il '
                                          'consent à une « faveur » privée, persuadé d’être choisi.',
                             'res_temp': 'Sanguine (Fugace)',
                             'effet': 'Son sang est vif, facile à prendre. Tu dois surtout gérer la discrétion '
                                      'sociale.',
                             'victoire_critique': 'Tu le laisses exalté mais stable : il reviendra seul, et parlera '
                                                  'peu.',
                             'victoire_pyrrhus': 'Tu réussis, mais sa pâleur intrigue son écuyer dès le lendemain.',
                             'reussite_bestiale': 'Tu le troubles trop : il devient dépendant de ta présence et '
                                                  'cherche à te revoir à tout prix.',
                             'echec_bestial': 'Tu le fais paniquer : il jure ne plus remettre les pieds ici et la '
                                              'rumeur peut naître.'},
                            {'rencontre': 'Un client régulier revient trop souvent, convaincu que les saignées '
                                          'l’apaisent. Il consent facilement, presque avec empressement.',
                             'res_temp': 'Aucune',
                             'effet': 'Tu te nourris sans difficulté, mais le vrai danger est la fréquence : l’usure '
                                      'se voit.',
                             'victoire_critique': 'Tu imposes une cadence raisonnable : il repart satisfait et ton '
                                                  'réseau reste propre.',
                             'victoire_pyrrhus': 'Tu réussis, mais sa faiblesse s’accumule : un proche parle d’« '
                                                 'étrange maladie ».',
                             'reussite_bestiale': 'Ta faim accélère la spirale : il s’évanouit, et l’échoppe s’agite.',
                             'echec_bestial': 'Tu perds le masque : il comprend qu’il n’était pas juste un patient.'},
                            {'rencontre': 'Une hémorragie post-partum menace une mère dans l’arrière-salle. La famille '
                                          'consent à tout soin. Le sang, là, est une urgence.',
                             'res_temp': 'Flegmatique (Intense)',
                             'effet': 'Tu peux te nourrir, mais chaque goutte compte : il faut rester du côté de la '
                                      'survie.',
                             'victoire_critique': 'Tu aides à stabiliser la perte : gratitude durable, accès renforcé '
                                                  'aux familles influentes.',
                             'victoire_pyrrhus': 'Tu réussis, mais la mère reste très faible : les proches scrutent '
                                                 'chaque détail des soins.',
                             'reussite_bestiale': 'Tu franchis la limite : la situation vacille, on frôle la mort, et '
                                                  'l’on cherchera un responsable.',
                             'echec_bestial': 'Ta Bête te pousse : tu dois fuir au pire moment, laissant le barbier '
                                              'gérer seul.'},
                            {'rencontre': 'Un homme est amené pour une chirurgie lourde : fracture ouverte, gangrène '
                                          'naissante, décision d’amputation. Il consent, terrorisé.',
                             'res_temp': 'Flegmatique (Intense)',
                             'effet': 'Le contexte est violent et sanglant, mais plein de témoins. La maîtrise est '
                                      'tout.',
                             'victoire_critique': 'Tu aides le barbier à tenir la scène : tu sors de là avec une aura '
                                                  'd’ombre indispensable.',
                             'victoire_pyrrhus': 'Tu réussis, mais la rumeur d’un « assistant étrange » circule parmi '
                                                 'les voisins.',
                             'reussite_bestiale': 'Tu t’abandonnes à l’odeur du sang : un cri, une panique, et tout le '
                                                  'monde te regarde.',
                             'echec_bestial': 'Tu craques : tu t’éclipses trop vite et la culpabilité retombe sur le '
                                              'barbier.'},
                            {'rencontre': 'De nuit, une jeune fille non mariée d’une famille dévote accouche en secret '
                                          'dans les murs. Le consentement est arraché à la honte et à la peur.',
                             'res_temp': 'Sanguine (Fugace)',
                             'effet': 'Une prise rapide et discrète est possible, mais la scène est fragile : un '
                                      'scandale peut éclater.',
                             'victoire_critique': 'Tu restes invisible et la naissance se passe sans témoins superflus '
                                                  ': le secret est préservé.',
                             'victoire_pyrrhus': 'Tu réussis… puis tout se précipite : la famille exige un transfert '
                                                 'immédiat pour cacher l’affaire. Un imprévu t’entraîne au-delà de la '
                                                 'frontière de ton territoire de chasse (en suivant le barbier ou le '
                                                 'patient) : ⚠️ tu franchis involontairement la limite.',
                             'reussite_bestiale': 'Tu prends trop : la mère s’effondre et la famille accuse le '
                                                  'barbier.',
                             'echec_bestial': 'Ta Bête te rend trop présent : on te chasse de la pièce, et le secret '
                                              'devient dangereux.'},
                            {'rencontre': 'Une bourgeoise influente accouche dans l’arrière-salle « par sécurité ». '
                                          'Les proches imposent silence et efficacité.',
                             'res_temp': 'Aucune',
                             'effet': 'Tu te nourris à la marge, sans jamais mettre en risque la mère. Le pouvoir '
                                      'social est palpable.',
                             'victoire_critique': 'La famille te doit un service discret : tu gagnes un accès rare aux '
                                                  'maisons bourgeoises du quartier.',
                             'victoire_pyrrhus': 'Tu réussis, mais la mère reste pâle plusieurs jours : on surveille '
                                                 'désormais les quantités de sang perdu.',
                             'reussite_bestiale': 'Ton excès se voit : agitation, cris, et une servante te fixe trop '
                                                  'longtemps.',
                             'echec_bestial': 'Tu perds ton calme : on te tient à distance lors des prochaines '
                                              'urgences.'},
                            {'rencontre': 'Une sage-femme pieuse collabore avec le barbier. Elle te trouve « trop '
                                          'présent » et surveille tes gestes pendant une saignée.',
                             'res_temp': 'Flegmatique (Fugace)',
                             'effet': 'Tu dois nourrir sans attirer son attention : la tension est intellectuelle, pas '
                                      'physique.',
                             'victoire_critique': 'Tu la convaincs par le professionnalisme : elle devient un paravent '
                                                  'utile plutôt qu’un risque.',
                             'victoire_pyrrhus': 'Tu réussis, mais elle note un détail (odeur, posture, absence de '
                                                 'souffle) qu’elle gardera pour elle… pour l’instant.',
                             'reussite_bestiale': 'Ta Bête s’irrite : tu la fais taire d’un regard trop dur, et elle '
                                                  'se met à prier contre toi.',
                             'echec_bestial': 'Elle t’accuse implicitement : le barbier te demande de te faire plus '
                                              'rare.'},
                            {'rencontre': 'À domicile, dans le quartier religieux intra-muros, un chanoine demande une '
                                          'saignée par « discipline ». Il consent avec calme.',
                             'res_temp': 'Flegmatique (Fugace)',
                             'effet': 'Sang stable, prélèvement mesuré : tout est feutré et surveillé.',
                             'victoire_critique': 'Le chanoine t’accorde une confiance discrète : certaines portes '
                                                  's’ouvrent sans question.',
                             'victoire_pyrrhus': 'Tu réussis, mais un diacre remarque sa fatigue inhabituelle et '
                                                 'commence à observer l’échoppe.',
                             'reussite_bestiale': 'Tu t’attardes : un serviteur vous surprend trop proches.',
                             'echec_bestial': 'La piété te dérange : tu pars trop vite et la scène laisse une '
                                              'impression.'},
                            {'rencontre': 'Un étudiant en théologie, anxieux, demande une saignée « pour calmer son '
                                          'esprit ». Il consent par superstition.',
                             'res_temp': 'Aucune',
                             'effet': 'Nourrissage simple, sans relief. La nuit reste nette.',
                             'victoire_critique': 'Il réussit son épreuve et attribue son succès au barbier : '
                                                  'réputation renforcée.',
                             'victoire_pyrrhus': 'Tu réussis, mais il vacille en public : moqueries et questions.',
                             'reussite_bestiale': 'Ton impatience le rend nerveux : il quitte les lieux en tremblant.',
                             'echec_bestial': 'Il parle d’une présence oppressante dans l’arrière-salle.'},
                            {'rencontre': 'Un noble du cœur bourgeois intra-muros est saigné sous l’œil discret d’un '
                                          'domestique « envoyé par la maison ». Il consent, mais tout est politique.',
                             'res_temp': 'Flegmatique (Fugace)',
                             'effet': 'Tu dois nourrir comme une ombre, sans laisser de trace sociale.',
                             'victoire_critique': 'Tu sors de là avec une dette de la maison : accès, invitations, '
                                                  'protection.',
                             'victoire_pyrrhus': 'Tu réussis, mais le domestique note la quantité exacte et la compare '
                                                 'aux habitudes.',
                             'reussite_bestiale': 'Ta présence devient trop magnétique : le domestique te suit plus '
                                                  'tard dans la rue.',
                             'echec_bestial': 'Une scène de tension éclate : on te somme de partir et l’affaire se '
                                              'referme sur toi.'},
                            {'rencontre': 'Une riche veuve pieuse demande une saignée « purificatrice ». Elle consent '
                                          'et exige discrétion absolue.',
                             'res_temp': 'Flegmatique (Fugace)',
                             'effet': 'Le sang est lent, presque froid. Tu restes parfaitement maître.',
                             'victoire_critique': 'Elle te protège socialement et détourne les rumeurs par son '
                                                  'influence.',
                             'victoire_pyrrhus': 'Tu réussis, mais sa pâleur intrigue une suivante trop observatrice.',
                             'reussite_bestiale': 'Tu te rapproches trop : une domestique voit ce qu’elle ne devrait '
                                                  'pas voir.',
                             'echec_bestial': 'La veuve prend peur : elle change de praticien et te fait perdre un '
                                              'appui.'},
                            {'rencontre': 'Un marchand prospère vient pour sa saignée saisonnière. Il consent par '
                                          'habitude plus que par conviction.',
                             'res_temp': 'Aucune',
                             'effet': 'Routine sans incident : tu gardes ton réseau propre.',
                             'victoire_critique': 'Il te confie un détail commercial utile sur les fortunes du '
                                                  'quartier.',
                             'victoire_pyrrhus': 'Il ressort plus faible que prévu : son épouse pose des questions.',
                             'reussite_bestiale': 'Tu prends trop : malaise au seuil, et on parle.',
                             'echec_bestial': 'Il s’emporte : il ne revient plus et se plaint à des proches.'},
                            {'rencontre': 'Un magistrat influent souffre de migraines et veut une saignée discrète. Il '
                                          'consent, mais exige contrôle et silence.',
                             'res_temp': 'Aucune',
                             'effet': 'Nourrissage posé. Le risque est la réputation : un homme de loi n’aime pas '
                                      'l’ombre.',
                             'victoire_critique': 'Il te doit une faveur et sait garder un secret quand ça l’arrange.',
                             'victoire_pyrrhus': 'Il reste pâle plusieurs jours : un confrère s’enquiert de son état.',
                             'reussite_bestiale': 'Tu le fais vaciller : on parle d’« abus médical ».',
                             'echec_bestial': 'Il te chasse : trop de malaise, trop de questions.'},
                            {'rencontre': 'Dans une maison attenante au cloître, un notable raffiné consent à une '
                                          'saignée « pour l’équilibre ». Il te confie qu’il aime être vu par '
                                          'l’exception.',
                             'res_temp': 'Aucune',
                             'effet': 'Son sang est vif, et le jeu social est dangereux : il veut se sentir unique.',
                             'victoire_critique': 'Tu le satisfais sans l’affaiblir : il devient une source régulière '
                                                  'et discrète.',
                             'victoire_pyrrhus': 'Il se sent trahi par sa fatigue le lendemain : il cherche à '
                                                 'comprendre ce qui s’est passé.',
                             'reussite_bestiale': 'Il s’attache trop : il veut te voir hors cadre, hors règles.',
                             'echec_bestial': 'Tu le heurtes : il parle trop, et la rumeur s’éveille.'},
                            {'rencontre': 'Un vieil homme du quartier religieux revient pour son rituel annuel. Il '
                                          'consent comme toujours, sans émotion.',
                             'res_temp': 'Aucune',
                             'effet': 'Rien d’exceptionnel : la routine est ta meilleure alliée.',
                             'victoire_critique': 'Il évoque ton sérieux auprès des voisins : l’échoppe gagne en '
                                                  'stabilité.',
                             'victoire_pyrrhus': 'Il met du temps à se remettre : quelques regards insistants.',
                             'reussite_bestiale': 'Tu prends trop : il manque de s’évanouir.',
                             'echec_bestial': 'Tu brises le calme : tout devient soudainement suspect.'},
                            {'rencontre': 'Un professeur de droit canon vient pour une saignée discrète. Il consent '
                                          'avec froideur analytique.',
                             'res_temp': 'Flegmatique (Fugace)',
                             'effet': 'Sang méthodique, prélèvement précis : tu n’as pas droit à l’improvisation.',
                             'victoire_critique': 'Il te donne une information sur des tensions internes du chapitre, '
                                                  'utile à long terme.',
                             'victoire_pyrrhus': 'Il remarque sa fatigue inhabituelle et te questionne subtilement.',
                             'reussite_bestiale': 'Tu te tends : il perçoit la faille et devient méfiant.',
                             'echec_bestial': 'Il te soupçonne d’excès : il ne revient plus.'},
                            {'rencontre': 'Une mère récemment accouchée demande une saignée « pour prévenir les '
                                          'fièvres ». Elle consent, mais son corps est encore fragile.',
                             'res_temp': 'Aucune',
                             'effet': 'Tu dois être d’une prudence absolue : nourrissage minimal, rien de plus.',
                             'victoire_critique': 'La convalescence se passe bien : la famille te considère comme une '
                                                  'ombre bienfaisante.',
                             'victoire_pyrrhus': 'Elle reste trop faible : la famille surveille désormais chaque '
                                                 'séance de près.',
                             'reussite_bestiale': 'Ton excès la fait s’évanouir : panique dans la maison.',
                             'echec_bestial': 'Tu perds ton masque : on te tient éloigné des femmes du foyer.'},
                            {'rencontre': 'Un jeune chevalier blessé lors d’un duel clandestin est amené en urgence. '
                                          'Il consent, exalté, à tout soin.',
                             'res_temp': 'Sanguine (Intense)',
                             'effet': 'Sang ardent et instable : le contrôle est difficile mais possible.',
                             'victoire_critique': 'Tu stabilises la scène : le chevalier te voue une loyauté secrète.',
                             'victoire_pyrrhus': 'Il survit, mais reste diminué : on cherchera à comprendre ce qui l’a '
                                                 'tant vidé.',
                             'reussite_bestiale': 'Ta Bête répond à son ardeur : tu frôles l’accident fatal.',
                             'echec_bestial': 'Tu laisses une trace : un témoin parle d’une ‘morsure’.'},
                            {'rencontre': 'Un hospice religieux du cœur intra-muros demande l’aide du barbier pour une '
                                          'saignée collective (fièvres, humeurs). Tout reste dans ton périmètre au '
                                          'départ.',
                             'res_temp': 'Aucune',
                             'effet': 'Tu peux te nourrir très prudemment, dans la foule des malades, sans qu’on '
                                      't’identifie.',
                             'victoire_critique': 'Tu ressors sans trace, et l’hospice devient une ressource discrète.',
                             'victoire_pyrrhus': 'Tu réussis, mais une sœur ordonne un transfert d’urgence vers un '
                                                 'autre établissement. Un imprévu t’entraîne au-delà de la frontière '
                                                 'de ton territoire de chasse (en suivant le barbier ou le patient) : '
                                                 '⚠️ tu franchis involontairement la limite.',
                             'reussite_bestiale': 'Tu prends trop sur un corps déjà faible : cris, prière, agitation.',
                             'echec_bestial': 'Ta Bête te rend trop visible : on te chasse et on se signe sur ton '
                                              'passage.'},
                            {'rencontre': 'À domicile, un patient du quartier religieux consent à une saignée… puis '
                                          'une querelle familiale éclate : on décide de le déplacer chez un parent « '
                                          'plus sûr ».',
                             'res_temp': 'Flegmatique (Fugace)',
                             'effet': 'Tu peux nourrir proprement, mais la logistique devient le vrai piège.',
                             'victoire_critique': 'Tu restes maître et la séance reste un secret de famille.',
                             'victoire_pyrrhus': 'Tu réussis, mais tu te laisses happer par le déplacement. Un imprévu '
                                                 't’entraîne au-delà de la frontière de ton territoire de chasse (en '
                                                 'suivant le barbier ou le patient) : ⚠️ tu franchis involontairement '
                                                 'la limite.',
                             'reussite_bestiale': 'Tu t’énerves : tu brusques un serviteur et attires l’attention du '
                                                  'voisinage.',
                             'echec_bestial': 'La scène dégénère : on t’interdit l’entrée et la famille se referme.'},
                            {'rencontre': 'Une famille influente te reçoit intra-muros : le patient consent, mais '
                                          'impose des conditions. Après la séance, le maître de maison ordonne un '
                                          'transfert « immédiat » vers une demeure plus éloignée.',
                             'res_temp': 'Sanguine (Fugace)',
                             'effet': 'Le sang est vif, mais le pouvoir social te tient en laisse.',
                             'victoire_critique': 'Tu t’en sors avec élégance : la maison te doit une discrétion '
                                                  'précieuse.',
                             'victoire_pyrrhus': 'Tu réussis… et tu suis l’ordre sans réfléchir. Un imprévu t’entraîne '
                                                 'au-delà de la frontière de ton territoire de chasse (en suivant le '
                                                 'barbier ou le patient) : ⚠️ tu franchis involontairement la limite.',
                             'reussite_bestiale': 'Tu perds ta mesure : on constate une faiblesse dramatique et on '
                                                  'cherche un coupable.',
                             'echec_bestial': 'Ta Bête te fait dominer la scène : la maison te considère comme une '
                                              'menace.'},
                            {'rencontre': 'Un couvent proche des limites intra-muros demande une intervention '
                                          'discrète. Tout est « juste dans le territoire »… jusqu’à ce qu’on veuille '
                                          'déplacer la convalescente.',
                             'res_temp': 'Aucune',
                             'effet': 'Tu peux nourrir très légèrement, dans un cadre de silence et de secrets.',
                             'victoire_critique': 'Les sœurs te couvrent d’un anonymat utile : personne ne pose de '
                                                  'questions.',
                             'victoire_pyrrhus': 'Tu réussis, puis on t’entraîne plus loin pour éviter les commérages. '
                                                 'Un imprévu t’entraîne au-delà de la frontière de ton territoire de '
                                                 'chasse (en suivant le barbier ou le patient) : ⚠️ tu franchis '
                                                 'involontairement la limite.',
                             'reussite_bestiale': 'Ton excès déclenche malaise et prières : l’atmosphère devient '
                                                  'hostile.',
                             'echec_bestial': 'Tu perds ton sang-froid : on te chasse et le couvent te ferme ses '
                                              'portes.'},
                            {'rencontre': 'Un membre du clergé remarque une succession de patients trop pâles. Il ne '
                                          'sait rien, mais il observe l’échoppe et ses allées-venues.',
                             'res_temp': 'Aucune',
                             'effet': 'Ce n’est pas une chasse : c’est une alerte. Tu dois réduire ton empreinte et '
                                      'jouer la normalité.',
                             'victoire_critique': 'Tu détournes l’attention : le soupçon glisse sur un autre praticien '
                                                  'du quartier.',
                             'victoire_pyrrhus': 'Tu t’en sors, mais tu dois nourrir moins souvent pendant un temps : '
                                                 'le réseau se tend.',
                             'reussite_bestiale': 'Tu réagis avec froideur : sa méfiance se transforme en vigilance '
                                                  'active.',
                             'echec_bestial': 'Tu te dévoiles trop : il commence une enquête informelle.'},
                            {'rencontre': 'Un apprenti observe tes gestes, tes horaires, ta manière de te tenir près '
                                          'des patients. Il n’accuse pas : il collecte.',
                             'res_temp': 'Flegmatique (Fugace)',
                             'effet': 'Tu peux nourrir, mais chaque détail compte : il faut l’aveugler socialement, '
                                      'pas médicalement.',
                             'victoire_critique': 'Tu le retournes par l’autorité : il devient discret et loyal, du '
                                                  'moins en surface.',
                             'victoire_pyrrhus': 'Tu réussis, mais il garde une question en réserve : il saura '
                                                 'marchander plus tard.',
                             'reussite_bestiale': 'Ta Bête le terrifie : il commence à prier et à parler en secret.',
                             'echec_bestial': 'Il te provoque : scène, cris, et le barbier doit trancher contre toi.'},
                            {'rencontre': 'Un rival du barbier répand l’idée que « trop de sang disparaît » autour de '
                                          'cette échoppe. Il cherche un prétexte pour nuire.',
                             'res_temp': 'Sanguine (Fugace)',
                             'effet': 'La chasse devient sociale : nourrir est facile, mais protéger le réseau ne '
                                      'l’est pas.',
                             'victoire_critique': 'Tu pièges le rival : sa rumeur se retourne contre lui et il perd '
                                                  'des clients.',
                             'victoire_pyrrhus': 'Tu le fais taire, mais l’affaire laisse des traces : vigilance '
                                                 'accrue dans le quartier.',
                             'reussite_bestiale': 'Tu t’emportes : tu lui fais peur, et il devient plus dangereux, '
                                                  'plus discret.',
                             'echec_bestial': 'Tu le sous-estimes : il touche une autorité qui peut vraiment '
                                              'enquêter.'},
                            {'rencontre': 'Un client sort affaibli, et la rumeur se fixe : « ici, on vide les gens ». '
                                          'Rien de prouvé, mais ça colle à la peau.',
                             'res_temp': 'Aucune',
                             'effet': 'Tu dois restaurer la confiance : nourrissage minimal, contrôle des quantités, '
                                      'mise en scène médicale.',
                             'victoire_critique': 'La rumeur s’éteint : le barbier gagne en prestige et tu gagnes en '
                                                  'sécurité.',
                             'victoire_pyrrhus': 'Tu stabilises, mais au prix de plusieurs nuits de retenue : '
                                                 'frustration et manque.',
                             'reussite_bestiale': 'Ta Bête veut compenser : tu fais une erreur visible dans une séance '
                                                  'banale.',
                             'echec_bestial': 'Tu craques : un incident public tue la discrétion de l’échoppe.'},
                            {'rencontre': 'Un notable d’apparence placide demande une saignée exceptionnelle. Il '
                                          'consent, mais son sang a une densité rare, presque enivrante.',
                             'res_temp': 'Flegmatique (Vive)',
                             'effet': 'Le sang est puissamment stable : une rareté qui peut te déséquilibrer par sa '
                                      'perfection.',
                             'victoire_critique': 'Tu canalises cette vigueur sans laisser la moindre trace : la nuit '
                                                  'te rend plus fort et plus lucide.',
                             'victoire_pyrrhus': 'Tu réussis, mais tu restes marqué par la puissance ressentie : '
                                                 'tentation de recommencer, rapidement.',
                             'reussite_bestiale': 'L’intensité te pousse à l’excès : tu manques de mettre le patient '
                                                  'en danger immédiat.',
                             'echec_bestial': 'Tu laisses une trace inquiétante : le barbier, cette fois, remarque '
                                              'quelque chose d’impossible.'},
                            {'rencontre': ("Un blessé amené en urgence suite à une impressionante entaille à la jambe qui commence à puruler. Une jeune femme l'accompagne. Le chirurgien pense que la blessure peut être désinfectée mais le blessé exige une amputation immédiate. La jeune femme s'occupe de son traitement pour atténuer la douleur et empêcher la transformation (garou elle aussi même si elle est \"faible\")"
                                          "Cet homme dégage une violence ancienne : un loup-garou. Tu l’as senti trop tard."),
                             'res_temp': 'Animal (Vive ; Dyscrasie : Puissance OU animalisme +1 ; Résistance à la frénésie -2d ; -2 soif min 0)',
                             'effet': 'Son sang est brûlant, brutal, indomptable. La chasse devient un piège que tu as su éviter et parviens à boire un peu de son sang que tu n\'as pas pu conserver, à moins de réussir test de médecine '
                                      '(conservation 4 à 24h selon succès pour trouver solution magique et permet aussi de faire "jet d\'occultisme" pour se demander pourquoi ce loup garou n\'a pas régénéré de son entaille.). Si humanité 7-, les garous sentent que l\'Ennemi se cache par ici aussi... Un autre ennemi que ce dont ils ont l\'habitude d\'affronter, mais  cette souillure ne passera tout de même pas inaperçue',
                             'victoire_critique': 'Tu identifies sa nature avant qu’il ne saisisse la tienne et tu '
                                                  't’arraches à la scène vivant en soutirant du sang que tu as pu conserver au frais + sel + vin 24h (hors conservation enchantée). Question : Pourquoi n\'a il pas régénéré de son entaille ? ',
                             'victoire_pyrrhus': 'Tu t’échappes blessé, marqué, et le souvenir te poursuit. Quelque '
                                                 'chose t’a reconnu et ressenti.',
                             'reussite_bestiale': 'Ta Bête répond à la sienne : chaos, cris, et une escalade que tu '
                                                  'contrôles à peine.',
                             'echec_bestial': 'Il révèle sa forme. La chasse s’inverse, et tu ne dois ta survie qu’à '
                                              'la fuite.'}]},
 'justicier_nocturne': {'label': 'Justicier — Bas-quartiers',
                        'entries': [{'rencontre': 'Un contremaître fait briser les doigts d’un tanneur incapable de '
                                                  'payer sa dette.',
                                     'res_temp': 'Bilieuse (Fugace)',
                                     'effet': 'Colère et violence dominent la scène.',
                                     'victoire_critique': 'Tu fais un exemple discret et la rumeur protège les '
                                                          'ouvriers.',
                                     'victoire_pyrrhus': 'Tu poursuis les racketteurs jusqu’à un entrepôt hors '
                                                         'secteur. ⚠️',
                                     'reussite_bestiale': 'Ta brutalité marque les esprits plus que prévu.',
                                     'echec_bestial': 'Le contremaître s’échappe et prépare des représailles.'},
                                    {'rencontre': 'Un usurier manipule les comptes des artisans pour les maintenir '
                                                  'sous contrôle.',
                                     'res_temp': 'Aucune',
                                     'effet': 'Affaire d’avidité plus que de sang.',
                                     'victoire_critique': 'Tu récupères des preuves compromettantes.',
                                     'victoire_pyrrhus': 'Il disparaît mais laisse un réseau actif.',
                                     'reussite_bestiale': 'Tu l’intimides trop violemment.',
                                     'echec_bestial': 'Il alerte des complices.'},
                                    {'rencontre': 'Un homme bat sa compagne dans une ruelle de la tannerie.',
                                     'res_temp': 'Bilieuse (Fugace)',
                                     'effet': 'Terreur et rage saturent l’air.',
                                     'victoire_critique': 'La victime trouve enfin protection.',
                                     'victoire_pyrrhus': 'Tu t’attardes et attires l’attention d’un voisin.',
                                     'reussite_bestiale': 'Tu vas trop loin dans la punition.',
                                     'echec_bestial': 'L’agresseur t’échappe.'},
                                    {'rencontre': 'Un contremaître abuse de son autorité sans violence apparente.',
                                     'res_temp': 'Aucune',
                                     'effet': 'Injustice sourde et constante.',
                                     'victoire_critique': 'Les ouvriers reprennent confiance.',
                                     'victoire_pyrrhus': 'Il se replie et prépare sa vengeance.',
                                     'reussite_bestiale': 'Tu laisses des traces visibles.',
                                     'echec_bestial': 'Il obtient le soutien d’un garde.'},
                                    {'rencontre': 'Un garde corrompu frappe un mendiant pour l’exemple.',
                                     'res_temp': 'Bilieuse (Fugace)',
                                     'effet': 'Colère froide contre l’autorité corrompue.',
                                     'victoire_critique': 'La garde hésite désormais à intervenir brutalement.',
                                     'victoire_pyrrhus': 'Tu le poursuis hors quartier dans ta rage. ⚠️',
                                     'reussite_bestiale': 'Tu le marques trop sévèrement.',
                                     'echec_bestial': 'Il mobilise ses collègues.'},
                                    {'rencontre': 'Un trafiquant vend de l’alcool frelaté qui rend malade les plus '
                                                  'pauvres.',
                                     'res_temp': 'Aucune',
                                     'effet': 'Crime indirect mais destructeur.',
                                     'victoire_critique': 'Tu fais cesser le trafic.',
                                     'victoire_pyrrhus': 'Il change simplement de cachette.',
                                     'reussite_bestiale': 'Ta violence effraie les témoins.',
                                     'echec_bestial': 'Il disparaît dans la foule.'},
                                    {'rencontre': 'Un ravisseur prépare des enfants pour la mendicité forcée.',
                                     'res_temp': 'Bilieuse (Intense)',
                                     'effet': 'Indignation brûlante.',
                                     'victoire_critique': 'Tu sauves les enfants et brises le réseau local.',
                                     'victoire_pyrrhus': 'Un complice s’enfuit.',
                                     'reussite_bestiale': 'Ta fureur manque de te faire perdre contrôle.',
                                     'echec_bestial': 'Le ravisseur t’échappe dans les ruines.'},
                                    {'rencontre': 'Une bande de coupe-jarrets terrorise les ruelles.',
                                     'res_temp': 'Bilieuse (Fugace)',
                                     'effet': 'Violence rapide et sale.',
                                     'victoire_critique': 'Le quartier respire à nouveau.',
                                     'victoire_pyrrhus': 'Un survivant jure de se venger.',
                                     'reussite_bestiale': 'Tu frappes trop fort.',
                                     'echec_bestial': 'Ils se dispersent.'},
                                    {'rencontre': 'Une femme sauvée tremble encore de peur.',
                                     'res_temp': 'Aucune',
                                     'effet': 'Tu peux te nourrir avec prudence.',
                                     'victoire_critique': 'Elle devient une alliée silencieuse.',
                                     'victoire_pyrrhus': 'Son état attire un médecin curieux.',
                                     'reussite_bestiale': 'Tu la marques trop profondément.',
                                     'echec_bestial': 'Elle te fuit.'},
                                    {'rencontre': 'Recel de peaux volées dans un atelier fermé.',
                                     'res_temp': 'Aucune',
                                     'effet': 'Affaire économique et dissimulée.',
                                     'victoire_critique': 'Le réseau s’effondre.',
                                     'victoire_pyrrhus': 'Il se reforme ailleurs.',
                                     'reussite_bestiale': 'Tu laisses des traces visibles.',
                                     'echec_bestial': 'On alerte la garde.'},
                                    {'rencontre': 'Disparitions répétées dans les souterrains.',
                                     'res_temp': 'Bilieuse (Fugace)',
                                     'effet': 'Malaise et colère montante.',
                                     'victoire_critique': 'Tu identifies le coupable.',
                                     'victoire_pyrrhus': 'Il fuit vers un passage secret.',
                                     'reussite_bestiale': 'Ta violence résonne trop fort.',
                                     'echec_bestial': 'Tu perds sa trace.'},
                                    {'rencontre': 'Un tunnel débouche hors de la tannerie.',
                                     'res_temp': 'Aucune',
                                     'effet': 'Passage stratégique découvert.',
                                     'victoire_critique': 'Tu sécurises l’accès.',
                                     'victoire_pyrrhus': 'Tu poursuis un criminel au-delà des limites. ⚠️',
                                     'reussite_bestiale': 'Tu effraies un témoin innocent.',
                                     'echec_bestial': 'Tu es repéré.'},
                                    {'rencontre': 'Chambre de torture clandestine.',
                                     'res_temp': 'Bilieuse (Intense)',
                                     'effet': 'Haine viscérale.',
                                     'victoire_critique': 'Tu mets fin à l’horreur.',
                                     'victoire_pyrrhus': 'Un complice s’échappe.',
                                     'reussite_bestiale': 'Tu dépasses les limites.',
                                     'echec_bestial': 'Tu es pris au piège.'},
                                    {'rencontre': 'Contrebandiers armés cachés dans les ruines.',
                                     'res_temp': 'Aucune',
                                     'effet': 'Affaire stratégique.',
                                     'victoire_critique': 'Tu les disperses.',
                                     'victoire_pyrrhus': 'Ils fuient vers un autre quartier.',
                                     'reussite_bestiale': 'Tu frappes trop fort.',
                                     'echec_bestial': 'Ils se retranchent.'},
                                    {'rencontre': 'Un enlèvement nocturne est en cours.',
                                     'res_temp': 'Bilieuse (Fugace)',
                                     'effet': 'Course contre la montre.',
                                     'victoire_critique': 'La victime est sauvée.',
                                     'victoire_pyrrhus': 'Tu le rattrapes, mais l’effort te coûte : tu laisses une '
                                                         'trace et la rumeur enfle.',
                                     'reussite_bestiale': 'Tu manques de tuer sous la rage.',
                                     'echec_bestial': 'Ils disparaissent.'},
                                    {'rencontre': 'Refuge de sans-abris menacé par intimidation.',
                                     'res_temp': 'Aucune',
                                     'effet': 'Tension sociale.',
                                     'victoire_critique': 'Le refuge est protégé.',
                                     'victoire_pyrrhus': 'Les intimidateurs reviennent en nombre.',
                                     'reussite_bestiale': 'Tu inspires trop de peur.',
                                     'echec_bestial': 'Ils incendient le lieu.'},
                                    {'rencontre': 'Un marchand d’esclaves opère dans les souterrains.',
                                     'res_temp': 'Bilieuse (Intense)',
                                     'effet': 'Colère profonde.',
                                     'victoire_critique': 'Le réseau est démantelé.',
                                     'victoire_pyrrhus': 'Un chef s’enfuit.',
                                     'reussite_bestiale': 'Tu frôles l’exécution publique.',
                                     'echec_bestial': 'Il disparaît.'},
                                    {'rencontre': 'Une fosse commune récente est découverte.',
                                     'res_temp': 'Aucune',
                                     'effet': 'Preuves d’un crime plus vaste.',
                                     'victoire_critique': 'Tu identifies le responsable.',
                                     'victoire_pyrrhus': 'Tu déranges quelque chose de plus ancien.',
                                     'reussite_bestiale': 'Tu agis impulsivement.',
                                     'echec_bestial': 'Tu quittes les lieux précipitamment.'},
                                    {'rencontre': 'Un assassin payé pour intimider un témoin.',
                                     'res_temp': 'Bilieuse (Fugace)',
                                     'effet': 'Violence froide.',
                                     'victoire_critique': 'Tu fais échouer la mission.',
                                     'victoire_pyrrhus': 'Il fuit vers un secteur voisin.',
                                     'reussite_bestiale': 'Tu l’écrases brutalement.',
                                     'echec_bestial': 'Il disparaît dans les ruelles.'},
                                    {'rencontre': 'Un réseau protégé par la garde opère en silence.',
                                     'res_temp': 'Aucune',
                                     'effet': 'Corruption enracinée.',
                                     'victoire_critique': 'Tu exposes une faille.',
                                     'victoire_pyrrhus': 'Tu poursuis un officier au-delà de ton territoire. ⚠️',
                                     'reussite_bestiale': 'Tu laisses un témoin traumatisé.',
                                     'echec_bestial': 'La garde renforce sa présence.'},
                                    {'rencontre': 'Un prêtre abuse de son autorité sur les fidèles.',
                                     'res_temp': 'Bilieuse (Fugace)',
                                     'effet': 'Colère mêlée de dégoût.',
                                     'victoire_critique': 'Il cesse ses abus.',
                                     'victoire_pyrrhus': 'L’affaire attire l’attention du diocèse.',
                                     'reussite_bestiale': 'Tu le frappes trop fort.',
                                     'echec_bestial': 'Il se réfugie derrière sa foi.'},
                                    {'rencontre': 'Orphelinat détourné pour enrichir un administrateur.',
                                     'res_temp': 'Aucune',
                                     'effet': 'Injustice financière.',
                                     'victoire_critique': 'Les fonds sont récupérés.',
                                     'victoire_pyrrhus': 'Il disparaît avec l’argent.',
                                     'reussite_bestiale': 'Tu effraies les enfants.',
                                     'echec_bestial': 'Il obtient une protection.'},
                                    {'rencontre': 'Un meurtrier confesse sans remords.',
                                     'res_temp': 'Bilieuse (Fugace)',
                                     'effet': 'Colère glaciale.',
                                     'victoire_critique': 'Tu rends justice.',
                                     'victoire_pyrrhus': 'Tu t’exposes en public.',
                                     'reussite_bestiale': 'Ta violence est excessive.',
                                     'echec_bestial': 'Il s’échappe.'},
                                    {'rencontre': 'Rumeur d’un démon justicier circulant dans le quartier.',
                                     'res_temp': 'Aucune',
                                     'effet': 'Ta légende grandit.',
                                     'victoire_critique': 'La peur protège les innocents.',
                                     'victoire_pyrrhus': 'La garde enquête.',
                                     'reussite_bestiale': 'La rumeur devient incontrôlable.',
                                     'echec_bestial': 'On prépare un piège.'},
                                    {'rencontre': 'Un ravisseur se cache dans une crypte.',
                                     'res_temp': 'Bilieuse (Fugace)',
                                     'effet': 'Traque tendue.',
                                     'victoire_critique': 'Tu sauves la victime.',
                                     'victoire_pyrrhus': 'Tu le coinces, mais un témoin innocent voit trop de choses : '
                                                         'tu dois choisir entre justice et discrétion.',
                                     'reussite_bestiale': 'Tu l’écrases sans retenue.',
                                     'echec_bestial': 'Il fuit.'},
                                    {'rencontre': 'Un réseau d’enlèvements organisé opère sous la tannerie.',
                                     'res_temp': 'Bilieuse (Intense)',
                                     'effet': 'Colère et mission personnelle.',
                                     'victoire_critique': 'Tu brises la structure locale.',
                                     'victoire_pyrrhus': 'Un chef disparaît dans l’ombre.',
                                     'reussite_bestiale': 'Tu frôles l’exécution publique.',
                                     'echec_bestial': 'Ils se replient.'},
                                    {'rencontre': 'Un témoin supplie pour la protection de sa famille.',
                                     'res_temp': 'Aucune',
                                     'effet': 'Responsabilité morale accrue.',
                                     'victoire_critique': 'Tu sécurises sa situation.',
                                     'victoire_pyrrhus': 'Tu t’impliques trop personnellement.',
                                     'reussite_bestiale': 'Tu l’effraies malgré toi.',
                                     'echec_bestial': 'Il se rétracte.'},
                                    {'rencontre': 'Un officier supérieur protège des criminels.',
                                     'res_temp': 'Bilieuse (Fugace)',
                                     'effet': 'Colère contre l’impunité.',
                                     'victoire_critique': 'Tu exposes sa corruption.',
                                     'victoire_pyrrhus': 'Tu le poursuis jusqu’aux abords d’un quartier noble. ⚠️',
                                     'reussite_bestiale': 'Tu le brises publiquement.',
                                     'echec_bestial': 'Il prépare une riposte.'},
                                    {'rencontre': 'Un criminel déjà puni recommence ses abus.',
                                     'res_temp': 'Aucune',
                                     'effet': 'Question sur l’efficacité de ta justice.',
                                     'victoire_critique': 'Tu rends un avertissement définitif.',
                                     'victoire_pyrrhus': 'Il fuit dans les ruines.',
                                     'reussite_bestiale': 'Tu cèdes à la frustration.',
                                     'echec_bestial': 'Il se cache.'},
                                    {'rencontre': 'Un maître tortionnaire organise enlèvements et supplices, protégé '
                                                  'par corruption.',
                                     'res_temp': 'Bilieuse (Vive)',
                                     'effet': 'Haine absolue et décision irrévocable.',
                                     'victoire_critique': 'Tu mets fin à son règne dans le sang.',
                                     'victoire_pyrrhus': 'Tu réussis mais déclenches une onde de choc dans les '
                                                         'bas-quartiers.',
                                     'reussite_bestiale': 'Tu franchis une limite morale définitive.',
                                     'echec_bestial': 'Il s’échappe en te marquant comme cible.'},
                                    {'rencontre': 'Un sorcier exalté enlève des pauvres pour offrir leur chair à un '
                                                  'ancien Tzimisce.',
                                     'res_temp': 'Sanguine (Vive)',
                                     'effet': 'Fanatisme et mission mystique saturent l’air.',
                                     'victoire_critique': 'Tu détruis le culte local avant qu’il ne prenne racine.',
                                     'victoire_pyrrhus': 'Le sorcier meurt, mais l’ancien apprend ton existence.',
                                     'reussite_bestiale': 'Ton affrontement révèle trop de choses.',
                                     'echec_bestial': 'Il s’échappe en proclamant que tu es un signe annoncé.'}]},
 'roi_de_la_nuit': {'label': 'Roi de la Nuit — Trémère du Chapitre',
                    'entries': [{'rencontre': 'Un jeune noble rennais sollicite une annulation discrète pour vice de '
                                              'forme canonique. L’affaire doit rester dans l’enceinte du Chapitre.',
                                 'res_temp': 'Atrabilaire (Fugace) ou Aucune',
                                 'effet': 'Vous examinez les clauses, puis orientez le dossier vers un juriste '
                                          'favorable. La procédure progresse sans bruit.',
                                 'victoire_critique': 'Vous identifiez une irrégularité décisive que personne n’avait '
                                                      'vue. L’annulation devient irréfutable et votre réputation '
                                                      's’affermit.',
                                 'victoire_pyrrhus': 'Vous découvrez trop tard que la dispute cachait un enjeu civil. '
                                                     'Si l’affaire s’ébruite, le Cœur Bourgeois pourrait en entendre '
                                                     'parler.',
                                 'reussite_bestiale': 'Le demandeur affiche une gratitude excessive et vous cite là où '
                                                      'il aurait dû se taire.',
                                 'echec_bestial': 'Un détail juridique vous échappe. La procédure est suspendue et '
                                                  'l’on s’interroge brièvement sur votre lecture.'},
                                {'rencontre': 'Deux familles mineures demandent une dispense de consanguinité pour '
                                              'unir leurs héritiers malgré un lien interdit.',
                                 'res_temp': 'Atrabilaire (Fugace) ou Aucune',
                                 'effet': 'Vous facilitez un avis favorable au sein du Chapitre, sans jamais promettre '
                                          'ouvertement.',
                                 'victoire_critique': 'Vous transformez la dispense en équilibre durable : les deux '
                                                      'maisons se stabilisent autour du Chapitre.',
                                 'victoire_pyrrhus': 'Un tiers laisse entendre que l’accord civil était déjà scellé '
                                                     'ailleurs. Vous avez été utilisé pour bénir une manœuvre.',
                                 'reussite_bestiale': 'Les familles proclament votre intervention avec trop de zèle.',
                                 'echec_bestial': 'Un chanoine pointilleux conteste la décision et la renvoie à '
                                                  'l’étude.'},
                                {'rencontre': 'Un débat théologique oppose deux chanoines sur l’interprétation d’un '
                                              'passage ancien.',
                                 'res_temp': 'Atrabilaire (Fugace)',
                                 'effet': 'Votre lecture conciliatrice apaise la querelle sans rompre l’orthodoxie.',
                                 'victoire_critique': 'Votre argumentaire est recopié comme référence interne ; on le '
                                                      'citera longtemps.',
                                 'victoire_pyrrhus': 'Votre solution renforce involontairement une faction interne qui '
                                                     'gagne en assurance.',
                                 'reussite_bestiale': 'Vous tranchez avec une froideur trop nette : certains se '
                                                      'taisent… et retiennent.',
                                 'echec_bestial': 'Un détail philologique fragilise votre démonstration et l’arbitrage '
                                                  'vacille.'},
                                {'rencontre': 'Un noble accusé d’impiété demande la protection morale du Chapitre afin '
                                              'd’éviter une humiliation publique.',
                                 'res_temp': 'Atrabilaire (Fugace)',
                                 'effet': 'Vous obtenez un ajournement et déplacez l’attention vers une procédure plus '
                                          'lente.',
                                 'victoire_critique': 'Vous retournez l’affaire : elle devient exemple de prudence et '
                                                      'de clémence religieuse.',
                                 'victoire_pyrrhus': 'La charge religieuse masquait un conflit civil. Vous avez touché '
                                                     'une corde qui ne vous appartenait pas.',
                                 'reussite_bestiale': 'Le noble devient dépendant et vous sollicite au-delà du cadre '
                                                      'canonique.',
                                 'echec_bestial': 'Un témoin inattendu ravive les soupçons et l’affaire s’éternise.'},
                                {'rencontre': 'Un manuscrit ambigu est soumis à votre lecture au scriptorium, sous les '
                                              'yeux d’un copiste anxieux.',
                                 'res_temp': 'Atrabilaire (Fugace)',
                                 'effet': 'Vous recommandez prudence plutôt que condamnation hâtive ; le texte reste '
                                          'sous surveillance.',
                                 'victoire_critique': 'Vous trouvez une annotation ancienne dissipant l’ambiguïté et '
                                                      'sauvant le manuscrit.',
                                 'victoire_pyrrhus': 'Votre intérêt attire des érudits extérieurs au Chapitre : les '
                                                     'regards se multiplient.',
                                 'reussite_bestiale': 'Votre curiosité paraît trop insistante et intrigue les scribes.',
                                 'echec_bestial': 'Une lecture malheureuse alimente brièvement la suspicion '
                                                  'd’hérésie.'},
                                {'rencontre': 'Un chanoine confesse une faute mineure mais politiquement gênante, '
                                              'redoutant la rumeur plus que la pénitence.',
                                 'res_temp': 'Atrabilaire (Fugace)',
                                 'effet': 'Vous lui imposez discrétion et mesure ; il vous doit désormais une loyauté '
                                          'prudente.',
                                 'victoire_critique': 'Vous obtenez un levier moral durable : il écoutera vos avis '
                                                      'avant de parler.',
                                 'victoire_pyrrhus': 'Il se révèle plus ambitieux que prévu et tente d’exploiter votre '
                                                     'indulgence.',
                                 'reussite_bestiale': 'Votre proximité devient visible et nourrit des jalousies '
                                                      'silencieuses.',
                                 'echec_bestial': 'La faute était plus grave qu’il ne l’a dit : vous avez été '
                                                  'instrumentalisé.'},
                                {'rencontre': 'Un juriste canonique vous demande un avis sur une affaire obscure, à la '
                                              'frontière de la jurisprudence locale.',
                                 'res_temp': 'Atrabilaire (Fugace)',
                                 'effet': 'Vous clarifiez le point de droit qui bloquait la procédure.',
                                 'victoire_critique': 'Votre formulation simplifie durablement des cas similaires ; on '
                                                      'l’adopte sans discuter.',
                                 'victoire_pyrrhus': 'Votre interprétation crée un précédent imprévu qui pourrait être '
                                                     'retourné contre vous.',
                                 'reussite_bestiale': 'Votre nom est cité lors d’une audience : trop public, trop tôt.',
                                 'echec_bestial': 'Un confrère contredit votre lecture et affaiblit votre position.'},
                                {'rencontre': 'Un scribe trop curieux vous demande un entretien privé après les '
                                              'heures, prétextant une question de copie. L’odeur du vice est discrète, '
                                              'mais réelle.',
                                 'res_temp': 'Sanguine (Fugace)',
                                 'effet': 'Son sang porte la tension d’un interdit goûté en secret : luxure, honte, et '
                                          'audace.',
                                 'victoire_critique': 'Vous le recadrez avec douceur et l’orientez vers des travaux '
                                                      'inoffensifs, sans briser sa façade.',
                                 'victoire_pyrrhus': 'Malgré vos précautions, il laisse traîner une annotation '
                                                     'compromettante. Quelqu’un la lira.',
                                 'reussite_bestiale': 'Vous le poussez trop : il s’enhardit dans la recherche de '
                                                      'textes interdits.',
                                 'echec_bestial': 'Pris de panique, il évoque une influence inquiétante au '
                                                  'scriptorium. Le mot circule, même mal compris.'},
                                {'rencontre': 'Un moine ambitieux sollicite votre soutien pour accéder à une charge '
                                              'plus élevée au sein du Chapitre.',
                                 'res_temp': 'Atrabilaire (Fugace)',
                                 'effet': 'Vous facilitez une recommandation mesurée auprès des bonnes personnes.',
                                 'victoire_critique': 'Il vous demeure loyal et devient un relais fiable dans les '
                                                      'couloirs du Chapitre.',
                                 'victoire_pyrrhus': 'Son ascension rapide attire l’attention de rivaux qui commencent '
                                                     'à examiner ses appuis.',
                                 'reussite_bestiale': 'Il affiche trop clairement votre soutien et suscite des '
                                                      'jalousies.',
                                 'echec_bestial': 'Il échoue malgré vous et nourrit un ressentiment silencieux.'},
                                {'rencontre': 'Une veuve influente cherche l’appui du Chapitre pour protéger '
                                              'l’héritage de son fils.',
                                 'res_temp': 'Atrabilaire (Fugace) ou Aucune',
                                 'effet': 'Vous orientez la décision vers une protection canonique favorable.',
                                 'victoire_critique': 'La famille devient un soutien discret et durable.',
                                 'victoire_pyrrhus': 'L’affaire dissimule un conflit civil plus large qui pourrait '
                                                     'dépasser le cadre religieux.',
                                 'reussite_bestiale': 'La veuve se montre trop reconnaissante en public.',
                                 'echec_bestial': 'Un document manquant fragilise la décision.'},
                                {'rencontre': 'Un litige oppose deux maisons mineures au sujet d’une promesse '
                                              'matrimoniale non tenue.',
                                 'res_temp': 'Atrabilaire (Fugace)',
                                 'effet': 'Vous proposez une lecture juridique équilibrée qui apaise la tension.',
                                 'victoire_critique': 'Les deux maisons sortent liées par une dette commune envers le '
                                                      'Chapitre.',
                                 'victoire_pyrrhus': 'Votre arbitrage favorise involontairement l’une des deux '
                                                     'maisons.',
                                 'reussite_bestiale': 'Votre rôle devient trop central dans le compromis.',
                                 'echec_bestial': 'Le conflit se ravive sous une forme plus amère.'},
                                {'rencontre': 'Un copiste épuisé demande audience : il dit craindre des ‘tentations’ '
                                              'nées d’un texte qu’il recopie la nuit. Son regard fuit, puis insiste.',
                                 'res_temp': 'Sanguine (Fugace)',
                                 'effet': 'Son sang mêle ferveur et désir : l’interdit a trouvé une porte, et le vice '
                                          'se cache sous l’encre.',
                                 'victoire_critique': 'Vous refermez la brèche sans bruit et replacez le copiste sous '
                                                      'une discipline utile.',
                                 'victoire_pyrrhus': 'Une page annotée circule. Personne ne comprend tout, mais '
                                                     'certains sentent le soufre.',
                                 'reussite_bestiale': 'Vous le rendez dépendant de vos entretiens : il reviendra, plus '
                                                      'hardi, plus sale.',
                                 'echec_bestial': 'Il se confesse au mauvais confesseur ; l’écho reste vague, mais il '
                                                  'existe.'},
                                {'rencontre': 'Une accusation implicite d’hérésie vise un prédicateur apprécié des '
                                              'fidèles, sans preuve claire.',
                                 'res_temp': 'Atrabilaire (Fugace)',
                                 'effet': 'Vous recommandez prudence et examen approfondi avant toute condamnation.',
                                 'victoire_critique': 'Vous transformez l’affaire en démonstration d’équilibre '
                                                      'doctrinal et préservez la paix.',
                                 'victoire_pyrrhus': 'Votre prudence vous rend visible au-delà du Chapitre : à la '
                                                     'Cathédrale, des regards Ventrues commencent à mesurer votre '
                                                     'influence.',
                                 'reussite_bestiale': 'Le prédicateur vous associe publiquement à sa défense.',
                                 'echec_bestial': 'Une phrase mal interprétée ravive la suspicion.'},
                                {'rencontre': 'Un chevalier demande la protection morale du Chapitre après un duel aux '
                                              'circonstances troubles.',
                                 'res_temp': 'Atrabilaire (Fugace)',
                                 'effet': 'Vous obtenez un ajournement de toute procédure religieuse.',
                                 'victoire_critique': 'Le chevalier devient un allié discret et redevable.',
                                 'victoire_pyrrhus': 'L’affaire touche indirectement une maison du Cœur Bourgeois qui '
                                                     'pourrait s’en souvenir.',
                                 'reussite_bestiale': 'Le chevalier vous sollicite au-delà du cadre religieux.',
                                 'echec_bestial': 'Un témoin civil contredit la version soutenue.'},
                                {'rencontre': 'Un manuscrit théologique à double lecture est soumis au scriptorium ; '
                                              'un copiste y cherche, trop clairement, une forme de reconnaissance '
                                              'interdite.',
                                 'res_temp': 'Sanguine (Fugace)',
                                 'effet': 'La tension du texte se mêle à un désir trouble : l’orthodoxie se fissure au '
                                          'bord des marges.',
                                 'victoire_critique': 'Vous identifiez une formulation sauvant le texte sans scandale, '
                                                      'et vous contrôlez sa diffusion.',
                                 'victoire_pyrrhus': 'Votre intervention crée un précédent interprétatif qui pourrait '
                                                     'être utilisé contre vous.',
                                 'reussite_bestiale': 'Le copiste se croit encouragé à aller plus loin dans ses '
                                                      'audaces.',
                                 'echec_bestial': 'Le texte est brièvement mis sous scellés et l’on s’interroge sur '
                                                  'votre jugement.'},
                                {'rencontre': 'Un juriste canonique central vous demande d’appuyer une lecture stricte '
                                              'd’un point de droit qui divise le Chapitre.',
                                 'res_temp': 'Atrabilaire (Fugace)',
                                 'effet': 'Vous tranchez avec sobriété et donnez au juriste l’argument qu’il lui '
                                          'manquait.',
                                 'victoire_critique': 'Votre formulation devient un modèle : même vos opposants la '
                                                      'reprennent, malgré eux.',
                                 'victoire_pyrrhus': 'Votre avis renforce une faction interne plus ambitieuse que '
                                                     'prévu ; on commencera à compter vos appuis, même si personne ne '
                                                     'vous accuse.',
                                 'reussite_bestiale': 'Vous imposez votre lecture avec une froideur trop visible : '
                                                      'certains se taisent… et retiennent.',
                                 'echec_bestial': 'Un détail de procédure vous échappe ; votre avis est relégué, et le '
                                                  'juriste s’en souvient.'},
                                {'rencontre': 'Un dossier sensible doit “disparaître” du circuit officiel, sans jamais '
                                              'quitter le Chapitre.',
                                 'res_temp': 'Atrabilaire (Fugace)',
                                 'effet': 'Vous organisez un ajournement, un classement discret, et un silence '
                                          'parfaitement justifié.',
                                 'victoire_critique': 'Le dossier se dissout dans les archives comme s’il n’avait '
                                                      'jamais existé, et l’on vous remercie sans vous nommer.',
                                 'victoire_pyrrhus': 'Le vide laissé par le dossier intrigue : un regard neuf au '
                                                     'scriptorium s’attarde sur ce qui manque plus que sur ce qui est '
                                                     'écrit.',
                                 'reussite_bestiale': 'Vous laissez une trace : une annotation trop précise, un geste '
                                                      'trop sûr, une signature indirecte.',
                                 'echec_bestial': 'Le dossier réapparaît au pire moment ; on s’interroge sur la chaîne '
                                                  'de garde, et votre proximité est devinée.'},
                                {'rencontre': 'Un moine respecté, connu pour sa rigueur, révèle en privé une dérive de '
                                              'luxure née au contact du scriptorium.',
                                 'res_temp': 'Sanguine (Fugace)',
                                 'effet': 'Son sang est lourd d’aveux retenus : l’interdit nourrit le désir plus que '
                                          'le désir ne nourrit l’interdit.',
                                 'victoire_critique': 'Vous détournez sa chute vers une pénitence utile et silencieuse '
                                                      '; il redevient fonctionnel et vous doit sa stabilité.',
                                 'victoire_pyrrhus': 'L’aveu, même étouffé, laisse une odeur : un frère soupçonne '
                                                     'qu’on protège quelque chose et observe les mauvaises heures.',
                                 'reussite_bestiale': 'Vous entretenez trop sa dépendance : il cherche à vous revoir, '
                                                      'à se confier encore.',
                                 'echec_bestial': 'Pris de honte, il se confesse au mauvais confesseur ; l’écho reste '
                                                  'vague, mais il existe.'},
                                {'rencontre': 'Une demande d’annulation scandalise par ses motifs : la cause est '
                                              'canonique, mais l’intention est purement politique.',
                                 'res_temp': 'Atrabilaire (Fugace)',
                                 'effet': 'Vous encadrez la procédure pour qu’elle paraisse légitime, et qu’aucune '
                                          'phrase ne dépasse.',
                                 'victoire_critique': 'Vous neutralisez les oppositions en amont ; même les plus '
                                                      'stricts n’ont rien de solide à attaquer.',
                                 'victoire_pyrrhus': 'Vous sous-estimez l’appétit de ceux que vous aidez : la faveur '
                                                     'attendue se transforme en exigence, et votre prudence devient un '
                                                     'outil entre leurs mains.',
                                 'reussite_bestiale': 'Une tournure laisse entendre que vous “faites et défaites” des '
                                                      'unions.',
                                 'echec_bestial': 'Un chanoine hostile exige une relecture complète ; la décision '
                                                  'traîne, et l’affaire s’envenime.'},
                                {'rencontre': 'Un noble lié au Cœur Bourgeois sollicite une “bénédiction” qui '
                                              'ressemble davantage à une couverture qu’à un acte religieux.',
                                 'res_temp': 'Atrabilaire (Fugace) ou Aucune',
                                 'effet': 'Vous accordez une voie de sortie canonique, propre, et suffisamment ambiguë '
                                          'pour satisfaire sans compromettre le Chapitre.',
                                 'victoire_critique': 'L’accord se fait sans bruit et sans trace ; l’homme repart '
                                                      'convaincu que le Chapitre est la seule porte qui compte.',
                                 'victoire_pyrrhus': 'Vous réalisez trop tard que cette affaire n’aurait jamais dû '
                                                     'franchir les limites du quartier : si cela se répète, le Cœur '
                                                     'Bourgeois — et peut-être Nantes — pourrait en entendre parler.',
                                 'reussite_bestiale': 'Vous laissez paraître votre mépris : l’homme sourit… et s’en '
                                                      'souviendra.',
                                 'echec_bestial': 'La demande revient par une autre bouche, déformée ; on parle d’un '
                                                  'érudit qui accorde des protections.'},
                                {'rencontre': 'Un prédicateur populaire est contesté : son succès inquiète les plus '
                                              'stricts, mais ses propos restent dans l’orthodoxie.',
                                 'res_temp': 'Atrabilaire (Fugace)',
                                 'effet': 'Vous recommandez mesure : examen des sermons, puis apaisement public.',
                                 'victoire_critique': 'Vous évitez une crise : le prédicateur est encadré sans être '
                                                      'brisé, et le Chapitre sort grandi.',
                                 'victoire_pyrrhus': 'Votre prudence est interprétée comme un choix de camp ; une '
                                                     'oreille de la Cathédrale s’intéresse à vous sans se montrer.',
                                 'reussite_bestiale': 'Un propos trop tranchant est répété en couloir, amputé de sa '
                                                      'nuance.',
                                 'echec_bestial': 'Un extrait de sermon, sorti du contexte, ravive la suspicion.'},
                                {'rencontre': 'Une intercession est demandée auprès d’un dignitaire du Chapitre : pas '
                                              'pour une faute, mais pour obtenir une décision ‘dans le bon sens’.',
                                 'res_temp': 'Atrabilaire (Fugace)',
                                 'effet': 'Vous obtenez une audience privée et placez les mots qui manquaient, sans '
                                          'jamais promettre ouvertement.',
                                 'victoire_critique': 'La décision tombe, légitime en apparence et favorable en '
                                                      'profondeur ; le demandeur ressort convaincu d’avoir trouvé le '
                                                      'bon passage.',
                                 'victoire_pyrrhus': 'Vous avez arrangé trop finement : le demandeur croit désormais '
                                                     'que tout s’achète et reviendra avec des demandes plus risquées.',
                                 'reussite_bestiale': 'Un regard comprend que vous aimez être indispensable.',
                                 'echec_bestial': 'Le dignitaire se ferme ; l’intercession échoue et l’on vous soupèse '
                                                  'un instant.'},
                                {'rencontre': 'On vous consulte au sujet d’une formulation qui pourrait justifier un '
                                              'décret local contre une œuvre jugée ‘déplacée’.',
                                 'res_temp': 'Atrabilaire (Fugace)',
                                 'effet': 'Vous rédigez une interprétation prudente, suffisante pour orienter la '
                                          'décision sans l’assumer publiquement.',
                                 'victoire_critique': 'Le décret passe sous une forme édulcorée : personne ne peut '
                                                      'vous désigner, et pourtant la ville s’aligne.',
                                 'victoire_pyrrhus': 'Vous sentez trop tard que vous avez quitté le terrain canonique '
                                                     'pour toucher au civil : si cela s’apprend, les maisons du Cœur '
                                                     'Bourgeois pourraient se saisir de l’affaire.',
                                 'reussite_bestiale': 'Vous montrez trop de certitude : un lecteur attentif comprend '
                                                      'que vous tenez la plume.',
                                 'echec_bestial': 'Un mot de trop rend le texte attaquable ; la décision se retourne '
                                                  'et l’on cherche un responsable.'},
                                {'rencontre': 'Un copiste est surpris avec des feuillets ‘personnels’ dissimulés sous '
                                              'des psaumes : prière et luxure partagent la même main.',
                                 'res_temp': 'Sanguine (Fugace)',
                                 'effet': 'Le sang a le goût du secret honteux : la corruption est là, feutrée, '
                                          'enracinée.',
                                 'victoire_critique': 'Vous étouffez l’incident et recadrez le copiste sans l’exposer '
                                                      '; il vous doit sa place et son silence.',
                                 'victoire_pyrrhus': 'Quelqu’un a vu le feuillet avant vous. L’écho ne dit pas tout… '
                                                     'mais il dit assez.',
                                 'reussite_bestiale': 'Vous le marquez trop : il s’attache à vous comme à un '
                                                      'confesseur du vice.',
                                 'echec_bestial': 'Il s’effondre et accuse ‘des influences’ ; le mot hérésie est '
                                                  'prononcé à voix basse.'},
                                {'rencontre': 'Une maison rennaise aux ambitions croissantes veut que le Chapitre '
                                              '‘certifie’ une décision qui relève surtout d’un rapport de force en '
                                              'ville.',
                                 'res_temp': 'Atrabilaire (Fugace)',
                                 'effet': 'Vous offrez une sortie canonique qui ressemble à un sceau, tout en restant '
                                          'juridiquement défendable.',
                                 'victoire_critique': 'La maison obtient ce qu’elle voulait et vous traite désormais '
                                                      'comme un passage obligé, mais discret.',
                                 'victoire_pyrrhus': 'Vous réalisez que l’affaire vous a tiré hors du territoire : si '
                                                     'la rumeur file, le Cœur Bourgeois écoutera… et Nantes aussi '
                                                     'pourrait noter le mouvement.',
                                 'reussite_bestiale': 'Votre geste est trop visible : un rival comprend que vous pesez '
                                                      'sur le jeu urbain.',
                                 'echec_bestial': 'Une résistance interne au Chapitre ralentit tout ; la maison '
                                                  's’impatiente et devient dangereuse.'},
                                {'rencontre': 'Un dossier évoque indirectement le pouvoir ducal : une demande '
                                              '‘religieuse’ dont les conséquences seraient politiques à l’échelle de '
                                              'la cité.',
                                 'res_temp': 'Atrabilaire (Fugace)',
                                 'effet': 'Vous tenez l’affaire à distance, en la renvoyant vers des étapes canoniques '
                                          'lentes et irréprochables.',
                                 'victoire_critique': 'Vous obtenez un compromis qui apaise tout le monde sans trace '
                                                      'd’ingérence.',
                                 'victoire_pyrrhus': 'Vous comprenez trop tard qu’en touchant ce dossier, votre nom '
                                                     'pourrait remonter jusqu’à Nantes — et ce n’est pas votre '
                                                     'territoire.',
                                 'reussite_bestiale': 'Vous vous sentez invulnérable : un mot de trop laisse deviner '
                                                      'votre rôle.',
                                 'echec_bestial': 'Le dossier change de mains ; vous perdez le contrôle et l’écho '
                                                  'devient imprévisible.'},
                                {'rencontre': 'Un chanoine au zèle suspect multiplie les questions ‘innocentes’ sur le '
                                              'scriptorium et ses horaires.',
                                 'res_temp': 'Atrabilaire (Fugace)',
                                 'effet': 'Vous répondez avec calme, en le renvoyant vers des procédures et des '
                                          'devoirs qui l’occupent.',
                                 'victoire_critique': 'Vous le neutralisez par l’étiquette et le texte : il se heurte '
                                                      'à un mur de légitimité.',
                                 'victoire_pyrrhus': 'Vous sentez qu’il n’est pas seul : à la Cathédrale, certains '
                                                     'aimeraient affaiblir l’influence Trémère. Sans accusation, la '
                                                     'pression existe.',
                                 'reussite_bestiale': 'Vous le méprisez trop : il devient plus dangereux par orgueil.',
                                 'echec_bestial': 'Il obtient une petite preuve administrative ; rien de grave, mais '
                                                  'assez pour poser des questions.'},
                                {'rencontre': 'Un texte théologique dangereux circule sous forme de copies incomplètes '
                                              '; les fragments excitent plus qu’ils n’enseignent.',
                                 'res_temp': 'Sanguine (Fugace)',
                                 'effet': 'Le sang a la saveur d’un vice érudit : hérésie murmurée, désir contenu, '
                                          'fascination pour l’interdit.',
                                 'victoire_critique': 'Vous reprenez les fragments et remplacez ce qui devait l’être : '
                                                      'le scandale s’éteint sans trace nette.',
                                 'victoire_pyrrhus': 'Vous en gardez trop : posséder ce texte, même pour le contrôler, '
                                                     'crée un risque si l’on fouille vos pas.',
                                 'reussite_bestiale': 'Vous laissez transparaître votre intérêt : un copiste comprend '
                                                      'qu’il a trouvé une porte.',
                                 'echec_bestial': 'Une copie sort du Chapitre et l’écho devient incontrôlable.'},
                                {'rencontre': 'Un arrangement matrimonial, présenté comme canonique, vise en réalité à '
                                              'déplacer un équilibre de pouvoir. On évoque, à demi-mot, Nantes.',
                                 'res_temp': 'Atrabilaire (Fugace)',
                                 'effet': 'Vous encadrez l’affaire dans un langage religieux irréprochable, tout en '
                                          'ménageant une issue pratique.',
                                 'victoire_critique': 'L’accord se fait sans éclat : chacun croit y gagner, et votre '
                                                      'rôle reste invisible.',
                                 'victoire_pyrrhus': 'Vous comprenez trop tard que l’affaire dépasse Rennes : si elle '
                                                     'remonte, la maison ducale de Nantes pourrait entendre votre nom.',
                                 'reussite_bestiale': 'Vous jouez trop fin : une phrase laisse deviner que vous avez '
                                                      '‘guidé’ la main du Chapitre.',
                                 'echec_bestial': 'L’accord casse. Chacun cherche un coupable, et votre proximité est '
                                                  'suspectée.'},
                                {'rencontre': 'Le Gardien du Tribunal Canonique vous convoque : un homme de texte, de '
                                              'règles, et de mémoire. Il veut comprendre votre méthode.',
                                 'res_temp': 'Atrabilaire (Fugace)',
                                 'effet': 'Vous répondez avec calme et précision. Il repart avec l’impression que tout '
                                          'est sous contrôle.',
                                 'victoire_critique': 'Vous gagnez son estime : il vous ouvrira des portes, sans '
                                                      'jamais le dire.',
                                 'victoire_pyrrhus': 'Votre échange laisse une trace écrite. Rien d’accusatoire — mais '
                                                     'assez pour qu’un lecteur futur s’y intéresse.',
                                 'reussite_bestiale': 'Vous imposez votre maîtrise avec trop d’assurance : il note '
                                                      'votre aplomb.',
                                 'echec_bestial': 'Il vous trouve imprécis. Sans vous condamner, il vous surveillera '
                                                  'davantage.'},
                                {'rencontre': 'Un Inquisiteur ‘de passage’ (Frère Séverin d’Angers) demande à consulter les archives et à '
                                              'rencontrer quelques scribes. Il est cordial, cultivé… et dangereusement '
                                              'attentif. (Manip+Investig+rempart diff4 base +- ajustements selon résultat du jet de chasse pour le détourner)',
                                 'res_temp': 'Sanguine (Vive) ou aucune',
                                 'effet': 'Vous lui facilitez l’accès sans lui offrir de prise. Il vous remercie avec '
                                          'une politesse parfaite.',
                                 'victoire_critique': 'Vous détournez son attention vers des pistes inoffensives. Il '
                                                      'repart convaincu d’avoir tout vu… ou feint de l’être.',
                                 'victoire_pyrrhus': 'Même en cas de réussite, sa présence est un poids : il dit être '
                                                     'de passage… mais reste un jour de plus, puis un autre. '
                                                     'L’inquiétude s’installe.',
                                 'reussite_bestiale': 'Vous le jaugez trop ouvertement : il le remarque, et sourit.',
                                 'echec_bestial': 'Il obtient un détail : un nom, une date, une incohérence. Rien '
                                                  'n’explose… mais quelque chose commence.'}]}}