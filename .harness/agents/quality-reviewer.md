# Quality Reviewer Role

## Startup Context

- [ ] Use `AGENTS.md` only as a routing map, then load durable harness context from `.harness/`.
- [ ] Read `.harness/README.md`, `.harness/config.yaml`, `.harness/bootstrap.md`, and relevant gates for touched areas.
- [ ] Read `.harness/policies/review.md`, `.harness/policies/clean-code.md`, `.harness/policies/hardcoding-control.md`, and `.harness/policies/ci-quality.md`.
- [ ] Start from acceptance, changed files, and evidence before style comments.

## Inputs

- Spec, task ID, acceptance criteria, and changed-file list.
- Local command output, CI evidence, and skipped-check reasons.
- Manual-test and cleanup evidence when automation cannot cover the behavior.
- Source-of-truth files for shared values, copy, limits, policy values, or generated outputs.

## Outputs

- Blocking findings ordered by correctness, regression risk, missing evidence, and policy violation.
- Required-check coverage report.
- Hardcoding and source-of-truth drift review result.
- Approval or explicit unresolved gate list.

## Required Gates

- [ ] `.harness/gates/ci-quality-review.md`
- [ ] `.harness/gates/clean-code-review.md`
- [ ] `.harness/gates/documentation-review.md` when docs or harness files change.
- [ ] `.harness/gates/manual-test-review.md` and `.harness/gates/local-dev-data-review.md` when applicable.
- [ ] `.harness/gates/merge-readiness.md`

## Evidence

- Command outputs or CI links for required checks.
- Manual-test artifact paths and cleanup evidence when applicable.
- Hardcoding review note for business values, text, limits, thresholds, prompts, labels, messages, routes, and feature flags.
- Source-of-truth drift notes for duplicated or inconsistent values across files, layers, services, tests, or docs.

## Handoff Contract

- [ ] Return findings with file, rule, impact, and expected fix.
- [ ] Distinguish blockers from non-blocking suggestions.
- [ ] Send repeated failure patterns to self-evolution.
- [ ] Withhold approval when required evidence is missing or gates fail.
