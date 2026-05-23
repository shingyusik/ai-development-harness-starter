# Local Dev Data Review Gate

## Inputs

- `.harness/policies/local-development-data.md`
- `.harness/config.yaml` local mock/test data command references.
- Fixtures, factories, seed scripts, generators, and teardown code.
- Automated or manual tests that create local data.

## Required Checks

- [ ] Use deterministic fixtures, factories, seed scripts, or generators for non-trivial states.
- [ ] Document the source-of-truth path, owner, deterministic seed or fixed identifiers, and supported scenario states.
- [ ] Scope generated records with a marker, prefix, fixed ID, or equivalent tag so cleanup targets only test-created data.
- [ ] Provide a cleanup or reset command for every generator.
- [ ] Ensure cleanup is scoped, idempotent, and never targets production data.
- [ ] Cover common, empty, edge, and failure states where relevant.
- [ ] Avoid private manual state, production credentials, or production data.
- [ ] Record manual cleanup owner and final state when automation cannot clean up.
- [ ] Capture evidence output for setup plus cleanup/reset results.

## Evidence

- Generator, fixture, factory, seed, or teardown source-of-truth path and owner.
- Deterministic seed, fixed IDs, supported scenarios, and scope marker/prefix.
- Cleanup or reset command output.
- Test output or manual artifact showing setup and cleanup ran.
- Rationale for any temporary manual setup.

## Fails When

- Local setup depends on private manual state.
- Generated data cannot be identified for scoped cleanup.
- Cleanup is missing, unsafe, or not idempotent.
- Production data or credentials are required.
- Evidence output is missing for generator setup or cleanup/reset.
- Manual cleanup lacks owner, steps, and final-state evidence.
