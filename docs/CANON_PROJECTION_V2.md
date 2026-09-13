# Canon Projection V2

## Purpose

The VDA_1505 Supabase canonical projection is a derived relational index of the active Google Drive corpus. It exists to support cross-document joins, consistency checks, impact analysis and structured queries.

It is deliberately separate from the Streamlit runtime tables.

## Authority

- Google Drive `CORPUS_ACTIF` remains the sole editorial/canonical source of truth.
- Supabase rows use `authority = DRIVE` and never become canon merely because they exist in the database.
- Git owns the projection schema, validation code and migrations, not narrative authority.
- Streamlit remains the physical-session runtime/interface and does not become the owner of canonical data.
- There is no automatic Supabase -> Drive write path.

## Semantic safeguards

The projection preserves distinctions required by the corpus:

- current / historical / played / preparation / hypothesis / retired / contradictory;
- GM truth / public version / rumor / lie / suspicion;
- information existence / actual actor knowledge;
- prepared scene / played scene;
- relation truth / actor belief about that relation;
- current campaign state / future preparation.

No inferred causal relationship is promoted to a certain canonical relation.

## Tables

`canon_entities`
: Central registry using the stable IDs already owned by Drive (`pnj_*`, `fac_*`, `arc_*`, `sec_*`, etc.).

`canon_relations`
: Explicit relational graph for owner-defined relations. Specialized relation rows must also exist as canonical entities.

`canon_references`
: Typed references between canonical entities when the corpus points from one stable ID to another without defining a standalone relation.

`scenario_links`
: Links an arc/scenario to entities explicitly referenced by its owner or by confirmed played-event records. A link does not imply that a prepared element was played.

`timeline_events` / `timeline_event_entities`
: Structured chronology and its participants/subjects. Future or prepared events retain their preparation status.

`knowledge_items` / `knowledge_assignments`
: Epistemic layer separating information from who knows, believes, suspects or has heard it.

`canon_aliases`
: Historical aliases and ID migrations. Aliases do not create parallel instances.

`canon_projection_runs`
: Operational audit trail for projection runs. It is not canon.

`canon_sync_registry`
: Whole-owner synchronization registry. Partial pilot projections must not mark an entire Drive owner as synchronized.

## Synchronization contract

A projection manifest follows this sequence:

1. read `00_INDEX_CANON`;
2. identify and read the owner files required for the scope;
3. read `04_ETAT_CAMPAGNE` and `04A_DELTA_SESSION`;
4. read `91_REGISTRE_CONTRADICTIONS` where conflicts matter;
5. read `90_REGISTRE_SOURCES` where provenance matters;
6. validate IDs, owner prefixes, statuses and references;
7. dry-run by default;
8. apply only after validation;
9. never delete/prune implicitly;
10. verify the resulting relational queries.

A partial projection records provenance on each projected row and in `canon_projection_runs`; it does not claim whole-owner synchronization in `canon_sync_registry`.

## Security model

V2 is server-side only. All exposed-schema projection tables have RLS enabled, no CRUD grants for `anon` or `authenticated`, and CRUD access for `service_role`. A server secret must never be exposed to player/browser code.

## Pilot scope

The first production pilot is Saint-Germain / `arc_saint_germain_la_terre_ment`. It is intended to prove that the relational representation can preserve:

- explicit faction and character relationships;
- places and resources;
- played vs prepared chronology;
- secrets and actor knowledge;
- current vs historical state;
- provenance and contradiction safeguards.

The pilot does not alter Drive, `04A`, or the canonical status of any narrative element.
