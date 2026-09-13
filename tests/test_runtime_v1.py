from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from repositories import runtime
from services import runtime as runtime_service


class RuntimeRepositoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        root = Path(self.temp.name)
        self.path_patches = [
            patch.object(runtime, "RUNTIME_DIR", root),
            patch.object(runtime, "SESSIONS_PATH", root / "campaign_sessions.json"),
            patch.object(runtime, "ACTIVE_SESSION_PATH", root / "active_campaign_session.json"),
            patch.object(runtime, "EVENTS_PATH", root / "runtime_events.ndjson"),
            patch.object(runtime, "SCENE_RUNS_PATH", root / "scene_runs.json"),
            patch.object(runtime, "PENDING_REMOTE_PATH", root / "pending_remote_ops.json"),
            patch.object(runtime, "supabase_enabled", return_value=False),
        ]
        for item in self.path_patches:
            item.start()

    def tearDown(self) -> None:
        for item in reversed(self.path_patches):
            item.stop()
        self.temp.cleanup()

    def _events(self) -> list[dict]:
        lines = runtime.EVENTS_PATH.read_text(encoding="utf-8").splitlines()
        return [json.loads(line) for line in lines if line.strip()]

    def test_session_and_event_are_local_first(self) -> None:
        session = runtime.start_campaign_session(title="Test", app_version="abc123")
        runtime.record_event(
            "scene_opened",
            session_id=session["id"],
            scene_ref="scene_test",
            payload={"run_id": "r1"},
        )
        self.assertEqual(runtime.current_campaign_session()["id"], session["id"])
        events = self._events()
        self.assertEqual(events[0]["event_type"], "session_started")
        self.assertEqual(events[1]["event_type"], "scene_opened")
        self.assertEqual(events[1]["play_status"], "unconfirmed")
        self.assertEqual(events[1]["consolidation_status"], "pending")

    def test_close_keeps_history_but_removes_active_marker(self) -> None:
        session = runtime.start_campaign_session(title="Test")
        closed = runtime.close_campaign_session()
        self.assertEqual(closed["id"], session["id"])
        self.assertEqual(closed["status"], "closed")
        self.assertIsNone(runtime.current_campaign_session())
        rows = json.loads(runtime.SESSIONS_PATH.read_text(encoding="utf-8"))
        self.assertEqual(rows[0]["status"], "closed")
        self.assertEqual(self._events()[-1]["event_type"], "session_closed")

    def test_failed_remote_upsert_is_idempotently_queued(self) -> None:
        payload = {"id": "00000000-0000-0000-0000-000000000001", "title": "One"}
        with patch.object(runtime, "supabase_enabled", return_value=True), patch.object(
            runtime, "_remote_upsert", side_effect=RuntimeError("offline")
        ):
            self.assertFalse(runtime._write_remote_best_effort("campaign_sessions", payload, "id"))
            payload2 = {**payload, "title": "Two"}
            self.assertFalse(runtime._write_remote_best_effort("campaign_sessions", payload2, "id"))
        queue = json.loads(runtime.PENDING_REMOTE_PATH.read_text(encoding="utf-8"))
        self.assertEqual(len(queue), 1)
        self.assertEqual(queue[0]["payload"]["title"], "Two")

    def test_scene_content_is_not_logged_until_render_hook(self) -> None:
        class Scene:
            id = "scene_test"
            title = "Scene test"

        class Run:
            active_choices = []
            transcript = [["Narrateur", "intro"]]
            last_answer_md = ""
            history_labels = []
            ended = False
            allow_undo = True
            allow_restart_after_choice = True

        session = runtime.start_campaign_session(title="Test")
        run = Run()
        with patch.object(runtime_service, "ensure_campaign_session", return_value=session), patch.object(
            runtime_service, "record_event"
        ) as record_event, patch.object(runtime_service, "upsert_scene_run"):
            runtime_service.scene_opened(
                run_id="00000000-0000-0000-0000-000000000002",
                scene=Scene(),
                run_state=run,
                started_at="2026-09-13T12:00:00+02:00",
            )
            self.assertEqual(record_event.call_count, 1)
            self.assertEqual(record_event.call_args.args[0], "scene_opened")
            runtime_service.scene_content_shown(
                run_id="00000000-0000-0000-0000-000000000002",
                scene_id="scene_test",
                transcript_index=0,
                content_md="intro",
            )
            self.assertEqual(record_event.call_count, 2)
            self.assertEqual(record_event.call_args.args[0], "scene_content_shown")

    def test_scene_run_recovery_metadata_survives_restart(self) -> None:
        session = runtime.start_campaign_session(title="Test")
        run_id = "00000000-0000-0000-0000-000000000099"
        runtime.upsert_scene_run(
            {
                "id": run_id,
                "session_id": session["id"],
                "scene_id": "scene_locked",
                "delivery_mode": None,
                "intended_character_ref": None,
                "started_at": "2026-09-13T12:00:00+02:00",
                "ended_at": None,
                "status": "open",
                "current_state": {
                    "history_labels": ["Choix"],
                    "allow_restart_after_choice": False,
                },
                "source_app_version": "test",
            }
        )
        found = runtime.latest_open_scene_run(session["id"])
        self.assertEqual(found["id"], run_id)
        self.assertEqual(runtime.sealed_scene_ids_for_session(session["id"]), {"scene_locked"})

    def test_logged_transcript_count_uses_actual_shown_events(self) -> None:
        session = runtime.start_campaign_session(title="Test")
        run_id = "00000000-0000-0000-0000-000000000100"
        runtime.record_event(
            "scene_content_shown",
            session_id=session["id"],
            scene_ref="scene_test",
            payload={"run_id": run_id, "transcript_index": 0, "content_md": "intro"},
        )
        runtime.record_event(
            "scene_choice_selected",
            session_id=session["id"],
            scene_ref="scene_test",
            payload={"run_id": run_id, "choice_id": "c1"},
        )
        self.assertEqual(runtime.logged_transcript_count_for_run(session["id"], run_id), 1)


class MigrationSecurityTests(unittest.TestCase):
    def test_migration_has_rls_and_no_player_grants(self) -> None:
        sql = Path("supabase/migrations/0001_runtime_v1.sql").read_text(encoding="utf-8").lower()
        for table in (
            "campaign_sessions",
            "runtime_events",
            "scene_runs",
            "hunt_runs",
            "published_scenes",
            "canon_entities",
            "canon_sync_registry",
        ):
            self.assertIn(f"alter table public.{table} enable row level security", sql)
            self.assertIn(f"revoke all on table public.{table} from anon, authenticated", sql)
        self.assertNotIn("grant select on table public.published_scenes to anon", sql)
        self.assertNotIn("grant select on table public.published_scenes to authenticated", sql)


if __name__ == "__main__":
    unittest.main()
