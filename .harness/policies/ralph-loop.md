# RALPH Loop Policy

## Purpose

- Keep repo-first agent work moving through a repeatable loop.
- Align autonomous batches with roadmap, tests, review, and evidence.
- Avoid broad documentation sprawl while preserving durable rules.

## Rules

- Follow the loop: plan, implement, test, verify, review or PR.
- Start from repo files and planning state, not chat memory alone.
- Keep each batch directly workable, coherent, and bounded.
- Load only the policy, gate, role, and planning context needed for the batch.
- Prefer code, tests, scripts, gates, and concise policies over long manuals.
- Report evidence before claiming completion.
- When repeated failures appear, route them into self-evolution work.
- Do not expand a batch into later roadmap tasks without explicit scope.

## Review Checks

- [ ] The batch maps to a ready task or an explicitly approved exception.
- [ ] Scope stayed within allowed files and requested behavior.
- [ ] Verification commands were run or blockers were recorded.
- [ ] Evidence is attached to the final report.
- [ ] Any recurring failure pattern has a follow-up path.

## Gate Evidence

- Task or roadmap identifier for the batch.
- Changed-file list.
- Verification command outputs.
- Follow-up tasks for scope intentionally deferred.
