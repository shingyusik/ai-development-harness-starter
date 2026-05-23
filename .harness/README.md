# AI Development Harness Starter

## Purpose

- Keep AI development guidance self-contained in `.harness/`.
- Define how agents start, choose roles, plan work, verify changes, and improve the harness over time.
- Provide generic policies, gates, planning files, templates, and decision records that each project can adapt.
- Keep root files as entry points and routing maps, not duplicated harness manuals.

## Startup Order

1. Read `AGENTS.md` for the short routing map when present.
2. Read `.harness/README.md`.
3. Read `.harness/config.yaml`.
4. Read `.harness/bootstrap.md`.
5. Read the relevant `.harness/agents/<role>.md` file.
6. Read the relevant `.harness/policies/*.md` files.
7. Read the relevant `.harness/gates/*.md` files.
8. Read the relevant `.harness/planning/*.yaml` entries.

## File Map

- `.harness/README.md`: harness entry point.
- `.harness/bootstrap.md`: agent startup contract.
- `.harness/config.yaml`: machine-readable manifest and check list.
- `.harness/CHANGELOG.md`: harness-level change log.
- `.harness/decisions/`: accepted or proposed harness decisions.
- `.harness/planning/`: roadmap, milestone, and task graph examples.
- `.harness/agents/`: role-specific operating guidance.
- `.harness/policies/`: durable rules.
- `.harness/gates/`: review and verification gates.
- `.harness/manual-tests/`: manual or assisted test evidence.
- `.harness/templates/`: reusable evidence and report templates.

## Source Of Truth

- Harness guidance lives in `.harness/`.
- Project-specific application docs may live elsewhere after a project defines them.
- `AGENTS.md` routes agents into the harness but does not replace `.harness`.
- Repeated failures should improve a policy, gate, check, template, or planning entry.

## Customization Checklist

- [ ] Replace placeholder project name and commands.
- [ ] Update `.harness/config.yaml` with project checks.
- [ ] Replace example planning entries with real milestones and tasks.
- [ ] Add project-specific architecture, security, release, and operations policies only when needed.
- [ ] Keep private workflow notes, local machine paths, and secrets out of the repo.

