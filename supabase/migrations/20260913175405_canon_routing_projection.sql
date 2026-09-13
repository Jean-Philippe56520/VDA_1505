create table if not exists public.canon_routing_steps (
  route_key text not null,
  step_order integer not null check (step_order > 0),
  step_ref text not null,
  step_kind text not null default 'source'
    check (step_kind = any (array[
      'source'::text,
      'conditional_source'::text,
      'dynamic'::text,
      'filter'::text
    ])),
  payload jsonb not null default '{}'::jsonb,
  source_file_id text not null,
  source_revision text not null,
  projection_scope text not null default 'index_routing_v1'::text,
  authority text not null default 'DRIVE'::text
    check (authority = 'DRIVE'::text),
  synced_at timestamptz not null default now(),
  primary key (route_key, step_order)
);

comment on table public.canon_routing_steps is
  'Derived ordered routing projection from 00_INDEX_CANON. It helps choose Drive owners to read; it never replaces 00 or changes canonical authority.';

comment on column public.canon_routing_steps.step_kind is
  'source=Drive source/owner key; conditional_source=read only when condition applies; dynamic=resolve owners at query time; filter=source used specifically to filter player-visible knowledge.';

alter table public.canon_routing_steps enable row level security;

create index if not exists canon_routing_steps_ref_idx
  on public.canon_routing_steps(step_ref);

create index if not exists canon_routing_steps_source_revision_idx
  on public.canon_routing_steps(source_file_id, source_revision);
