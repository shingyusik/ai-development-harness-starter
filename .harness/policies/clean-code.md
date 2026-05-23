# Clean Code Policy

## Purpose

- Keep code readable, change-friendly, and reviewable.
- Translate Clean Code principles into concrete checks for every production change.
- Prefer local clarity over cleverness or broad abstractions.

## Rules

- Use meaningful names that reveal domain intent and avoid ambiguous abbreviations.
- Keep functions small and focused on one responsibility.
- Keep each function at one abstraction level; extract mixed policy/detail logic.
- Minimize function arguments; group related values behind clear data structures.
- Avoid hidden side effects; make writes, network calls, and mutations explicit.
- Remove harmful duplication, but do not invent abstractions before repeated need is clear.
- Comments explain intent, constraints, or non-obvious tradeoffs, not unclear code.
- Handle errors explicitly and keep error handling separate from normal flow where practical.
- Isolate third-party and framework boundaries behind narrow adapters.
- Keep modules cohesive with a narrow reason to change.
- Do not hardcode business numbers, user-facing strings, limits, thresholds, prompts, labels, messages, or feature flags in source code.
- Values live in domain-appropriate JSON/config data sources and source code reads that data or generated typed constants from it.
- Splitting config files is allowed by domain, feature, locale, or runtime boundary, but the same logical variable/message must not be duplicated across files.

## Review Checks

- [ ] Names make behavior and domain meaning obvious at the call site.
- [ ] Functions and modules have a single clear responsibility.
- [ ] Control flow is understandable without tracing unrelated side effects.
- [ ] Error paths are explicit, tested when practical, and not swallowed.
- [ ] Comments are necessary and do not repeat the code.
- [ ] Duplication is removed or intentionally documented as local duplication.
- [ ] Business literals and user-facing copy are externalized to JSON/config data sources.
- [ ] All consumers use the same source value for shared limits, messages, labels, and validation rules.
- [ ] The same logical variable/message was not duplicated across separate config/data files.
- [ ] Tests read as behavior examples, not implementation transcripts.

## Gate Evidence

- Diff showing code scoped to the requested behavior.
- Test output covering changed behavior and error paths where practical.
- Reviewer notes for any accepted duplication, side effect, or abstraction tradeoff.
- Path to JSON/config source for shared numbers, strings, limits, messages, and validation rules.
