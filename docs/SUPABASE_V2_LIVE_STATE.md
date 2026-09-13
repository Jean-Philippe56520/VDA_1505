# Supabase V2 live state

Project: `VDA_1505` (`mcwxpkhhjasmabwucuzz`, eu-west-3).

Applied migrations after Runtime V1:

- `canon_projection_v2`
- `scenario_link_role`
- `knowledge_assignment_indexes`

Security model:

- RLS enabled on all V2 projection tables;
- no CRUD grant to `anon` or `authenticated`;
- server `service_role` CRUD only;
- Supabase security advisor reports only the expected informational `rls_enabled_no_policy` notices for this server-only model.

Performance advisor after the index migration reports no unindexed foreign keys. Remaining `unused_index` notices are expected on the new/low-volume database and are not a reason to remove the indexes.

Drive remains the canonical authority. This live database state does not constitute a Drive or canon mutation.
