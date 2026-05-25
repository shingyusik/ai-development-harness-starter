---
name: harness-planning
description: Use for roadmap, milestone, task graph, dependency, and acceptance-criteria work under .harness/planning.
---

# Harness Planning

Use this skill when editing or reviewing `.harness/planning/*.yaml`.

## Inputs

- `.harness/planning/roadmap.yaml`
- `.harness/planning/milestones.yaml`
- `.harness/planning/tasks.yaml`
- `.harness/agents/pm.md`
- `.harness/gates/pm-planning.md`

## Steps

1. Identify the requested planning change and the affected roadmap, milestone, or task IDs.
2. Preserve dependency direction and avoid orphaning tasks.
3. Keep acceptance criteria concrete and checkable.
4. Separate planning state from implementation logs or temporary task diary entries.
5. Run `python scripts/harness/check_planning_graph.py` after any planning YAML edit.
6. Also run documentation/harness checks when planning changes affect docs, gates, or policies.

## Output

Report changed planning IDs, dependency changes, validation commands, skipped checks, and unresolved decisions.
