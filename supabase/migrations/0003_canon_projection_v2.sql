-- VDA_1505 canonical projection V2
--
-- Drive/CORPUS_ACTIF remains the sole canonical authority. These tables are
-- a derived relational projection for analysis, consistency checks and joins.
-- Writing here never changes canon and never writes back to Drive.

alter table public.canon_entities
    add column if not exists canon_status text not null default 'actuel'
        check (canon_status in ('actuel', 'historique', 'joue', 'preparation', 'hypothese', 'retire', 'contradictoire')),
    add column if not exists activation_status text
        check (activation_status is null or activation_status in ('actif', 'non_declenche', 'a_confirmer', 'clos')),
    add column if not exists verification_status text not null default 'a_verifier'
        check (verification_status in ('confirme', 'a_verifier', 'non_confirme')),
    add column if not exists visibility text not null default 'MJ'
        check (visibility in ('MJ', 'publique', 'faction', 'PNJ', 'PJ_commun', 'PJ_individuel', 'support_joueur')),
    add column if not exists source_block_id text,
    add column if not exists projection_scope text,
    add column if not exists source_updated_at timestamptz;

create table if not exists public.canon_projection_runs (
    id uuid primary key default gen_random_uuid(),
    projection_scope text not null,
    mode text not null default 'apply' check (mode in ('dry_run', 'apply')),
    status text not null default 'running' check (status in ('running', 'succeeded', 'failed', 'rejected')),
    started_at timestamptz not null default now(),
    completed_at timestamptz,
    source_revisions jsonb not null default '{}'::jsonb,
    projected_counts jsonb not null default '{}'::jsonb,
    issues jsonb not null default '[]'::jsonb,
    notes text,
    authority text not null default 'DRIVE' check (authority = 'DRIVE')
);

create table if not exists public.canon_aliases (
    alias_id text primary key,
    entity_id text not null references public.canon_entities(entity_id) on delete cascade,
    alias_status text not null default 'historique'
        check (alias_status in ('courant', 'historique', 'retire')),
    owner_file text not null,
    drive_file_id text,
    drive_revision text,
    source_block_id text,
    content_hash text,
    projection_scope text,
    authority text not null default 'DRIVE' check (authority = 'DRIVE'),
    synced_at timestamptz not null default now()
);

create table if not exists public.canon_references (
    reference_id text primary key,
    source_entity_id text not null references public.canon_entities(entity_id) on delete cascade,
    target_entity_id text not null references public.canon_entities(entity_id) on delete restrict,
    ref_role text not null,
    owner_file text not null,
    drive_file_id text,
    drive_revision text,
    source_block_id text,
    content_hash text,
    projection_scope text,
    authority text not null default 'DRIVE' check (authority = 'DRIVE'),
    synced_at timestamptz not null default now(),
    unique (source_entity_id, target_entity_id, ref_role, owner_file)
);

create table if not exists public.canon_relations (
    relation_id text primary key references public.canon_entities(entity_id) on delete cascade,
    source_entity_id text not null references public.canon_entities(entity_id) on delete restrict,
    target_entity_id text not null references public.canon_entities(entity_id) on delete restrict,
    relation_type text not null,
    directed boolean not null default true,
    certainty text not null default 'certaine'
        check (certainty in ('certaine', 'probable', 'possible', 'contestee', 'inconnue')),
    canon_status text not null default 'actuel'
        check (canon_status in ('actuel', 'historique', 'joue', 'preparation', 'hypothese', 'retire', 'contradictoire')),
    activation_status text
        check (activation_status is null or activation_status in ('actif', 'non_declenche', 'a_confirmer', 'clos')),
    verification_status text not null default 'a_verifier'
        check (verification_status in ('confirme', 'a_verifier', 'non_confirme')),
    visibility text not null default 'MJ'
        check (visibility in ('MJ', 'publique', 'faction', 'PNJ', 'PJ_commun', 'PJ_individuel', 'support_joueur')),
    valid_from_text text,
    valid_to_text text,
    owner_file text not null,
    drive_file_id text,
    drive_revision text,
    source_block_id text,
    content_hash text,
    projection_scope text,
    payload jsonb not null default '{}'::jsonb,
    authority text not null default 'DRIVE' check (authority = 'DRIVE'),
    synced_at timestamptz not null default now(),
    check (source_entity_id <> target_entity_id or relation_type in ('identite', 'reflexive'))
);

create table if not exists public.scenario_links (
    link_id text primary key,
    scenario_id text not null references public.canon_entities(entity_id) on delete cascade,
    target_entity_id text not null references public.canon_entities(entity_id) on delete restrict,
    link_type text not null,
    role text,
    canon_status text not null default 'preparation'
        check (canon_status in ('actuel', 'historique', 'joue', 'preparation', 'hypothese', 'retire', 'contradictoire')),
    visibility text not null default 'MJ'
        check (visibility in ('MJ', 'publique', 'faction', 'PNJ', 'PJ_commun', 'PJ_individuel', 'support_joueur')),
    owner_file text not null,
    drive_file_id text,
    drive_revision text,
    source_block_id text,
    content_hash text,
    projection_scope text,
    payload jsonb not null default '{}'::jsonb,
    authority text not null default 'DRIVE' check (authority = 'DRIVE'),
    synced_at timestamptz not null default now(),
    unique (scenario_id, target_entity_id, link_type, role)
);

create table if not exists public.timeline_events (
    event_id text primary key references public.canon_entities(entity_id) on delete cascade,
    event_kind text not null default 'event',
    game_date_text text,
    game_year integer,
    game_month integer check (game_month is null or game_month between 1 and 12),
    game_day integer check (game_day is null or game_day between 1 and 31),
    canon_status text not null default 'historique'
        check (canon_status in ('actuel', 'historique', 'joue', 'preparation', 'hypothese', 'retire', 'contradictoire')),
    activation_status text
        check (activation_status is null or activation_status in ('actif', 'non_declenche', 'a_confirmer', 'clos')),
    verification_status text not null default 'a_verifier'
        check (verification_status in ('confirme', 'a_verifier', 'non_confirme')),
    visibility text not null default 'MJ'
        check (visibility in ('MJ', 'publique', 'faction', 'PNJ', 'PJ_commun', 'PJ_individuel', 'support_joueur')),
    owner_file text not null,
    drive_file_id text,
    drive_revision text,
    source_block_id text,
    content_hash text,
    projection_scope text,
    payload jsonb not null default '{}'::jsonb,
    authority text not null default 'DRIVE' check (authority = 'DRIVE'),
    synced_at timestamptz not null default now()
);

create table if not exists public.timeline_event_entities (
    event_id text not null references public.timeline_events(event_id) on delete cascade,
    entity_id text not null references public.canon_entities(entity_id) on delete restrict,
    role text not null default 'participant',
    projection_scope text,
    primary key (event_id, entity_id, role)
);

create table if not exists public.knowledge_items (
    item_id text primary key references public.canon_entities(entity_id) on delete cascade,
    information_kind text not null default 'secret'
        check (information_kind in ('verite_MJ', 'version_publique', 'rumeur', 'mensonge', 'soupcon', 'secret', 'observation')),
    subject_entity_id text references public.canon_entities(entity_id) on delete set null,
    summary text,
    canon_status text not null default 'actuel'
        check (canon_status in ('actuel', 'historique', 'joue', 'preparation', 'hypothese', 'retire', 'contradictoire')),
    verification_status text not null default 'a_verifier'
        check (verification_status in ('confirme', 'a_verifier', 'non_confirme')),
    visibility text not null default 'MJ'
        check (visibility in ('MJ', 'publique', 'faction', 'PNJ', 'PJ_commun', 'PJ_individuel', 'support_joueur')),
    owner_file text not null,
    drive_file_id text,
    drive_revision text,
    source_block_id text,
    content_hash text,
    projection_scope text,
    payload jsonb not null default '{}'::jsonb,
    authority text not null default 'DRIVE' check (authority = 'DRIVE'),
    synced_at timestamptz not null default now()
);

create table if not exists public.knowledge_assignments (
    assignment_id text primary key,
    item_id text not null references public.knowledge_items(item_id) on delete cascade,
    holder_ref text not null,
    holder_kind text not null default 'entity'
        check (holder_kind in ('entity', 'faction', 'PJ_commun', 'groupe', 'public', 'MJ')),
    knowledge_state text not null default 'connue'
        check (knowledge_state in ('connue', 'crue', 'soupconnee', 'rumeur_entendue', 'mensonge_accepte', 'ignoree', 'niee')),
    reliability text not null default 'certaine'
        check (reliability in ('certaine', 'probable', 'incertaine', 'fausse', 'inconnue')),
    acquisition_event_id text references public.timeline_events(event_id) on delete set null,
    acquisition_text text,
    owner_file text not null,
    drive_file_id text,
    drive_revision text,
    source_block_id text,
    content_hash text,
    projection_scope text,
    payload jsonb not null default '{}'::jsonb,
    authority text not null default 'DRIVE' check (authority = 'DRIVE'),
    synced_at timestamptz not null default now()
);

create index if not exists canon_entities_type_status_idx
    on public.canon_entities(entity_type, canon_status, activation_status);
create index if not exists canon_entities_scope_idx
    on public.canon_entities(projection_scope, owner_file);
create index if not exists canon_aliases_entity_idx
    on public.canon_aliases(entity_id);
create index if not exists canon_references_source_idx
    on public.canon_references(source_entity_id, ref_role);
create index if not exists canon_references_target_idx
    on public.canon_references(target_entity_id, ref_role);
create index if not exists canon_relations_source_idx
    on public.canon_relations(source_entity_id, relation_type);
create index if not exists canon_relations_target_idx
    on public.canon_relations(target_entity_id, relation_type);
create index if not exists scenario_links_scenario_idx
    on public.scenario_links(scenario_id, link_type);
create index if not exists scenario_links_target_idx
    on public.scenario_links(target_entity_id, link_type);
create index if not exists timeline_events_date_idx
    on public.timeline_events(game_year, game_month, game_day);
create index if not exists timeline_event_entities_entity_idx
    on public.timeline_event_entities(entity_id, event_id);
create index if not exists knowledge_items_subject_idx
    on public.knowledge_items(subject_entity_id, information_kind);
create index if not exists knowledge_assignments_holder_idx
    on public.knowledge_assignments(holder_ref, knowledge_state);

-- V2 remains server-side only. No player/browser Data API access is introduced.
revoke all on table public.canon_projection_runs from public, anon, authenticated;
revoke all on table public.canon_aliases from public, anon, authenticated;
revoke all on table public.canon_references from public, anon, authenticated;
revoke all on table public.canon_relations from public, anon, authenticated;
revoke all on table public.scenario_links from public, anon, authenticated;
revoke all on table public.timeline_events from public, anon, authenticated;
revoke all on table public.timeline_event_entities from public, anon, authenticated;
revoke all on table public.knowledge_items from public, anon, authenticated;
revoke all on table public.knowledge_assignments from public, anon, authenticated;

grant select, insert, update, delete on table public.canon_projection_runs to service_role;
grant select, insert, update, delete on table public.canon_aliases to service_role;
grant select, insert, update, delete on table public.canon_references to service_role;
grant select, insert, update, delete on table public.canon_relations to service_role;
grant select, insert, update, delete on table public.scenario_links to service_role;
grant select, insert, update, delete on table public.timeline_events to service_role;
grant select, insert, update, delete on table public.timeline_event_entities to service_role;
grant select, insert, update, delete on table public.knowledge_items to service_role;
grant select, insert, update, delete on table public.knowledge_assignments to service_role;

alter table public.canon_projection_runs enable row level security;
alter table public.canon_aliases enable row level security;
alter table public.canon_references enable row level security;
alter table public.canon_relations enable row level security;
alter table public.scenario_links enable row level security;
alter table public.timeline_events enable row level security;
alter table public.timeline_event_entities enable row level security;
alter table public.knowledge_items enable row level security;
alter table public.knowledge_assignments enable row level security;

comment on table public.canon_projection_runs is
'Operational audit log for derived Drive-to-Supabase projection runs. It is not canon.';
comment on table public.canon_relations is
'Derived graph of relations explicitly owned by the active Drive corpus. No inferred relation becomes canon here.';
comment on table public.scenario_links is
'Derived scenario/arc links. A linked scene or consequence remains preparation unless Drive says it was played.';
comment on table public.knowledge_items is
'Derived epistemic projection. Truth, rumor, lie, suspicion and actor knowledge remain distinct.';
comment on table public.knowledge_assignments is
'Who knows/believes/suspects a knowledge item according to Drive. Existence in Supabase does not grant knowledge.';
comment on table public.timeline_events is
'Derived chronology. Prepared future events remain preparation and cannot update the current campaign checkpoint.';
