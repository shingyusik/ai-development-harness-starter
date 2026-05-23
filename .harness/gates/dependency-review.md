# Dependency Review Gate

## Inputs

- `.harness/policies/dependency-control.md`
- Dependency manifest and lockfile diffs.
- Changed integration, adapter, and build files.

## Required Checks

- [ ] Prefer existing repo code, platform APIs, or standard libraries first.
- [ ] State the reason, owner, and expected update path for each new dependency.
- [ ] Review security, license, maintenance, runtime, and bundle impact where relevant.
- [ ] Confirm versions are pinned or managed through the repo lock path.
- [ ] Review lockfile changes for expected packages only.
- [ ] Contain third-party coupling behind a narrow boundary when practical.
- [ ] Remove unused dependencies with matching manifest and lockfile changes.
- [ ] Record rollback or replacement path for high-impact dependencies.

## Evidence

- Dependency manifest diff.
- Lockfile diff or package manager output.
- Justification with owner and update path.
- Security, license, or size evidence when relevant.
- Test output covering dependency integration.

## Fails When

- A dependency lacks justification, owner, or update path.
- Lockfile changes include unexplained packages.
- Direct coupling spreads across unrelated layers.
- A small utility dependency replaces a reasonable platform API.
- Removed dependencies remain referenced in code or config.
