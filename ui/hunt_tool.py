from __future__ import annotations

import html
import random

import streamlit as st

from data.hunt_enrichment import find_hunt_enrichment
from data.hunt_names import find_hunt_prepared_name
from data.hunt_runtime import (
    HUNT_BASE_DIFFICULTY,
    HUNT_DIFFICULTY_OPTIONS,
    HUNT_SPECIAL_POINTS,
    LOCAL_HUNT_TABLE_DEFAULT_CONTEXT,
    LOCAL_HUNT_TABLE_DEFAULT_PREDATOR,
    LOCAL_HUNT_TABLE_NOTES,
    PREDATOR_TYPES,
    hunt_point_style_status,
)
from data.hunt_tables import HUNT_TABLES
from data.territory_runtime import COTERIE_DOMAINS, HUNT_ZONES, coterie_label
from ui.components import card_close, card_open, section_label


OTHER_TERRITORY = "__other__"


def _escaped(value: object) -> str:
    return html.escape(str(value or "—")).replace("\n", "<br>")


def _pick_entry(table_id: str) -> dict:
    entries = HUNT_TABLES[table_id]["entries"]
    if not entries:
        return {"table_id": table_id, "index": None, "entry": None}
    index = random.randrange(len(entries))
    return {"table_id": table_id, "index": index, "entry": entries[index]}


def _points_registry() -> dict[str, dict]:
    registry: dict[str, dict] = {}
    for zone_id, zone in HUNT_ZONES.items():
        for point in zone["points"]:
            registry[point["id"]] = {
                **point,
                "zone_id": zone_id,
                "zone_label": zone["label"],
            }
    for point_id, point in HUNT_SPECIAL_POINTS.items():
        registry[point_id] = dict(point)
    return registry


def _territory_ids(points: dict[str, dict]) -> list[str]:
    controlled = {point.get("controller_ref") for point in points.values() if point.get("controller_ref")}
    return [OTHER_TERRITORY, *[cid for cid in COTERIE_DOMAINS if cid in controlled]]


def _territory_label(territory_id: str) -> str:
    if territory_id == OTHER_TERRITORY:
        return "Autre secteur / aucun domaine reconnu"
    return COTERIE_DOMAINS[territory_id]["label"]


def _point_ids_for_territory(territory_id: str, points: dict[str, dict]) -> list[str]:
    if territory_id == OTHER_TERRITORY:
        return [pid for pid, point in points.items() if not point.get("controller_ref")]
    return [pid for pid, point in points.items() if point.get("controller_ref") == territory_id]


def _point_label(point_id: str, points: dict[str, dict]) -> str:
    point = points[point_id]
    return f"{point['label']} — {point.get('zone_label', 'Rennes')}"


def _predator_label(style_id: str) -> str:
    return PREDATOR_TYPES[style_id]["label"]


def _default_index(options: list[str], default: str | None) -> int:
    if default in options:
        return options.index(default)
    return 0


def _territory_memo(territory_id: str, point: dict, style_id: str) -> tuple[str, bool]:
    status = hunt_point_style_status(point["id"], style_id)
    parts: list[str] = [f"Base diff. {HUNT_BASE_DIFFICULTY}"]

    if territory_id == OTHER_TERRITORY:
        controller = point.get("controller_ref")
        parts.append(f"Contrôle : {coterie_label(controller)}" if controller else "Hors domaine reconnu")
    else:
        totals = COTERIE_DOMAINS[territory_id]["totals"]
        parts.append(f"Territoire : {COTERIE_DOMAINS[territory_id]['label']}")
        parts.append(f"Viandis {totals['viandis']}")

    if status == "impossible":
        parts.append("CHASSE IMPOSSIBLE")
        return " · ".join(parts), True

    if status == "inadapte":
        parts.append(f"{PREDATOR_TYPES[style_id]['label']} inadapté : +2 difficulté")
    else:
        parts.append(f"{PREDATOR_TYPES[style_id]['label']} : normal")

    zone_id = point.get("zone_id")
    zone = HUNT_ZONES.get(str(zone_id), {})
    zone_mod = int(zone.get("difficulty_modifier", 0) or 0)
    if zone_mod:
        parts.append(f"{zone.get('difficulty_origin', 'Circonstance territoriale')} : +{zone_mod} difficulté")

    return " · ".join(parts), False


def _optional_line(label: str, value: str | None, margin: int = 4) -> str:
    if not value:
        return ""
    return f"<div style='margin-top:{margin}px'><b>{_escaped(label)}</b> : {_escaped(value)}</div>"


def _enrichment_html(table_id: str, entry: dict) -> str:
    rencontre = entry.get("rencontre")
    enrichment = find_hunt_enrichment(table_id, rencontre)
    if enrichment is None:
        return ""

    prepared_name = find_hunt_prepared_name(table_id, rencontre)
    importance = enrichment["importance"]
    major_warning = ""
    if importance == "majeure":
        major_warning = (
            "<div style='margin-top:8px'><b>Crochet d’arc</b> : "
            "ce jet détermine l’accès, l’indice ou la complication initiale ; "
            "il ne résout jamais l’arc.</div>"
        )

    supplements = "".join(
        [
            _optional_line("Réussite normale — complément", enrichment["supplement_reussite"]),
            _optional_line("Échec normal — complément", enrichment["supplement_echec"]),
            _optional_line("Victoire critique — complément", enrichment["supplement_critique"]),
            _optional_line("Victoire à la Pyrrhus — complément", enrichment["supplement_pyrrhus"]),
            _optional_line("Réussite bestiale — complément", enrichment["supplement_reussite_bestiale"]),
            _optional_line("Échec bestial — complément", enrichment["supplement_echec_bestial"]),
        ]
    )

    return f"""
    <div style='margin-top:12px'><b>Enrichissement MJ — {_escaped(importance)}</b></div>
    {_optional_line('Nom de circonstance — préparation non canonique', prepared_name)}
    {_optional_line('Identité / rôle exploitable', enrichment['identite'])}
    {_optional_line('Description minimale', enrichment['description'])}
    {_optional_line('Ouverture d’action / dialogue', enrichment['ouverture'])}
    {_optional_line('Conséquence contextuelle potentielle', enrichment['consequence_contextuelle'])}
    {_optional_line('Piste / question ouverte', enrichment['crochet'])}
    {major_warning}
    <div style='margin-top:8px'><b>Compléments contextuels par issue</b></div>
    {supplements}
    """


def _render_result_bubble(table_id: str, result: dict, point: dict, territory_id: str, style_id: str) -> None:
    entry = result.get("entry")
    if entry is None:
        st.info("Cette table ne contient aucune rencontre.")
        return

    index = result.get("index")
    total = len(HUNT_TABLES[table_id]["entries"])
    memo, impossible = _territory_memo(territory_id, point, style_id)
    enrichment_html = _enrichment_html(table_id, entry)

    content_html = f"""
    <div><b>{_escaped(HUNT_TABLES[table_id]['label'])}</b></div>
    <div style='margin-top:4px'>{_escaped(point['label'])} · {_escaped(point.get('zone_label', 'Rennes'))}</div>
    <div style='margin-top:4px'><b>Mémo</b> : {_escaped(memo)}</div>
    <div style='margin-top:6px'><b>Tirage</b> : {_escaped(f'{index + 1}/{total}' if index is not None else '—')}</div>
    <div style='margin-top:8px'><b>Rencontre</b> : {_escaped(entry.get('rencontre'))}</div>
    <div style='margin-top:8px'><b>Résonance / Tempérament — seulement si nourrissage applicable et chasse réussie</b> : {_escaped(entry.get('res_temp'))}</div>
    <div style='margin-top:6px'><b>Effet sanguin / de nourrissage — seulement si applicable et chasse réussie</b> : {_escaped(entry.get('effet'))}</div>
    {enrichment_html}
    <div style='margin-top:10px'><b>Issues préparées de la table</b></div>
    <div style='margin-top:4px'><b>Victoire critique</b> : {_escaped(entry.get('victoire_critique'))}</div>
    <div style='margin-top:4px'><b>Victoire à la Pyrrhus</b> : {_escaped(entry.get('victoire_pyrrhus'))}</div>
    <div style='margin-top:4px'><b>Réussite bestiale</b> : {_escaped(entry.get('reussite_bestiale'))}</div>
    <div style='margin-top:4px'><b>Échec bestial</b> : {_escaped(entry.get('echec_bestial'))}</div>
    """

    role = "Narrateur — chasse impossible" if impossible else "Narrateur — préparation MJ"
    st.markdown(
        f"""
        <div class="chat">
          <div class="bubble bot fade-in">
            <div class="role">{role}</div>
            <div class="content">{content_html}</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_hunt_generator_tool() -> None:
    """Générateur express multi-chasses ; les jets et décisions restent physiques."""

    points = _points_registry()
    territory_ids = _territory_ids(points)
    table_ids = list(HUNT_TABLES.keys())

    card_open(fade=False)
    section_label("Chasses express")
    st.caption(
        "Sélectionne directement les tables à tirer. Chaque chasse garde son propre territoire, point d'intérêt et style utilisé."
    )

    configurations: dict[str, dict] = {}
    for table_id in table_ids:
        default_style = LOCAL_HUNT_TABLE_DEFAULT_PREDATOR.get(table_id, next(iter(PREDATOR_TYPES)))
        default_territory, default_point = LOCAL_HUNT_TABLE_DEFAULT_CONTEXT.get(
            table_id, (OTHER_TERRITORY, next(iter(points)))
        )

        cols = st.columns([1.5, 1.6, 2.2, 3.2])
        with cols[0]:
            active = st.checkbox(HUNT_TABLES[table_id]["label"], key=f"hunt_active_{table_id}")

        with cols[1]:
            style_key = f"hunt_style_{table_id}"
            style_ids = list(PREDATOR_TYPES.keys())
            style_id = st.selectbox(
                "Style",
                style_ids,
                index=_default_index(style_ids, default_style),
                format_func=_predator_label,
                key=style_key,
                label_visibility="collapsed",
            )

        with cols[2]:
            territory_key = f"hunt_territory_{table_id}"
            territory_id = st.selectbox(
                "Territoire de chasse",
                territory_ids,
                index=_default_index(territory_ids, default_territory),
                format_func=_territory_label,
                key=territory_key,
                label_visibility="collapsed",
            )

        point_ids = _point_ids_for_territory(territory_id, points)
        if not point_ids:
            point_ids = list(points.keys())

        point_key = f"hunt_point_{table_id}"
        if point_key in st.session_state and st.session_state[point_key] not in point_ids:
            del st.session_state[point_key]

        with cols[3]:
            point_id = st.selectbox(
                "Point d'intérêt",
                point_ids,
                index=_default_index(point_ids, default_point),
                format_func=lambda value, p=points: _point_label(value, p),
                key=point_key,
                label_visibility="collapsed",
            )

        memo, impossible = _territory_memo(territory_id, points[point_id], style_id)
        if active:
            if impossible:
                st.error(f"{HUNT_TABLES[table_id]['label']} — {memo}")
            else:
                st.caption(f"{HUNT_TABLES[table_id]['label']} — {memo}")

        configurations[table_id] = {
            "active": active,
            "style_id": style_id,
            "territory_id": territory_id,
            "point_id": point_id,
        }

    selected = [table_id for table_id, cfg in configurations.items() if cfg["active"]]
    col_generate, col_clear = st.columns(2)
    with col_generate:
        if st.button(
            "Générer / relancer les chasses sélectionnées",
            use_container_width=True,
            key="hunt_generate_selected",
            disabled=not selected,
        ):
            results = dict(st.session_state.get("hunt_results", {}))
            for table_id in selected:
                results[table_id] = _pick_entry(table_id)
            st.session_state["hunt_results"] = results

    with col_clear:
        if st.button("Effacer tous les tirages", use_container_width=True, key="hunt_clear_all"):
            st.session_state["hunt_results"] = {}

    st.caption(
        "Jet physique : le critique prime. Succès = difficulté → Pyrrhus ; succès > difficulté → réussite. "
        "Résonance et bénéfices sanguins ne sont acquis que si le nourrissage est applicable et la chasse réussie. "
        "Une conséquence contextuelle peut exister sans nourrissage ; « Aucune » résonance n'accorde jamais un bonus automatique."
    )
    card_close()

    with st.expander("Mémo — options de chasse", expanded=False):
        st.markdown(
            "Résonance puissante **+2 difficulté** · autre résonance **+1** · cible connue **+1** · "
            "chasse prudente **+1** · style ponctuellement différent **+1 difficulté** (canon courant)."
        )
        st.markdown(
            "**Viandis : +1 dé par point effectif mobilisable par le chasseur.** Le score affiché dans la ligne "
            "est celui du territoire choisi ; il n'est pas automatiquement accordé à un chasseur étranger."
        )
        st.markdown(
            "**Récompenses contextuelles :** +1 dé vise normalement un prochain jet étroitement lié ; "
            "une opportunité RP peut donner **-1 difficulté** au prochain projet pertinent d'Historique, usage unique. "
            "Volonté, Souillure/Humanité et autres monnaies sensibles restent des effets rares explicitement préparés."
        )
        st.markdown(
            "Un style déclaré inadapté au point ajoute automatiquement **+2 difficulté**. Le Caern est un interdit absolu."
        )

    results = dict(st.session_state.get("hunt_results", {}))
    visible_results = [table_id for table_id in selected if table_id in results]
    if not visible_results:
        return

    card_open(fade=False)
    section_label("Rencontres générées")
    st.caption(
        "Chaque bulle reste indépendante. Les enrichissements sont des aides MJ : ils ne deviennent joués, acquis ou connus qu'après la scène physique."
    )
    card_close()

    for table_id in visible_results:
        cfg = configurations[table_id]
        point = points[cfg["point_id"]]

        col_reroll, col_clear_one = st.columns([3, 1])
        with col_reroll:
            if st.button(
                f"Relancer — {HUNT_TABLES[table_id]['label']}",
                use_container_width=True,
                key=f"hunt_reroll_{table_id}",
            ):
                results[table_id] = _pick_entry(table_id)
                st.session_state["hunt_results"] = results
        with col_clear_one:
            if st.button("Effacer", use_container_width=True, key=f"hunt_clear_{table_id}"):
                results.pop(table_id, None)
                st.session_state["hunt_results"] = results

        if table_id not in results:
            continue

        _render_result_bubble(
            table_id,
            results[table_id],
            point,
            cfg["territory_id"],
            cfg["style_id"],
        )
        st.caption(LOCAL_HUNT_TABLE_NOTES.get(table_id, "Table narrative locale."))
