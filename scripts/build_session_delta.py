from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from repositories.runtime import EVENTS_PATH, current_campaign_session


def _events(path: Path, session_id: str) -> list[dict]:
    out: list[dict] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return out
    for line in lines:
        if not line.strip():
            continue
        try:
            item = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(item, dict) and item.get("session_id") == session_id:
            out.append(item)
    return out


def _quote(value: object) -> str:
    return str(value or "").replace("\n", " ").strip()


def build_delta(session_id: str) -> str:
    events = _events(EVENTS_PATH, session_id)
    counts = Counter(str(event.get("event_type")) for event in events)
    lines = [
        "# Pré-delta de séance — BROUILLON NON CANONIQUE",
        "",
        f"session_id: `{session_id}`",
        "",
        "> Généré depuis le journal runtime. Un clic, un affichage ou une scène terminée ne devient pas canon automatiquement. Revue MJ obligatoire avant toute inscription dans 04A.",
        "",
        "## Résumé technique",
    ]
    if counts:
        for event_type, count in sorted(counts.items()):
            lines.append(f"- `{event_type}`: {count}")
    else:
        lines.append("- Aucun événement enregistré.")

    lines.extend(["", "## Scènes ouvertes / terminées"])
    for event in events:
        if event.get("event_type") not in {"scene_opened", "scene_finished", "scene_restarted"}:
            continue
        lines.append(
            f"- {_quote(event.get('occurred_at'))} — `{_quote(event.get('event_type'))}` — `{_quote(event.get('scene_ref'))}`"
        )

    lines.extend(["", "## Choix effectués"])
    for event in events:
        if event.get("event_type") != "scene_choice_selected":
            continue
        payload = event.get("payload") if isinstance(event.get("payload"), dict) else {}
        lines.append(
            f"- `{_quote(event.get('scene_ref'))}` — `{_quote(payload.get('choice_id'))}` — {_quote(payload.get('label'))}"
        )

    lines.extend(["", "## Informations effectivement affichées"])
    for event in events:
        if event.get("event_type") != "scene_content_shown":
            continue
        payload = event.get("payload") if isinstance(event.get("payload"), dict) else {}
        content = _quote(payload.get("content_md"))
        if len(content) > 220:
            content = content[:217] + "..."
        lines.append(
            f"- `{_quote(event.get('scene_ref'))}` — {_quote(payload.get('content_kind'))}: {content}"
        )

    lines.extend(["", "## Chasses marquées « jouées » dans l'outil"])
    for event in events:
        if event.get("event_type") != "hunt_marked_played":
            continue
        payload = event.get("payload") if isinstance(event.get("payload"), dict) else {}
        lines.append(
            f"- `{_quote(payload.get('draw_id'))}` — {_quote(payload.get('point_label'))} — {_quote(payload.get('rencontre'))}"
        )

    lines.extend(
        [
            "",
            "## Revue MJ requise",
            "- Confirmer ce qui a réellement été joué.",
            "- Distinguer contenu seulement affiché, connaissance effectivement acquise et information hors personnage.",
            "- Retirer les clics annulés, tests UI et scènes seulement préparées.",
            "- Reporter uniquement les changements confirmés dans 04A, puis consolider selon les propriétaires du corpus.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a non-canonical 04A pre-delta from runtime events.")
    parser.add_argument("--session-id", default=None)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    session_id = args.session_id
    if not session_id:
        current = current_campaign_session()
        if not current:
            raise SystemExit("No active runtime session. Pass --session-id.")
        session_id = str(current["id"])
    text = build_delta(session_id)
    if args.output:
        args.output.write_text(text, encoding="utf-8")
        print(args.output)
    else:
        print(text)


if __name__ == "__main__":
    main()
