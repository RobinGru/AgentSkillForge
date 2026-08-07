---
name: feature-specification
description: Define one substantial product capability as an observable, testable behavior contract and maintain its canonical specification plus compact feature-index entry. Use before technical planning when actors, rules, permissions, states, or acceptance criteria are incomplete.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.6.5
---

# Feature specification

Use the repository's established language and conventions for any artifacts you create or update.
Use the smallest sufficient context and bounded tool output. Reuse inspected
evidence and stop once the task can proceed safely; never trade correctness,
safety, or required verification for brevity.

Define what users or systems can observe for one capability. Persist the contract;
leave architecture, technical tasks, and implementation to later work.

## Activation boundary

Use for one known substantial capability with incomplete behavior, rules,
permissions, states, failures, or acceptance criteria. Route unclear product
purpose to `project-discovery`, consequential technical choice to
`solution-framing`, and a small, understood change to `safe-code-change`.

## Rules

- Specify exactly one independently testable capability.
- Inspect current artifacts, behavior, tests, and neighboring contracts first.
- Separate observed facts, provided decisions, assumptions, and blockers.
- Keep product obligations independent from implementation choices.
- Make actors, protected objects, allowed actions, denial, and data effects explicit.
- Do not write code or invent technical tasks while direction is open.
- Treat `specification.md` as behavior authority and `index.md` as projection only.

## Canonical artifacts

Follow repository convention; otherwise use:

```text
docs/features/
├── index.md
└── <feature-id>/
    ├── specification.md
    ├── implementation.md
    └── tasks.md
```

Derive a stable lowercase hyphenated ID. Write
`docs/features/<feature-id>/specification.md`. Create or update only that row in
`docs/features/index.md` with feature, specification link and status, lifecycle
link and state, task link and summary, overall state, and next action. Preserve
unrelated rows. Initialize `implementation.md` only for durable coordination; do
not create `tasks.md` before technical direction supports bounded work.

## Workflow

### 1. Bound behavior

Confirm ID, name, outcome, actor, trigger, dependencies, approval, scope, non-goals,
preconditions, business rules, data, permissions, and measurable obligations.
Split independently acceptable capabilities.

### 2. Model observable states and effects

Cover only material initial, empty, loading, partial, success, denied, recoverable
and terminal errors, cancellation, retry, duplicate action, concurrency, and
dependency failure. State protected object or tenant, required relationship,
denial response, sensitive data, visibility, retention, deletion, notification,
and audit effects. Hidden UI is not authorization.

### 3. Define criteria and persist

Write independently passable Given/When/Then criteria. Trace every requirement to
at least one criterion and planned proof; exclude implementation tasks.

Write or update `specification.md`, the single index row, and optionally the
compact `feature-lifecycle` record. Approval must be explicit. Return here if
delivery exposes changed behavior obligations.

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
## Updated artifacts
## Handoff state
```

Choose one state: `READY FOR IMPLEMENTATION PLANNING`, `PRODUCT DECISION REQUIRED`,
`SPLIT REQUIRED`, or `MORE SYSTEM EVIDENCE REQUIRED`.
