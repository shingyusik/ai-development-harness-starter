# Self-Evolution Policy

## Purpose

- Convert repeated failures into durable harness improvements.
- Keep the harness small, executable, and grounded in observed problems.
- Prefer enforceable fixes over reminders.

## Rules

- A repeated failure is a pattern seen in review, CI, manual testing, production, or agent execution.
- Repeated failures become a policy, gate, script, test, lint rule, workflow, template, or skill improvement.
- Prefer the smallest improvement that prevents or detects the failure earlier.
- Avoid broad manuals when a mechanical check can enforce the invariant.
- Record harness-level changes in `.harness/CHANGELOG.md`.
- Keep retrospectives concise and action-oriented.
- Do not add self-evolution work without evidence of the failure pattern.
- Track follow-up tasks when the improvement cannot be implemented immediately.

## Review Checks

- [ ] The failure pattern is concrete and recurring.
- [ ] The proposed improvement would catch or prevent the pattern.
- [ ] The improvement is placed in the right harness artifact.
- [ ] The change does not create broad process sprawl.
- [ ] Changelog or planning updates reflect durable harness changes.

## Gate Evidence

- Examples of the repeated failure.
- Chosen improvement type and file path.
- Verification output for new checks when applicable.
- Linked follow-up task for deferred automation.
