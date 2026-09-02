from __future__ import annotations

import random
import uuid
from datetime import datetime

import streamlit as st

from data.hunt_history import is_draw_played, load_played_hunts, played_count_for_encounter, record_played_hunt
from data.hunt_overrides import (
    DANGER,
    DEFAULT_CONTEXT,
    DEFAULT_PREDATOR,
    OPERATIONAL_LABELS,
    OPERATIONAL_POINTS,
    PREDATOR_LABELS,
    SPECIAL_POINTS,
    TABLE_NOTES,
    style_status,
)
from data.hunt_runtime import (
    HUNT_BASE_DIFFICULTY,
    LOCAL_HUNT_TABLE_DEFAULT_CONTEXT,
    LOCAL_HUNT_TABLE_DEFAULT_PREDATOR,
    LOCAL_HUNT_TABLE_NOTES,
    PREDATOR_TYPES,
)
from data.hunt_saint_germain import SAINT_GERMAIN_HUNT_TABLE
from data.hunt_tables import HUNT_TABLES as BASE_HUNT_TABLES
from data.territory_runtime import COTERIE_DOMAINS, HUNT_ZONES, coterie_label
from ui import hunt_tool as legacy
from ui.components import card_close, card_open, section_label


OTHER_TERRITORY = legacy.OTHER_TERRITORY
HUNT_TABLES = {**BASE_HUNT_TABLES, "executeurs_front_saint_germain": SAINT_GERMAIN_HUNT_TABLE}
NOTES = {**LOCAL_HUNT_TABLE_NOTES, **TABLE_NOTES}
DEFAULT_PREDATORS = {**LOCAL_HUNT_TABLE_DEFAULT_PREDATOR, **DEFAULT_PREDATOR}
DEFAULT_CONTEXTS = {**LOCAL_HUNT_TABLE_DEFAULT_CONTEXT, **DEFAULT_CONTEXT}

# Traduction d'affichage seulement : les IDs techniques restent inchangés.
for _style_id, _label in PREDATOR_LABELS.items():
    if _style_id in PREDATOR_TYPES:
        PREDATOR_TYPES[_style_id]["label"] = _label


def _points_registry() -> dict[str, dict]:
    points: dict[str, dict] = {}
    for zone_id, zone in HUNT_ZONES.items():
        for point in zone["points"]:
            points[point["id"]] = {**point, "zone_id": zone_id, "zone_label": zone["label"]}
    for point_id, point in SPECIAL_POINTS.items():
        points[point_id] = dict(point)
    return points


def _territory_ids(points: dict[str, dict]) -> list[str]:
    controlled = {p.get("controller_ref") for p in points.values() if p.get("controller_ref")}
    controlled.update(OPERATIONAL_POINTS)
    return [OTHER_TERRITORY, *[cid for cid in COTERIE_DOMAINS if cid in controlled]]


def _territory_label(territory_id: str) -> str:
    if territory_id == OTHER_TERRITORY:
        return "Autre secteur / aucun domaine reconnu"
    return OPERATIONAL_LABELS.get(territory_id, COTERIE_DOMAINS[territory_id]["label"])


def _point_ids_for_territory(territory_id: str, points: dict[str, dict]) -> list[str]:
    if territory_id == OTHER_TERRITORY:
        return [pid for pid, p in points.items() if not p.get("controller_ref")]
    operational = OPERATIONAL_POINTS.get(territory_id, set())
    return [pid for pid, p in points.items() if p.get("controller_ref") == territory_id or pid in operational]


def _point_label(point_id: str, points: dict[str, dict]) -> str:
    p = points[point_id]
    return f"{p['label']} — {p.get('zone_label', 'Rennes')}"


def _predator_label(style_id: str) -> str:
    return PREDATOR_TYPES[style_id]["label"]


def _default_index(options: list[str], default: str | None) -> int:
    return options.index(default) if default in options else 0


def _memo(territory_id: str, point: dict, style_id: str) -> tuple[str, bool]:
    status = style_status(point["id"], style_id)
    parts = [f"Base diff. {HUNT_BASE_DIFFICULTY}"]
    controller = point.get("controller_ref")

    if territory_id == OTHER_TERRITORY:
        parts.append(f"Contrôle : {coterie_label(controller)}" if controller else "Hors domaine reconnu")
    elif controller == territory_id:
        totals = COTERIE_DOMAINS[territory_id]["totals"]
        parts.extend([f"Territoire : {COTERIE_DOMAINS[territory_id]['label']}", f"Viandis {totals['viandis']}"])
    elif point["id"] in OPERATIONAL_POINTS.get(territory_id, set()):
        parts.extend([f"Front opérationnel : {COTERIE_DOMAINS[territory_id]['label']} — hors domaine", "Viandis 0 via ce périmètre"])
    else:
        parts.append(f"Présence : {COTERIE_DOMAINS[territory_id]['label']} — sans contrôle du point")

    if status == "impossible":
        parts.append("CHASSE IMPOSSIBLE")
    elif status == "inadapte":
        parts.append(f"{_predator_label(style_id)} inadapté : +2 difficulté")
    else:
        parts.append(f"{_predator_label(style_id)} : normal")

    zone = HUNT_ZONES.get(str(point.get("zone_id")), {})
    zone_mod = int(zone.get("difficulty_modifier", 0) or 0)
    if zone_mod:
        parts.append(f"{zone.get('difficulty_origin', 'Circonstance territoriale')} : +{zone_mod} difficulté")

    danger = DANGER.get(point["id"])
    if danger:
        parts.append(f"Danger actuel : {danger[0]}")
    return " · ".join(parts), status == "impossible"


def _eligible_entries(table_id: str, point_id: str) -> list[dict]:
    entries = HUNT_TABLES[table_id]["entries"]
    if not any(entry.get("points") for entry in entries):
        return list(entries)
    return [entry for entry in entries if point_id in entry.get("points", [])]


def _pick_entry(table_id: str, cfg: dict) -> dict:
    point_id = cfg["point_id"]
    base = {
        "table_id": table_id,
        "point_id": point_id,
        "style_id": cfg["style_id"],
        "territory_id": cfg["territory_id"],
        "draw_id": uuid.uuid4().hex,
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
    }
    if style_status(point_id, cfg["style_id"]) == "impossible":
        return {**base, "entry": None, "index": None, "eligible_total": 0, "blocked": "Chasse impossible sur ce point."}
    entries = _eligible_entries(table_id, point_id)
    if not entries:
        return {**base, "entry": None, "index": None, "eligible_total": 0, "blocked": "Aucune rencontre préparée pour ce point."}
    index = random.randrange(len(entries))
    return {**base, "entry": entries[index], "index": index, "eligible_total": len(entries)}


def _embedded_enrichment(entry: dict) -> str:
    if not entry.get("importance"):
        return ""
    warning = ""
    if entry.get("importance") == "majeure":
        warning = "<div style='margin-top:8px'><b>Crochet d’arc</b> : le jet ouvre ou complique la piste ; il ne résout jamais l’arc.</div>"
    return f"""
    <div style='margin-top:12px'><b>Enrichissement MJ — {legacy._escaped(entry.get('importance'))}</b></div>
    {legacy._optional_line('Nom / désignation', entry.get('nom'))}
    {legacy._optional_line('Identité / rôle', entry.get('identite'))}
    {legacy._optional_line('Description', entry.get('description'))}
    {legacy._optional_line('Ouverture', entry.get('ouverture'))}
    {legacy._optional_line('Conséquence contextuelle potentielle', entry.get('consequence_contextuelle'))}
    {legacy._optional_line('Piste / question', entry.get('crochet'))}
    {warning}
    {legacy._optional_line('Réussite normale — complément', entry.get('supplement_reussite'))}
    {legacy._optional_line('Échec normal — complément', entry.get('supplement_echec'))}
    """


def _render_result(table_id: str, result: dict, point: dict) -> None:
    entry = result.get("entry")
    if entry is None:
        st.warning(result.get("blocked") or "Aucune rencontre compatible.")
        return
    memo, impossible = _memo(result["territory_id"], point, result["style_id"])
    enrichment = _embedded_enrichment(entry) or legacy._enrichment_html(table_id, entry)
    enrichment = "".join(line.strip() for line in enrichment.splitlines())
    idx = result.get("index")
    total = result.get("eligible_total") or len(HUNT_TABLES[table_id]["entries"])
    content = f"""
    <div><b>{legacy._escaped(HUNT_TABLES[table_id]['label'])}</b></div>
    <div style='margin-top:4px'>{legacy._escaped(point['label'])} · {legacy._escaped(point.get('zone_label', 'Rennes'))}</div>
    <div style='margin-top:4px'><b>Style</b> : {legacy._escaped(_predator_label(result['style_id']))}</div>
    <div style='margin-top:4px'><b>Mémo</b> : {legacy._escaped(memo)}</div>
    <div style='margin-top:6px'><b>Tirage compatible avec ce point</b> : {legacy._escaped(f'{idx + 1}/{total}' if idx is not None else '—')}</div>
    <div style='margin-top:8px'><b>Rencontre</b> : {legacy._escaped(entry.get('rencontre'))}</div>
    <div style='margin-top:8px'><b>Résonance / Tempérament — seulement si nourrissage applicable et chasse réussie</b> : {legacy._escaped(entry.get('res_temp'))}</div>
    <div style='margin-top:6px'><b>Effet sanguin / nourrissage — seulement si applicable et chasse réussie</b> : {legacy._escaped(entry.get('effet'))}</div>
    {enrichment}
    <div style='margin-top:10px'><b>Issues préparées</b></div>
    <div style='margin-top:4px'><b>Victoire critique</b> : {legacy._escaped(entry.get('victoire_critique'))}</div>
    <div style='margin-top:4px'><b>Victoire à la Pyrrhus</b> : {legacy._escaped(entry.get('victoire_pyrrhus'))}</div>
    <div style='margin-top:4px'><b>Réussite bestiale</b> : {legacy._escaped(entry.get('reussite_bestiale'))}</div>
    <div style='margin-top:4px'><b>Échec bestial</b> : {legacy._escaped(entry.get('echec_bestial'))}</div>
    """
    role = "Narrateur — chasse impossible" if impossible else "Narrateur — préparation MJ"
    st.markdown(f'<div class="chat"><div class="bubble bot fade-in"><div class="role">{role}</div><div class="content">{content}</div></div></div>', unsafe_allow_html=True)
    danger = DANGER.get(point["id"])
    if danger:
        st.caption(f"Danger actuel — {danger[0]} : {danger[1]} Ce niveau n'ajoute pas automatiquement de difficulté.")


def _played_record(table_id: str, result: dict, point: dict) -> dict:
    entry = result["entry"]
    return {
        "draw_id": result["draw_id"],
        "generated_at": result.get("generated_at"),
        "played_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "table_id": table_id,
        "table_label": HUNT_TABLES[table_id]["label"],
        "point_id": point["id"],
        "point_label": point["label"],
        "zone_label": point.get("zone_label", "Rennes"),
        "territory_id": result["territory_id"],
        "territory_label": _territory_label(result["territory_id"]),
        "style_id": result["style_id"],
        "style_label": _predator_label(result["style_id"]),
        "rencontre": entry.get("rencontre"),
        "entry_id": entry.get("id"),
        "importance": entry.get("importance"),
    }


def _render_history(history: list[dict]) -> None:
    with st.expander(f"Historique local — scènes de chasse marquées jouées ({len(history)})", expanded=False):
        if not history:
            st.caption("Aucune scène de chasse enregistrée comme jouée sur cette installation.")
            return
        st.caption("Journal local de repérage. Il ne remplace pas 04A et ne déduit aucune conséquence canonique.")
        for item in reversed(history[-30:]):
            st.markdown(
                f"**{item.get('table_label', 'Chasse')}** — {item.get('point_label', '—')} — {item.get('style_label', '—')}  \n"
                f"{item.get('rencontre', '—')}  \n*Jouée : {item.get('played_at', 'date inconnue')}*"
            )


def render_hunt_generator_tool() -> None:
    points = _points_registry()
    territory_ids = _territory_ids(points)
    table_ids = list(HUNT_TABLES)
    history = load_played_hunts()

    card_open(fade=False)
    section_label("Chasses express")
    st.caption("Chaque chasse garde son périmètre, son point d'intérêt et son style de prédation.")

    configs: dict[str, dict] = {}
    for table_id in table_ids:
        default_style = DEFAULT_PREDATORS.get(table_id, next(iter(PREDATOR_TYPES)))
        default_territory, default_point = DEFAULT_CONTEXTS.get(table_id, (OTHER_TERRITORY, next(iter(points))))
        cols = st.columns([1.5, 1.6, 2.4, 3.2])
        with cols[0]:
            active = st.checkbox(HUNT_TABLES[table_id]["label"], key=f"hunt_active_{table_id}")
        with cols[1]:
            styles = list(PREDATOR_TYPES)
            style_id = st.selectbox("Style de prédation", styles, index=_default_index(styles, default_style), format_func=_predator_label, key=f"hunt_style_{table_id}", label_visibility="collapsed")
        with cols[2]:
            territory_id = st.selectbox("Territoire / périmètre", territory_ids, index=_default_index(territory_ids, default_territory), format_func=_territory_label, key=f"hunt_territory_{table_id}", label_visibility="collapsed")
        point_ids = _point_ids_for_territory(territory_id, points) or list(points)
        point_key = f"hunt_point_{table_id}"
        if point_key in st.session_state and st.session_state[point_key] not in point_ids:
            del st.session_state[point_key]
        with cols[3]:
            point_id = st.selectbox("Point d'intérêt", point_ids, index=_default_index(point_ids, default_point), format_func=lambda value, p=points: _point_label(value, p), key=point_key, label_visibility="collapsed")
        memo, impossible = _memo(territory_id, points[point_id], style_id)
        eligible = len(_eligible_entries(table_id, point_id))
        if active:
            if impossible:
                st.error(f"{HUNT_TABLES[table_id]['label']} — {memo}")
            elif not eligible:
                st.warning(f"{HUNT_TABLES[table_id]['label']} — aucune rencontre préparée pour ce point.")
            else:
                st.caption(f"{HUNT_TABLES[table_id]['label']} — {memo} · {eligible} rencontre(s) compatible(s)")
        configs[table_id] = {"active": active, "style_id": style_id, "territory_id": territory_id, "point_id": point_id}

    selected = [tid for tid, cfg in configs.items() if cfg["active"]]
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Générer / relancer les chasses sélectionnées", use_container_width=True, key="hunt_generate_selected", disabled=not selected):
            results = dict(st.session_state.get("hunt_results", {}))
            for table_id in selected:
                results[table_id] = _pick_entry(table_id, configs[table_id])
            st.session_state["hunt_results"] = results
    with c2:
        if st.button("Effacer tous les tirages", use_container_width=True, key="hunt_clear_all"):
            st.session_state["hunt_results"] = {}
    st.caption("Jet physique à la table. Une conséquence contextuelle peut exister sans nourrissage ; « Aucune » résonance n'accorde aucun bonus automatique.")
    card_close()

    with st.expander("Mémo — difficulté, lieux et danger", expanded=False):
        st.markdown("**Style inadapté : +2 difficulté.** La matrice stable tient notamment compte des lieux nobles, bourgeois, religieux, institutionnels et sécurisés : une approche violente ou coercitive y est souvent moins adaptée.")
        st.markdown("**Danger actuel ≠ difficulté automatique.** À Saint-Germain, Surveillé / Tendu / Hostile / Très hostile / Mortel calibre surtout les complications et les bascules en scène.")
        st.markdown("**Front des Exécuteurs :** leurs deux portes et Saint-Germain sont un périmètre opérationnel ; cela ne crée ni domaine ni Viandis supplémentaire.")
        st.markdown("Le **périmètre interdit de la lisière** reste une chasse impossible.")

    _render_history(history)
    results = dict(st.session_state.get("hunt_results", {}))
    visible = [tid for tid in selected if tid in results]
    if not visible:
        return

    card_open(fade=False)
    section_label("Rencontres générées")
    st.caption("Non cochée : la scène n'est pas enregistrée. Cochée « Jouée » : le tirage et son contexte sont mémorisés localement pour les prochaines sessions. L'issue exacte reste à consolider séparément dans 04A.")
    card_close()

    for table_id in visible:
        result = results[table_id]
        c1, c2 = st.columns([3, 1])
        with c1:
            if st.button(f"Relancer — {HUNT_TABLES[table_id]['label']}", use_container_width=True, key=f"hunt_reroll_{table_id}"):
                results[table_id] = _pick_entry(table_id, configs[table_id])
                st.session_state["hunt_results"] = results
                result = results[table_id]
        with c2:
            if st.button("Effacer", use_container_width=True, key=f"hunt_clear_{table_id}"):
                results.pop(table_id, None)
                st.session_state["hunt_results"] = results
        if table_id not in results:
            continue

        result = results[table_id]
        point = points[result["point_id"]]
        _render_result(table_id, result, point)
        entry = result.get("entry")
        if entry:
            already = is_draw_played(history, result.get("draw_id"))
            prior = played_count_for_encounter(history, table_id, point["id"], str(entry.get("rencontre") or ""))
            if prior:
                st.info(f"Cette rencontre a déjà été enregistrée comme jouée {prior} fois sur ce point.")
            key = f"hunt_played_{result['draw_id']}"
            if already:
                st.checkbox("Jouée — scène déjà enregistrée", value=True, disabled=True, key=key)
            elif st.checkbox("Jouée — enregistrer durablement cette scène", key=key, help="Si la case reste vide, aucun historique durable n'est écrit."):
                if record_played_hunt(_played_record(table_id, result, point)):
                    st.success("Scène enregistrée comme jouée. Elle sera reconnue aux prochains lancements.")
                    st.rerun()
        st.caption(NOTES.get(table_id, "Table narrative locale."))
