# Skill Authoring Policy

## Purpose

When the self-evolution loop creates, modifies, or evaluates repo-scoped skills, it should reuse the Anthropic `skill-creator` workflow instead of inventing a one-off process.

Upstream reference:

- https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md
- Raw URL for direct inspection: https://raw.githubusercontent.com/anthropics/skills/main/skills/skill-creator/SKILL.md

## Applies When

- Creating a new `.agents/skills/*/SKILL.md` file.
- Editing an existing `.agents/skills/*/SKILL.md` file.
- Moving repeated harness feedback into a reusable skill.
- Evaluating whether a skill triggers correctly or improves task outcomes.

## Required Workflow

1. Capture intent before writing.
   - What should the skill enable?
   - When should it trigger?
   - What output format or behavior should it produce?
   - What success evidence or eval prompts are appropriate?
2. Write the skill with strong trigger metadata.
   - `name` and `description` are required.
   - The `description` must include both what the skill does and when to use it.
   - Prefer clear, slightly proactive trigger wording to avoid under-triggering.
3. Use progressive disclosure.
   - Keep the main `SKILL.md` focused.
   - Put large details in `references/`, deterministic helpers in `scripts/`, reusable files in `assets/` or templates.
   - Tell the agent when to read each bundled resource.
4. Add or update realistic eval prompts when the skill behavior is testable.
   - Use 2-3 prompts for small changes.
   - Compare expected behavior with and without the skill when practical.
   - If evals are skipped, record why in the report.
5. Iterate from evidence.
   - Review outputs qualitatively.
   - Use objective assertions for file transforms, extraction, code generation, or fixed workflows.
   - Improve the skill based on observed failures, not temporary task history.
6. Keep the starter generic.
   - Do not store project-specific residue, personal names, local paths, or stale task progress in reusable skills.
   - Do not add surprising, unsafe, or hidden behavior.

## Harness-Specific Placement

- Repo-scoped skills live under `.agents/skills/<skill-name>/SKILL.md`.
- Executable Codex role instructions live under `.codex/agents/*.toml`, not inside skills.
- Harness policy/gate/planning rules live under `.harness/`.
- If a skill change needs a durable rule, update this policy or the relevant gate instead of duplicating guidance in multiple skills.

## Evidence Required For Skill Changes

Report:

- Skill path changed.
- Trigger intent and expected use case.
- Evals or smoke prompts used, or why they were skipped.
- Relevant harness checks run.
- Any follow-up needed for larger benchmark coverage.
