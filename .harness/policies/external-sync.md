# External Sync Policy

## Purpose

- Keep local repo state authoritative for harness decisions, planning, policies, gates, templates, and stable state.
- Allow external views only as downstream mirrors or preserved references.
- Avoid process-note sprawl when harness state is displayed outside the repo.

## Rules

- Local repo state remains authoritative.
- External sync is downstream and read-only with respect to harness design decisions.
- External tools may display or preserve harness state; they must not override local repo state.
- External sync happens only after local harness state is committed or otherwise explicitly recorded in repo files.
- External sync must not drive local harness design, sequencing, or acceptance criteria.
- Each synced decision or stable state artifact uses one consolidated source-preserving document.
- No secrets or credentials are synced.
- External sync is optional and never required for a generic starter.

## Review Checks

- [ ] Local repo state remains the source of truth.
- [ ] The sync target is downstream and read-only for harness decisions.
- [ ] The sync uses one consolidated source-preserving document per decision or stable state artifact.
- [ ] Source paths, artifact identity, sync date/tool, and update strategy are present.
- [ ] No secrets or credentials are included.

## Gate Evidence

- Source repo path for each synced artifact.
- Destination name and document identity.
- Sync date/tool and update strategy.
- Confirmation that the local source was committed or explicitly recorded before sync.

## Forbidden

- External tools overriding local repo state.
- External sync driving harness design decisions.
- Incremental process-note sprawl.
- One-message-per-update knowledge files.
- Syncing secrets, credentials, tokens, or private runtime values.
- Treating any external destination as required harness infrastructure.

