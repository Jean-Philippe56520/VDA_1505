from __future__ import annotations

from pathlib import Path
from typing import Dict, Tuple

import streamlit as st

from domain.engine import validate_scene, SceneValidationError, RunState, can_undo_choice
from ui.components import (
    header,
    section,
    card_open,
    card_close,
    section_label,
    primary_button,
    secondary_button,
    seal_choice,
)
from ui.actions import start_scene, restart_scene, resume_scene, undo_choice, pick, go_home
from ui.state import get_state


HUNT_TOOL_SCENE_ID = "generateur_de_chasse"


def _safe_df(data: dict, index: list[str]):
    """Build a DataFrame if pandas is available, else return a simple dict."""
    try:
        import pandas as pd  # type: ignore

        return pd.DataFrame(data, index=index)
    except Exception:
        # Fallback: Streamlit can render dict-like objects too.
        return {"index": index, **data}


def _render_hunt_generator_tool() -> None:
    """UI spécifique pour la scène-outil de génération de chasse."""
    from data.hunt_tables import HUNT_TABLES

    ROWS = [
        "Jet",
        "Rencontre",
        "Résonnance / Tempérament",
        "Effet spécial",
        "Victoire critique",
        "Victoire à la Pyrrhus",
        "Réussite bestiale",
        "Échec bestial",
    ]

    def pick_entry(style_id: str) -> dict:
        entries = HUNT_TABLES[style_id]["entries"]
        n = len(entries)
        if n == 0:
            return {"jet": "—", "entry": None, "n": 0, "k": None}
        k = __import__("random").randrange(n)
        return {"jet": f"{k+1}/{n}", "entry": entries[k], "n": n, "k": k}

    # State
    if "hunt_selected" not in st.session_state:
        st.session_state["hunt_selected"] = []
    if "hunt_results" not in st.session_state:
        st.session_state["hunt_results"] = {}

    card_open(fade=False)
    section_label("Styles")
    st.caption("Coche les styles à générer (1 colonne par style).")

    selected: list[str] = []
    # stable ordering by label
    for sid, meta in sorted(HUNT_TABLES.items(), key=lambda kv: kv[1]["label"].lower()):
        if st.checkbox(meta["label"], key=f"hunt_style_{sid}"):
            selected.append(sid)

    st.session_state["hunt_selected"] = selected

    # --- AUTO-GÉNÉRATION ---
    # - cocher un style => génère automatiquement un tirage
    # - décocher => oublie le tirage
    changed = False

    # Supprime les styles décochés
    for sid in list(st.session_state["hunt_results"].keys()):
        if sid not in selected:
            del st.session_state["hunt_results"][sid]
            changed = True

    # Génère pour les styles nouvellement cochés
    for sid in selected:
        if sid not in st.session_state["hunt_results"]:
            st.session_state["hunt_results"][sid] = pick_entry(sid)
            changed = True

    card_close()

    # Si l'état a changé, on relance le rendu pour afficher immédiatement.
    if changed:
        st.rerun()

    if not selected:
        section("Résultats", "Aucun style sélectionné.", fade=True)
        return

    # Build result matrix (rows=info, cols=styles)
    data: dict[str, list[str]] = {}
    for sid in selected:
        label = HUNT_TABLES[sid]["label"]
        r = st.session_state["hunt_results"].get(sid)
        if not r:
            col = ["—"] * len(ROWS)
        elif r["entry"] is None:
            col = [
                "—",
                "Table vide (aucune rencontre définie)",
                "—",
                "—",
                "—",
                "—",
                "—",
                "—",
            ]
        else:
            e = r["entry"]
            col = [
                r["jet"],
                e.get("rencontre", "—"),
                e.get("res_temp", "—"),
                e.get("effet", "—"),
                e.get("victoire_critique", "—"),
                e.get("victoire_pyrrhus", "—"),
                e.get("reussite_bestiale", "—"),
                e.get("echec_bestial", "—"),
            ]
        data[label] = col

    card_open(fade=False)
    section_label("Résultats (format conversation)")
    st.caption("Chaque bulle correspond à 1 style sélectionné. (Pas de tableau type Excel.)")

    st.markdown('<div class="chat">', unsafe_allow_html=True)

    def _fmt_value(v: str) -> str:
        v = (v or "—").strip()
        # Préserve les retours à la ligne dans nos bulles HTML.
        return v.replace("\n", "<br>")

    for sid in selected:
        label = HUNT_TABLES[sid]["label"]
        r = st.session_state["hunt_results"].get(sid)
        if not r:
            jet = "—"
            rencontre = "—"
            res_temp = "—"
            effet = "—"
            vc = "—"
            py = "—"
            rb = "—"
            eb = "—"
        elif r["entry"] is None:
            jet = "—"
            rencontre = "Table vide (aucune rencontre définie)"
            res_temp = "—"
            effet = "—"
            vc = "—"
            py = "—"
            rb = "—"
            eb = "—"
        else:
            e = r["entry"]
            jet = r["jet"]
            rencontre = e.get("rencontre", "—")
            res_temp = e.get("res_temp", "—")
            effet = e.get("effet", "—")
            vc = e.get("victoire_critique", "—")
            py = e.get("victoire_pyrrhus", "—")
            rb = e.get("reussite_bestiale", "—")
            eb = e.get("echec_bestial", "—")

        content_html = f"""
        <div><b>{label}</b></div>
        <div style='margin-top:6px'><b>Jet</b> : {_fmt_value(jet)}</div>
        <div style='margin-top:6px'><b>Rencontre</b> : {_fmt_value(rencontre)}</div>
        <div style='margin-top:6px'><b>Résonnance / Tempérament</b> : {_fmt_value(res_temp)}</div>
        <div style='margin-top:6px'><b>Effet spécial</b> : {_fmt_value(effet)}</div>
        <div style='margin-top:8px'><b>Variantes</b></div>
        <div style='margin-top:4px'><b>Victoire critique</b> : {_fmt_value(vc)}</div>
        <div style='margin-top:4px'><b>Victoire à la Pyrrhus</b> : {_fmt_value(py)}</div>
        <div style='margin-top:4px'><b>Réussite bestiale</b> : {_fmt_value(rb)}</div>
        <div style='margin-top:4px'><b>Échec bestial</b> : {_fmt_value(eb)}</div>
        """

        st.markdown(
            f"""
            <div class="bubble bot fade-in">
              <div class="role">Narrateur</div>
              <div class="content">{content_html}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)
    card_close()


def page_home(scenes: Dict[str, Tuple[str, object]]) -> None:
    header("Accueil MJ", "Choisis une scène, puis laisse le joueur lire et répondre.")
    state = get_state()

    if state.last_error:
        section("Erreur", state.last_error, fade=True)

    # Une scene quittee via "Accueil MJ" reste disponible ici.
    if state.active_scene_id and state.run_state is not None:
        suspended_entry = scenes.get(state.active_scene_id)
        suspended_scene = suspended_entry[1] if suspended_entry else None
        suspended_title = getattr(suspended_scene, "title", state.active_scene_id)

        card_open(fade=True)
        section_label("Scène suspendue")
        st.markdown(f"### {suspended_title}")
        st.caption("La conversation et les choix sont conservés.")
        if primary_button(f"Reprendre : {suspended_title}", key="resume_active_scene"):
            resume_scene()
            st.rerun()
        card_close()

    items = []
    for scene_id, (module_name, scene) in scenes.items():
        title = getattr(scene, "title", scene_id)
        items.append((title, scene_id, module_name, scene))
    items.sort(key=lambda x: x[0].lower())

    for title, scene_id, module_name, scene in items:
        try:
            _warnings = validate_scene(scene)  # on garde la validation, mais on n'affiche plus les warnings
            invalid_error = None
        except SceneValidationError as e:
            invalid_error = str(e)

        card_open()
        st.markdown(f"### {title}")
        st.caption(f"ID: {scene_id}")

        if invalid_error:
            st.error(f"Scène invalide ({module_name}) : {invalid_error}")
            card_close()
            continue

        if state.active_scene_id and state.run_state is not None:
            if scene_id == state.active_scene_id:
                launch_label = f"Recommencer : {title}"
            else:
                launch_label = f"Lancer : {title} (remplace la scène suspendue)"
        else:
            launch_label = f"Lancer : {title}"

        if primary_button(launch_label, key=f"start_{scene_id}"):
            start_scene(scene_id, scene)
            st.rerun()

        card_close()


def _render_transcript(rs: RunState) -> None:
    card_open(fade=False)
    section_label("Conversation")
    st.markdown('<div class="chat">', unsafe_allow_html=True)

    for role, md in rs.transcript:
        cls = "pj" if role == "PJ" else "bot"
        st.markdown(
            f"""
            <div class="bubble {cls} fade-in">
              <div class="role">{role}</div>
              <div class="content">{md}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)
    card_close()


def _resolve_scene_music_path(scene_id: str) -> Path | None:
    """
    Ultra simple :
    - Mets les MP3 dans : vda_kiosk/assets/audio/
    - Nom conseillé : {scene_id}.mp3
    - Fallback auto : si scene_id commence par 'sNN_' alors essaie aussi 'sNN.mp3'
      ex: s00_assignation -> s00.mp3
    """
    root = Path(__file__).resolve().parents[1]  # -> dossier vda_kiosk/
    audio_dir = root / "assets" / "audio"

    candidates: list[Path] = [audio_dir / f"{scene_id}.mp3"]

    # Fallback: "s00_assignation" -> aussi "s00.mp3"
    if len(scene_id) >= 3 and scene_id[0] == "s" and scene_id[1:3].isdigit():
        candidates.append(audio_dir / f"{scene_id[:3]}.mp3")

    for p in candidates:
        if p.exists():
            return p

    return None


def _render_scene_navigation(scene_id: str, scene: object, rs: RunState) -> None:
    """Navigation MJ persistante, sans transformer un clic en événement canonique."""
    card_open(fade=False)
    section_label("Navigation MJ")
    col_home, col_back, col_restart = st.columns(3)

    with col_home:
        if secondary_button("← Accueil MJ", key="nav_home"):
            go_home()
            st.rerun()

    with col_back:
        if can_undo_choice(rs):
            if secondary_button("← Choix précédent", key="nav_undo"):
                undo_choice()
                st.rerun()
        else:
            st.button("← Choix précédent", disabled=True, use_container_width=True, key="nav_undo_disabled")

    with col_restart:
        if secondary_button("Recommencer", key="nav_restart"):
            if scene_id == HUNT_TOOL_SCENE_ID:
                st.session_state.pop("hunt_selected", None)
                st.session_state.pop("hunt_results", None)
                # Les checkbox Streamlit ont leurs propres clés.
                for key in list(st.session_state.keys()):
                    if str(key).startswith("hunt_style_"):
                        del st.session_state[key]
            restart_scene(scene_id, scene)
            st.rerun()

    st.caption("Accueil conserve la scène. Recommencer la remet explicitement à zéro.")
    card_close()


def page_scene(scene: object) -> None:
    state = get_state()
    rs: RunState | None = state.run_state

    scene_id = getattr(scene, "id", None) or state.active_scene_id or "scene"
    title = getattr(scene, "title", "Scène")
    header(title, "Lis et réponds. Le fil reste visible comme une conversation.")

    if rs is None:
        section("Erreur", "RunState manquant. Retour à l'accueil.", fade=True)
        if primary_button("Retour accueil", key="back_home"):
            go_home()
            st.rerun()
        return

    # Navigation toujours visible avant le contenu joueur.
    _render_scene_navigation(str(scene_id), scene, rs)

    # Musique auto par scène (sans config dans les fichiers de scène)
    music_path = _resolve_scene_music_path(str(scene_id))
    if music_path:
        st.audio(music_path.read_bytes(), format="audio/mpeg", loop=True)

    _render_transcript(rs)

    # Scène-outil : rendu spécifique (pas de "Choix")
    if str(scene_id) == HUNT_TOOL_SCENE_ID:
        _render_hunt_generator_tool()
        return

    if rs.ended:
        card_open(fade=True)
        section_label("Fin de scène")
        st.markdown("La scène est terminée.")
        st.caption("Tu peux revenir au choix précédent avec la barre MJ ci-dessus, ou retourner à l'accueil sans perdre cette scène.")
        if primary_button("Retour Accueil MJ", key="end_scene"):
            go_home()
            st.rerun()
        card_close()
        return

    card_open()
    section_label("Choix")
    st.markdown("Choisis une réponse :")
    card_close()

    for i, ch in enumerate(rs.active_choices, start=1):
        if seal_choice(ch.label, key=f"ch_{ch.id}", index=i):
            pick(ch.id)
            st.rerun()
