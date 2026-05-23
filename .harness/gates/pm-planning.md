# PM Planning Gate

## Inputs

- `.harness/planning/tasks.yaml`
- `.harness/planning/milestones.yaml`
- `.harness/planning/roadmap.yaml`
- `.harness/policies/roadmap-alignment.md`

## Required Checks

- [ ] Select the batch task from `.harness/planning/tasks.yaml`.
- [ ] Confirm every dependency for the selected task is `done` or the task is already `ready`.
- [ ] Respect priority order unless an explicit dependency blocker requires different sequencing.
- [ ] Confirm the selected task has `sequencing_rationale`.
- [ ] Keep tasks with unfinished dependencies `blocked`.
- [ ] Set downstream tasks to `ready` only when all dependencies are `done`.
- [ ] Update milestone status from `done_when` criteria, not expected future work.
- [ ] Keep roadmap state unchanged unless the batch explicitly owns roadmap planning.

## Evidence

- Diff for `.harness/planning/tasks.yaml`.
- Diff for `.harness/planning/milestones.yaml` when milestone status changes.
- Output from `python scripts/harness/check_planning_graph.py`.
- Selected task ID and any newly unblocked task IDs.

## Fails When

- The selected task is missing from `.harness/planning/tasks.yaml`.
- A task is `ready` or `active` while any dependency is not `done`.
- A task is `blocked` while all dependencies are `done`.
- Required `sequencing_rationale` is missing.
- Milestone status conflicts with its `done_when` criteria.
