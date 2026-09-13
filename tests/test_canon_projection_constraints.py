from __future__ import annotations

import unittest
from pathlib import Path


class CanonProjectionConstraintTests(unittest.TestCase):
    def test_scenario_link_role_is_not_nullable(self) -> None:
        sql = Path("supabase/migrations/0004_scenario_link_role.sql").read_text(encoding="utf-8").lower()
        self.assertIn("alter column role set default 'reference'", sql)
        self.assertIn("where role is null", sql)
        self.assertIn("alter column role set not null", sql)


if __name__ == "__main__":
    unittest.main()
