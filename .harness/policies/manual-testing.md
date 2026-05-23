# Manual Testing Policy

## Purpose

- Record manual or browser-assisted evidence when automation cannot fully cover behavior.
- Make manual tests repeatable without chat history.
- Require cleanup evidence for data created during manual testing.

## Rules

- Prefer automated unit, integration, contract, architecture, and E2E tests where practical.
- Create a standalone `.harness/manual-tests/YYYY-MM-DD-short-name.md` artifact for uncovered behavior.
- Manual testing may be done by a human, an agent, Playwright, browser automation, or another named tool.
- Every artifact lists tester/tool, scope, preconditions, steps, observations, pass criteria, result, evidence, cleanup, and follow-up.
- Steps must be specific enough for another reviewer to repeat.
- Pass criteria must be observable and tied to the requested behavior.
- Failed or blocked manual tests create follow-up work.
- Test-created data must be cleaned up or have a tracked cleanup blocker.

## Review Checks

- [ ] Automation coverage was considered before accepting manual coverage.
- [ ] The artifact is standalone and names the tester/tool used.
- [ ] Steps, observations, and pass criteria are concrete.
- [ ] Evidence includes screenshots, logs, traces, browser notes, or user confirmation.
- [ ] Cleanup steps and final state are recorded.
- [ ] Follow-up exists for any failed, blocked, or partial result.

## Gate Evidence

- Path to the manual test artifact.
- Test runner, browser, tool, or human tester identity.
- Evidence references and cleanup confirmation.
- Linked follow-up task for unresolved findings.
