from __future__ import annotations
import base64
from pathlib import Path

def image_to_data_uri(path: str) -> str:
    p = Path(path)
    ext = p.suffix.lower().lstrip(".")
    mime = {
        "png": "image/png",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "webp": "image/webp",
    }.get(ext, "image/png")

    data = base64.b64encode(p.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{data}"
