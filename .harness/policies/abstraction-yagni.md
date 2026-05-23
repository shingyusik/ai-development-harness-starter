# Abstraction YAGNI Policy

## Purpose

- Keep designs direct until repeated need justifies abstraction.
- Avoid speculative layers, factories, interfaces, or configuration.
- Prefer simple code that can evolve safely.

## Rules

- Do not add abstractions before demonstrated need.
- Start with the simplest direct design that satisfies the current spec.
- Introduce an abstraction when it reduces real duplication, isolates a boundary, or expresses a stable domain concept.
- Avoid interfaces with one implementation unless needed for boundary inversion or tests.
- Avoid generic helpers that hide domain meaning.
- Keep configuration minimal and tied to current runtime needs.
- Refactor toward abstraction after the second or third real use clarifies the shape.
- Remove unused extension points and placeholder methods.

## Review Checks

- [ ] Each abstraction has at least one current reason to exist.
- [ ] The design is understandable without speculative future requirements.
- [ ] Interfaces, factories, and helpers reduce real complexity.
- [ ] Domain meaning is clearer after abstraction, not hidden.
- [ ] Unused extension points are removed or rejected.

## Gate Evidence

- Rationale for any new abstraction.
- Call sites or repeated use demonstrating need.
- Boundary or test requirement that justifies single-implementation interfaces.
- Diff showing unused abstraction was avoided or removed.
