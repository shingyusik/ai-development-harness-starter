# CI Quality Policy

## Purpose

- Treat CI as required merge evidence, not optional advice.
- Keep local and remote quality checks aligned where practical.
- Convert repeated review failures into stronger automated checks.

## Rules

- Pull requests do not merge while required quality checks fail.
- Required checks are listed in `.harness/config.yaml` or an equivalent machine-readable manifest.
- CI should run practical tests, lint, typecheck, format, architecture, docs, planning graph, and harness contract checks.
- Agents run relevant local checks before requesting review.
- Missing checks are recorded as follow-up when they are too expensive for the current batch.
- Manual-test artifacts cover behavior that cannot be automated.
- Repeated CI or review escapes become a policy, gate, script, test, lint rule, workflow, template, or skill improvement.

## Review Checks

- [ ] Test evidence covers changed production behavior where practical.
- [ ] Lint, typecheck, format, and architecture checks are run or explicitly scoped out.
- [ ] Docs, planning graph, and harness contract checks run when touched areas require them.
- [ ] CI-required checks match the change area.
- [ ] Failed, skipped, or unavailable checks have a clear reason and follow-up.

## Gate Evidence

- Local command output for relevant checks.
- CI run link or status summary.
- Manifest entry for required checks when available.
- Manual-test artifact paths for automation gaps.
