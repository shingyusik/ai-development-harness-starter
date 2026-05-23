# Duplication Control Policy

## Purpose

- Remove duplication that creates drift, inconsistent behavior, or review confusion.
- Allow intentional local duplication when abstraction would add more risk.
- Keep duplication decisions explicit.

## Rules

- Remove duplicated business rules, contracts, and validation paths unless intentionally separated.
- Centralize shared constants or schemas when multiple callers must stay in sync.
- Preserve small local duplication when it keeps code simpler and changes are unlikely to couple.
- Do not create a shared abstraction from a single use.
- Prefer behavior tests around deduplicated logic.
- Document intentional duplication when reviewers could reasonably treat it as drift.
- Revisit intentional duplication after repeated changes show a stable shared concept.
- Avoid copy-paste tests that obscure the behavior being asserted.

## Review Checks

- [ ] Duplicated logic does not create inconsistent behavior.
- [ ] Shared concepts have a single source of truth where needed.
- [ ] Intentional duplication has a clear rationale.
- [ ] New abstractions are supported by repeated need.
- [ ] Tests cover shared behavior after deduplication.

## Gate Evidence

- Code search showing duplicated symbols or rules were checked.
- Rationale for intentional duplication.
- Test output for shared behavior.
- Follow-up task when cleanup is deferred.
