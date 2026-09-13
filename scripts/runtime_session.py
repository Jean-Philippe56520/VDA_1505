from __future__ import annotations

import argparse
import json

from repositories.runtime import (
    close_campaign_session,
    current_campaign_session,
    flush_pending_remote,
    start_campaign_session,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Manage the local/Supabase VDA runtime session.")
    parser.add_argument("action", choices=["status", "start", "close", "sync"])
    parser.add_argument("--title", default=None)
    args = parser.parse_args()

    if args.action == "start":
        result = start_campaign_session(title=args.title)
    elif args.action == "close":
        result = close_campaign_session()
    elif args.action == "sync":
        result = flush_pending_remote()
    else:
        result = current_campaign_session()
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
