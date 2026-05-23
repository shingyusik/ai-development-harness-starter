# Branch Ownership Policy

## Purpose

- Keep branch responsibilities explicit and reviewable.
- Prevent unsafe direct merges to shared branches.
- Avoid overlapping ownership across agents and workstreams.

## Rules

- Each branch has one primary owner role for the active batch.
- Feature, fix, harness, and docs branches merge to `develop` through PR.
- `develop` merges to `main` through PR.
- Do not merge directly into `develop` or `main` outside the approved PR path.
- Avoid assigning the same files to multiple owners unless coordination is explicit.
- Rebase, merge, or resolve conflicts only after inspecting affected user or peer changes.
- Do not revert unrelated changes to make the current branch easier.
- Branch state should be explainable from task, milestone, and changed files.

## Review Checks

- [ ] The branch has a clear owner and task scope.
- [ ] Shared branch changes are proposed through PR.
- [ ] Overlapping file ownership is resolved or documented.
- [ ] Conflict resolution preserves unrelated work.
- [ ] The changed-file list matches the branch purpose.

## Gate Evidence

- Branch name, owner role, and task identifier.
- PR link when merging to `develop` or `main`.
- Changed-file list.
- Notes for any coordinated overlapping ownership.
