---
name: compatibility-migration
description: Coordinate a selected multi-step migration while old and new contracts coexist. Use when consumers, interfaces, schemas, or data move independently and need safe states, transition evidence, rollback limits, and retirement gates; do not choose strategy or implement steps.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.6.4
---

# Compatibility migration

Use the repository's established language and conventions for any artifacts you create or update.
Use the smallest sufficient context and bounded tool output. Reuse inspected
evidence and stop once the task can proceed safely; never trade correctness,
safety, or required verification for brevity.

Move a chosen contract through independently safe states while old and new forms
coexist. Make each transition observable and destructive retirement evidence-gated.

## Activation boundary

Use when schemas, interfaces, events, dependencies, formats, protocols,
implementations, or consumers must coexist across steps or mixed deployments.

Route an undecided direction to `solution-framing`, one already-compatible local
change to `safe-code-change`, a completed diff to `fact-based-code-review`, and
measured transition bottlenecks to `performance-investigation`. Do not use without
coexistence or multi-step coordination.

## Workflow

### 1. Establish contracts and envelope

Inventory current and target behavior, producers, consumers, owners, versions,
data shapes, deployment order, usage, and undocumented dependencies. Distinguish
known consumers from assumed completeness.

Define invariants, allowed temporary differences, invalid combinations,
coexistence duration, integrity, and availability. Use the
[compatibility envelope](references/compatibility-envelope.md) for mixed states.

### 2. Design safe intermediate states

Create the smallest ordered sequence that introduces the new path, supports
coexistence, moves consumers or data, and retires the old path. Every state must
be safe to pause in and independently deployable when deployment is involved.
Record preconditions, change, valid combinations, verification, rollback, and
exit criterion.

### 3. Plan data movement

When data changes, define source of truth, read/write rules per state,
transformation or backfill, idempotency, resumability, reconciliation, conflicts,
load limits, and unrepresentable values. Apply
[data transition checks](references/data-transition-checks.md).

### 4. Gate transitions and retirement

Define advance, hold, and stop evidence using consumer status, old-path usage,
reconciliation, divergence, compatibility tests, observation windows, and owner
approval. Absence of reported errors is not proof.

Classify rollback as fully reversible, reversible before data movement, forward-
recoverable, or irreversible. A code revert does not restore transformed data.
Retire only after consumers moved, required zero-usage evidence exists,
documentation and ownership are current, and rollback no longer depends on the
old path.

Choose one state: `READY TO RETIRE`, `HOLD`, `MORE EVIDENCE REQUIRED`, or
`DECISION REQUIRED`.

Hand each implementation step to `safe-code-change` and completed diff to
`fact-based-code-review`. `feature-lifecycle` may link feature evidence; this
skill remains authoritative for compatibility states and retirement.

## Output contract

Use these exact headings in this order:

```markdown
## Migration target
## Current contract
## Consumers and owners
## Compatibility envelope
## Intermediate states
## Data movement
## Transition evidence
## Rollback limits
## Retirement conditions
## Handoff state
```

Each state uses `### State name` with `Preconditions`, `Change`,
`Valid combinations`, `Verification`, `Rollback`, and `Exit criterion`.
