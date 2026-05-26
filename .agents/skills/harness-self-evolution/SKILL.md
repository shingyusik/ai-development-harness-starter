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

1. Read `.harness/roles.yaml`, `.harness/policies/self-evolution.md`, and `.harness/gates/self-evolution.md`.
2. Identify the smallest durable change: policy, gate, template, script, `.codex/agents/*.toml`, or `.agents/skills/*/SKILL.md`.
3. If creating or modifying `.agents/skills/*/SKILL.md`, read `.harness/policies/skill-authoring.md` and apply the upstream Anthropic `skill-creator` workflow linked there: capture intent, write strong trigger metadata, use progressive disclosure, add eval prompts when useful, and iterate from evidence.
4. Prefer checkable rules over long prose.
5. Keep the starter generic; do not record temporary task progress.
6. Run relevant harness checks and `git diff --check`.
7. Report what changed and what future failure it prevents.
