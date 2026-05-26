---
name: harness-bootstrap
description: "Use after the /harness entrypoint is selected, or when directly bootstrapping a task under this repository harness. Defines only the operational procedure: inspect state, load the contract, choose the narrowest role, execute one coherent slice, run checks, and report evidence."
---

# Harness Bootstrap

This skill defines the harness operating procedure. Keep it focused on what the agent does during a harness-scoped task.

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

1. Loading every harness file instead of role-bound files only.
2. Choosing a broad role when a narrower role fits.
3. Turning temporary task progress into permanent policy or skill text.
4. Trusting subagent output without parent verification.
