# Agent Routing Map

Use this file as a short entry point for Codex and other coding agents. The harness source of truth is `.harness/`.

## Required Startup

1. Read `.harness/README.md`.
2. Read `.harness/config.yaml`.
3. Read `.harness/bootstrap.md`.
4. Select the narrowest role from `.harness/agents/`.
5. Load only the `.harness/policies/`, `.harness/gates/`, planning files, and templates that apply to the user request.

## Role Routing

- Planning, task selection, acceptance criteria: `.harness/agents/pm.md`
- Technical approach, sequencing, cross-file scope: `.harness/agents/tech-lead.md`
- Implementation work: `.harness/agents/implementer.md`
- Requirements review: `.harness/agents/spec-reviewer.md`
- Verification and evidence review: `.harness/agents/quality-reviewer.md`
- Architecture and dependency review: `.harness/agents/architecture-reviewer.md`
- Branch and PR hygiene: `.harness/agents/branch-manager.md`
- Harness improvement work: `.harness/agents/self-evolution.md`

## Default Rules

- Keep durable harness guidance under `.harness/`.
- Prefer the project's local conventions after they are defined.
- Run the checks listed in `.harness/config.yaml` when relevant.
- Report changed files, checks run, skipped checks, assumptions, and follow-up work.
