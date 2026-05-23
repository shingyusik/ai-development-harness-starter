# Branch Manager Role

## Startup Context

- [ ] Use `AGENTS.md` only as a routing map, then load durable harness context from `.harness/`.
- [ ] Read `.harness/README.md`, `.harness/config.yaml`, `.harness/bootstrap.md`, `.harness/policies/worktree.md`, and `.harness/policies/branch-ownership.md`.
- [ ] Read `.harness/gates/merge-readiness.md` before PR or integration work.
- [ ] Inspect git branch and `git status --short` before changes.

## Inputs

- Active branch, target branch, task ID, and owner role.
- Changed-file list and file ownership notes.
- Required verification evidence and CI status when available.
- PR requirements and repository merge policy.

## Outputs

- Branch/worktree hygiene assessment.
- Coherent commit grouping recommendation or commit set when requested.
- PR readiness notes, target branch, and unresolved blockers.
- Integration warnings for overlapping or unrelated changes.

## Required Gates

- [ ] `.harness/gates/merge-readiness.md`
- [ ] `.harness/gates/ci-quality-review.md`
- [ ] Branch and worktree policy checks.
- [ ] Relevant area checks from `.harness/config.yaml` before merge readiness.

## Evidence

- Branch name, target branch, task ID, and owner role.
- `git status --short` output.
- Changed-file list and commit grouping.
- Required check or CI evidence, with skip reasons when unavailable.

## Handoff Contract

- [ ] Keep feature, fix, harness, and docs work flowing to `develop` through PR.
- [ ] Keep `develop` to `main` integration on the approved PR path.
- [ ] Do not mix direct `main` and `develop` changes outside policy.
- [ ] Preserve unrelated user or peer changes and flag overlap before integration.
