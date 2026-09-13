# Canon projection operations

## Authority boundary

Google Drive `CORPUS_ACTIF` remains the canonical authority for the Rennes 1505 campaign. Supabase is a derived relational/indexing layer only. Git owns schema, migrations, validation code and technical documentation. Streamlit remains the table runtime.

No Supabase row, runtime event, application click or scene availability can change canon by itself. There is no automatic Supabase-to-Drive writeback.

## Projection layers

The V2 projection provides:

- entity registry and typed references;
- explicit relation graph;
- scenario links;
- chronology events and event/entity links;
- knowledge items separated from knowledge assignments;
- campaign checkpoint and session-delta indexes;
- contradiction index;
- Drive source revision tracking and drift detection.

`authority = DRIVE` is enforced for projected canonical data.

## Source revision tracking

`canon_source_files` records current and projected Drive revisions. `v_canon_source_drift` reports a source as changed when its current revision differs from the revision last projected.

A detected change does not update the canonical projection automatically. It is a review signal only. The safe flow is:

1. read Drive authority/index and affected owners;
2. inspect current campaign state and delta;
3. review contradictions/provenance when relevant;
4. validate the derived manifest/diff;
5. apply projection changes;
6. update the projected revision only after verification.

## Current registry coverage

The registry expansion intentionally distinguishes full coverage from partial coverage.

- `02`: full registry coverage;
- `03`: partial — later appended/projection blocks contain 9 IDs whose status is not normalized to the global status vocabulary;
- `05`: partial — 1 sector ID has no unambiguous global status;
- `06`: full registry coverage;
- `07`: full domain registry coverage; a Saint-Germain resource derived from the Caern block also exists in the projection;
- `07A`: full registry coverage;
- `08`: full arc/scene registry coverage;
- `09`: partial — 8 nested/projection IDs need source normalization before safe promotion to the global registry;
- `10`: partial — 11 event IDs need source normalization before safe promotion to the global registry.

These unresolved cases are retained as normalization backlog in `canon_source_files.payload`. They are not guessed or silently promoted.

## Knowledge guardrail

An information item existing in `knowledge_items` does not mean any PC/NPC/faction knows it. `knowledge_assignments` is the only structured holder mapping. Assignments must be grounded in explicit Drive acquisition/knowledge data or a validated played delta.

## Runtime separation

Runtime tables (`campaign_sessions`, `runtime_events`, `scene_runs`, `hunt_runs`) are operational. A runtime record remains non-canonical until the GM confirms the played fact and it is handled through the Drive delta/consolidation process.

The application must remain local-first/offline-tolerant for physical table use.

## Backup and recovery

Technical backups are kept outside `CORPUS_ACTIF`. Canonical narrative data should be reconstructed from Drive; published scenes can be reconstructed from Git snapshots/migrations. Mutable runtime data must be backed up separately once it exists.

A backup is never a canonical source.

## Merge gate

V1 and V2 pull requests remain drafts. Before merging V1 into `main`, run the physical Windows table smoke test:

1. server secret configured locally and not committed;
2. local backend session works;
3. hybrid backend catalogue and scene work;
4. deliberate network loss preserves table continuity and queues writes;
5. reconnection flushes queued events without duplication;
6. scene/session state resumes correctly.

V2 can then follow V1 after explicit GM validation. Database deployment does not by itself authorize Git merge.
