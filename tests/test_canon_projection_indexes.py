from __future__ import annotations

import unittest
from pathlib import Path


class CanonProjectionIndexTests(unittest.TestCase):
    def test_knowledge_assignment_foreign_keys_are_indexed(self) -> None:
        sql = Path("supabase/migrations/0005_knowledge_assignment_indexes.sql").read_text(encoding="utf-8").lower()
        self.assertIn("knowledge_assignments_item_idx", sql)
        self.assertIn("on public.knowledge_assignments(item_id)", sql)
        self.assertIn("knowledge_assignments_acquisition_event_idx", sql)
        self.assertIn("on public.knowledge_assignments(acquisition_event_id)", sql)


if __name__ == "__main__":
    unittest.main()
