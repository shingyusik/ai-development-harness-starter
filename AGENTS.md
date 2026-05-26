# Project Agent Entry Point

This repository uses a skill-first harness entrypoint.

Start harness-scoped work through:

- `/harness <task>`
- `$harness <task>`

Source-of-truth locations:

- Command entry skill: `.agents/skills/harness/SKILL.md`
- Bootstrap procedure: `.agents/skills/harness-bootstrap/SKILL.md`
- Codex roles/subagents: `.codex/agents/*.toml`
- Role registry: `.harness/roles.yaml`
- Harness policy/gates/planning: `.harness/`
- Repo skills: `.agents/skills/*/SKILL.md`
