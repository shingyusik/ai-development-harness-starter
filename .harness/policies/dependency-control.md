# Dependency Control Policy

## Purpose

- Add dependencies only when they solve a real project problem.
- Keep ownership, update path, and coupling impact explicit.
- Prevent unnecessary package, service, and framework coupling.

## Rules

- New runtime or tooling dependencies need a stated reason and owner.
- Prefer existing repo libraries and helpers before adding a dependency.
- Evaluate license, maintenance, security, bundle/runtime cost, and ecosystem fit.
- Dependency versions are locked or managed through the repo's normal lock path.
- Boundary wrappers isolate third-party APIs when direct coupling would spread.
- Remove unused dependencies with the same care as adding new ones.
- Avoid dependencies for small utilities the platform or standard library already covers.
- Record update and rollback paths for high-impact dependencies.

## Review Checks

- [ ] The dependency is necessary for the requested behavior.
- [ ] Existing code or platform APIs cannot reasonably cover the need.
- [ ] Owner, lock/update path, and risk are clear.
- [ ] Coupling is contained behind a narrow interface when practical.
- [ ] Security, license, and size/runtime impacts are acceptable.

## Gate Evidence

- Dependency diff and lockfile diff.
- Justification, owner, and update path.
- Security or license review when relevant.
- Test output covering integration with the dependency.
