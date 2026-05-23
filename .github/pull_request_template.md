## Summary

<!-- What changed and why. Keep this to one or two sentences. -->

## Type

- [ ] Feature
- [ ] Bug fix
- [ ] Documentation
- [ ] Harness / process
- [ ] Chore

## Harness Context

- Active role:
- Planning task or decision record:
- Relevant policies:
- Relevant gates:

## What Changed

-

## Verification

- [ ] `python scripts/check_docs_harness.py`
- [ ] `python scripts/harness/check_planning_graph.py`
- [ ] `python scripts/harness/check_harness_contract.py`
- [ ] `python scripts/harness/check_documentation_policy.py`
- [ ] Project-specific checks from `.harness/config.yaml`:
- [ ] Manual checks or skip reason:

## Review Checklist

- [ ] Scope matches the request and planning entry.
- [ ] Durable harness guidance remains under `.harness/`.
- [ ] New or changed rules are reflected in a policy, gate, check, or template.
- [ ] Repeated failures are routed to self-evolution follow-up when needed.
- [ ] Secrets, local paths, and private workflow details are not included.

## Notes

<!-- Risks, assumptions, skipped checks, or reviewer focus areas. -->

