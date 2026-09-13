from __future__ import annotations

import argparse

from repositories.scenes import publish_local_scenes


def main() -> None:
    parser = argparse.ArgumentParser(description="Publish Git scene modules to Supabase runtime tables.")
    parser.add_argument("--git-sha", default=None)
    args = parser.parse_args()
    count = publish_local_scenes(git_sha=args.git_sha)
    print(f"published_scenes={count}")


if __name__ == "__main__":
    main()
