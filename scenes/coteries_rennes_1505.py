from domain.schema import Scene, Choice


ECHELLE_STATS = """
<div style=\"margin:0.8rem 0 1.2rem 0; padding:1rem 1.2rem; border:1px solid rgba(255,255,255,0.16); border-radius:14px; background:rgba(0,0,0,0.24); line-height:1.5;\">
  <b>Lecture des indicateurs</b><br/>
  0 ou 1 = contrôle faible ; 2 ou 3 = contrôle partiel ; 4 ou 5 = contrôle fort.<br/><br/>
  Les totaux affichés sont les <b>totaux de base</b>. Les valeurs entre parenthèses ne sont pas incluses : elles signalent un tribut, une répression ou un modificateur contextuel.<br/>
  <b>+1 tribut</b> : la coterie bénéficie d'un tribut redistribué par le Prince.<br/>
  <b>-1 tribut</b> : la coterie verse ce tribut au Prince, qui peut le conserver ou le redistribuer.
</div>
"""


def _fiche_coterie(
    registre: str,
    nom: str,
    appartenance: str,
    type_coterie: str,
    territoires_html: str,
    total: str,
    synthese: str,
    special: str = "",
    notes: str = "",
) -> str:
    special_html = ""
    if special.strip():
        special_html = f"""
<div style=\"margin-top:0.9rem; padding:0.75rem 0.9rem; border-left:3px solid rgba(255,255,255,0.35); background:rgba(255,255,255,0.04); line-height:1.45;\">
  <b>Spécial</b> : {special}
</div>
"""

    notes_html = ""
    if notes.strip():
        notes_html = f"""
<div style=\"margin-top:0.75rem; font-size:0.92rem; opacity:0.9; line-height:1.45;\">
  <b>Note</b> : {notes}
</div>
"""

    return f"""
<div style=\"margin:0.8rem 0 1.2rem 0; padding:1rem 1.2rem; border:1px solid rgba(255,255,255,0.18); border-radius:16px; background:linear-gradient(145deg, rgba(255,255,255,0.05), rgba(0,0,0,0.25)); box-shadow:0 8px 24px rgba(0,0,0,0.35);\">
  <div style=\"font-size:0.75rem; letter-spacing:0.12em; text-transform:uppercase; opacity:0.75;\">✦ {registre} ✦</div>
  <div style=\"margin-top:0.6rem; line-height:1.45;\">
    <b>Coterie</b> : {nom}<br/>
    <b>Faction</b> : {appartenance}<br/>
    <b>Type</b> : {type_coterie}
  </div>
</div>

{territoires_html}

<div style=\"margin:1rem 0; padding:1rem 1.2rem; border:1px solid rgba(255,255,255,0.16); border-radius:14px; background:rgba(0,0,0,0.28);\">
  <b>Total de base</b> : {total}
  <div style=\"margin-top:0.65rem; font-size:0.92rem; opacity:0.9; line-height:1.45;\">
    Les valeurs entre parenthèses ne sont pas incluses dans le total de base affiché. Elles indiquent un effet externe, un tribut ou une contrainte spéciale.
  </div>
  {notes_html}
  {special_html}
</div>

<div style=\"margin:1rem 0 0.4rem 0; padding:1rem 1.2rem; border-left:4px solid rgba(180,35,35,0.85); border-radius:12px; background:rgba(120,15,15,0.18); line-height:1.55;\">
  <b>Synthèse narrative</b><br/>
  {synthese}
</div>
"""


def get_scene() -> Scene:
    return Scene(
        id="coteries_rennes_1505",
        title="Registre stratégique — Coteries de Rennes 1505",
        intro_md=f"""
La conversation change de nature.  
Ce ne sont plus des rumeurs que l'on échange, mais des rapports.

Des territoires, des portes, des faubourgs.  
Des points de Viandis, de Servage et de Rempart.  
Des équilibres que chacun prétend contrôler.

À Rennes, une coterie ne possède jamais seulement un lieu.  
Elle possède une pression, une peur, une dette ou une frontière.

{ECHELLE_STATS}

Quelle faction souhaites-tu consulter ?
""",
        choices=[
            Choice(
                id="coterie_prince",
                label="Prince — Régence de Rennes",
                answer_md=_fiche_coterie(
                    registre="Registre stratégique : autorité princière",
                    nom="Prince",
                    appartenance="Camarilla",
                    type_coterie="Régence (+1 Viandis)",
                    territoires_html="""
<div style=\"line-height:1.55;\">
  <h4>Cœur Bourgeois — 3/3</h4>
  <ul>
    <li><b>Place des Lices</b> : +2 Viandis</li>
    <li><b>Maison des Bourgeois</b> : +2 Servage</li>
    <li><b>Grand Comptoir</b> : +1 Servage, +2 Viandis</li>
    <li><b>Bonus domination</b> : +1 Servage</li>
  </ul>

  <h4>Porte Saint-Michel — Porte des Abbesses</h4>
  <ul>
    <li><b>Contrôle porte</b> : +1 Rempart, +1 Servage</li>
  </ul>
</div>
""",
                    total="Viandis 5 / Servage 5 (-1 répression) / Rempart 1 (+1 tribut)",
                    special="Répression : sacrifie 1 point de Servage pour maintenir la répression aux faubourgs de la Porte Saint-Germain.",
                    notes="+1 tribut signifie que la coterie bénéficie d'un tribut redistribué par le Prince. -1 répression est une dépense de contrôle et n'est pas incluse dans le total de Servage.",
                    synthese="""
Le Prince règne sur le cœur riche de Rennes, là où circulent les proies, l'argent et les serments.  
Sa Viandis et son Servage indiquent un contrôle fort : il nourrit sa cour autant qu'il tient les hommes en laisse.  
Son Rempart reste faible, preuve que son autorité repose davantage sur la peur, les tributs et la répression que sur une maîtrise directe du terrain.  
À Rennes, son pouvoir est immense, mais il doit sans cesse être entretenu.
""",
                ),
                followups=[],
                ends_scene=True,
            ),
            Choice(
                id="coterie_ventrue",
                label="Ventrue — Défenseurs du Sacré",
                answer_md=_fiche_coterie(
                    registre="Registre stratégique : aristocratie sacrée",
                    nom="Ventrue",
                    appartenance="Camarilla",
                    type_coterie="Firme (+1 Servage)",
                    territoires_html="""
<div style=\"line-height:1.55;\">
  <h4>Ceinture Sacrée — 2/3</h4>
  <ul>
    <li><b>Cathédrale Saint-Pierre</b> : +1 Servage, +2 Rempart</li>
    <li><b>Cloître des Chanoines</b> : +2 Rempart</li>
  </ul>

  <h4>Porte Saint-Hélier — Porte du Sang Neuf</h4>
  <ul>
    <li><b>Contrôle porte</b> : +1 Rempart, +1 Servage</li>
  </ul>
</div>
""",
                    total="Viandis 0 (+1 tribut) / Servage 3 / Rempart 5 (-1 tribut)",
                    notes="+1 tribut signifie que la coterie bénéficie d'un tribut redistribué par le Prince. -1 tribut signifie que la coterie verse un tribut au Prince, qui peut le conserver ou le redistribuer.",
                    synthese="""
Les Ventrue tiennent le sacré comme une forteresse, avec une discipline froide et méthodique.  
Leur Rempart indique un contrôle fort : rien ne bouge dans leur domaine sans être vu, pesé ou arrêté.  
Mais leur Viandis est faible : sans tribut, faveur ou arrangement, leur prestige ne nourrit personne.  
Ils incarnent une puissance verrouillée, solide, mais dépendante.
""",
                ),
                followups=[],
                ends_scene=True,
            ),
            Choice(
                id="coterie_tremere",
                label="Tremere — Fondation de la Pierre Noire",
                answer_md=_fiche_coterie(
                    registre="Registre stratégique : occultation contrôlée",
                    nom="Tremere",
                    appartenance="Camarilla",
                    type_coterie="Aucune",
                    territoires_html="""
<div style=\"line-height:1.55;\">
  <h4>Ceinture Sacrée — 1/3</h4>
  <ul>
    <li><b>Archives du Chapitre</b> : +1 Servage, +1 Viandis</li>
  </ul>
</div>
""",
                    total="Viandis 1 / Servage 1 / Rempart 0",
                    synthese="""
Les Tremere ne possèdent presque rien, sinon un point d'ancrage discret dans les archives du Chapitre.  
Leur Viandis, leur Servage et leur Rempart restent faibles : ils ne tiennent pas encore un territoire, ils s'y glissent.  
Leur force n'est pas visible sur la carte, mais dans ce qu'ils apprennent, conservent et taisent.  
À Rennes, ils sont moins un pouvoir établi qu'une menace en gestation.
""",
                ),
                followups=[],
                ends_scene=True,
            ),
            Choice(
                id="coterie_brujah",
                label="Brujah — Ombres des rues",
                answer_md=_fiche_coterie(
                    registre="Registre stratégique : pression populaire",
                    nom="Brujah",
                    appartenance="Camarilla",
                    type_coterie="Bande de Crocs (+1 Viandis)",
                    territoires_html="""
<div style=\"line-height:1.55;\">
  <h4>Bas-quartiers / Ombres des rues — 3/3</h4>
  <ul>
    <li><b>Tanneries</b> : +2 Viandis</li>
    <li><b>Ruines &amp; Souterrains</b> : +1 Rempart</li>
    <li><b>Quartier des paroisses populaires</b> : +1 Viandis, +1 Servage, +1 Rempart</li>
    <li><b>Bonus domination</b> : +1 Servage</li>
  </ul>
</div>
""",
                    total="Viandis 4 (-1 tribut) / Servage 2 / Rempart 2 (-1 tribut)",
                    notes="-1 tribut signifie que la coterie verse ce tribut au Prince. Le Prince peut ensuite le redistribuer à sa propre coterie ou à une autre coterie.",
                    synthese="""
Les Brujah règnent dans les bas-quartiers, là où la colère, la faim et les ombres leur ouvrent la voie.  
Leur Viandis indique un contrôle fort : les rues leur offrent du sang, du bruit et des disparitions faciles.  
Leur Servage et leur Rempart restent partiels, trop dispersés pour transformer la brutalité en véritable ordre.  
Ils dominent par l'impact, pas par la stabilité.
""",
                ),
                followups=[],
                ends_scene=True,
            ),
            Choice(
                id="coterie_gangrel",
                label="Gangrel — Crocs Silencieux",
                answer_md=_fiche_coterie(
                    registre="Registre stratégique : surveillance des lisières",
                    nom="Gangrel",
                    appartenance="Camarilla",
                    type_coterie="Sentinelles (+1 Rempart)",
                    territoires_html="""
<div style=\"line-height:1.55;\">
  <h4>Faubourgs Saint-Martin — 3/3</h4>
  <ul>
    <li><b>Saint-Martin</b> : +1 Viandis</li>
    <li><b>Jardins &amp; Vignes</b> : +1 Viandis</li>
    <li><b>Ferme Fortifiée</b> : +1 Rempart</li>
    <li><b>Bonus faubourgs</b> : +1 Servage</li>
  </ul>

  <h4>Porte Saint-Martin — Porte des Brumes</h4>
  <ul>
    <li><b>Contrôle porte</b> : +1 Rempart, +1 Servage</li>
  </ul>
</div>
""",
                    total="Viandis 2 / Servage 2 / Rempart 3",
                    synthese="""
Les Gangrel tiennent Saint-Martin comme une lisière vivante, entre ville, champs et chemins de fuite.  
Leur Viandis, leur Servage et leur Rempart indiquent un contrôle partiel, mais cohérent et bien enraciné.  
Ils connaissent leurs limites, leurs passages et leurs silences mieux que quiconque.  
Ils ne cherchent pas à briller, mais à survivre mieux que les autres.
""",
                ),
                followups=[],
                ends_scene=True,
            ),
            Choice(
                id="coterie_executeurs",
                label="Les Exécuteurs — Main armée du pouvoir",
                answer_md=_fiche_coterie(
                    registre="Registre stratégique : coercition directe",
                    nom="Les Exécuteurs",
                    appartenance="Camarilla",
                    type_coterie="Aucune",
                    territoires_html="""
<div style=\"line-height:1.55;\">
  <h4>Porte Madeleine — Porte des Mourants</h4>
  <ul>
    <li><b>Contrôle porte</b> : +1 Rempart, +1 Servage</li>
  </ul>

  <h4>Porte Saint-Germain — Porte du Pont Noir</h4>
  <ul>
    <li><b>Contrôle porte</b> : +1 Rempart, +1 Servage</li>
  </ul>
</div>
""",
                    total="Viandis 0 / Servage 2 / Rempart 2",
                    synthese="""
Les Exécuteurs ne possèdent pas Rennes : ils en tiennent les seuils.  
Leur Viandis est faible, car leur rôle n'est pas de se nourrir, mais de surveiller, bloquer et frapper.  
Leur Servage et leur Rempart indiquent un contrôle partiel, utile mais limité aux points de passage.  
Ils ne font pas naître l'autorité du Prince : ils la rendent crédible.
""",
                ),
                followups=[],
                ends_scene=True,
            ),
            Choice(
                id="coterie_anarchs",
                label="Anarchs — Saboteurs des faubourgs",
                answer_md=_fiche_coterie(
                    registre="Registre stratégique : dissidence organisée",
                    nom="Anarchs",
                    appartenance="Anarch",
                    type_coterie="Saboteur (+1 Rempart)",
                    territoires_html="""
<div style=\"line-height:1.55;\">
  <h4>Faubourgs Madeleine — 3/3</h4>
  <ul>
    <li><b>La Madeleine</b> : +1 Viandis</li>
    <li><b>Saint-Yves / Hospices</b> : +1 Viandis</li>
    <li><b>Hôpital des Pèlerins</b> : +1 Servage</li>
    <li><b>Bonus faubourgs</b> : +1 Servage</li>
  </ul>
</div>
""",
                    total="Viandis 2 / Servage 2 / Rempart 1 (+1 répression sauf contre le Prince)",
                    special="La répression imposée par le Prince augmente de +1 la difficulté pour chasser, mais confère +1 Rempart face aux autres coteries. Si la coterie du Prince agit contre ce territoire, ce bonus ne s'applique pas : le Rempart est alors traité à -1 au lieu de +1.",
                    notes="+1 répression est une valeur conditionnelle subie. Elle n'est pas incluse dans le total de Rempart et ne compte pas comme tribut.",
                    synthese="""
Les Anarchs tiennent les faubourgs de la Madeleine, un territoire pauvre mais nerveux, accroché aux marges de la ville.  
Leur Viandis et leur Servage indiquent un contrôle partiel : assez pour survivre, trop peu pour imposer un ordre durable.  
La répression du Prince pèse sur leur chasse, mais rend leurs rues plus dures à pénétrer pour les autres.  
Ils ne dominent rien ; ils résistent, et parfois cela suffit à faire trembler les puissants.
""",
                ),
                followups=[],
                ends_scene=True,
            ),
        ],
    )
