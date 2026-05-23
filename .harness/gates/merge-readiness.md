# Merge Readiness Gate

## Inputs

- Requested spec, task, issue, or PR description.
- Required gate results for changed areas.
- `.harness/config.yaml` `required_checks` manifest.
- `.harness/planning/*.yaml` and harness contract evidence when touched.
- CI, test, documentation, manual-test, and cleanup evidence.

## Required Checks

- [ ] Confirm the implementation matches the requested spec and acceptance criteria.
- [ ] Confirm changed files stay within approved scope.
- [ ] Confirm all required review gates have passed or are explicitly not applicable.
- [ ] Confirm required checks from `.harness/config.yaml` have evidence or documented skip reasons.
- [ ] Confirm tests and local quality checks cover the touched areas.
- [ ] Confirm CI required checks pass when CI is available.
- [ ] Confirm documentation updates are current-state-only and correctly located.
- [ ] Confirm hardcoding review passed for changed numbers, messages, limits, thresholds, prompts, labels, routes, and feature flags.
- [ ] Confirm shared values have one source of truth; split config/data files do not duplicate the same logical variable/message.
- [ ] Confirm manual-test artifacts exist for automation gaps.
- [ ] Confirm generated or test-created data was cleaned up or tracked.
- [ ] Confirm planning graph and harness contract checks pass when applicable.
- [ ] Confirm no required gate remains unresolved before merge.

## Evidence

- Spec, task, issue, or PR link.
- Changed-file list.
- Required-check manifest path: `.harness/config.yaml`.
- Test, CI, docs, planning, and harness command output.
- JSON/config source paths for shared values touched by the change and duplicate-check notes for split files.
- Manual-test artifact paths.
- Cleanup evidence and unresolved follow-up links.

## Fails When

- Acceptance criteria are incomplete or unverifiable.
- A required gate is failing, missing, or unresolved.
- CI or local required checks fail.
- Hardcoded shared values or user-facing messages remain in source code without approved local-only rationale.
- The same logical variable/message is duplicated across config/data files instead of sharing one source of truth.
- Manual-test or cleanup evidence is missing where required.
- Scope includes unrelated work without explicit approval.
