from __future__ import annotations

import unittest
from pathlib import Path


class CanonProjectionViewTests(unittest.TestCase):
    def test_views_are_security_invoker_and_server_only(self) -> None:
        sql = Path("supabase/migrations/0006_canon_projection_views.sql").read_text(encoding="utf-8").lower()
        views = (
            "v_canon_relation_edges",
            "v_scenario_graph",
            "v_actor_knowledge",
            "v_entity_impact_links",
        )
        for view in views:
            self.assertIn(f"view public.{view}\nwith (security_invoker = true)", sql)
            self.assertIn(f"revoke all on public.{view} from public, anon, authenticated", sql)
            self.assertIn(f"grant select on public.{view} to service_role", sql)

    def test_actor_knowledge_view_only_reads_explicit_assignments(self) -> None:
        sql = Path("supabase/migrations/0006_canon_projection_views.sql").read_text(encoding="utf-8").lower()
        start = sql.index("create or replace view public.v_actor_knowledge")
        end = sql.index("create or replace view public.v_entity_impact_links")
        actor_view = sql[start:end]
        self.assertIn("from public.knowledge_assignments", actor_view)
        self.assertIn("join public.knowledge_items", actor_view)
        self.assertNotIn("canon_relations", actor_view)


if __name__ == "__main__":
    unittest.main()
