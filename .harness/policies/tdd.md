# TDD Policy

## Purpose

- Protect production behavior with tests that fail before the implementation.
- Keep implementation feedback fast and behavior-focused.
- Allow explicit exceptions for docs and configuration-only work.

## Rules

- For production behavior changes, write or update a failing test first.
- Follow RED, GREEN, REFACTOR: observe failure, implement the minimum fix, then improve structure.
- Tests describe externally meaningful behavior, contracts, errors, or boundaries.
- Refactors keep behavior tests passing throughout the change.
- Bug fixes include a regression test when practical.
- Architecture and policy changes use mechanical checks when tests are not the right tool.
- Docs/config-only batches may skip failing-test-first with an explicit reason and verification commands.
- Do not treat manual testing as a substitute for automatable regression coverage.

## Review Checks

- [ ] Production behavior changes include test evidence from the RED/GREEN path.
- [ ] The failing test would fail against the old behavior.
- [ ] Refactoring did not broaden behavior unexpectedly.
- [ ] Docs/config exceptions state why a failing test is not applicable.
- [ ] Manual tests are used only for true automation gaps.

## Gate Evidence

- Test file path and command output.
- Failing-test evidence or explicit docs/config exception.
- Regression test reference for bug fixes.
- Manual-test artifact for non-automatable behavior.
