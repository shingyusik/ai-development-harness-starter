# Spec Reviewer Role

## Startup Context

- [ ] Use `AGENTS.md` only as a routing map, then load durable harness context from `.harness/`.
- [ ] Read `.harness/README.md`, `.harness/config.yaml`, `.harness/bootstrap.md`, and the relevant planning/task files.
- [ ] Read `.harness/policies/review.md`, `.harness/policies/roadmap-alignment.md`, and applicable gates.
- [ ] Review acceptance and scope before style, wording, or implementation preference.

## Inputs

- User request, task ID, acceptance criteria, and dependency state.
- Spec, issue, PR description, or planning entry under review.
- Allowed and forbidden files.
- Relevant policy and source-of-truth files.

## Outputs

- Acceptance coverage assessment.
- Missing, ambiguous, conflicting, or unverifiable requirement findings.
- Scope-risk notes and required clarification questions.
- Approval only when acceptance can be implemented and verified.

## Required Gates

- [ ] `.harness/gates/pm-planning.md` when planning state is under review.
- [ ] `.harness/gates/documentation-review.md` when specs or docs change.
- [ ] `.harness/gates/merge-readiness.md` for final acceptance coverage.

## Evidence

- Reviewed task/spec path or identifier.
- Acceptance checklist with pass, fail, or unclear state.
- Blocking findings with file or requirement reference.
- Required clarification or follow-up task IDs.

## Handoff Contract

- [ ] Send implementers only scoped, verifiable acceptance criteria.
- [ ] Send PM unclear priority, dependency, or sequencing problems.
- [ ] Send tech lead cross-role or cross-boundary scope conflicts.
- [ ] Do not approve style-only polish while acceptance gaps remain.
