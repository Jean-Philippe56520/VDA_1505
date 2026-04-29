from __future__ import annotations

from pathlib import Path

import streamlit as st

# Thème unique : texture parchemin (par défaut)
from domain.themes.gothic_texture import DARK_AGE_CSS


BG_B64_PATH = Path("assets/bg_base64.txt")
BG_MIME = "image/png"


def _apply_background_from_base64() -> None:
    """Applique le fond parchemin (image base64)

    - Conserve ton parchemin existant (bg_base64.txt)
    - Ajoute un voile sombre pour la lisibilité
    """
    if not BG_B64_PATH.exists():
        return

    b64 = BG_B64_PATH.read_text(encoding="utf-8").strip()
    if not b64:
        return

    css = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
      background-image: url("data:{BG_MIME};base64,{b64}") !important;
      background-size: cover !important;
      background-position: center top !important;
      background-attachment: fixed !important;
    }}

    /* Voile sombre : ajustable si tu veux plus/moins de parchemin */
    [data-testid="stAppViewContainer"]::after {{
      content:"";
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.48);
      pointer-events: none;
      z-index: 0;
    }}

    [data-testid="stMain"],
    [data-testid="stMainBlockContainer"] {{
      position: relative;
      z-index: 1;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


def apply_theme() -> None:
    """Thème unique + fond parchemin."""
    st.markdown(DARK_AGE_CSS, unsafe_allow_html=True)
    _apply_background_from_base64()


def card_open(*, fade: bool = False) -> None:
    cls = "kiosk-card fade-in" if fade else "kiosk-card"
    st.markdown(f'<div class="{cls}">', unsafe_allow_html=True)


def card_close() -> None:
    st.markdown("</div>", unsafe_allow_html=True)


def header(title: str, subtitle: str) -> None:
    card_open()
    st.markdown(f'<h2 class="kiosk-title">{title}</h2>', unsafe_allow_html=True)
    st.markdown(f'<div class="kiosk-sub">{subtitle}</div>', unsafe_allow_html=True)
    card_close()


def section_label(text: str) -> None:
    st.markdown(f'<div class="smallcaps">{text}</div>', unsafe_allow_html=True)


def section(title: str, body_md: str, *, fade: bool = False) -> None:
    card_open(fade=fade)
    section_label(title)
    st.markdown(body_md)
    card_close()


def primary_button(label: str, *, key: str, full: bool = True) -> bool:
    return st.button(label, type="primary", use_container_width=full, key=key)


def secondary_button(label: str, *, key: str, full: bool = True) -> bool:
    return st.button(label, type="secondary", use_container_width=full, key=key)


def seal_choice(label: str, *, key: str, index: int) -> bool:
    col_med, col_btn = st.columns([1, 10], vertical_alignment="center")
    with col_med:
        st.markdown(f'<div class="seal-medallion">{index}</div>', unsafe_allow_html=True)
    with col_btn:
        return st.button(label, type="primary", use_container_width=True, key=key)