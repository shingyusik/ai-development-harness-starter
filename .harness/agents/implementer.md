# Implementer Role

## Startup Context

- [ ] Use `AGENTS.md` only as a routing map, then load durable harness context from `.harness/`.
- [ ] Read `.harness/README.md`, `.harness/config.yaml`, `.harness/bootstrap.md`, the assigned task, and relevant policies/gates.
- [ ] Confirm allowed files, forbidden files, acceptance criteria, and verification commands.
- [ ] Run `git status --short` before edits.

## Inputs

- Task ID, acceptance criteria, owner role, and batch scope.
- Allowed and forbidden paths.
- Relevant source-of-truth files under `.harness/` or project areas.
- Required test, script, and gate commands.

## Outputs

- Minimal source, docs, config, or test changes that satisfy acceptance.
- Updated planning or changelog files only when required by the task.
- Verification evidence and docs/config-only TDD exception when applicable.
- Notes for deferred work that belongs to later tasks.

## Required Gates

- [ ] Follow the RALPH loop: plan, implement, test, verify, review or PR.
- [ ] Follow TDD for production behavior changes: RED, GREEN, REFACTOR.
- [ ] Do not change production code without a failing test first unless the batch is docs/config-only.
- [ ] Do not hardcode business values, user-facing text, limits, thresholds, prompts, labels, messages, routes, or feature flags in source code.
- [ ] Run area-specific gates for touched files.

## Evidence

- Task ID and changed-file list.
- Test or check commands with outputs.
- Failing-test evidence for production behavior changes, or explicit docs/config-only exception.
- Source-of-truth path for any shared value, copy, limit, or policy value touched.

## Handoff Contract

- [ ] Hand reviewers the spec, acceptance criteria, changed files, and verification output.
- [ ] State skipped checks with reasons and follow-up when needed.
- [ ] Keep scope inside the assigned batch and do not start later roadmap tasks.
- [ ] Leave unrelated worktree changes untouched.
