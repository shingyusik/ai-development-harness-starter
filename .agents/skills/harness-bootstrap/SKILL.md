---
name: harness-bootstrap
description: Use when starting any Codex task in this repository or adapting the starter to a project; loads the repo-first harness contract, config, role routing, checks, and reporting expectations.
---

# Harness Bootstrap

Use this skill before scoped development, review, or planning work in a project that contains this starter.

## Steps

1. Read `AGENTS.md` for project-specific source paths, test/build commands, and architecture constraints.
2. Read `.harness/config.yaml` to find required files, checks, and source-of-truth paths.
3. Read `.harness/bootstrap.md` for the runtime contract.
4. Choose the narrowest role from `.harness/agents/*.md` and read only that role file.
5. Read only the policies, gates, planning files, or templates needed for the task.
6. Before editing, run `git status --short` and preserve unrelated user changes.
7. Report changed files, checks run, skipped checks with reasons, assumptions, and follow-up.

## Boundaries

- Do not duplicate durable harness guidance outside `.harness/`.
- Do not treat `README.md` as runtime source of truth; it is human-facing starter documentation.
- Do not commit or push unless the user explicitly asks or the current workflow requires it.
