# Starter Adaptation Roadmap

Status: accepted
Date: 2026-05-24
Source: `.harness/decisions/0001-harness-operating-model.md`
Scope: generic steps for adapting this starter to a new project.

## Goal

Provide a starter harness that can be cloned into any software project and made project-specific without importing private workflows, vendor assumptions, local paths, or legacy repository details.

## Non-Goals

- Do not prescribe a programming language, framework, deployment platform, storage system, or payment provider.
- Do not require external knowledge bases or dashboards.
- Do not store secrets, credentials, personal names, or machine-local paths.
- Do not duplicate durable harness guidance outside `.harness/`.

## Roadmap

1. Establish harness spine and starter checks.
2. Customize project identity, commands, and quality gates.
3. Replace example planning entries with real roadmap, milestones, and tasks.
4. Add project-specific architecture and operations policies only when needed.
5. Strengthen checks when review or CI exposes repeated failures.

## Adoption Checklist

- [ ] Replace placeholder project name.
- [ ] Update `README.md` with project purpose and run commands.
- [ ] Update `.harness/config.yaml` with project checks.
- [ ] Replace example planning entries in `.harness/planning/*.yaml`.
- [ ] Add architecture, security, release, and operations policies only when they reflect real project decisions.
- [ ] Keep generic starter guidance separate from application code and docs.
