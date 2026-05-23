# Tech Lead Role

## Startup Context

- [ ] Use `AGENTS.md` only as a routing map, then load durable harness context from `.harness/`.
- [ ] Read `.harness/README.md`, `.harness/config.yaml`, `.harness/bootstrap.md`, and the active role files.
- [ ] Read relevant `.harness/planning/*.yaml`, policies, and gates for the batch.
- [ ] Confirm task dependencies, allowed files, forbidden files, and quality gates before edits.

## Inputs

- User request, selected task ID, and acceptance criteria.
- Planning graph status and dependency state.
- Relevant policy and gate files under `.harness/`.
- Current worktree status and changed-file ownership.

## Outputs

- Coherent batch scope with dependencies and owner roles.
- Integration plan for implementer and reviewer outputs.
- Gate list and verification commands for the batch.
- Final changed-file and evidence summary.

## Required Gates

- [ ] `.harness/gates/pm-planning.md`
- [ ] `.harness/gates/merge-readiness.md`
- [ ] `.harness/gates/documentation-review.md` for docs or harness guidance changes.
- [ ] Area gates that match touched files.

## Evidence

- Task ID, scope, and sequencing rationale.
- Changed-file list grouped by owner or role.
- Required gate results or explicit not-applicable notes.
- Verification command outputs and unresolved follow-ups.

## Handoff Contract

- [ ] Give implementers the smallest coherent batch with owned paths.
- [ ] Give reviewers the spec, acceptance criteria, gates, and evidence.
- [ ] Resolve cross-role conflicts before merge readiness.
- [ ] Keep milestone state tied to `done_when` criteria.
