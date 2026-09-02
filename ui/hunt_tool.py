from __future__ import annotations

import html
import random

import streamlit as st

from data.hunt_runtime import (
    HUNT_BASE_DIFFICULTY,
    HUNT_DIFFICULTY_OPTIONS,
    LOCAL_HUNT_TABLE_NOTES,
    PREDATOR_TYPES,
)
from data.hunt_tables import HUNT_TABLES
from data.territory_runtime import (
    COTERIE_DOMAINS,
    HUNT_ZONES,
    coterie_label,
    effective_viandis_for_hunt,
)
from ui.components import card_close, card_open, section_label


NONE_COTERIE = "__none__"
NONE_TABLE = "__none__"


def _style_format(style_id: str) -> str:
    return PREDATOR_TYPES[style_id]["label"]


def _zone_format(zone_id: str) -> str:
    return HUNT_ZONES[zone_id]["label"]


def _point_format(point_id: str, points_by_id: dict[str, dict]) -> str:
    return points_by_id[point_id]["label"]


def _coterie_format(coterie_id: str) -> str:
    if coterie_id == NONE_COTERIE:
        return "Aucune coterie / aucun Viandis mobilisé"
    return COTERIE_DOMAINS[coterie_id]["label"]


def _table_format(table_id: str) -> str:
    if table_id == NONE_TABLE:
        return "Aucune table narrative"
    return HUNT_TABLES[table_id]["label"]


def _escaped(value: object) -> str:
    return html.escape(str(value or "—")).replace("\n", "<br>")


def _pick_entry(table_id: str) -> dict:
    entries = HUNT_TABLES[table_id]["entries"]
    if not entries:
        return {"table_id": table_id, "index": None, "entry": None}
    index = random.randrange(len(entries))
    return {"table_id": table_id, "index": index, "entry": entries[index]}


def _render_calculation(
    *,
    coterie_id: str,
    habitual_style: str,
    used_style: str,
    zone_id: str,
    point: dict,
    options: dict[str, bool],
) -> tuple[int, int, list[str], list[str]]:
    coterie_ref = None if coterie_id == NONE_COTERIE else coterie_id
    viandis = effective_viandis_for_hunt(coterie_ref, point)

    dice_lines: list[str] = []
    if viandis:
        dice_lines.append(
            f"Viandis effectif de {coterie_label(coterie_ref)} : +{viandis} dé{'s' if viandis > 1 else ''}"
        )
    else:
        point_controller = point.get("controller_ref")
        if coterie_ref and point_controller and point_controller != coterie_ref:
            dice_lines.append(
                f"Point contrôlé par {coterie_label(point_controller)} : aucun Viandis de {coterie_label(coterie_ref)} appliqué"
            )
        elif coterie_ref:
            dice_lines.append("Aucun Viandis de la coterie applicable à ce point")
        else:
            dice_lines.append("Aucun Viandis de coterie appliqué")

    difficulty = HUNT_BASE_DIFFICULTY
    difficulty_lines = [f"Difficulté de base : {HUNT_BASE_DIFFICULTY}"]

    zone = HUNT_ZONES[zone_id]
    zone_mod = int(zone.get("difficulty_modifier", 0) or 0)
    if zone_mod:
        difficulty += zone_mod
        origin = zone.get("difficulty_origin", "circonstance territoriale")
        difficulty_lines.append(f"{origin} : +{zone_mod}")

    if habitual_style != used_style:
        label, modifier = HUNT_DIFFICULTY_OPTIONS["different_style"]
        difficulty += modifier
        difficulty_lines.append(f"{label} : +{modifier}")

    option_keys = (
        "strong_resonance",
        "balance_resonance",
        "known_target",
        "cautious",
        "inappropriate_point",
    )
    for option_key in option_keys:
        if options.get(option_key):
            label, modifier = HUNT_DIFFICULTY_OPTIONS[option_key]
            difficulty += modifier
            difficulty_lines.append(f"{label} : +{modifier}")

    return viandis, difficulty, dice_lines, difficulty_lines


def _render_encounter(table_id: str) -> None:
    if table_id == NONE_TABLE:
        st.session_state.pop("hunt_result", None)
        st.info("Aucune table narrative sélectionnée. Le calcul mécanique peut être utilisé seul.")
        return

    current = st.session_state.get("hunt_result")
    if current and current.get("table_id") != table_id:
        st.session_state.pop("hunt_result", None)
        current = None

    col_draw, col_clear = st.columns(2)
    with col_draw:
        button_label = "Relancer la rencontre" if current else "Tirer une rencontre"
        if st.button(button_label, use_container_width=True, key="hunt_draw"):
            st.session_state["hunt_result"] = _pick_entry(table_id)
            current = st.session_state["hunt_result"]
    with col_clear:
        if st.button("Effacer le tirage", use_container_width=True, key="hunt_clear_draw"):
            st.session_state.pop("hunt_result", None)
            current = None

    st.caption(LOCAL_HUNT_TABLE_NOTES.get(table_id, "Table narrative locale."))
    st.warning(
        "Un tirage est une proposition de préparation MJ. Il ne devient ni scène jouée, ni fait canonique, ni connaissance PJ par sa seule apparition dans l'application."
    )

    if not current:
        return

    entry = current.get("entry")
    if entry is None:
        st.info("Cette table ne contient aucune rencontre.")
        return

    index = current.get("index")
    total = len(HUNT_TABLES[table_id]["entries"])
    content_html = f"""
    <div><b>{_escaped(HUNT_TABLES[table_id]['label'])}</b></div>
    <div style='margin-top:6px'><b>Tirage</b> : {_escaped(f'{index + 1}/{total}' if index is not None else '—')}</div>
    <div style='margin-top:6px'><b>Rencontre</b> : {_escaped(entry.get('rencontre'))}</div>
    <div style='margin-top:6px'><b>Résonance / Tempérament</b> : {_escaped(entry.get('res_temp'))}</div>
    <div style='margin-top:6px'><b>Effet spécial</b> : {_escaped(entry.get('effet'))}</div>
    <div style='margin-top:8px'><b>Issues préparées</b></div>
    <div style='margin-top:4px'><b>Victoire critique</b> : {_escaped(entry.get('victoire_critique'))}</div>
    <div style='margin-top:4px'><b>Victoire à la Pyrrhus</b> : {_escaped(entry.get('victoire_pyrrhus'))}</div>
    <div style='margin-top:4px'><b>Réussite bestiale</b> : {_escaped(entry.get('reussite_bestiale'))}</div>
    <div style='margin-top:4px'><b>Échec bestial</b> : {_escaped(entry.get('echec_bestial'))}</div>
    """
    st.markdown(
        f"""
        <div class="chat">
          <div class="bubble bot fade-in">
            <div class="role">Narrateur — préparation MJ</div>
            <div class="content">{content_html}</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_hunt_generator_tool() -> None:
    """Assistant de chasse dérivé du canon, sans lancer les dés ni écrire le canon."""

    card_open(fade=False)
    section_label("1. Chasseur et style")

    coterie_ids = [NONE_COTERIE, *COTERIE_DOMAINS.keys()]
    coterie_id = st.selectbox(
        "Coterie bénéficiant du domaine",
        coterie_ids,
        format_func=_coterie_format,
        key="hunt_coterie",
    )

    style_ids = list(PREDATOR_TYPES.keys())
    col_habitual, col_used = st.columns(2)
    with col_habitual:
        habitual_style = st.selectbox(
            "Predator Type habituel",
            style_ids,
            format_func=_style_format,
            key="hunt_habitual_style",
        )
    with col_used:
        used_style = st.selectbox(
            "Style utilisé cette chasse",
            style_ids,
            format_func=_style_format,
            key="hunt_used_style",
        )

    used_meta = PREDATOR_TYPES[used_style]
    st.caption(f"Adaptation 1505 : {used_meta['medieval_reading']} — source : {used_meta['source']}.")
    if habitual_style != used_style:
        st.info("Style ponctuellement différent du style habituel : le canon local courant applique +1 difficulté.")
    card_close()

    card_open(fade=False)
    section_label("2. Zone et point d'intérêt canonique")

    zone_ids = list(HUNT_ZONES.keys())
    zone_id = st.selectbox("Zone / secteur", zone_ids, format_func=_zone_format, key="hunt_zone")
    zone = HUNT_ZONES[zone_id]
    points = zone["points"]
    points_by_id = {point["id"]: point for point in points}
    point_ids = list(points_by_id.keys())
    point_id = st.selectbox(
        "Point d'intérêt",
        point_ids,
        format_func=lambda value: _point_format(value, points_by_id),
        key="hunt_point",
    )
    point = points_by_id[point_id]

    controller_ref = point.get("controller_ref")
    st.caption(f"Contrôle courant du point : {coterie_label(controller_ref)}.")
    if point_id == "zone_lisiere_bois_saint_germain":
        st.warning(
            "La lisière contient notamment le Caern sacré. Le Caern lui-même est interdit à la chasse et au nourrissage ; cette entrée ne vaut jamais autorisation d'y entrer."
        )
    card_close()

    card_open(fade=False)
    section_label("3. Circonstances de chasse")
    st.caption(
        "La matrice complète Predator Type × point d'intérêt n'est pas encore validée. Le MJ indique donc manuellement si le style est inadapté ; ce choix applique toujours +2 difficulté."
    )

    options = {
        "strong_resonance": st.checkbox("Résonance puissante (+2 difficulté)", key="hunt_opt_strong_resonance"),
        "balance_resonance": st.checkbox("Chercher une résonance différente (+1 difficulté)", key="hunt_opt_balance_resonance"),
        "known_target": st.checkbox("Cibler un mortel connu (+1 difficulté)", key="hunt_opt_known_target"),
        "cautious": st.checkbox("Chasse prudente (+1 difficulté)", key="hunt_opt_cautious"),
        "inappropriate_point": st.checkbox(
            "Style inadapté à ce point d'intérêt (+2 difficulté)", key="hunt_opt_inappropriate_point"
        ),
    }
    card_close()

    viandis, difficulty, dice_lines, difficulty_lines = _render_calculation(
        coterie_id=coterie_id,
        habitual_style=habitual_style,
        used_style=used_style,
        zone_id=zone_id,
        point=point,
        options=options,
    )

    card_open(fade=False)
    section_label("4. Calcul à appliquer au jet physique")
    st.markdown(f"### Réserve : pool du style utilisé **+ {viandis} dé(s)**")
    st.markdown(f"### Difficulté finale : **{difficulty}**")

    st.markdown("**Modificateurs de dés**")
    for line in dice_lines:
        st.markdown(f"- {line}")

    st.markdown("**Modificateurs de difficulté**")
    for line in difficulty_lines:
        st.markdown(f"- {line}")

    st.caption(
        "L'application ne lance pas le jet et ne décide pas de son résultat. Les dés restent joués physiquement à la table."
    )
    card_close()

    card_open(fade=False)
    section_label("5. Rencontre narrative locale — optionnelle")
    table_ids = [NONE_TABLE, *HUNT_TABLES.keys()]
    table_id = st.selectbox(
        "Table de rencontre",
        table_ids,
        format_func=_table_format,
        key="hunt_local_table",
    )
    _render_encounter(table_id)
    card_close()

    card_open(fade=False)
    section_label("6. Note MJ")
    coterie_ref = None if coterie_id == NONE_COTERIE else coterie_id
    note_lines = [
        f"Coterie : {coterie_label(coterie_ref)}",
        f"Style habituel : {PREDATOR_TYPES[habitual_style]['label']}",
        f"Style utilisé : {PREDATOR_TYPES[used_style]['label']}",
        f"Zone : {zone['label']}",
        f"Point d'intérêt : {point['label']}",
        f"Viandis appliqué : +{viandis} dé(s)",
        f"Difficulté finale : {difficulty}",
    ]
    current = st.session_state.get("hunt_result")
    if current and current.get("table_id") == table_id and current.get("entry"):
        note_lines.append(f"Rencontre préparée : {current['entry'].get('rencontre', '—')}")
    st.code("\n".join(note_lines), language=None)
    st.caption("Cette note est un aide-mémoire. Elle n'écrit rien dans 04A et ne prouve pas que la chasse a été jouée.")
    card_close()
