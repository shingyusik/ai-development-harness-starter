---
name: harness-review-gates
description: Use for review, merge readiness, quality evidence, policy compliance, or gate-based validation of a change.
---

# Harness Review Gates

Use this skill when a task asks for review, quality validation, merge readiness, or evidence checking.

## Steps

1. Read `.harness/config.yaml` and identify required checks for the changed scope.
2. Read the relevant `.harness/gates/*.md` files.
3. Read the matching `.harness/policies/*.md` files only when the gate depends on them.
4. Inspect `git diff --stat` and targeted diffs before judging readiness.
5. Run the required validation commands or explain why a check is skipped.
6. Treat missing evidence as a finding, not as a pass.

## Review priorities

- Correctness and behavior regression risk.
- Required checks and manual evidence.
- Security, secrets, local data, and generated-file safety.
- Architecture/dependency boundaries.
- Scope creep and documentation drift.

## Output

Return PASS only when evidence supports it. Otherwise list concrete findings with paths, commands, and required fixes.
