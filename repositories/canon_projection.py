from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from typing import Any

from infrastructure.supabase_client import get_supabase_client


TABLE_SPECS: tuple[tuple[str, str, str], ...] = (
    ("entities", "canon_entities", "entity_id"),
    ("aliases", "canon_aliases", "alias_id"),
    ("references", "canon_references", "reference_id"),
    ("relations", "canon_relations", "relation_id"),
    ("scenario_links", "scenario_links", "link_id"),
    ("timeline_events", "timeline_events", "event_id"),
    ("timeline_event_entities", "timeline_event_entities", "event_id,entity_id,role"),
    ("knowledge_items", "knowledge_items", "item_id"),
    ("knowledge_assignments", "knowledge_assignments", "assignment_id"),
)

VALID_CANON_STATUS = {
    "actuel",
    "historique",
    "joue",
    "preparation",
    "hypothese",
    "retire",
    "contradictoire",
}
VALID_ACTIVATION_STATUS = {"actif", "non_declenche", "a_confirmer", "clos"}
VALID_VERIFICATION_STATUS = {"confirme", "a_verifier", "non_confirme"}
VALID_VISIBILITY = {
    "MJ",
    "publique",
    "faction",
    "PNJ",
    "PJ_commun",
    "PJ_individuel",
    "support_joueur",
}

OWNER_PREFIXES: tuple[tuple[tuple[str, ...], str], ...] = (
    (("pj_",), "02"),
    (("pnj_",), "03"),
    (("fait_",), "04"),
    (("loc_", "route_", "secteur_"), "05"),
    (("fac_", "cot_", "rel_"), "06"),
    (("dom_", "source_mystique_"), "07"),
    (("fav_", "dec_", "stat_", "pact_"), "07A"),
    (("arc_", "scn_"), "08"),
    (("sec_", "conn_"), "09"),
    (("evt_",), "10"),
    (("src_",), "90"),
)


def _issue(code: str, message: str, *, severity: str = "error", row_id: str | None = None) -> dict[str, Any]:
    item: dict[str, Any] = {"severity": severity, "code": code, "message": message}
    if row_id:
        item["row_id"] = row_id
    return item


def _expected_owner(entity_id: str) -> str | None:
    for prefixes, owner in OWNER_PREFIXES:
        if entity_id.startswith(prefixes):
            return owner
    return None


def _validate_statuses(row: dict[str, Any], row_id: str, issues: list[dict[str, Any]]) -> None:
    canon_status = row.get("canon_status")
    if canon_status is not None and canon_status not in VALID_CANON_STATUS:
        issues.append(_issue("invalid_canon_status", f"canon_status invalide: {canon_status}", row_id=row_id))

    activation_status = row.get("activation_status")
    if activation_status is not None and activation_status not in VALID_ACTIVATION_STATUS:
        issues.append(
            _issue("invalid_activation_status", f"activation_status invalide: {activation_status}", row_id=row_id)
        )

    verification = row.get("verification_status")
    if verification is not None and verification not in VALID_VERIFICATION_STATUS:
        issues.append(
            _issue("invalid_verification_status", f"verification_status invalide: {verification}", row_id=row_id)
        )

    visibility = row.get("visibility")
    if visibility is not None and visibility not in VALID_VISIBILITY:
        issues.append(_issue("invalid_visibility", f"visibility invalide: {visibility}", row_id=row_id))


def validate_manifest(manifest: dict[str, Any]) -> dict[str, Any]:
    """Validate a Drive-derived projection manifest without touching Supabase.

    The manifest must be explicit and self-contained for all new references. Existing
    projected endpoints can be declared in ``external_entity_ids`` for incremental
    projections. Validation never upgrades preparation to played/current state.
    """

    issues: list[dict[str, Any]] = []
    scope = str(manifest.get("projection_scope") or "").strip()
    if not scope:
        issues.append(_issue("missing_scope", "projection_scope est obligatoire"))

    external_ids = {str(value) for value in manifest.get("external_entity_ids", []) if str(value).strip()}
    entities = manifest.get("entities", [])
    if not isinstance(entities, list):
        issues.append(_issue("invalid_entities", "entities doit être une liste"))
        entities = []

    entity_ids: set[str] = set()
    for row in entities:
        if not isinstance(row, dict):
            issues.append(_issue("invalid_entity_row", "chaque entité doit être un objet"))
            continue
        entity_id = str(row.get("entity_id") or "").strip()
        if not entity_id:
            issues.append(_issue("missing_entity_id", "entity_id est obligatoire"))
            continue
        if entity_id in entity_ids:
            issues.append(_issue("duplicate_entity_id", f"entity_id dupliqué: {entity_id}", row_id=entity_id))
            continue
        entity_ids.add(entity_id)

        if row.get("authority", "DRIVE") != "DRIVE":
            issues.append(_issue("invalid_authority", "authority doit rester DRIVE", row_id=entity_id))
        if not str(row.get("owner_file") or "").strip():
            issues.append(_issue("missing_owner", "owner_file est obligatoire", row_id=entity_id))
        if not str(row.get("entity_type") or "").strip():
            issues.append(_issue("missing_entity_type", "entity_type est obligatoire", row_id=entity_id))

        expected_owner = _expected_owner(entity_id)
        owner_file = str(row.get("owner_file") or "")
        if expected_owner and owner_file and not owner_file.startswith(expected_owner):
            issues.append(
                _issue(
                    "owner_prefix_mismatch",
                    f"{entity_id} devrait appartenir à {expected_owner}, pas {owner_file}",
                    row_id=entity_id,
                )
            )
        _validate_statuses(row, entity_id, issues)

    known_entities = entity_ids | external_ids

    def require_entity(value: Any, *, row_id: str, field: str) -> None:
        target = str(value or "").strip()
        if not target:
            issues.append(_issue("missing_reference", f"{field} est obligatoire", row_id=row_id))
        elif target not in known_entities:
            issues.append(
                _issue("unknown_reference", f"{field} référence une entité absente: {target}", row_id=row_id)
            )

    seen_ids: dict[str, set[str]] = {}
    for key, _table, pk in TABLE_SPECS:
        rows = manifest.get(key, [])
        if not isinstance(rows, list):
            issues.append(_issue("invalid_collection", f"{key} doit être une liste"))
            continue
        if "," in pk:
            continue
        collection_seen: set[str] = set()
        for row in rows:
            if not isinstance(row, dict):
                issues.append(_issue("invalid_row", f"ligne invalide dans {key}"))
                continue
            row_id = str(row.get(pk) or "").strip()
            if not row_id:
                issues.append(_issue("missing_primary_key", f"{pk} est obligatoire dans {key}"))
                continue
            if row_id in collection_seen:
                issues.append(_issue("duplicate_primary_key", f"{pk} dupliqué dans {key}: {row_id}", row_id=row_id))
            collection_seen.add(row_id)
        seen_ids[key] = collection_seen

    for row in manifest.get("aliases", []):
        row_id = str(row.get("alias_id") or "<alias>")
        require_entity(row.get("entity_id"), row_id=row_id, field="entity_id")

    for row in manifest.get("references", []):
        row_id = str(row.get("reference_id") or "<reference>")
        require_entity(row.get("source_entity_id"), row_id=row_id, field="source_entity_id")
        require_entity(row.get("target_entity_id"), row_id=row_id, field="target_entity_id")

    relation_ids = seen_ids.get("relations", set())
    for row in manifest.get("relations", []):
        row_id = str(row.get("relation_id") or "<relation>")
        if row_id not in known_entities:
            issues.append(
                _issue(
                    "relation_missing_entity",
                    "une relation canonique doit aussi exister dans canon_entities",
                    row_id=row_id,
                )
            )
        require_entity(row.get("source_entity_id"), row_id=row_id, field="source_entity_id")
        require_entity(row.get("target_entity_id"), row_id=row_id, field="target_entity_id")
        _validate_statuses(row, row_id, issues)

    for row in manifest.get("scenario_links", []):
        row_id = str(row.get("link_id") or "<scenario_link>")
        require_entity(row.get("scenario_id"), row_id=row_id, field="scenario_id")
        require_entity(row.get("target_entity_id"), row_id=row_id, field="target_entity_id")
        _validate_statuses(row, row_id, issues)

    timeline_ids = seen_ids.get("timeline_events", set())
    for row in manifest.get("timeline_events", []):
        row_id = str(row.get("event_id") or "<event>")
        if row_id not in known_entities:
            issues.append(
                _issue("event_missing_entity", "un événement doit aussi exister dans canon_entities", row_id=row_id)
            )
        _validate_statuses(row, row_id, issues)

    event_link_keys: set[tuple[str, str, str]] = set()
    for row in manifest.get("timeline_event_entities", []):
        event_id = str(row.get("event_id") or "")
        entity_id = str(row.get("entity_id") or "")
        role = str(row.get("role") or "participant")
        row_id = f"{event_id}:{entity_id}:{role}"
        if event_id not in timeline_ids:
            issues.append(_issue("unknown_event", f"event_id absent du manifeste: {event_id}", row_id=row_id))
        require_entity(entity_id, row_id=row_id, field="entity_id")
        key = (event_id, entity_id, role)
        if key in event_link_keys:
            issues.append(_issue("duplicate_event_link", f"liaison événement dupliquée: {row_id}", row_id=row_id))
        event_link_keys.add(key)

    knowledge_ids = seen_ids.get("knowledge_items", set())
    for row in manifest.get("knowledge_items", []):
        row_id = str(row.get("item_id") or "<knowledge>")
        if row_id not in known_entities:
            issues.append(
                _issue("knowledge_missing_entity", "une information doit aussi exister dans canon_entities", row_id=row_id)
            )
        if row.get("subject_entity_id"):
            require_entity(row.get("subject_entity_id"), row_id=row_id, field="subject_entity_id")
        _validate_statuses(row, row_id, issues)

    for row in manifest.get("knowledge_assignments", []):
        row_id = str(row.get("assignment_id") or "<assignment>")
        item_id = str(row.get("item_id") or "")
        if item_id not in knowledge_ids:
            issues.append(_issue("unknown_knowledge_item", f"item_id absent du manifeste: {item_id}", row_id=row_id))
        holder_kind = str(row.get("holder_kind") or "entity")
        if holder_kind in {"entity", "faction"}:
            require_entity(row.get("holder_ref"), row_id=row_id, field="holder_ref")
        acquisition_event_id = row.get("acquisition_event_id")
        if acquisition_event_id and str(acquisition_event_id) not in timeline_ids:
            issues.append(
                _issue(
                    "unknown_acquisition_event",
                    f"acquisition_event_id absent du manifeste: {acquisition_event_id}",
                    row_id=row_id,
                )
            )

    # A specialized relation row without its canonical relation entity is always invalid.
    for relation_id in relation_ids:
        if relation_id not in entity_ids and relation_id not in external_ids:
            issues.append(_issue("orphan_relation", "relation spécialisée orpheline", row_id=relation_id))

    errors = [item for item in issues if item["severity"] == "error"]
    warnings = [item for item in issues if item["severity"] == "warning"]
    counts = {
        key: len(manifest.get(key, [])) if isinstance(manifest.get(key, []), list) else 0
        for key, _table, _pk in TABLE_SPECS
    }
    return {
        "valid": not errors,
        "projection_scope": scope or None,
        "counts": counts,
        "errors": errors,
        "warnings": warnings,
    }


def _prepare_rows(manifest: dict[str, Any], key: str) -> list[dict[str, Any]]:
    scope = str(manifest["projection_scope"])
    now = datetime.now(timezone.utc).isoformat()
    prepared: list[dict[str, Any]] = []
    for source in manifest.get(key, []):
        row = deepcopy(source)
        if key != "timeline_event_entities":
            row.setdefault("authority", "DRIVE")
            row.setdefault("projection_scope", scope)
            if key != "entities" or "synced_at" in row or True:
                row.setdefault("synced_at", now)
        else:
            row.setdefault("projection_scope", scope)
        prepared.append(row)
    return prepared


def sync_manifest(manifest: dict[str, Any], *, apply: bool = False, client: Any | None = None) -> dict[str, Any]:
    """Validate, dry-run or apply a canonical projection manifest.

    Default behavior is a dry-run. Apply mode is non-destructive: it upserts rows
    owned by the manifest but never prunes rows implicitly. Drive remains authority.
    """

    report = validate_manifest(manifest)
    report["mode"] = "apply" if apply else "dry_run"
    if not report["valid"] or not apply:
        report["applied"] = False
        return report

    db = client or get_supabase_client()
    if db is None:
        raise RuntimeError("Supabase server client unavailable; no projection was written")

    projection_scope = str(manifest["projection_scope"])
    run_payload = {
        "projection_scope": projection_scope,
        "mode": "apply",
        "status": "running",
        "source_revisions": manifest.get("source_revisions", {}),
        "projected_counts": report["counts"],
        "issues": [],
        "notes": manifest.get("notes"),
        "authority": "DRIVE",
    }
    run_response = db.table("canon_projection_runs").insert(run_payload).execute()
    run_rows = getattr(run_response, "data", None) or []
    run_id = run_rows[0].get("id") if run_rows else None

    try:
        for key, table, on_conflict in TABLE_SPECS:
            rows = _prepare_rows(manifest, key)
            if not rows:
                continue
            db.table(table).upsert(rows, on_conflict=on_conflict).execute()

        registry_rows = []
        for owner_file, source in (manifest.get("source_registry") or {}).items():
            registry_rows.append(
                {
                    "owner_file": owner_file,
                    "drive_file_id": source.get("drive_file_id"),
                    "drive_revision": source.get("drive_revision"),
                    "content_hash": source.get("content_hash"),
                    "synced_at": datetime.now(timezone.utc).isoformat(),
                    "sync_status": "synced",
                    "notes": f"Projection scope: {projection_scope}",
                }
            )
        if registry_rows:
            db.table("canon_sync_registry").upsert(registry_rows, on_conflict="owner_file").execute()

        if run_id:
            db.table("canon_projection_runs").update(
                {"status": "succeeded", "completed_at": datetime.now(timezone.utc).isoformat()}
            ).eq("id", run_id).execute()
        report["applied"] = True
        report["projection_run_id"] = run_id
        return report
    except Exception as exc:
        if run_id:
            try:
                db.table("canon_projection_runs").update(
                    {
                        "status": "failed",
                        "completed_at": datetime.now(timezone.utc).isoformat(),
                        "issues": [{"severity": "error", "code": "apply_failed", "message": str(exc)}],
                    }
                ).eq("id", run_id).execute()
            except Exception:
                pass
        raise
