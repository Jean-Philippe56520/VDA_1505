from __future__ import annotations

import os
from functools import lru_cache
from typing import Any


def _truthy(value: str | None, default: bool = False) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def get_setting(name: str) -> str | None:
    """Read server configuration from environment, then Streamlit secrets."""
    value = os.environ.get(name)
    if value:
        return value.strip()

    try:
        import streamlit as st

        if name in st.secrets:
            secret = str(st.secrets[name]).strip()
            return secret or None
    except Exception:
        # Streamlit can be absent in scripts/tests, and secrets can be unavailable
        # before the app runtime is initialised.
        return None
    return None


def supabase_enabled() -> bool:
    explicit = get_setting("VDA_SUPABASE_ENABLED")
    if explicit is not None:
        return _truthy(explicit)
    return bool(get_setting("SUPABASE_URL") and get_setting("SUPABASE_SECRET_KEY"))


@lru_cache(maxsize=1)
def get_supabase_client() -> Any | None:
    """Return the server-side Supabase client when configured.

    The app deliberately uses a server-side secret key for the V1 runtime.
    That key must only live in deployment secrets/environment variables and
    must never be committed to Git or exposed to player-side code.
    """
    if not supabase_enabled():
        return None

    url = get_setting("SUPABASE_URL")
    key = get_setting("SUPABASE_SECRET_KEY")
    if not url or not key:
        return None

    try:
        from supabase import Client, create_client
    except ImportError:
        return None

    client: Client = create_client(url, key)
    return client


def reset_supabase_client_cache() -> None:
    get_supabase_client.cache_clear()
