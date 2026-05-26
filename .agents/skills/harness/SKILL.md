---
name: harness
description: "Use when the user enters /harness or asks to run a task under the repository harness. This is the single harness entry skill: inspect state, load the contract, choose the narrowest Codex role, execute one coherent slice, run checks, and report evidence."
---

# Harness

Use this skill as the single user-facing `/harness <task>` or `$harness <task>` entrypoint.

Do not split command entry and bootstrap procedure into separate skills. The runtime contract stays in `.harness/bootstrap.md`; the executable skill entrypoint is this file.

## Procedure

1. Restate the requested task in one sentence.
2. Run or inspect `git status --short` before editing and preserve unrelated user changes.
3. Discover only the repo context needed for the task:
   - source paths, tests, build config, package manifests, runtime config, and architecture docs;
   - `.harness/config.yaml` required files, source-of-truth paths, and required checks;
   - `.harness/bootstrap.md` for the minimal runtime contract.
4. Read `.harness/roles.yaml` and choose the narrowest role:
   - `pm` for roadmap, milestone, task selection, and acceptance criteria;
   - `tech_lead` for approach, sequencing, and cross-file scope;
   - `implementer` for scoped code, docs, or script changes;
   - `spec_reviewer` for requirement and acceptance review;
   - `quality_reviewer` for evidence and merge readiness;
   - `architecture_reviewer` for dependency and boundary review;
   - `branch_manager` for branch, worktree, and PR hygiene;
   - `self_evolution` for harness policy, gate, template, script, Codex agent, or skill changes.
5. Read the selected role's `.codex/agents/*.toml` file and only the `reads` paths listed for that role.
6. Load additional `.harness/policies/*.md`, `.harness/gates/*.md`, `.harness/planning/*.yaml`, templates, or `.agents/skills/*/SKILL.md` only when the task needs them.
7. Execute the smallest coherent slice that satisfies the request.
8. Run relevant checks from `.harness/config.yaml`; include `git diff --check` for file edits.
9. Verify the result independently before reporting.

## Required Report Shape

Always end with:

- Changed files.
- Role used and why.
- Checks run and results.
- Skipped checks and reasons.
- Assumptions.
- Follow-up work.

## Common Pitfalls

1. Creating alias/bootstrap duplicate skills when one `harness` skill is enough.
2. Loading every harness file instead of role-bound files only.
3. Choosing a broad role when a narrower role fits.
4. Turning temporary task progress into permanent policy or skill text.
5. Trusting subagent output without parent verification.
