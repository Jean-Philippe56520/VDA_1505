-- Bootstrap the runtime scene projection from an immutable CI-generated snapshot.
-- Canon authority is unchanged: this imports Git runtime preparation only.

create extension if not exists http with schema extensions;

create temporary table vda_runtime_snapshot_import (
    doc jsonb not null
) on commit drop;

insert into vda_runtime_snapshot_import (doc)
select content::jsonb
from extensions.http_get(
    'https://raw.githubusercontent.com/Jean-Philippe56520/VDA_1505/4708b02c595779c1b1ca7a195eab415862c7ce91/runtime_snapshot.json'
)
where status = 200;

do $$
declare
    snapshot jsonb;
    scene_count integer;
begin
    select doc into snapshot
    from vda_runtime_snapshot_import
    limit 1;

    if snapshot is null then
        raise exception 'Runtime snapshot download failed or returned non-200 status';
    end if;

    if snapshot->>'git_sha' <> '7ed09a124c2f41ec16bf9d65552ad3b6ad07359b' then
        raise exception 'Runtime snapshot git_sha mismatch: %', snapshot->>'git_sha';
    end if;

    if (snapshot->>'schema_version')::integer <> 1 then
        raise exception 'Unsupported runtime snapshot schema_version: %', snapshot->>'schema_version';
    end if;

    scene_count := jsonb_array_length(snapshot->'scenes');
    if scene_count <> 6 then
        raise exception 'Expected 6 runtime scenes, got %', scene_count;
    end if;

    if exists (
        select 1
        from jsonb_array_elements(snapshot->'scenes') as scene
        where scene->>'scene_id' is null
           or scene->'payload'->>'id' is distinct from scene->>'scene_id'
           or coalesce(scene->>'delivery_mode', '') not in ('group', 'individual')
           or scene->>'source_git_sha' is distinct from snapshot->>'git_sha'
    ) then
        raise exception 'Runtime snapshot scene validation failed';
    end if;

    if (
        select count(distinct scene->>'scene_id')
        from jsonb_array_elements(snapshot->'scenes') as scene
    ) <> scene_count then
        raise exception 'Runtime snapshot contains duplicate scene_id values';
    end if;
end
$$;

insert into public.published_scenes (
    scene_id,
    title,
    delivery_mode,
    intended_character_ref,
    schema_version,
    payload,
    source_kind,
    legacy_source_path,
    source_git_sha,
    published_at,
    enabled
)
select
    scene->>'scene_id',
    scene->>'title',
    scene->>'delivery_mode',
    nullif(scene->>'intended_character_ref', ''),
    coalesce((scene->>'schema_version')::integer, 1),
    scene->'payload',
    coalesce(scene->>'source_kind', 'git'),
    scene->>'legacy_source_path',
    scene->>'source_git_sha',
    now(),
    coalesce((scene->>'enabled')::boolean, true)
from vda_runtime_snapshot_import,
     lateral jsonb_array_elements(doc->'scenes') as scene
on conflict (scene_id) do update set
    title = excluded.title,
    delivery_mode = excluded.delivery_mode,
    intended_character_ref = excluded.intended_character_ref,
    schema_version = excluded.schema_version,
    payload = excluded.payload,
    source_kind = excluded.source_kind,
    legacy_source_path = excluded.legacy_source_path,
    source_git_sha = excluded.source_git_sha,
    published_at = excluded.published_at,
    enabled = excluded.enabled;

-- The http extension is needed only for this immutable bootstrap import.
drop extension if exists http;
