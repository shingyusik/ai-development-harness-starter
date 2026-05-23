# Self-Evolution Gate

## Inputs

- `.harness/policies/self-evolution.md`
- `.harness/templates/self-evolution-report.md`
- Review findings, CI failures, manual-test failures, production issues, or agent execution failures.
- Existing harness policies, gates, scripts, tests, templates, workflows, and skills.

## Triggers

- Repeated review failure.
- Repeated CI failure.
- Repeated manual-test failure.
- Production/user-visible incident.
- Agent execution failure.
- Recurring process confusion.

## Required Checks

- [ ] Confirm the failure is repeated or high-impact enough to justify harness change.
- [ ] Identify concrete examples of the failure pattern.
- [ ] Choose the smallest durable improvement that catches or prevents the pattern earlier.
- [ ] Prefer a script, test, lint rule, workflow, gate, template, or skill over broad prose.
- [ ] Place the improvement in the correct harness artifact.
- [ ] Update `.harness/CHANGELOG.md` for harness-level changes.
- [ ] Add planning follow-up when the improvement cannot fit the current batch.
- [ ] Keep the output concise and action-oriented.

## Output

- Concise report path using `.harness/templates/self-evolution-report.md`.
- Chosen improvement type/path for the policy, gate, script, test, workflow, template, or skill change.
- Verification evidence for any changed or added mechanical check.
- Changelog/planning update covering harness-level changes and task status.
- Deferred follow-up when the improvement is not fixed immediately.

## Evidence

- Links or paths for repeated failure examples.
- Chosen improvement type and changed path.
- Verification output for new or changed mechanical checks.
- Changelog entry or planning follow-up path.

## Fails When

- The failure pattern is speculative or unsupported.
- The change adds broad instructions where a practical check could enforce the rule.
- The improvement is stored outside the harness boundary.
- Verification evidence for new checks is missing.
- Required changelog or planning follow-up is absent.
