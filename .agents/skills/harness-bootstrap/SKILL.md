---
name: harness-bootstrap
description: Use when a user invokes the harness entry command such as /harness, /harness-start, or $harness-bootstrap, or when starting any Codex task under this repo's harness. This skill is the primary user-facing way to enter harness mode: discover project context, load the harness contract, choose the narrowest Codex role, and run/report the required checks without putting bootstrap instructions in AGENTS.md.
---

# Harness Bootstrap

This is the user-facing entry skill for working under the harness. Treat it as the command target behind a slash command such as `/harness <task>` or the direct skill invocation `$harness-bootstrap <task>`.

Keep `AGENTS.md` thin. Do not move this startup sequence back into `AGENTS.md`, `AGENT.md`, `CLAUDE.md`, or `.harness/agents/`.

## What this skill does

- Turns a user request into a harness-scoped task.
- Discovers project context from the repository instead of relying on a long root instruction file.
- Loads only the harness files needed for the task.
- Routes work to the narrowest Codex custom agent in `.codex/agents/*.toml` through `.harness/roles.yaml`.
- Applies repo skills from `.agents/skills/*/SKILL.md` only when relevant.
- Reports checks, assumptions, skipped checks, and follow-up.

## Entry commands

Preferred user flows:

- `/harness <task>`: user-facing slash command, if the client maps slash commands to repo skills.
- `/harness-start <task>`: explicit bootstrap alias, if available.
- `$harness-bootstrap <task>`: direct Codex skill invocation.

If no slash-command integration exists yet, tell users to invoke `$harness-bootstrap` directly. Do not duplicate the workflow in `AGENTS.md` just to simulate a command.

## Startup sequence

1. Restate the requested task in one sentence.
2. Run or inspect `git status --short` before editing and preserve unrelated user changes.
3. Discover project context from current repo files:
   - source paths, tests, build config, package manifests, runtime config, and architecture docs;
   - `.harness/config.yaml` required files, source-of-truth paths, and required checks;
   - `.harness/bootstrap.md` for the minimal runtime contract.
4. Read `.harness/roles.yaml` and choose the narrowest role:
   - `pm` for roadmap, milestone, task selection, acceptance criteria;
   - `tech_lead` for approach, sequencing, and cross-file scope;
   - `implementer` for scoped code/docs changes;
   - `spec_reviewer` for requirement/acceptance review;
   - `quality_reviewer` for evidence and merge readiness;
   - `architecture_reviewer` for dependency and boundary review;
   - `branch_manager` for branch, worktree, and PR hygiene;
   - `self_evolution` for harness policy, gate, template, script, Codex agent, or skill changes.
5. Read the selected role's `.codex/agents/*.toml` and only the `reads` paths listed for that role.
6. Load additional `.harness/policies/*.md`, `.harness/gates/*.md`, `.harness/planning/*.yaml`, templates, or `.agents/skills/*/SKILL.md` only when the task needs them.
7. Execute the task in the smallest coherent slice.
8. Run relevant checks from `.harness/config.yaml`; include `git diff --check` for file edits.
9. Report using the required output shape below.

## Role and skill boundary

- `.codex/agents/*.toml` defines executable Codex roles/subagents.
- `.agents/skills/*/SKILL.md` defines reusable procedures such as bootstrap, planning, review gates, and self-evolution.
- `.harness/roles.yaml` binds harness roles to Codex agents and policy/gate/planning files.
- `.harness/` stores policy, gates, planning, templates, and registry data.
- `.harness/agents/` is forbidden in this Codex-first harness.

## Project-context policy

Do not require a long root `AGENTS.md` for project setup. When adapting this starter to a real project, put stable project-specific data in checkable harness files instead:

- required checks and source paths: `.harness/config.yaml`
- roadmap/milestones/tasks: `.harness/planning/*.yaml`
- durable rules: `.harness/policies/*.md`
- review criteria: `.harness/gates/*.md`
- reusable workflows: `.agents/skills/*/SKILL.md`
- runtime roles: `.codex/agents/*.toml`

`AGENTS.md` may remain as a tiny pointer telling Codex where the entry skill lives, but it should not contain the full harness operating manual.

## When changing skills

If the task creates or edits `.agents/skills/*/SKILL.md`, read `.harness/policies/skill-authoring.md` first and follow the upstream Anthropic `skill-creator` workflow referenced there:

- capture intent and trigger conditions;
- write strong description metadata;
- use progressive disclosure with `references/`, `scripts/`, or assets when needed;
- add realistic eval prompts or record why evals are skipped;
- iterate from evidence rather than one-off task history.

## Required report shape

Always end with:

- Changed files.
- Role used and why.
- Checks run and results.
- Skipped checks and reasons.
- Assumptions.
- Follow-up work.

## Common pitfalls

1. Loading every harness file. Read the role binding first, then load only relevant files.
2. Recreating `.harness/agents/`. Codex-first role definitions belong in `.codex/agents/*.toml`.
3. Turning temporary task progress into a permanent skill or policy. Only durable, reusable rules belong in the harness.
4. Treating slash-command absence as a reason to expand `AGENTS.md`. Use `$harness-bootstrap` directly until slash-command wiring exists.
5. Trusting subagent output without parent verification. Re-run targeted checks and inspect diffs before reporting success.
