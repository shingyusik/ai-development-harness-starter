# Starter Migration Notes

## Purpose

Use this file only when adapting the starter into an existing repository that already has process or agent documentation.

## Classification Rules

- `migrate`: durable generic harness guidance that belongs under `.harness`.
- `project-doc`: current project architecture, operations, or domain knowledge that belongs in project docs.
- `retire`: stale, duplicate, or process-diary material that should not be carried forward.

## Migration Guardrails

- Keep `.harness` as the source of truth for harness guidance.
- Keep root docs short and current-state focused.
- Preserve source paths when importing existing guidance.
- Avoid importing private workflow notes, local paths, personal names, credentials, or vendor assumptions.
- Add mechanical checks when a migrated rule should be enforced.
