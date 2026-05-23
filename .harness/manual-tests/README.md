# Manual Tests

Use this directory for standalone manual or browser-assisted test artifacts when practical automation cannot fully cover behavior.

## Artifact Naming

- Name each artifact `.harness/manual-tests/YYYY-MM-DD-short-name.md`.
- Use a short lowercase name tied to the behavior under test.
- Keep one artifact focused on one task, spec, or automation gap.

## When Required

- Manual tests are required when behavior is changed and automated tests cannot practically verify the full outcome.
- Browser-assisted, Playwright-assisted, human, agent, or tool-driven checks count as manual tests when they rely on observed evidence outside an automated assertion.
- Failed, blocked, partial, or manual-only results require follow-up.

## Automation First

- Prefer unit, integration, contract, architecture, and E2E tests where practical.
- Use a manual artifact only for the remaining automation gap.
- Record the automation gap in the artifact preconditions.

## Cleanup Requirement

- Record every account, record, file, workspace, run, external resource, or fixture created during the test.
- Include exact cleanup steps and final state.
- Link a follow-up when cleanup cannot be completed.

## Evidence Requirements

- Include paths or links for screenshots, logs, traces, browser notes, command output, or user confirmation.
- Tie each evidence item to the tested behavior.
- Keep evidence references stable enough for review without chat history.

## Use The Template

1. Copy `.harness/templates/manual-test.md` to `.harness/manual-tests/YYYY-MM-DD-short-name.md`.
2. Fill in tester/tool, date, task/spec reference, scope, environment, and preconditions before testing.
3. Record exact steps, observations, pass criteria, result, evidence, created test data, cleanup steps, final state, and follow-up.
