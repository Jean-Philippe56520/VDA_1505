from domain.schema import Scene, Choice


def get_scene() -> Scene:
    return Scene(
        id="rumeurs_elysium_1505",
        title="Registre officieux – Rumeurs de l’Elysium",
        intro_md="""
La musique se fait plus discrète.  
Les voix se rapprochent, mais ne s’élèvent jamais.

On t’accorde un murmure — un seul.

Tu as su écouter sans te faire remarquer.  
À présent, choisis le nom que tu veux entendre.

À Rennes, rien n’est jamais totalement vrai.  
Mais rien n’est jamais totalement faux non plus.

Qui souhaites-tu écouter ?
""",
        choices=[

            # ——— Institutions & figures d'Elysium ———

            Choice(
                id="heloise",
                label="Héloïse de Fougères",
                answer_md="""
<div style="margin:0.8rem 0 1.2rem 0; padding:1rem 1.2rem; border:1px solid rgba(255,255,255,0.18); border-radius:16px; background:linear-gradient(145deg, rgba(255,255,255,0.05), rgba(0,0,0,0.25)); box-shadow:0 8px 24px rgba(0,0,0,0.35);">
  <div style="font-size:0.75rem; letter-spacing:0.12em; text-transform:uppercase; opacity:0.75;">✦ Registre : identité consignée ✦</div>
  <div style="margin-top:0.6rem; line-height:1.45;">
    <b>Clan</b> : Ventrue &nbsp;•&nbsp; <b>Âge</b> : Ancilla &nbsp;•&nbsp; <b>Génération</b> : 10e<br/>
    <b>Rôle</b> : Harpie &nbsp;•&nbsp; <b>Coterie</b> : Les Gardiens du Sacré<br/>
    <b>Sire</b> : Odon
  </div>
</div>

On prononce son nom comme on effleure une lame.

> « Héloïse ne lance pas les rumeurs.  
> Elle les pèse… puis elle décide lesquelles méritent un avenir. »

Un souffle plus discret :

> « Ces derniers temps, elle semble écouter avec une attention particulière  
> ceux qui confondent grâce princière et innocence. »

Un sourire presque imperceptible.

> « À Rennes, être récompensé ne signifie pas toujours  
> que l’on a été irréprochable.  
> Seulement que l’on a été utile. »

Ici, l’autorité n’a pas besoin de hausser la voix.
""",
                followups=[],
                ends_scene=True,
            ),

            # ——— Camarilla & périphérie ———

            Choice(
                id="aodren",
                label="Aodren",
                answer_md="""
<div style="margin:0.8rem 0 1.2rem 0; padding:1rem 1.2rem; border:1px solid rgba(255,255,255,0.18); border-radius:16px; background:linear-gradient(145deg, rgba(255,255,255,0.05), rgba(0,0,0,0.25)); box-shadow:0 8px 24px rgba(0,0,0,0.35);">
  <div style="font-size:0.75rem; letter-spacing:0.12em; text-transform:uppercase; opacity:0.75;">✦ Registre : identité consignée ✦</div>
  <div style="margin-top:0.6rem; line-height:1.45;">
    <b>Clan</b> : Gangrel &nbsp;•&nbsp; <b>Âge</b> : Ancilla &nbsp;•&nbsp; <b>Génération</b> : 10e<br/>
    <b>Rôle</b> : Fléau &nbsp;•&nbsp; <b>Coterie</b> : Les Exécuteurs<br/>
    <b>Sire</b> : Kerzu
  </div>
</div>

La voix baisse d’un ton, comme si la salle elle-même écoutait.

> « Aodren est le bras du Prince.  
> Il ne promet rien. Il applique. »

Puis, plus bas encore :

> « On dit que les Exécuteurs n’aiment pas qu’on marche sur leurs traces.  
> Pourtant, récemment, certaines traces ont été partagées.  
> Sans morsure. Sans sanction. »

Un sourire prudent.

> « Peut-être était-ce une exception.  
> Peut-être un calcul.  
> Avec Aodren, la différence est rarement visible. »

On ne nomme pas l’ennemi.  
On laisse la peur remplir le reste.
""",
                followups=[],
                ends_scene=True,
            ),

            Choice(
                id="maela",
                label="Maëla la Veilleuse",
                answer_md="""
<div style="margin:0.8rem 0 1.2rem 0; padding:1rem 1.2rem; border:1px solid rgba(255,255,255,0.18); border-radius:16px; background:linear-gradient(145deg, rgba(255,255,255,0.05), rgba(0,0,0,0.25)); box-shadow:0 8px 24px rgba(0,0,0,0.35);">
  <div style="font-size:0.75rem; letter-spacing:0.12em; text-transform:uppercase; opacity:0.75;">✦ Registre : identité consignée ✦</div>
  <div style="margin-top:0.6rem; line-height:1.45;">
    <b>Clan</b> : Gangrel &nbsp;•&nbsp; <b>Âge</b> : Nouveau-né &nbsp;•&nbsp; <b>Génération</b> : 11e<br/>
    <b>Rôle</b> : — &nbsp;•&nbsp; <b>Coterie</b> : Les Crocs Silencieux<br/>
    <b>Sire</b> : Aodren
  </div>
</div>

Un regard glisse vers les portes, puis revient sur toi.

> « Maëla voit ce qui s’approche des frontières.  
> Et quand elle se tait… ce n’est pas qu’elle ignore. »

On raconte qu’elle juge rarement.  
Parce qu’elle intervient avant qu’on puisse plaider.
""",
                followups=[],
                ends_scene=True,
            ),

            Choice(
                id="ysabeau",
                label="Ysabeau",
                answer_md="""
<div style="margin:0.8rem 0 1.2rem 0; padding:1rem 1.2rem; border:1px solid rgba(255,255,255,0.18); border-radius:16px; background:linear-gradient(145deg, rgba(255,255,255,0.05), rgba(0,0,0,0.25)); box-shadow:0 8px 24px rgba(0,0,0,0.35);">
  <div style="font-size:0.75rem; letter-spacing:0.12em; text-transform:uppercase; opacity:0.75;">✦ Registre : identité consignée ✦</div>
  <div style="margin-top:0.6rem; line-height:1.45;">
    <b>Clan</b> : Nosferatu &nbsp;•&nbsp; <b>Âge</b> : Ancilla &nbsp;•&nbsp; <b>Génération</b> : 11e<br/>
    <b>Rôle</b> : — &nbsp;•&nbsp; <b>Coterie</b> : La Main du Prince<br/>
    <b>Sire</b> : Magda l'Ecorchée (détruite)
  </div>
</div>

Le murmure a quelque chose d’amusé, comme une confidence partagée.

> « Ysabeau sait toujours plus qu’elle ne devrait.  
> La question n’est pas ce qu’elle sait…  
> mais à qui ses secrets finissent par appartenir. »

Un souffle discret.

> « On dit que certains papiers disparaissent.  
> Et que les copies, elles, voyagent mieux que les originaux. »

À Rennes, l’information circule.  
Et personne ne jure qu’elle circule seule.
""",
                followups=[],
                ends_scene=True,
            ),

            Choice(
                id="ysoria",
                label="Ysoria la Silencieuse",
                answer_md="""
<div style="margin:0.8rem 0 1.2rem 0; padding:1rem 1.2rem; border:1px solid rgba(255,255,255,0.18); border-radius:16px; background:linear-gradient(145deg, rgba(255,255,255,0.05), rgba(0,0,0,0.25)); box-shadow:0 8px 24px rgba(0,0,0,0.35);">
  <div style="font-size:0.75rem; letter-spacing:0.12em; text-transform:uppercase; opacity:0.75;">✦ Registre : identité consignée ✦</div>
  <div style="margin-top:0.6rem; line-height:1.45;">
    <b>Clan</b> : Tremere &nbsp;•&nbsp; <b>Âge</b> : Nouveau-né &nbsp;•&nbsp; <b>Génération</b> : 11e<br/>
    <b>Rôle</b> : — &nbsp;•&nbsp; <b>Coterie</b> : La Fondation<br/>
    <b>Sire</b> : Magister Leopold von Hartheim (actif à Vienne)
  </div>
</div>

Le souffle se refroidit.

> « Tout le monde sait qu’Ysoria vient de Vienne.  
> Arrivée sans qu’on l’ait vraiment demandée,  
> installée sans qu’on l’ait franchement validée. »

Un temps.

> « La rumeur ne porte pas sur ses talents.  
> Mais sur la main qui tient la plume  
> lorsqu’elle rédige ses conclusions. »

Dans ce clan, on ne doute pas de la discipline.  
On doute de la destination.
""",
                followups=[],
                ends_scene=True,
            ),

            Choice(
                id="maloch",
                label="Frère Maloch l’Insondable",
                answer_md="""
<div style="margin:0.8rem 0 1.2rem 0; padding:1rem 1.2rem; border:1px solid rgba(255,255,255,0.18); border-radius:16px; background:linear-gradient(145deg, rgba(255,255,255,0.05), rgba(0,0,0,0.25)); box-shadow:0 8px 24px rgba(0,0,0,0.35);">
  <div style="font-size:0.75rem; letter-spacing:0.12em; text-transform:uppercase; opacity:0.75;">✦ Registre : identité consignée ✦</div>
  <div style="margin-top:0.6rem; line-height:1.45;">
    <b>Clan</b> : Malkavien &nbsp;•&nbsp; <b>Âge</b> : Nouveau-né &nbsp;•&nbsp; <b>Génération</b> : 9e<br/>
    <b>Rôle</b> : — &nbsp;•&nbsp; <b>Coterie</b> : La Fondation<br/>
    <b>Sire</b> : Agnès des Murmures
  </div>
</div>

Un rire nerveux précède la phrase, comme un réflexe.

> « Maloch dit parfois la vérité par erreur.  
> Ceux qui l’écoutent assez longtemps regrettent toujours d’avoir compris. »

On prétend qu’il délire.  
Mais personne ne le pousse à répéter.
""",
                followups=[],
                ends_scene=True,
            ),

            Choice(
                id="guillaume",
                label="Guillaume",
                answer_md="""
<div style="margin:0.8rem 0 1.2rem 0; padding:1rem 1.2rem; border:1px solid rgba(255,255,255,0.18); border-radius:16px; background:linear-gradient(145deg, rgba(255,255,255,0.05), rgba(0,0,0,0.25)); box-shadow:0 8px 24px rgba(0,0,0,0.35);">
  <div style="font-size:0.75rem; letter-spacing:0.12em; text-transform:uppercase; opacity:0.75;">✦ Registre : identité consignée ✦</div>
  <div style="margin-top:0.6rem; line-height:1.45;">
    <b>Clan</b> : Brujah &nbsp;•&nbsp; <b>Âge</b> : Ancilla &nbsp;•&nbsp; <b>Génération</b> : 9e<br/>
    <b>Rôle</b> : — &nbsp;•&nbsp; <b>Coterie</b> : Les Héritiers d'Alexandrie<br/>
    <b>Sire</b> : Gwilherm
  </div>
</div>

Le nom tombe plus bas que les autres.

> « Il y a des morts qui terminent une guerre.  
> Et d’autres qui commencent une pourriture. »

On raconte qu’à la Porte de la Madeleine, dans Rennes même, pendant que les portes cédaient et que les paysans de la Madeleine envahissaient les rues, deux vampires s’affrontèrent à l’écart du tumulte.

Mikolai von Hohenberg — le Toreador brillant, prestigieux, trop éclatant pour qu’on imagine sa lumière s’éteindre ainsi.  
Et Guillaume.

> « Ceux qui disent se souvenir jurent qu’il n’y eut ni meute, ni embuscade.  
> Un combat singulier.  
> Du sang sur les pierres.  
> Puis Guillaume debout… et la tête de Mikolai qui ne l’était plus. »

Un silence suit toujours cette partie.

> « Certains Anciens pourraient encore confirmer chaque pierre, chaque cri, peut-être même la façon dont Mikolai est tombé.  
> Curieusement, ils aiment peu qu’on leur pose la question. »

Puis vient le murmure que les Toreador détestent davantage :

> « Peut-être que leur clan n’a pas commencé à mourir sous les flammes de l’Inquisition.  
> Peut-être que cela avait commencé là.  
> Quand Guillaume a séparé Mikolai de sa tête… et Rennes de l’idée que les Roses étaient intouchables. »

Personne ne peut prouver que cette nuit fut le commencement de leur chute.  
Mais à Rennes, certaines rumeurs survivent précisément parce qu’elles ressemblent trop à des souvenirs.
""",
                followups=[],
                ends_scene=True,
            ),

            Choice(
                id="ronan",
                label="Ronan",
                answer_md="""
<div style="margin:0.8rem 0 1.2rem 0; padding:1rem 1.2rem; border:1px solid rgba(255,255,255,0.18); border-radius:16px; background:linear-gradient(145deg, rgba(255,255,255,0.05), rgba(0,0,0,0.25)); box-shadow:0 8px 24px rgba(0,0,0,0.35);">
  <div style="font-size:0.75rem; letter-spacing:0.12em; text-transform:uppercase; opacity:0.75;">✦ Registre : identité consignée ✦</div>
  <div style="margin-top:0.6rem; line-height:1.45;">
    <b>Clan</b> : Brujah &nbsp;•&nbsp; <b>Âge</b> : Nouveau-né &nbsp;•&nbsp; <b>Génération</b> : 10e<br/>
    <b>Rôle</b> : — &nbsp;•&nbsp; <b>Coterie</b> : Les Héritiers d'Alexandrie<br/>
    <b>Sire</b> : Sten Hurlesang
  </div>
</div>

Le murmure se fait sec, presque fataliste.

> « Tout le monde sait d’où vient Ronan.  
> Son sire a choisi la rupture. Un traître, dit-on. »

Un silence.

> « S’il ne l'a pas rejoints, ce n’est pas par dévotion.  
> Disons simplement qu’il existe des laisses  
> qu’on ne voit pas… mais qu’on sent. »

On évite d’expliquer davantage.
""",
                followups=[],
                ends_scene=True,
            ),

            Choice(
                id="karel",
                label="Karel",
                answer_md="""
<div style="margin:0.8rem 0 1.2rem 0; padding:1rem 1.2rem; border:1px solid rgba(255,255,255,0.18); border-radius:16px; background:linear-gradient(145deg, rgba(255,255,255,0.05), rgba(0,0,0,0.25)); box-shadow:0 8px 24px rgba(0,0,0,0.35);">
  <div style="font-size:0.75rem; letter-spacing:0.12em; text-transform:uppercase; opacity:0.75;">✦ Registre : identité consignée ✦</div>
  <div style="margin-top:0.6rem; line-height:1.45;">
    <b>Clan</b> : Caitiff &nbsp;•&nbsp; <b>Âge</b> : Ancilla &nbsp;•&nbsp; <b>Génération</b> : 11e<br/>
    <b>Rôle</b> : — &nbsp;•&nbsp; <b>Coterie</b> : Les Exécuteurs<br/>
    <b>Sire</b> : Inconnu
  </div>
</div>

La voix se fait prudente, et l’on regarde autour avant de poursuivre.

> « Karel n’a de place ici que parce que le Fléau l’accepte.  
> Et parfois… c’est la seule légitimité qui compte. »

Un silence.

> « On dit qu’il a récemment escorté quelqu’un  
> qui n’appartenait pas à ses affaires.  
> Pas par bonté. Karel n’a pas ce genre de faiblesse. »

Un sourire bref.

> « Peut-être a-t-il vu une utilité.  
> Peut-être a-t-il vu une dette.  
> Ou peut-être a-t-il simplement reconnu  
> qu’il valait mieux ramener certains témoins vivants. »

Le rire est une monnaie dangereuse, à Rennes.
""",
                followups=[],
                ends_scene=True,
            ),

            # ——— Rumeurs sur les PJ (nouveau-nés) ———

            Choice(
                id="pj_brujah",
                label="PJ Brujah",
                answer_md="""
<div style="margin:0.8rem 0 1.2rem 0; padding:1rem 1.2rem; border:1px solid rgba(255,255,255,0.18); border-radius:16px; background:linear-gradient(145deg, rgba(255,255,255,0.05), rgba(0,0,0,0.25)); box-shadow:0 8px 24px rgba(0,0,0,0.35);">
  <div style="font-size:0.75rem; letter-spacing:0.12em; text-transform:uppercase; opacity:0.75;">✦ Registre : identité consignée ✦</div>
  <div style="margin-top:0.6rem; line-height:1.45;">
    <b>Clan</b> : Brujah &nbsp;•&nbsp; <b>Âge</b> : Nouveau-né &nbsp;•&nbsp; <b>Génération</b> : 9e<br/>
    <b>Rôle</b> : — &nbsp;•&nbsp; <b>Coterie</b> : Les Héritiers d'Alexandrie<br/>
    <b>Sire</b> : Gwilherm
  </div>
</div>

Le murmure est teinté d’une ironie délicate.

> « Il parle de libre arbitre.  
> De justice.  
> De défendre ceux que l’Elysium oublie. »

Un sourire bref.

> « C’est admirable.  
> Surtout chez quelqu’un qu’il faut parfois sortir  
> des mains des mortels comme un enfant pris en faute. »

La voix se fait plus basse.

> « Pourtant, on dit aussi qu’il a tenu.  
> Face à ce qui aurait dû le rompre.  
> Trop fort pour être simplement imprudent.  
> Trop visible pour être simplement innocent. »

Certains idéaux sont offerts comme des cadeaux.  
Et les cadeaux, parfois, portent une chaîne invisible.
""",
                followups=[],
                ends_scene=True,
            ),

            Choice(
                id="pj_ventrue",
                label="PJ Ventrue",
                answer_md="""
<div style="margin:0.8rem 0 1.2rem 0; padding:1rem 1.2rem; border:1px solid rgba(255,255,255,0.18); border-radius:16px; background:linear-gradient(145deg, rgba(255,255,255,0.05), rgba(0,0,0,0.25)); box-shadow:0 8px 24px rgba(0,0,0,0.35);">
  <div style="font-size:0.75rem; letter-spacing:0.12em; text-transform:uppercase; opacity:0.75;">✦ Registre : identité consignée ✦</div>
  <div style="margin-top:0.6rem; line-height:1.45;">
    <b>Clan</b> : Ventrue &nbsp;•&nbsp; <b>Âge</b> : Nouveau-né &nbsp;•&nbsp; <b>Génération</b> : 10e<br/>
    <b>Rôle</b> : — &nbsp;•&nbsp; <b>Coterie</b> : Les Gardiens du Sacré<br/>
    <b>Sire</b> : Odon
  </div>
</div>

La confidence prend un parfum de stratégie.

> « Celui-là n’a pas été étreint pour errer.  
> On l’a préparé. Formé. Placé. »

Un temps.

> « Et pourtant, même les pièces bien placées  
> se retrouvent parfois sur de mauvaises cases. »

Un sourire contrôlé.

> « On raconte qu’il a été interrogé par des hommes du duché.  
> Humiliant, sans doute.  
> Mais instructif.  
> Il est revenu. Propre. Vivant. Couvert par plus grand que lui. »

À l’Elysium, la propreté est rarement innocente.
""",
                followups=[],
                ends_scene=True,
            ),

            Choice(
                id="pj_tremere",
                label="PJ Tremere",
                answer_md="""
<div style="margin:0.8rem 0 1.2rem 0; padding:1rem 1.2rem; border:1px solid rgba(255,255,255,0.18); border-radius:16px; background:linear-gradient(145deg, rgba(255,255,255,0.05), rgba(0,0,0,0.25)); box-shadow:0 8px 24px rgba(0,0,0,0.35);">
  <div style="font-size:0.75rem; letter-spacing:0.12em; text-transform:uppercase; opacity:0.75;">✦ Registre : identité consignée ✦</div>
  <div style="margin-top:0.6rem; line-height:1.45;">
    <b>Clan</b> : Trémère &nbsp;•&nbsp; <b>Âge</b> : Nouveau-né &nbsp;•&nbsp; <b>Génération</b> : 8e<br/>
    <b>Rôle</b> : — &nbsp;•&nbsp; <b>Coterie</b> : La Fondation<br/>
    <b>Sire</b> : Simon
  </div>
</div>

La confidence se fait plus feutrée.

> « On raconte qu’il n’a pas été étreint par nécessité…  
> mais pour renforcer la position politique de son clan. »

Un silence.

> « La vraie question n’est pas pourquoi il est là.  
> Mais au détriment de qui. »

On murmure que son sire est ambitieux —  
pour lui, le savoir est un pouvoir.  
Et le pouvoir… une fin en soi.

Certains observent cette expansion avec prudence.  
Reste à savoir si les rivalités s’exploiteront…  
ou si elles s’effaceront, le temps d’en contenir les velléités.
""",
                followups=[],
                ends_scene=True,
            ),

            Choice(
                id="pj_toreador",
                label="PJ Toréador",
                answer_md="""
<div style="margin:0.8rem 0 1.2rem 0; padding:1rem 1.2rem; border:1px solid rgba(255,255,255,0.18); border-radius:16px; background:linear-gradient(145deg, rgba(255,255,255,0.05), rgba(0,0,0,0.25)); box-shadow:0 8px 24px rgba(0,0,0,0.35);">
  <div style="font-size:0.75rem; letter-spacing:0.12em; text-transform:uppercase; opacity:0.75;">✦ Registre : identité consignée ✦</div>
  <div style="margin-top:0.6rem; line-height:1.45;">
    <b>Clan</b> : Toréador &nbsp;•&nbsp; <b>Âge</b> : Nouveau-née &nbsp;•&nbsp; <b>Génération</b> : 9e<br/>
    <b>Rôle</b> : — &nbsp;•&nbsp; <b>Coterie</b> : La Main du Prince<br/>
    <b>Sire</b> : Aliénor de Dinan
  </div>
</div>

Le murmure sonne presque tendre, mais l’intention est claire.

> « Elle a vécu dans les jupons de sa sire,  
> à l’abri des conflits, dans une cage dorée.  
> Le velours n’adoucit pas les barreaux. »

Un sourire.

> « On dit qu’elle tremble quand les lames parlent.  
> Mais qu’elle sait encore rappeler aux autres  
> quand il faut se taire, mentir, sourire  
> et laisser la ville croire ce qu’elle doit croire. »

Un silence plus fin.

> « Fragile, oui.  
> Inutile, non.  
> Et cela rend son cas beaucoup plus intéressant. »

À Rennes, la liberté se négocie souvent au pas de quelqu’un d’autre.
""",
                followups=[],
                ends_scene=True,
            ),
        ],
    )