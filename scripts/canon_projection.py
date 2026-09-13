from __future__ import annotations

import argparse
import json
from pathlib import Path

from repositories.canon_projection import sync_manifest


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Valide et projette un manifeste canonique dérivé de Drive vers Supabase."
    )
    parser.add_argument("manifest", type=Path, help="Fichier JSON de projection dérivé de CORPUS_ACTIF")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Applique les upserts après validation. Sans ce drapeau, le mode est dry-run.",
    )
    args = parser.parse_args()

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    report = sync_manifest(manifest, apply=args.apply)
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if report.get("valid") else 2


if __name__ == "__main__":
    raise SystemExit(main())
