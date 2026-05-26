---
name: harness
description: "Use when the user enters /harness or asks to run a task under the repository harness. This skill is the command-facing entrypoint that loads the bootstrap procedure and starts the smallest suitable Codex role workflow."
---

# Harness

Use this skill as the user-facing `/harness <task>` or `$harness <task>` entrypoint.

## Steps

1. Treat the text after `/harness` as the task request.
2. Read `.agents/skills/harness-bootstrap/SKILL.md` for the harness procedure.
3. Follow that procedure exactly: inspect repo state, load the harness contract, choose the narrowest role, do the work, run checks, and report evidence.

## Output

Use the report shape from `harness-bootstrap`.
