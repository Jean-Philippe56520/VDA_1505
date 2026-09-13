-- Read-only analytical surfaces over the Drive-authoritative projection.
-- security_invoker makes the views honor privileges/RLS of underlying tables.

create or replace view public.v_canon_relation_edges
with (security_invoker = true) as
select
    r.relation_id,
    r.relation_type,
    r.canon_status,
    r.activation_status,
    r.certainty,
    r.directed,
    r.source_entity_id,
    se.entity_type as source_entity_type,
    se.name as source_name,
    r.target_entity_id,
    te.entity_type as target_entity_type,
    te.name as target_name,
    r.owner_file,
    r.drive_revision,
    r.projection_scope,
    r.payload
from public.canon_relations r
join public.canon_entities se on se.entity_id = r.source_entity_id
join public.canon_entities te on te.entity_id = r.target_entity_id;

create or replace view public.v_scenario_graph
with (security_invoker = true) as
select
    l.scenario_id,
    s.name as scenario_name,
    s.canon_status as scenario_canon_status,
    s.activation_status as scenario_activation_status,
    l.link_id,
    l.link_type,
    l.role,
    l.canon_status as link_canon_status,
    l.target_entity_id,
    t.entity_type as target_entity_type,
    t.name as target_name,
    l.owner_file,
    l.drive_revision,
    l.projection_scope,
    l.payload
from public.scenario_links l
join public.canon_entities s on s.entity_id = l.scenario_id
join public.canon_entities t on t.entity_id = l.target_entity_id;

create or replace view public.v_actor_knowledge
with (security_invoker = true) as
select
    a.assignment_id,
    a.holder_ref,
    a.holder_kind,
    a.knowledge_state,
    a.reliability,
    a.acquisition_event_id,
    a.acquisition_text,
    k.item_id,
    k.information_kind,
    k.summary,
    k.subject_entity_id,
    k.canon_status as item_canon_status,
    k.verification_status,
    a.owner_file,
    a.drive_revision,
    a.projection_scope
from public.knowledge_assignments a
join public.knowledge_items k on k.item_id = a.item_id;

create or replace view public.v_entity_impact_links
with (security_invoker = true) as
select
    r.source_entity_id as entity_id,
    'relation'::text as link_domain,
    r.relation_type as link_role,
    r.target_entity_id as linked_entity_id,
    r.relation_id as source_record_id,
    r.canon_status,
    r.projection_scope
from public.canon_relations r
union all
select
    r.target_entity_id,
    'relation',
    r.relation_type,
    r.source_entity_id,
    r.relation_id,
    r.canon_status,
    r.projection_scope
from public.canon_relations r
union all
select
    l.scenario_id,
    'scenario',
    l.link_type,
    l.target_entity_id,
    l.link_id,
    l.canon_status,
    l.projection_scope
from public.scenario_links l
union all
select
    l.target_entity_id,
    'scenario',
    l.link_type,
    l.scenario_id,
    l.link_id,
    l.canon_status,
    l.projection_scope
from public.scenario_links l
union all
select
    ee.entity_id,
    'timeline',
    ee.role,
    ee.event_id,
    ee.event_id || ':' || ee.entity_id || ':' || ee.role,
    ev.canon_status,
    ee.projection_scope
from public.timeline_event_entities ee
join public.timeline_events ev on ev.event_id = ee.event_id
union all
select
    k.subject_entity_id,
    'knowledge_subject',
    k.information_kind,
    k.item_id,
    k.item_id,
    k.canon_status,
    k.projection_scope
from public.knowledge_items k
where k.subject_entity_id is not null;

revoke all on public.v_canon_relation_edges from public, anon, authenticated;
revoke all on public.v_scenario_graph from public, anon, authenticated;
revoke all on public.v_actor_knowledge from public, anon, authenticated;
revoke all on public.v_entity_impact_links from public, anon, authenticated;

grant select on public.v_canon_relation_edges to service_role;
grant select on public.v_scenario_graph to service_role;
grant select on public.v_actor_knowledge to service_role;
grant select on public.v_entity_impact_links to service_role;

comment on view public.v_actor_knowledge is
'Only explicit knowledge assignments. Absence of a row means no knowledge is attributed by the projection.';
comment on view public.v_entity_impact_links is
'Derived cross-reference surface for impact analysis. Links are navigational and do not themselves alter canon.';
