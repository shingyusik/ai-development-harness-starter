# Clean Code Review Gate

## Inputs

- `.harness/policies/clean-code.md`
- `.harness/policies/hardcoding-control.md`
- `.harness/policies/duplication-control.md`
- `.harness/policies/abstraction-yagni.md`
- `.harness/policies/architecture-governance.md`
- Changed production, test, and review files.

## Required Checks

- [ ] Names reveal domain intent at the call site.
- [ ] Functions are small and keep one clear responsibility.
- [ ] Modules remain cohesive with one primary reason to change.
- [ ] Side effects, writes, network calls, and mutations are explicit.
- [ ] Error paths are handled intentionally and not swallowed.
- [ ] Tests cover changed behavior and important error paths where practical.
- [ ] Duplication is removed when it creates drift or inconsistent behavior.
- [ ] Business numbers, user-facing strings, limits, thresholds, prompts, labels, messages, and feature flags are not hardcoded in source code.
- [ ] Shared values read from JSON/config data sources or generated typed constants derived from them.
- [ ] Config/data files may be split intentionally, but the same logical variable/message is not duplicated across files.
- [ ] New abstractions have current need and do not hide domain meaning.
- [ ] Architecture boundaries and dependency direction are preserved.

## Evidence

- Diff for changed code and tests.
- Relevant test command output.
- Reviewer notes for accepted duplication, side effects, or abstraction tradeoffs.
- JSON/config source paths for shared values and messages, including duplicate-check notes for values split across files.
- Architecture check output when boundaries are touched.

## Fails When

- Names, flow, or module shape obscure the changed behavior.
- A function or module mixes unrelated responsibilities.
- Side effects or errors are hidden from callers or tests.
- Duplication creates inconsistent behavior without rationale.
- A shared value or user-facing message is hardcoded in source code.
- Any two consumers can drift because they do not read the same source value.
- The same logical variable or message is duplicated in multiple config/data files.
- A speculative abstraction is added without current need.
