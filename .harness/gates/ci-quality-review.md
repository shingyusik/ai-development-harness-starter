# CI Quality Review Gate

## Inputs

- `.harness/policies/ci-quality.md`
- `.harness/config.yaml` `required_checks` manifest.
- Local quality command output.
- CI status or required-check evidence when available.
- Changed code, docs, planning, and harness files.

## Required Checks

- [ ] Identify required checks from `.harness/config.yaml` `required_checks`.
- [ ] Run relevant tests for changed behavior.
- [ ] Run lint, typecheck, and format checks where practical for touched areas.
- [ ] Run architecture checks when boundaries, imports, APIs, or data access are touched.
- [ ] Run docs checks when documentation policy can be mechanically checked.
- [ ] Run planning graph checks when `.harness/planning/*.yaml` changes.
- [ ] Run harness contract checks when `.harness/` structure changes.
- [ ] Link CI results or local command output for every required check that applies.
- [ ] Record skipped or unavailable required checks with reason and follow-up.

## Evidence

- Local command output for tests, lint, typecheck, format, architecture, docs, planning, and harness checks.
- CI run link or status summary.
- Required-check manifest path: `.harness/config.yaml`.
- Follow-up task for checks that should become automated.

## Fails When

- A relevant required check fails.
- Required-check evidence is missing without rationale.
- CI evidence is absent for merge readiness when CI is available.
- Skipped checks have no reason or follow-up.
- Repeated failures are not routed to a stronger check.
