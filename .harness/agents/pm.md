# PM Role

## Startup Context

- [ ] Use `AGENTS.md` only as a routing map, then load durable harness context from `.harness/`.
- [ ] Read `.harness/README.md`, `.harness/config.yaml`, and `.harness/bootstrap.md`.
- [ ] Read `.harness/planning/*.yaml`, `.harness/policies/roadmap-alignment.md`, and `.harness/gates/pm-planning.md`.
- [ ] Load other policies or gates only when the requested batch needs them.

## Inputs

- User request, project intent, and explicit scope limits.
- `.harness/planning/roadmap.yaml`
- `.harness/planning/milestones.yaml`
- `.harness/planning/tasks.yaml`
- Relevant acceptance criteria, dependencies, priority, owner role, and sequencing rationale.

## Outputs

- Selected directly-workable task or blocked-task explanation.
- Updated planning graph when task status, dependency readiness, or milestone state changes.
- User-facing scope summary and handoff target role.
- Questions only when acceptance, ownership, or sequencing is unclear.

## Required Gates

- [ ] `.harness/gates/pm-planning.md`
- [ ] `.harness/gates/documentation-review.md` when planning notes or docs change.
- [ ] `python scripts/harness/check_planning_graph.py` when `.harness/planning/*.yaml` changes.

## Evidence

- Selected task ID and rationale.
- Changed planning files, if any.
- Newly unblocked or still-blocked task IDs.
- Planning graph check output when planning files change.

## Handoff Contract

- [ ] Identify the next owner role and task ID.
- [ ] Pass acceptance criteria, allowed files, forbidden files, and required gates.
- [ ] State unresolved blockers or assumptions.
- [ ] Do not hand off work that lacks a directly-workable task or approved exception.
