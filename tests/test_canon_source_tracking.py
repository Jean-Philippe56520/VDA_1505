from __future__ import annotations

import unittest
from pathlib import Path


class CanonSourceTrackingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sql = Path("supabase/migrations/0007_canon_source_tracking.sql").read_text(
            encoding="utf-8"
        ).lower()

    def test_source_tracking_objects_exist(self) -> None:
        for object_name in (
            "canon_source_files",
            "canon_source_change_log",
            "campaign_checkpoints",
            "session_delta_records",
            "canon_contradictions_index",
            "v_canon_source_drift",
        ):
            self.assertIn(object_name, self.sql)

    def test_projection_authority_stays_drive(self) -> None:
        self.assertGreaterEqual(self.sql.count("authority = 'drive'"), 5)
        self.assertIn("it never changes drive authority", self.sql)
        self.assertIn("must never infer missing played facts from scenario preparation", self.sql)

    def test_server_only_security_contract(self) -> None:
        for table_name in (
            "canon_source_files",
            "canon_source_change_log",
            "campaign_checkpoints",
            "session_delta_records",
            "canon_contradictions_index",
        ):
            self.assertIn(f"alter table public.{table_name} enable row level security", self.sql)
            self.assertIn(
                f"revoke all on table public.{table_name} from public, anon, authenticated",
                self.sql,
            )
            self.assertIn(
                f"grant select, insert, update, delete on table public.{table_name} to service_role",
                self.sql,
            )

    def test_drift_view_invokes_caller_security(self) -> None:
        self.assertIn(
            "create or replace view public.v_canon_source_drift with (security_invoker = true)",
            self.sql,
        )
        self.assertIn(
            "revoke all on table public.v_canon_source_drift from public, anon, authenticated",
            self.sql,
        )
        self.assertIn("grant select on table public.v_canon_source_drift to service_role", self.sql)

    def test_partial_coverage_is_first_class(self) -> None:
        self.assertIn("coverage_status", self.sql)
        self.assertIn("'none','metadata_only','partial','full'", self.sql.replace(" ", ""))
        self.assertIn("current_revision", self.sql)
        self.assertIn("projected_revision", self.sql)


if __name__ == "__main__":
    unittest.main()
