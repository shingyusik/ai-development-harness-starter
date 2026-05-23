# Manual Test Review Gate

## Inputs

- `.harness/policies/manual-testing.md`
- Changed behavior and automation evidence.
- Manual or browser-assisted test artifact when automation has a gap.

## Required Checks

- [ ] Prefer automated coverage before accepting manual-only evidence.
- [ ] Create a standalone artifact when behavior cannot be fully automated.
- [ ] Include tester or tool, scope, preconditions, and environment.
- [ ] Write exact repeatable steps.
- [ ] Record observations tied to the requested behavior.
- [ ] Define observable pass criteria.
- [ ] Attach evidence such as screenshots, logs, traces, browser notes, or user confirmation.
- [ ] Record cleanup steps, final state, and follow-up for unresolved gaps.

## Evidence

- Path to the manual test artifact.
- Relevant automated test output or automation-gap rationale.
- Evidence artifact paths or links.
- Cleanup confirmation and linked follow-up task when needed.

## Fails When

- Manual testing replaces practical automated coverage.
- Steps, observations, or pass criteria are too vague to repeat.
- Evidence is missing or not tied to the behavior.
- Test-created data lacks cleanup evidence.
- Failed, blocked, or partial results have no follow-up.
