# Project Agent Entry Point

This repository uses a skill-first harness entrypoint.

Start harness-scoped work through the repo skill:

- Preferred user command: `/harness <task>` if your client maps slash commands to skills.
- Direct Codex skill invocation: `$harness-bootstrap <task>`.

`AGENTS.md` is intentionally thin. Do not put the harness operating manual here.

Source-of-truth locations:

- Bootstrap workflow: `.agents/skills/harness-bootstrap/SKILL.md`
- Codex roles/subagents: `.codex/agents/*.toml`
- Role registry: `.harness/roles.yaml`
- Harness policy/gates/planning: `.harness/`
- Repo skills: `.agents/skills/*/SKILL.md`

Do not create `.harness/agents/`; Codex-first executable roles belong in `.codex/agents/*.toml`.
