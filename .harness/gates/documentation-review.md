# Documentation Review Gate

## Inputs

- `.harness/policies/documentation.md`
- Changed documentation files.
- Source material used to update documentation.

## Required Checks

- [ ] Keep harness guidance under `.harness/`.
- [ ] Keep project docs focused on current project behavior, architecture, operations, and run commands.
- [ ] Do not add harness manuals to root docs or root agent instruction files.
- [ ] Write current-state documentation, not a process diary or implementation history.
- [ ] Keep changelog prose only in changelog files.
- [ ] Preserve source filenames, links, or references for imported material.
- [ ] Prefer concise bullets, checklists, and fields over long prose.
- [ ] Add or update mechanical checks when a durable rule should be enforced.

## Evidence

- List of documentation paths changed.
- Reason each changed document belongs in its location.
- Source filenames or links for imported material.
- Documentation checker output when available.

## Fails When

- Harness guidance is placed outside `.harness/`.
- Project docs describe task history instead of current state.
- Changelog-style prose appears in current-state docs.
- External source context is lost.
- A rule remains manual when a practical check could enforce it.
