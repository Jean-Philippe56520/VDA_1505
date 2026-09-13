-- Cover foreign keys reported by the Supabase database linter.

create index if not exists knowledge_assignments_item_idx
    on public.knowledge_assignments(item_id);

create index if not exists knowledge_assignments_acquisition_event_idx
    on public.knowledge_assignments(acquisition_event_id)
    where acquisition_event_id is not null;
