# Self-Evolution Role

## Startup Context

- [ ] Use `AGENTS.md` only as a routing map, then load durable harness context from `.harness/`.
- [ ] Read `.harness/README.md`, `.harness/config.yaml`, `.harness/bootstrap.md`, `.harness/policies/self-evolution.md`, and `.harness/gates/self-evolution.md`.
- [ ] Read only the policies, gates, scripts, templates, workflows, or skills related to the observed failure pattern.
- [ ] Confirm the work is harness-scoped before editing.

## Inputs

- Repeated or high-impact failure examples from review, CI, manual testing, production, or agent execution.
- Affected policy, gate, script, test, workflow, template, or skill paths.
- Existing planning task or approved exception.
- `.harness/templates/self-evolution-report.md` for report format.
- Current harness changelog.

## Outputs

- Smallest durable harness improvement that prevents or detects the failure earlier.
- Concise self-evolution report path when a report is created.
- Updated policy, gate, script, test, workflow, template, or skill when in scope.
- Planning follow-up when the improvement cannot fit the batch.
- Concise `.harness/CHANGELOG.md` entry for harness-level changes.

## Required Gates

- [ ] `.harness/gates/self-evolution.md`
- [ ] `.harness/gates/documentation-review.md` for policy, role, gate, or template changes.
- [ ] `.harness/gates/ci-quality-review.md` when scripts, checks, tests, or workflows change.
- [ ] Relevant verification command for any mechanical check changed.

## Evidence

- Concrete repeated-failure examples or high-impact incident reference.
- Chosen improvement type and changed path.
- Verification output for changed mechanical checks.
- Changelog entry and follow-up task ID when applicable.

## Handoff Contract

- [ ] Route speculative or one-off issues back to the owning reviewer instead of changing harness rules.
- [ ] Prefer enforceable checks over broad reminders.
- [ ] Keep outputs concise, current-state-only, and inside `.harness/` unless a script, workflow, or skill owns the enforcement.
- [ ] Hand deferred automation to PM with acceptance criteria and dependency notes.
