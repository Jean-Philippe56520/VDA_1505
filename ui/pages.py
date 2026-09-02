from __future__ import annotations

from pathlib import Path
from typing import Dict, Tuple

import streamlit as st

from domain.engine import SceneValidationError, RunState, can_undo_choice, validate_scene
from ui.actions import go_home, pick, restart_scene, resume_scene, start_scene, undo_choice
from ui.components import (
    card_close,
    card_open,
    header,
    primary_button,
    seal_choice,
    secondary_button,
    section,
    section_label,
)
from ui.hunt_tool_v2 import render_hunt_generator_tool
from ui.state import get_state


HUNT_TOOL_SCENE_ID = "generateur_de_chasse"


def _clear_hunt_runtime_state() -> None:
    """Efface uniquement l'état Streamlit du générateur de chasse."""
    for key in list(st.session_state.keys()):
        if str(key).startswith("hunt_"):
            del st.session_state[key]


def page_home(scenes: Dict[str, Tuple[str, object]]) -> None:
    header("Accueil MJ", "Choisis une scène, puis laisse le joueur lire et répondre.")
    state = get_state()

    if state.last_error:
        section("Erreur", state.last_error, fade=True)

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
            validate_scene(scene)
            invalid_error = None
        except SceneValidationError as exc:
            invalid_error = str(exc)

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
            if scene_id == HUNT_TOOL_SCENE_ID:
                _clear_hunt_runtime_state()
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
    """Resolve an optional MP3 for a scene from assets/audio/."""
    root = Path(__file__).resolve().parents[1]
    audio_dir = root / "assets" / "audio"

    candidates: list[Path] = [audio_dir / f"{scene_id}.mp3"]
    if len(scene_id) >= 3 and scene_id[0] == "s" and scene_id[1:3].isdigit():
        candidates.append(audio_dir / f"{scene_id[:3]}.mp3")

    for path in candidates:
        if path.exists():
            return path
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
            st.button(
                "← Choix précédent",
                disabled=True,
                use_container_width=True,
                key="nav_undo_disabled",
            )

    with col_restart:
        if secondary_button("Recommencer", key="nav_restart"):
            if scene_id == HUNT_TOOL_SCENE_ID:
                _clear_hunt_runtime_state()
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

    _render_scene_navigation(str(scene_id), scene, rs)

    music_path = _resolve_scene_music_path(str(scene_id))
    if music_path:
        st.audio(music_path.read_bytes(), format="audio/mpeg", loop=True)

    _render_transcript(rs)

    if str(scene_id) == HUNT_TOOL_SCENE_ID:
        render_hunt_generator_tool()
        return

    if rs.ended:
        card_open(fade=True)
        section_label("Fin de scène")
        st.markdown("La scène est terminée.")
        st.caption(
            "Tu peux revenir au choix précédent avec la barre MJ ci-dessus, ou retourner à l'accueil sans perdre cette scène."
        )
        if primary_button("Retour Accueil MJ", key="end_scene"):
            go_home()
            st.rerun()
        card_close()
        return

    card_open()
    section_label("Choix")
    st.markdown("Choisis une réponse :")
    card_close()

    for index, choice in enumerate(rs.active_choices, start=1):
        if seal_choice(choice.label, key=f"ch_{choice.id}", index=index):
            pick(choice.id)
            st.rerun()
