# Architecture Governance Policy

## Purpose

- Preserve the architecture boundaries declared by the adopting project.
- Keep architecture docs current-state-only.
- Make dependency direction reviewable and mechanically checked where practical.

## Rules

- Declare project layers, modules, packages, or service boundaries before enforcing them.
- Code should depend inward toward stable domain concepts and outward only through explicit adapters or interfaces.
- Runtime, storage, network, access-control, queue, and external-service details stay behind the boundary chosen by the project.
- Architecture docs describe current boundaries, not migration history.
- Boundary changes update architecture docs and checks in the same batch when practical.
- New architecture exceptions require rationale and follow-up to remove or codify them.

## Review Checks

- [ ] Imports and calls follow declared dependency direction.
- [ ] Runtime, storage, network, access-control, queue, and external-service boundaries are preserved.
- [ ] New adapters isolate framework or third-party details.
- [ ] Architecture docs changed when boundaries or contracts changed.
- [ ] Existing architecture checks pass or gaps are tracked.

## Gate Evidence

- Architecture test, lint, or review output.
- Diff for changed architecture docs or contracts.
- Rationale for any temporary boundary exception.
- Follow-up task for missing mechanical coverage.
