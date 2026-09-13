-- VDA_1505 canon projection source tracking.
--
-- Drive/CORPUS_ACTIF remains the canonical authority. These tables index
-- source revisions, campaign checkpoint/delta state and contradiction status
-- so that projection drift can be detected without making Supabase canonical.

create table if not exists public.canon_source_files (
  source_key text primary key,
  drive_file_id text not null unique,
  title text not null,
  file_role text not null
    check (file_role in ('index','owner','checkpoint','delta','provenance','contradictions','migration')),
  projection_kind text not null
    check (projection_kind in ('index','owner_entities','checkpoint','delta','provenance','contradictions','migration')),
  coverage_status text not null default 'none'
    check (coverage_status in ('none','metadata_only','partial','full')),
  current_revision text not null,
  projected_revision text,
  projection_scope text,
  last_checked_at timestamptz not null default now(),
  last_projected_at timestamptz,
  payload jsonb not null default '{}'::jsonb,
  authority text not null default 'DRIVE' check (authority = 'DRIVE')
);

create table if not exists public.canon_source_change_log (
  id uuid primary key default gen_random_uuid(),
  source_key text not null references public.canon_source_files(source_key) on delete cascade,
  previous_revision text,
  observed_revision text not null,
  detected_at timestamptz not null default now(),
  review_status text not null default 'pending'
    check (review_status in ('pending','reviewing','projected','ignored')),
  note text,
  authority text not null default 'DRIVE' check (authority = 'DRIVE'),
  unique (source_key, observed_revision)
);

create table if not exists public.campaign_checkpoints (
  checkpoint_id text primary key,
  is_current boolean not null default false,
  game_date_text text not null,
  game_day_status text,
  primary_location_ref text,
  last_precise_scene text,
  active_arc_refs jsonb not null default '[]'::jsonb,
  closed_arc_refs jsonb not null default '[]'::jsonb,
  prepared_arc_refs jsonb not null default '[]'::jsonb,
  fact_refs jsonb not null default '[]'::jsonb,
  source_file_id text not null,
  source_revision text not null,
  payload jsonb not null default '{}'::jsonb,
  authority text not null default 'DRIVE' check (authority = 'DRIVE'),
  synced_at timestamptz not null default now()
);

create unique index if not exists campaign_checkpoints_one_current_idx
  on public.campaign_checkpoints ((is_current)) where is_current;

create table if not exists public.session_delta_records (
  delta_id text primary key,
  status text not null,
  game_date_text text,
  chronological_position text,
  capture_nature text,
  reliability text,
  arc_ref text,
  consolidation_status text not null
    check (consolidation_status in ('pending','partial','consolidated','not_applicable')),
  secret_refs jsonb not null default '[]'::jsonb,
  chronology_refs jsonb not null default '[]'::jsonb,
  owner_update_refs jsonb not null default '[]'::jsonb,
  source_file_id text not null,
  source_revision text not null,
  payload jsonb not null default '{}'::jsonb,
  authority text not null default 'DRIVE' check (authority = 'DRIVE'),
  synced_at timestamptz not null default now()
);

create table if not exists public.canon_contradictions_index (
  contradiction_id text primary key,
  status text not null,
  subject text not null,
  affects_current_1505 boolean not null default true,
  affected_owner_keys jsonb not null default '[]'::jsonb,
  refs jsonb not null default '[]'::jsonb,
  source_file_id text not null,
  source_revision text not null,
  payload jsonb not null default '{}'::jsonb,
  authority text not null default 'DRIVE' check (authority = 'DRIVE'),
  synced_at timestamptz not null default now()
);

create index if not exists canon_source_files_role_idx
  on public.canon_source_files(file_role, coverage_status);
create index if not exists canon_source_change_log_status_idx
  on public.canon_source_change_log(review_status, detected_at);
create index if not exists session_delta_records_consolidation_idx
  on public.session_delta_records(consolidation_status, synced_at);
create index if not exists canon_contradictions_status_idx
  on public.canon_contradictions_index(status, affects_current_1505);

create or replace view public.v_canon_source_drift with (security_invoker = true) as
select
  source_key,
  title,
  file_role,
  projection_kind,
  coverage_status,
  current_revision,
  projected_revision,
  projection_scope,
  last_checked_at,
  last_projected_at,
  case
    when projected_revision is null then true
    else current_revision <> projected_revision
  end as drift_detected
from public.canon_source_files;

revoke all on table public.canon_source_files from public, anon, authenticated;
revoke all on table public.canon_source_change_log from public, anon, authenticated;
revoke all on table public.campaign_checkpoints from public, anon, authenticated;
revoke all on table public.session_delta_records from public, anon, authenticated;
revoke all on table public.canon_contradictions_index from public, anon, authenticated;
revoke all on table public.v_canon_source_drift from public, anon, authenticated;

grant select, insert, update, delete on table public.canon_source_files to service_role;
grant select, insert, update, delete on table public.canon_source_change_log to service_role;
grant select, insert, update, delete on table public.campaign_checkpoints to service_role;
grant select, insert, update, delete on table public.session_delta_records to service_role;
grant select, insert, update, delete on table public.canon_contradictions_index to service_role;
grant select on table public.v_canon_source_drift to service_role;

alter table public.canon_source_files enable row level security;
alter table public.canon_source_change_log enable row level security;
alter table public.campaign_checkpoints enable row level security;
alter table public.session_delta_records enable row level security;
alter table public.canon_contradictions_index enable row level security;

comment on table public.canon_source_files is
'Drive source revision registry for a derived Supabase projection. It never changes Drive authority.';
comment on table public.campaign_checkpoints is
'Derived checkpoint projection of 04_ETAT_CAMPAGNE. Detailed mutable data remains owned by its canonical owner.';
comment on table public.session_delta_records is
'Derived index of 04A session deltas. It must never infer missing played facts from scenario preparation.';
comment on table public.canon_contradictions_index is
'Derived contradiction/arbitration index from 91. Current owner values remain authoritative.';
