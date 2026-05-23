# AI Development Harness Starter

This repository is a generic starter template for a repo-first AI development harness. It gives coding agents and humans a shared operating model for planning, implementation, review, verification, and controlled process improvement.

The harness source of truth lives in `.harness/`. Root files such as this README and `AGENTS.md` are entry points and routing maps; durable policies, gates, agent roles, planning data, templates, and decision records belong under `.harness/`.

## Start A New Project

1. Create a new repository from this starter.
2. Replace placeholder project language with your project name, stack, and commands.
3. Read `.harness/README.md` and `.harness/bootstrap.md`.
4. Update `.harness/config.yaml` with project-specific checks.
5. Replace the example planning entries in `.harness/planning/*.yaml`.
6. Keep secrets out of the repo and use local environment files ignored by `.gitignore`.
7. Run the harness checks before opening a PR.

## Agent Startup

Coding agents should start with `AGENTS.md` for routing, then load `.harness/bootstrap.md` and only the `.harness` files relevant to the requested role and task.

Default order:

1. `AGENTS.md`
2. `.harness/README.md`
3. `.harness/config.yaml`
4. `.harness/bootstrap.md`
5. relevant `.harness/agents/<role>.md`
6. relevant `.harness/policies/*.md`
7. relevant `.harness/gates/*.md`
8. relevant `.harness/planning/*.yaml`

## Checks

Run these starter checks from the repository root:

```bash
python scripts/check_docs_harness.py
python scripts/harness/check_planning_graph.py
python scripts/harness/check_harness_contract.py
python scripts/harness/check_documentation_policy.py
git diff --check
```

Projects should add their own test, lint, typecheck, security, and build commands to `.harness/config.yaml`.

## Safe Adaptation

- Change `.harness` first when the operating model changes.
- Record lasting decisions in `.harness/decisions/`.
- Keep planning state in `.harness/planning/`.
- Convert repeated review or CI failures into stronger checks, gates, templates, or policies.
- Keep `AGENTS.md` short and route agents to `.harness` instead of duplicating harness instructions.
- Do not put secrets, machine-local paths, personal workflow notes, or vendor-specific assumptions into the starter.

