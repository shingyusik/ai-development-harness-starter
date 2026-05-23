# Local Development Data Policy

## Purpose

- Make local and test states reproducible without fragile manual setup.
- Keep generated data scoped, deterministic, and safe to clean up.
- Prevent production data or credentials from being required for local development.

## Rules

- Prefer generators, factories, seed scripts, and fixtures over manual setup.
- Each generator declares a source-of-truth path, owner, supported scenarios, and intended scope.
- Generators are deterministic by default and document any random seed, fixed identifiers, or stable defaults.
- Fixtures cover common, empty, edge, and failure states when relevant.
- Generated records use a scope marker, prefix, fixed ID, or equivalent tag so cleanup targets only test data.
- Every generator has a matching cleanup or reset command.
- Test-created data is cleaned up after automated, manual, and browser-assisted tests.
- Cleanup is safe, scoped, idempotent, and never targets production data or production credentials.
- If automatic cleanup is impossible, manual evidence records cleanup owner, steps, and final state.

## Review Checks

- [ ] New non-trivial states have fixture or generator support where practical.
- [ ] Generator path, owner, scope marker/prefix, deterministic seed or fixed IDs, and scenario coverage are documented.
- [ ] Setup does not rely on private manual state.
- [ ] Cleanup/reset command exists, is idempotent, and is documented in current-state form.
- [ ] Tests that create data also remove it or isolate it.
- [ ] No production credentials or production data are needed.
- [ ] Evidence output shows generated data setup and cleanup/reset results.

## Gate Evidence

- Generator, fixture, seed, or factory source-of-truth path and owner.
- Deterministic seed, fixed IDs, scope marker/prefix, and supported scenarios.
- Cleanup/reset command or scoped teardown code, including idempotent rerun behavior when practical.
- Test output or manual artifact showing setup and cleanup ran.
- Rationale for any temporary manual setup.

## Starter Placeholder

- Add project-specific generator and cleanup commands only after the project has real local data needs.

