# Documentation Policy

## Purpose

- Keep project documentation concise, current-state-only, and useful to agents and humans.
- Keep harness guidance under `.harness/`.
- Preserve source context for external references without creating process-note sprawl.

## Rules

- Project docs describe the current project behavior, architecture, operations, and run commands.
- Harness policies, roles, gates, templates, and changelog entries live under `.harness/`.
- Do not place harness manuals in `AGENTS.md`, `AGENT.md`, `CLAUDE.md`, or root project docs.
- Do not write docs as a task diary or implementation history.
- Avoid changelog phrases in current-state docs, including "previously" and "changed from".
- Prefer short sections, bullets, checklists, and field lists over long prose.
- Preserve external-source references when importing or condensing outside material.
- Prefer mechanical checks, scripts, gates, or tests over broad manual instructions.

## Review Checks

- [ ] The doc states current behavior or policy, not what a task just changed.
- [ ] Harness content is under `.harness/`; project docs remain project-focused.
- [ ] External material keeps enough source attribution to audit origin.
- [ ] Completed plans are not copied into durable docs as process history.
- [ ] Instructions are enforceable by a check, gate, script, or test when practical.

## Gate Evidence

- List of documentation files changed.
- Reason each changed doc belongs in its location.
- Source links or filenames for any imported external reference.
- Output from documentation policy checks when available.
