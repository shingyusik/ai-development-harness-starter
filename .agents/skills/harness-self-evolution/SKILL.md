---
name: harness-self-evolution
description: Use when repeated failures or user feedback indicate the starter needs a new policy, gate, template, check, or Codex agent/skill update.
---

# Harness Self Evolution

Use this skill to improve the harness itself without turning one-off task history into permanent guidance.

## Trigger conditions

- A repeated failure would be prevented by a policy, gate, template, or script.
- The user corrects a workflow assumption.
- A Codex agent or repo skill is missing, too broad, or outdated.
- A starter file contains project-specific residue.

## Steps

1. Read `.harness/agents/self-evolution.md` and `.harness/gates/self-evolution.md`.
2. Identify the smallest durable change: policy, gate, template, script, `.codex/agents/*.toml`, or `.agents/skills/*/SKILL.md`.
3. Prefer checkable rules over long prose.
4. Keep the starter generic; do not record temporary task progress.
5. Run relevant harness checks and `git diff --check`.
6. Report what changed and what future failure it prevents.
