# Roadmap Alignment Policy

## Purpose

- Select work from the planning graph instead of ad hoc memory.
- Keep task priority, dependencies, and sequencing rationale explicit.
- Update downstream readiness when dependencies are completed.

## Rules

- Roadmap, milestone, and task state live in `.harness/planning/*.yaml`.
- The next task must be directly workable: all dependencies are done or the task is explicitly ready.
- Priority order guides selection, with dependency blockers handled before optional work.
- Each task records rationale, acceptance criteria, owner role, and sequencing rationale.
- Completing a task updates tasks it unblocks from `blocked` to `ready` when all dependencies are done.
- Tasks with unfinished dependencies remain `blocked`.
- Milestone status reflects done_when criteria, not optimism.
- Planning graph changes must pass the planning graph checker.

## Review Checks

- [ ] The selected task is present in `.harness/planning/tasks.yaml`.
- [ ] Dependency status supports the selected task state.
- [ ] Unblocked tasks were advanced to `ready` only when all dependencies are done.
- [ ] Blocked tasks with remaining dependencies stayed blocked.
- [ ] Milestone status is justified by done_when text.

## Gate Evidence

- Diff for `.harness/planning/*.yaml`.
- Output from `python scripts/harness/check_planning_graph.py`.
- Brief sequencing rationale for the selected batch.
- List of newly unblocked tasks.
