# Review Policy

## Purpose

- Review against the spec first, then code quality, then evidence.
- Prevent approval without required gates.
- Keep review findings actionable and tied to file, behavior, or policy.

## Rules

- Start with the requested scope, acceptance criteria, and roadmap task.
- Confirm behavior and docs match the spec before judging style.
- Check Clean Code, hardcoding control, architecture, dependencies, duplication, and abstraction policy.
- Require test, CI, docs, planning, manual-test, and cleanup evidence where applicable.
- Do not approve when required gates are failing, missing, or unexplained.
- Prioritize correctness, safety, regressions, and missing tests over preference comments.
- Findings identify the affected file, rule, behavior, and expected fix.
- Non-blocking suggestions are labeled clearly.

## Review Checks

- [ ] Acceptance criteria are satisfied or gaps are called out.
- [ ] Changed files stay within scope.
- [ ] Code quality and architecture policies were applied.
- [ ] Hardcoded business values, user-facing strings, limits, thresholds, prompts, labels, messages, and feature flags were rejected or justified as local-only technical constants.
- [ ] Required verification evidence is present.
- [ ] Manual-test or cleanup evidence exists when automation cannot cover the behavior.
- [ ] Approval is withheld for unresolved gate failures.

## Gate Evidence

- Review checklist result or report.
- Links to test/CI/manual evidence.
- List of blocking findings and their resolution.
- Explicit approval only after required gates pass.
