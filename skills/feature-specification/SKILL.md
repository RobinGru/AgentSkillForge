---
name: feature-specification
description: Define or refine the observable behavior contract for one substantial product capability. Use before planning a larger change when actors, scope, rules, permissions, states, edge cases, or acceptance criteria are incomplete and product direction is known.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.6.2
---

# Feature specification

Use the repository's established language and conventions for any artifacts you create or update.


Produce a testable behavior contract for one capability. Describe what users or
systems can observe; leave architecture and implementation details to later
work.

## Use this skill when

- A substantial known capability lacks complete behavior or acceptance criteria.
- Permissions, business rules, failure states, or edge cases are implicit.
- Implementation exposed a product-rule gap that must be resolved.
- An existing specification needs a bounded clarification.

## Do not use this skill when

- Product purpose, users, or first-release scope are still unclear; use
  `project-discovery`.
- The behavior is agreed and only a consequential technical choice remains; use
  `solution-framing`.
- The request contains several independently acceptable capabilities.
- A small, understood change has clear expected behavior; implement it directly
  with `safe-code-change` and proportionate verification.
- The task is implementation, defect diagnosis, code review, or release work.

## Rules

- Specify exactly one independently testable capability.
- Inspect current product artifacts, behavior, tests, and neighboring contracts
  before asking questions.
- Distinguish observed facts, provided decisions, assumptions, and blockers.
- Keep product obligations separate from non-contractual implementation choices.
- Make protected objects, actors, allowed actions, and denial behavior explicit.
- Do not hide missing rules behind proposed code or UI behavior.
- Do not write implementation code.

## Workflow

### 1. Establish identity and boundary

Confirm the capability, intended outcome, primary actor, trigger, dependencies,
and current approval state. Split the work if separate actors, outcomes, or
acceptance decisions can stand alone.

### 2. Gather behavioral evidence

Inspect related flows, domain rules, permissions, data contracts, interfaces,
tests, and existing behavior. Record conflicts and unknowns; current behavior is
evidence, not automatically the desired contract.

### 3. Define scope and rules

State preconditions, in-scope and excluded behavior, functional requirements,
business rules, data involved, permission boundaries, dependencies, and
measurable non-functional obligations.

### 4. Model observable states

Cover the primary and alternate flows plus relevant initial, empty, loading,
partial, success, denied, recoverable-error, terminal-error, cancellation,
retry, duplicate-action, concurrency, and dependency-failure states. Include
only states that can materially occur for this capability.

### 5. Specify permissions and data effects

For each protected action, identify the actor, target object or tenant, required
role or relationship, allowed operation, denied response, sensitive data, and
relevant visibility, retention, deletion, notification, or audit effects. A
hidden interface control is not authorization.

### 6. Write acceptance criteria

Use independently passable Given/When/Then obligations. Each criterion should
name one observable result and the proof that could demonstrate it. Include
material denial and failure behavior without prescribing internal structure.

Trace every requirement to at least one criterion and planned proof. Remove
criteria that only restate implementation tasks.

### 7. Review and hand off

Have the product owner review scope, invariants, permissions, states, edge cases,
and criteria. A draft remains unapproved. If implementation reveals a changed
behavior obligation, return to specification before continuing. For durable
multi-session coordination, `feature-lifecycle` may link this approved contract
without changing its behavior obligations.

## Output contract

Return exactly these headings:

```markdown
## Capability and actor

## Scope and dependencies

## Behavior and rules

## Permissions and data

## States and edge cases

## Acceptance criteria

## Traceability

## Assumptions and blockers

## Handoff state
```

Choose one handoff state: `READY FOR IMPLEMENTATION PLANNING`, `PRODUCT DECISION
REQUIRED`, `SPLIT REQUIRED`, or `MORE SYSTEM EVIDENCE REQUIRED`.

The result is complete only when all requirements are observable and traceable,
important failure and denial behavior is defined, assumptions remain visible,
and approval is not inferred.
