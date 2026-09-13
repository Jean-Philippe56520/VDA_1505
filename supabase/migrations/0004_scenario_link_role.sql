-- Make scenario link identity deterministic even when a generic reference has no
-- semantic role beyond its link_type. PostgreSQL UNIQUE treats NULL values as
-- distinct, so role must be non-null for reliable idempotent projection upserts.

alter table public.scenario_links
    alter column role set default 'reference';

update public.scenario_links
set role = 'reference'
where role is null;

alter table public.scenario_links
    alter column role set not null;
