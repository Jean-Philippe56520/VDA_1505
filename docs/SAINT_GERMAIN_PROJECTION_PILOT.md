# Saint-Germain projection pilot

Status: operational Supabase projection pilot, non-authoritative.

Scope: `saint_germain_v1`.

The live pilot is derived from active Drive owners 02, 03, 05, 06, 07, 07A, 08, 09 and 10 after consulting 00, 04, 04A, 90 and 91. Narrative row contents are intentionally not committed to this public repository.

Validated live counts:

- 47 canonical entity projections;
- 9 explicit relation projections;
- 8 typed references;
- 2 scenario links;
- 8 timeline events;
- 28 event/entity links;
- 6 knowledge items;
- 1 knowledge assignment representing the common knowledge explicitly acquired by the PCs during the first played Saint-Germain session.

Safeguards validated:

- all projected entities use `authority = DRIVE`;
- exactly one pilot timeline event is marked `joue`;
- that played session has four PC participant links;
- projected secrets receive no automatic knowledge assignment;
- `canon_sync_registry` is intentionally untouched because this is a partial projection, not a complete owner synchronization;
- no Drive file, `04_ETAT_CAMPAGNE` or `04A_DELTA_SESSION` was modified by the pilot.

The live database records the exact Drive revision IDs used by the pilot in `canon_projection_runs.source_revisions`.
