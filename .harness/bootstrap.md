# Harness Bootstrap Contract

## Scope

- Harness-aware agents load durable guidance from `.harness/`.
- `AGENTS.md` is a routing map into the harness when present.
- `.harness/bootstrap.md` defines the minimum startup contract after the entry points are found.
- Config, role, policy, gate, template, and planning files marked required by config must exist.

## Core Source Of Truth

- `.harness/README.md` = entry point and file map.
- `.harness/bootstrap.md` = agent startup contract.
- `.harness/config.yaml` = machine-readable manifest.
- `.harness/decisions/0001-harness-operating-model.md` = operating principles.
- `.harness/decisions/0002-starter-adaptation-roadmap.md` = starter adaptation roadmap.
- `.harness/planning/*.yaml` = planning graph examples or project planning state.

## Minimum Startup Order

1. `AGENTS.md` when present.
2. `.harness/README.md`.
3. `.harness/config.yaml`.
4. `.harness/bootstrap.md`.
5. Relevant `.harness/agents/<role>.md`.
6. Relevant `.harness/policies/*.md`.
7. Relevant `.harness/gates/*.md`.
8. Relevant `.harness/planning/*.yaml`.

## Role Categories

- `pm`: shape intent, acceptance criteria, milestones, and dependency-aware task order.
- `tech-lead`: coordinate approach, sequencing, ownership, and cross-area decisions.
- `branch-manager`: manage branch hygiene, integration readiness, and PR flow.
- `implementer`: make scoped changes that satisfy accepted criteria.
- `spec-reviewer`: review requirements, specs, and tasks for clarity and completeness.
- `quality-reviewer`: verify checks, evidence, regressions, and acceptance coverage.
- `architecture-reviewer`: assess boundaries, dependencies, and long-term fit.
- `self-evolution`: improve harness guidance and checks through controlled harness work.

## Before Editing Checklist

- [ ] Confirm user request, active planning task, or decision record.
- [ ] Confirm allowed and forbidden files.
- [ ] Run `git status`.
- [ ] Load relevant `.harness` source-of-truth files.
- [ ] Identify required checks before editing.
- [ ] Preserve user changes already present in the worktree.

## Required Outputs And Evidence

- [ ] Changed files.
- [ ] Checks run and results.
- [ ] Skipped checks with reason.
- [ ] Assumptions or unresolved follow-up work.
- [ ] Confirmation that project-specific checks were used when configured.

## Failure Behavior

- Stop when `.harness/README.md` is missing.
- Stop when `.harness/bootstrap.md` is missing.
- Stop when `.harness/config.yaml` exists but cannot be parsed.
- Stop when config marks a file required and it is missing.
- Continue when optional project-specific files are absent from a fresh starter.
- Report each failure with the exact path and blocked startup step.

