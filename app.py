from __future__ import annotations

import streamlit as st

from repositories.runtime import (
    close_campaign_session,
    current_campaign_session,
    flush_pending_remote,
    start_campaign_session,
)
from services import runtime as runtime_service
from ui.components import apply_theme
from ui.data import get_scene_by_id, get_scenes_cached
from ui.state import Screen, get_state, set_state
from ui.pages import page_home, page_private_scenes, page_scene
from ui.actions import go_home

APP_TITLE = "Vampire: Dark Ages — Secret Kiosk"


def _runtime_sidebar() -> None:
    """Operational session controls. They never write to the canonical Drive."""
    with st.sidebar:
        st.caption("Runtime de table")
        session = current_campaign_session()
        if session:
            st.success(f"Séance ouverte — {session.get('title', 'Séance VDA')}")
            st.caption(f"ID : {session.get('id')}")
            state = get_state()
            active_run = bool(
                state.active_scene_id
                and state.run_state is not None
                and not getattr(state.run_state, "ended", False)
            )
            if active_run:
                st.caption("Termine ou abandonne la scène active avant de clore la séance runtime.")
            if st.button(
                "Clore la séance runtime",
                use_container_width=True,
                disabled=active_run,
            ):
                close_campaign_session(app_version=runtime_service.APP_VERSION)
                st.rerun()
        else:
            st.caption("Aucune séance runtime ouverte.")
            if st.button("Ouvrir une séance runtime", use_container_width=True):
                start_campaign_session(app_version=runtime_service.APP_VERSION)
                st.rerun()

        if st.button("Synchroniser les écritures hors ligne", use_container_width=True):
            result = flush_pending_remote()
            if result["remaining"]:
                st.warning(
                    f"{result['remaining']} écriture(s) restent locales. "
                    "La partie peut continuer hors ligne."
                )
            else:
                st.success(f"Synchronisation terminée ({result['synced']} écriture(s)).")

        st.caption(
            "Journal technique uniquement : affichage, clic ou fin de scène ne vaut jamais canon ni 04A sans validation MJ."
        )


def _record_rendered_scene_content() -> None:
    """Record BOT transcript content only after Streamlit actually rendered it."""
    state = get_state()
    rs = state.run_state
    if rs is None or not state.active_scene_id or not state.active_scene_run_id:
        return

    transcript = list(getattr(rs, "transcript", []) or [])
    start = min(max(int(getattr(state, "runtime_logged_transcript_count", 0)), 0), len(transcript))
    logged_through = start
    for index in range(start, len(transcript)):
        role, md = transcript[index]
        if role == "PJ" or not str(md or "").strip():
            logged_through = index + 1
            continue
        try:
            runtime_service.scene_content_shown(
                run_id=state.active_scene_run_id,
                scene_id=state.active_scene_id,
                transcript_index=index,
                content_md=str(md),
            )
        except Exception:
            # Keep the failed index pending so a later rerun can retry it.
            break
        logged_through = index + 1

    state.runtime_logged_transcript_count = logged_through
    set_state(state)


def main() -> None:
    st.set_page_config(page_title=APP_TITLE, layout="centered")

    apply_theme()
    _runtime_sidebar()

    # Replaying a small offline queue is best-effort and must never block UI.
    try:
        flush_pending_remote()
    except Exception:
        pass

    scenes = get_scenes_cached()
    if not scenes:
        st.error(
            "Aucune scène trouvée dans le backend configuré ni dans le fallback local "
            "(/scenes et /scenes_private)."
        )
        return

    state = get_state()

    if state.screen == Screen.HOME:
        page_home(scenes)
        return

    if state.screen == Screen.PRIVATE_SCENES:
        page_private_scenes(scenes)
        return

    # Screen.SCENE
    scene = get_scene_by_id(scenes, state.active_scene_id)
    if scene is None:
        st.error("Scène introuvable. Retour à l'accueil.")
        go_home()
        st.rerun()
        return

    page_scene(scene)
    _record_rendered_scene_content()


if __name__ == "__main__":
    main()
