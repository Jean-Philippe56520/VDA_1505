-- VDA_1505 Supabase runtime V1
-- Drive remains the canonical source of truth. These tables are runtime and projections.

create extension if not exists pgcrypto;

create table if not exists public.campaign_sessions (
    id uuid primary key default gen_random_uuid(),
    title text not null default 'Séance VDA',
    status text not null default 'open' check (status in ('open', 'closed')),
    started_at timestamptz not null default now(),
    ended_at timestamptz,
    app_version text,
    metadata jsonb not null default '{}'::jsonb,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);

create table if not exists public.runtime_events (
    id uuid primary key default gen_random_uuid(),
    session_id uuid references public.campaign_sessions(id) on delete set null,
    event_type text not null,
    occurred_at timestamptz not null default now(),
    actor_ref text,
    scene_ref text,
    payload jsonb not null default '{}'::jsonb,
    source_app_version text,
    play_status text not null default 'unconfirmed'
        check (play_status in ('unconfirmed', 'gm_confirmed_played', 'gm_confirmed_not_played')),
    consolidation_status text not null default 'pending'
        check (consolidation_status in ('pending', 'reviewed', 'consolidated')),
    created_at timestamptz not null default now()
);

create table if not exists public.scene_runs (
    id uuid primary key default gen_random_uuid(),
    session_id uuid references public.campaign_sessions(id) on delete set null,
    scene_id text not null,
    delivery_mode text check (delivery_mode in ('group', 'individual')),
    intended_character_ref text,
    started_at timestamptz not null default now(),
    ended_at timestamptz,
    status text not null default 'open' check (status in ('open', 'finished', 'abandoned')),
    current_state jsonb not null default '{}'::jsonb,
    source_app_version text,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);

create table if not exists public.hunt_runs (
    id uuid primary key default gen_random_uuid(),
    session_id uuid references public.campaign_sessions(id) on delete set null,
    draw_id text not null unique,
    generated_at timestamptz,
    played_at timestamptz,
    play_status text not null default 'unconfirmed'
        check (play_status in ('unconfirmed', 'gm_confirmed_played', 'gm_confirmed_not_played')),
    payload jsonb not null default '{}'::jsonb,
    source_app_version text,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);

create table if not exists public.published_scenes (
    scene_id text primary key,
    title text not null,
    delivery_mode text not null default 'group'
        check (delivery_mode in ('group', 'individual')),
    intended_character_ref text,
    schema_version integer not null default 1,
    payload jsonb not null,
    source_kind text not null default 'git',
    legacy_source_path text,
    source_git_sha text,
    published_at timestamptz not null default now(),
    enabled boolean not null default true
);

create table if not exists public.canon_entities (
    entity_id text primary key,
    entity_type text not null,
    name text,
    owner_file text not null,
    payload jsonb not null default '{}'::jsonb,
    drive_file_id text,
    drive_revision text,
    content_hash text,
    synced_at timestamptz,
    authority text not null default 'DRIVE' check (authority = 'DRIVE')
);

create table if not exists public.canon_sync_registry (
    owner_file text primary key,
    drive_file_id text,
    drive_revision text,
    content_hash text,
    synced_at timestamptz,
    sync_status text not null default 'synced'
        check (sync_status in ('synced', 'drive_newer', 'projection_newer', 'conflict', 'invalid')),
    notes text
);

create index if not exists runtime_events_session_time_idx
    on public.runtime_events(session_id, occurred_at);
create index if not exists runtime_events_scene_time_idx
    on public.runtime_events(scene_ref, occurred_at);
create index if not exists runtime_events_type_time_idx
    on public.runtime_events(event_type, occurred_at);
create index if not exists scene_runs_session_idx
    on public.scene_runs(session_id, started_at);
create index if not exists scene_runs_scene_idx
    on public.scene_runs(scene_id, started_at);
create index if not exists hunt_runs_session_idx
    on public.hunt_runs(session_id, played_at);
create index if not exists published_scenes_delivery_idx
    on public.published_scenes(delivery_mode, enabled);
create index if not exists canon_entities_owner_idx
    on public.canon_entities(owner_file, entity_type);

-- V1 is server-side only. Public/players receive no direct Data API grants.
revoke all on table public.campaign_sessions from public;
revoke all on table public.runtime_events from public;
revoke all on table public.scene_runs from public;
revoke all on table public.hunt_runs from public;
revoke all on table public.published_scenes from public;
revoke all on table public.canon_entities from public;
revoke all on table public.canon_sync_registry from public;
revoke all on table public.campaign_sessions from anon, authenticated;
revoke all on table public.runtime_events from anon, authenticated;
revoke all on table public.scene_runs from anon, authenticated;
revoke all on table public.hunt_runs from anon, authenticated;
revoke all on table public.published_scenes from anon, authenticated;
revoke all on table public.canon_entities from anon, authenticated;
revoke all on table public.canon_sync_registry from anon, authenticated;

grant select, insert, update, delete on table public.campaign_sessions to service_role;
grant select, insert, update, delete on table public.runtime_events to service_role;
grant select, insert, update, delete on table public.scene_runs to service_role;
grant select, insert, update, delete on table public.hunt_runs to service_role;
grant select, insert, update, delete on table public.published_scenes to service_role;
grant select, insert, update, delete on table public.canon_entities to service_role;
grant select, insert, update, delete on table public.canon_sync_registry to service_role;

alter table public.campaign_sessions enable row level security;
alter table public.runtime_events enable row level security;
alter table public.scene_runs enable row level security;
alter table public.hunt_runs enable row level security;
alter table public.published_scenes enable row level security;
alter table public.canon_entities enable row level security;
alter table public.canon_sync_registry enable row level security;

comment on table public.runtime_events is
'Append-only application event journal. A click or display is not canon; GM confirmation and Drive consolidation remain separate.';
comment on table public.published_scenes is
'Runtime publication of scenes. delivery_mode=individual replaces ambiguous private terminology; it is not a security classification.';
comment on table public.canon_entities is
'Derived structured projection only. authority is fixed to DRIVE in V1.';
