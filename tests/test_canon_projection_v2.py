from __future__ import annotations

import unittest
from pathlib import Path
from unittest.mock import patch

from repositories.canon_projection import sync_manifest, validate_manifest


def valid_manifest() -> dict:
    return {
        "projection_scope": "synthetic_test",
        "source_revisions": {"03": "rev03", "06": "rev06", "08": "rev08", "09": "rev09", "10": "rev10"},
        "source_registry": {
            "03_PNJ_VAMPIRES_MORTELS_CREATURES": {
                "drive_file_id": "drive03",
                "drive_revision": "rev03",
            }
        },
        "entities": [
            {
                "entity_id": "arc_test_projection",
                "entity_type": "arc",
                "name": "Arc test",
                "owner_file": "08_CHRONIQUES_SCENARIOS_ARCS",
                "canon_status": "preparation",
                "activation_status": "non_declenche",
                "verification_status": "confirme",
                "visibility": "MJ",
            },
            {
                "entity_id": "pnj_alpha",
                "entity_type": "pnj",
                "name": "Alpha",
                "owner_file": "03_PNJ_VAMPIRES_MORTELS_CREATURES",
                "canon_status": "actuel",
                "verification_status": "confirme",
                "visibility": "MJ",
            },
            {
                "entity_id": "pnj_beta",
                "entity_type": "pnj",
                "name": "Beta",
                "owner_file": "03_PNJ_VAMPIRES_MORTELS_CREATURES",
                "canon_status": "actuel",
                "verification_status": "confirme",
                "visibility": "MJ",
            },
            {
                "entity_id": "fac_test",
                "entity_type": "faction",
                "name": "Faction test",
                "owner_file": "06_CLANS_COTERIES_FACTIONS_POLITIQUE",
                "canon_status": "actuel",
                "verification_status": "confirme",
                "visibility": "MJ",
            },
            {
                "entity_id": "rel_alpha_beta",
                "entity_type": "relation",
                "name": "Relation Alpha Beta",
                "owner_file": "06_CLANS_COTERIES_FACTIONS_POLITIQUE",
                "canon_status": "actuel",
                "verification_status": "confirme",
                "visibility": "MJ",
            },
            {
                "entity_id": "evt_test_projection",
                "entity_type": "event",
                "name": "Événement test",
                "owner_file": "10_CHRONOLOGIE_HISTOIRE_LOCALE",
                "canon_status": "historique",
                "verification_status": "confirme",
                "visibility": "MJ",
            },
            {
                "entity_id": "sec_test_projection",
                "entity_type": "secret",
                "name": "Secret test",
                "owner_file": "09_SECRETS_CONNAISSANCES_REVELATIONS",
                "canon_status": "actuel",
                "verification_status": "confirme",
                "visibility": "MJ",
            },
        ],
        "aliases": [
            {
                "alias_id": "pnj_alpha_ancien",
                "entity_id": "pnj_alpha",
                "owner_file": "03_PNJ_VAMPIRES_MORTELS_CREATURES",
            }
        ],
        "references": [
            {
                "reference_id": "ref_arc_alpha",
                "source_entity_id": "arc_test_projection",
                "target_entity_id": "pnj_alpha",
                "ref_role": "participant_ref",
                "owner_file": "08_CHRONIQUES_SCENARIOS_ARCS",
            }
        ],
        "relations": [
            {
                "relation_id": "rel_alpha_beta",
                "source_entity_id": "pnj_alpha",
                "target_entity_id": "pnj_beta",
                "relation_type": "rivalite",
                "owner_file": "06_CLANS_COTERIES_FACTIONS_POLITIQUE",
                "canon_status": "actuel",
                "verification_status": "confirme",
                "visibility": "MJ",
            }
        ],
        "scenario_links": [
            {
                "link_id": "lnk_arc_alpha",
                "scenario_id": "arc_test_projection",
                "target_entity_id": "pnj_alpha",
                "link_type": "participant",
                "role": "antagoniste",
                "owner_file": "08_CHRONIQUES_SCENARIOS_ARCS",
                "canon_status": "preparation",
                "visibility": "MJ",
            }
        ],
        "timeline_events": [
            {
                "event_id": "evt_test_projection",
                "event_kind": "historique",
                "game_date_text": "1504",
                "game_year": 1504,
                "canon_status": "historique",
                "verification_status": "confirme",
                "visibility": "MJ",
                "owner_file": "10_CHRONOLOGIE_HISTOIRE_LOCALE",
            }
        ],
        "timeline_event_entities": [
            {"event_id": "evt_test_projection", "entity_id": "pnj_alpha", "role": "participant"}
        ],
        "knowledge_items": [
            {
                "item_id": "sec_test_projection",
                "information_kind": "secret",
                "subject_entity_id": "pnj_beta",
                "summary": "Information synthétique",
                "canon_status": "actuel",
                "verification_status": "confirme",
                "visibility": "MJ",
                "owner_file": "09_SECRETS_CONNAISSANCES_REVELATIONS",
            }
        ],
        "knowledge_assignments": [
            {
                "assignment_id": "know_alpha_secret",
                "item_id": "sec_test_projection",
                "holder_ref": "pnj_alpha",
                "holder_kind": "entity",
                "knowledge_state": "connue",
                "reliability": "certaine",
                "acquisition_event_id": "evt_test_projection",
                "owner_file": "09_SECRETS_CONNAISSANCES_REVELATIONS",
            }
        ],
    }


class CanonProjectionValidationTests(unittest.TestCase):
    def test_valid_manifest_passes(self) -> None:
        report = validate_manifest(valid_manifest())
        self.assertTrue(report["valid"], report["errors"])
        self.assertEqual(report["counts"]["entities"], 7)
        self.assertEqual(report["counts"]["relations"], 1)

    def test_duplicate_entity_is_rejected(self) -> None:
        manifest = valid_manifest()
        manifest["entities"].append(dict(manifest["entities"][0]))
        report = validate_manifest(manifest)
        self.assertFalse(report["valid"])
        self.assertIn("duplicate_entity_id", {item["code"] for item in report["errors"]})

    def test_broken_reference_is_rejected(self) -> None:
        manifest = valid_manifest()
        manifest["scenario_links"][0]["target_entity_id"] = "pnj_absent"
        report = validate_manifest(manifest)
        self.assertFalse(report["valid"])
        self.assertIn("unknown_reference", {item["code"] for item in report["errors"]})

    def test_relation_requires_canonical_relation_entity(self) -> None:
        manifest = valid_manifest()
        manifest["entities"] = [row for row in manifest["entities"] if row["entity_id"] != "rel_alpha_beta"]
        report = validate_manifest(manifest)
        self.assertFalse(report["valid"])
        self.assertIn("relation_missing_entity", {item["code"] for item in report["errors"]})

    def test_owner_prefix_mismatch_is_rejected(self) -> None:
        manifest = valid_manifest()
        manifest["entities"][1]["owner_file"] = "08_CHRONIQUES_SCENARIOS_ARCS"
        report = validate_manifest(manifest)
        self.assertFalse(report["valid"])
        self.assertIn("owner_prefix_mismatch", {item["code"] for item in report["errors"]})

    def test_entity_holder_must_exist(self) -> None:
        manifest = valid_manifest()
        manifest["knowledge_assignments"][0]["holder_ref"] = "pnj_absent"
        report = validate_manifest(manifest)
        self.assertFalse(report["valid"])
        self.assertIn("unknown_reference", {item["code"] for item in report["errors"]})

    def test_dry_run_never_opens_supabase_client(self) -> None:
        with patch("repositories.canon_projection.get_supabase_client") as get_client:
            report = sync_manifest(valid_manifest(), apply=False)
        self.assertTrue(report["valid"])
        self.assertFalse(report["applied"])
        get_client.assert_not_called()


class CanonProjectionMigrationTests(unittest.TestCase):
    def test_v2_migration_is_server_only_and_drive_authoritative(self) -> None:
        sql = Path("supabase/migrations/0003_canon_projection_v2.sql").read_text(encoding="utf-8").lower()
        tables = (
            "canon_projection_runs",
            "canon_aliases",
            "canon_references",
            "canon_relations",
            "scenario_links",
            "timeline_events",
            "timeline_event_entities",
            "knowledge_items",
            "knowledge_assignments",
        )
        for table in tables:
            self.assertIn(f"alter table public.{table} enable row level security", sql)
            self.assertIn(f"revoke all on table public.{table} from public, anon, authenticated", sql)
            self.assertIn(f"grant select, insert, update, delete on table public.{table} to service_role", sql)
        self.assertNotIn("grant select on table public.canon_relations to anon", sql)
        self.assertNotIn("grant select on table public.knowledge_items to authenticated", sql)
        self.assertGreaterEqual(sql.count("check (authority = 'drive')"), 8)

    def test_preparation_status_is_preserved_in_schema(self) -> None:
        sql = Path("supabase/migrations/0003_canon_projection_v2.sql").read_text(encoding="utf-8").lower()
        self.assertIn("'preparation'", sql)
        self.assertIn("a linked scene or consequence remains preparation unless drive says it was played", sql)


if __name__ == "__main__":
    unittest.main()
