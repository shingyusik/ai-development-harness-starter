# M1. Harness Spine and Bootstrap

Status: example
Priority: P0
Source: `.harness/decisions/0002-starter-adaptation-roadmap.md`
Owner role: tech-lead

## Objective

- Establish `.harness/` as the source of truth for harness guidance.
- Define how agents load harness context.
- Add contract checks so missing or misplaced harness files fail early.

## Scope

Included:

- `.harness/README.md`
- `.harness/CHANGELOG.md`
- `.harness/config.yaml`
- `.harness/bootstrap.md`
- `.harness/decisions/*.md`
- `.harness/planning/*.yaml`
- `scripts/harness/check_harness_contract.py`

Excluded:

- Project application code.
- Project-specific infrastructure.
- External dashboard automation.
- Secrets or local machine configuration.

## Acceptance

- Required spine files exist.
- Bootstrap contract routes agents into `.harness`.
- Config lists starter checks.
- Harness contract check passes.
- Planning graph check passes against example planning files.

