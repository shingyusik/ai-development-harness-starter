# AI Development Harness Operating Model

Status: accepted
Date: 2026-05-24
Scope: generic repo-first AI development harness starter.

## Decision

This starter keeps AI development guidance in `.harness/` and treats the repository as the source of truth for planning, implementation, review, verification, and harness self-evolution.

Root files such as `README.md` and `AGENTS.md` orient humans and agents, but durable rules belong under `.harness/`.

## Operating Loop

1. Align with the user request and planning graph.
2. Select the narrowest agent role.
3. Load only relevant policies, gates, templates, and planning entries.
4. Make scoped changes.
5. Run relevant checks.
6. Record evidence and follow-up work.
7. Improve the harness when repeated failures show a durable process gap.

## Planning Model

Planning state is kept in YAML so humans and agents can inspect it and scripts can validate it.

Required concepts:

- roadmap entries describe larger goals.
- milestones group work toward a roadmap goal.
- tasks carry status, priority, dependencies, owner role, rationale, acceptance criteria, and sequencing rationale.
- dependency status must match task status.
- repeated planning ambiguity should improve the planning templates or checks.

## Documentation Model

- Current-state docs describe how the project works now.
- Decision records explain accepted tradeoffs.
- Changelog entries record durable harness changes.
- Root docs avoid private process notes and local machine assumptions.
- Harness docs avoid project-specific vendor assumptions until a project intentionally adds them.

## Quality Model

- Gates translate policy into reviewable evidence.
- Checks enforce rules that can be made mechanical.
- Manual testing is recorded only when practical automation cannot cover the behavior.
- Project-specific test, lint, typecheck, security, and build commands are added by the adopting project.

## Self-Evolution

The harness changes when a failure pattern is repeated, high-impact, or cheaply preventable. Improvements should be small, durable, and placed in the policy, gate, check, template, or planning file that will catch the issue earlier next time.

