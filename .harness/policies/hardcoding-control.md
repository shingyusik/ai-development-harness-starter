# Hardcoding Control Policy

## Purpose

- Prevent drift between code paths, layers, services, tests, documentation, and user-facing behavior.
- Keep numbers, text, labels, thresholds, limits, messages, and policy values in managed data/config files.
- Make value changes reviewable by changing source-of-truth files instead of hunting through source code.

## Rules

- Do not hardcode business values, limits, thresholds, user-facing copy, validation messages, prompts, labels, routes, or feature flags inside source code.
- Source code reads values from versioned JSON/config data files or from generated typed constants derived from those files.
- Values do not have to live in one global file; split files by domain, feature, locale, or runtime boundary when that improves ownership and readability.
- The same logical variable or message must not be duplicated across multiple source files; it has one source of truth and all consumers read from it.
- Shared values used by multiple code paths, services, packages, clients, tests, or docs must come from the same source value or generated output.
- Cross-runtime drift is one example: if two project surfaces need the same request limit or warning text, both read the same source value instead of each hardcoding it.
- Source code may define local-only technical constants only when they are not business policy, user-facing text, or shared behavior.
- Any local-only constant must be named, scoped narrowly, and documented when the reason is not obvious.
- Changing a value such as a request limit, quota, warning message, timeout policy, display label, or validation rule updates the source data once; all readers consume the updated value.
- Generated files are allowed only when their source JSON/config file and generation command are listed.

## Review Checks

- [ ] No new or changed business number, string, limit, threshold, label, prompt, message, route, or feature flag is hardcoded in source code.
- [ ] Values are stored in domain-appropriate JSON/config source files or explicitly approved typed config sources.
- [ ] File splitting is intentional, but the same logical variable/message is not duplicated across multiple source files.
- [ ] Every consumer reads from the source data file or generated typed output instead of copying the literal.
- [ ] Cross-layer or cross-runtime behavior uses the same source value when multiple consumers depend on the same rule.
- [ ] Tests cover the shared config path or generated constants when behavior depends on the value.
- [ ] Any remaining source-code literal is local-only technical detail with clear scope and rationale.

## Gate Evidence

- Path to the JSON/config source file or generated source-of-truth output.
- Diff showing source code reads the data file or generated constants.
- Evidence that duplicate logical variables/messages were not added in separate files.
- Test output covering consumers of the shared value when behavior changed.
- Reviewer note for any accepted local-only literal.
