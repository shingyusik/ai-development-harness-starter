# Architecture Reviewer Role

## Startup Context

- [ ] Use `AGENTS.md` only as a routing map, then load durable harness context from `.harness/`.
- [ ] Read `.harness/README.md`, `.harness/config.yaml`, `.harness/bootstrap.md`, and architecture-related policies.
- [ ] Read `.harness/policies/architecture-governance.md`, `.harness/policies/dependency-control.md`, and `.harness/policies/hardcoding-control.md`.
- [ ] Load relevant project architecture docs only when the batch touches production boundaries.

## Inputs

- Task ID, acceptance criteria, changed files, and dependency or adapter diffs.
- Current architecture source of truth for touched boundaries.
- Config/data source files for shared values, messages, limits, thresholds, labels, routes, or feature flags.
- Architecture, dependency, and test check outputs.

## Outputs

- Boundary and dependency-direction findings.
- Adapter, data-access, access-control, isolation, and runtime-contract review notes.
- Dependency justification review for new or changed packages, services, or frameworks.
- Hardcoding and source-of-truth drift findings for architecture-relevant values.

## Required Gates

- [ ] `.harness/gates/dependency-review.md`
- [ ] `.harness/gates/clean-code-review.md`
- [ ] `.harness/gates/merge-readiness.md`
- [ ] Existing architecture tests or documented architecture-check substitute for touched boundaries.

## Evidence

- Architecture check or test output.
- Changed architecture docs or contracts when boundaries change.
- Dependency manifest and lockfile diff when dependencies change.
- Source-of-truth paths and duplicate-check notes for shared config, data, copy, limits, and policy values.

## Handoff Contract

- [ ] Send implementers concrete boundary fixes with expected dependency direction.
- [ ] Send tech lead unresolved architecture exceptions and follow-up tasks.
- [ ] Send quality reviewer required verification commands.
- [ ] Do not approve drift from declared boundaries without rationale and follow-up.
