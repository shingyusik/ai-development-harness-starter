# Worktree Policy

## Purpose

- Keep interacting edits isolated by branch or worktree lane.
- Reduce accidental overlap between parallel agents or humans.
- Integrate only after verification evidence exists.

## Rules

- Use one branch/worktree lane for each coherent implementation stream.
- Avoid simultaneous overlapping edits to the same files across lanes.
- Assign ownership before parallel work touches shared areas.
- Keep generated artifacts and dependency updates scoped to the lane that owns them.
- Verify each lane before integration.
- Integrate through the agreed branch/PR path after checks pass.
- Do not merge unrelated work just because it is nearby.
- Preserve user changes and coordinate before touching files outside the lane scope.

## Review Checks

- [ ] The branch/worktree maps to one coherent task or batch.
- [ ] File ownership is clear for interacting edits.
- [ ] Parallel lanes do not silently edit the same files.
- [ ] Verification ran before integration.
- [ ] Integration includes only intended files.

## Gate Evidence

- Branch/worktree name and task identifier.
- Owned file or module list for the lane.
- Verification output before integration.
- Final changed-file list.
