from __future__ import annotations

import argparse
from pathlib import Path

from repositories.scenes import export_snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the offline VDA runtime scene snapshot.")
    parser.add_argument("--git-sha", default=None)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    path = export_snapshot(git_sha=args.git_sha, destination=args.output)
    print(path)


if __name__ == "__main__":
    main()
