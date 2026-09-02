from __future__ import annotations

from domain.schema import Choice, Scene
from data.territory_runtime import COTERIE_DOMAINS


ECHELLE_STATS = """
<div style="margin:0.8rem 0 1.2rem 0; padding:1rem 1.2rem; border:1px solid rgba(255,255,255,0.16); border-radius:14px; background:rgba(0,0,0,0.24); line-height:1.5;">
  <b>Lecture des indicateurs</b><br/>
  0 ou 1 = contrôle faible ; 2 ou 3 = contrôle partiel ; 4 ou 5 = contrôle fort.<br/><br/>
  Les valeurs affichées sont les <b>scores effectifs courants</b> de Viandis, Servage et Rempart : potentiels contrôlés, bonus de contrôle, portes, tributs et autres modificateurs chiffrés sont déjà intégrés.<br/>
  Chaque gain, coût ou tribut est détaillé séparément afin de conserver son origine.
</div>
"""


COTERIE_ORDER = [
    "cot_main_prince",
    "cot_gardiens_sacre",
    "cot_fondation_pierre_noire",
    "cot_heritiers_alexandrie",
    "cot_crocs_silencieux",
    "cot_executeurs",
    "cot_fracture",
]


def _list_html(items: list[tuple[str, str]]) -> str:
    if not items:
        return "<p><i>Aucun modificateur courant supplémentaire.</i></p>"
    rows = "".join(f"<li><b>{label}</b> : {value}</li>" for label, value in items)
    return f"<ul>{rows}</ul>"


def _fiche_coterie(coterie_ref: str) -> str:
    data = COTERIE_DOMAINS[coterie_ref]
    totals = data["totals"]
    components_html = _list_html(data.get("components", []))
    modifiers_html = _list_html(data.get("modifiers", []))

    return f"""
<div style="margin:0.8rem 0 1.2rem 0; padding:1rem 1.2rem; border:1px solid rgba(255,255,255,0.18); border-radius:16px; background:linear-gradient(145deg, rgba(255,255,255,0.05), rgba(0,0,0,0.25)); box-shadow:0 8px 24px rgba(0,0,0,0.35);">
  <div style="font-size:0.75rem; letter-spacing:0.12em; text-transform:uppercase; opacity:0.75;">Registre territorial courant</div>
  <div style="margin-top:0.6rem; line-height:1.5;">
    <b>Coterie</b> : {data['label']}<br/>
    <b>Faction</b> : {data['faction']}<br/>
    <b>Type</b> : {data['type']}<br/>
    <b>Domaine / charge</b> : {data['domain']}
  </div>
</div>

<div style="margin:1rem 0; padding:1rem 1.2rem; border:1px solid rgba(255,255,255,0.16); border-radius:14px; background:rgba(0,0,0,0.28); line-height:1.55;">
  <b>Scores effectifs courants</b><br/>
  <span style="font-size:1.08rem;">Viandis {totals['viandis']} / Servage {totals['servage']} / Rempart {totals['rempart']}</span>
</div>

<div style="margin:1rem 0; padding:1rem 1.2rem; border:1px solid rgba(255,255,255,0.14); border-radius:14px; background:rgba(255,255,255,0.035); line-height:1.55;">
  <b>Assise territoriale</b>
  {components_html}
</div>

<div style="margin:1rem 0; padding:1rem 1.2rem; border:1px solid rgba(255,255,255,0.14); border-radius:14px; background:rgba(255,255,255,0.035); line-height:1.55;">
  <b>Tributs, investissements et modificateurs</b>
  {modifiers_html}
</div>

<div style="margin:1rem 0 0.4rem 0; padding:1rem 1.2rem; border-left:4px solid rgba(180,35,35,0.85); border-radius:12px; background:rgba(120,15,15,0.18); line-height:1.55;">
  <b>Lecture stratégique</b><br/>
  {data['summary']}
</div>
"""


def get_scene() -> Scene:
    choices: list[Choice] = []
    for coterie_ref in COTERIE_ORDER:
        data = COTERIE_DOMAINS[coterie_ref]
        choices.append(
            Choice(
                id=f"coterie_{coterie_ref}",
                label=data["label"],
                answer_md=_fiche_coterie(coterie_ref),
                followups=[],
                ends_scene=True,
            )
        )

    return Scene(
        id="coteries_rennes_1505",
        title="Registre stratégique — Coteries de Rennes 1505",
        intro_md=f"""
Ce registre est une vue opérationnelle dérivée du canon territorial du Drive.

Il affiche les **scores effectifs courants**, et non d'anciens totaux de base : les tributs, investissements et modificateurs actifs sont déjà répercutés dans les valeurs finales. Chaque effet reste néanmoins visible avec son origine afin d'éviter les doubles comptes.

{ECHELLE_STATS}

Quelle coterie souhaites-tu consulter ?
""",
        choices=choices,
    )
