---
name: compatibility-migration
description: Plan and coordinate a selected migration when old and new schemas, interfaces, dependencies, implementations, or consumers must remain valid across multiple steps. Define the compatibility envelope, safe intermediate states, transition evidence, rollback limits, and retirement conditions.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.3.0-beta.1
---

# Compatibility migration

Coordinate a chosen change through independently safe states while old and new
contracts coexist. Make every transition observable, reversible where possible,
and destructive only after evidence permits retirement.

## Activation boundary

Use this skill when schemas, interfaces, events, dependencies, implementations,
formats, protocols, or consumers must coexist across multiple steps or mixed
deployments. It applies when consumers move independently, data needs backfill or
reconciliation, rollout and data state differ, or removal depends on usage proof.

Do not use it when:

- The migration direction is still undecided; use `solution-framing` first.
- A single local change is already compatible; use `safe-code-change`.
- A completed migration diff needs assessment; use `fact-based-code-review`.
- The task only explains migration concepts or writes deprecation prose.
- No coexistence, consumer coordination, or multi-step transition exists.
- The need is a general launch checklist, communication plan, or production
  approval after compatibility has already been established.

## Capability disclosure

- **Positive example:** Move an event field while old and new producers and
  consumers deploy independently over several releases.
- **Near non-trigger:** Choose between two incompatible target schemas; that
  strategic decision belongs to `solution-framing`.
- **Main output:** A compatibility envelope and ordered safe states with evidence,
  rollback limits, and retirement criteria.
- **Explicit non-actions:** Do not choose the migration strategy, implement local
  steps, approve a diff, or claim unrun compatibility checks passed.

## Workflow

### 1. Establish the current contract

Inventory observable behavior, producers, consumers, data and interface shapes,
versions, deployment order, owners, current usage, and evidenced undocumented
dependencies. Distinguish known consumers from assumed completeness.

### 2. Bound the compatibility envelope

Define target behavior, invariants that must hold throughout transition, allowed
temporary differences, invalid combinations, coexistence duration, and integrity
and availability requirements. Use
[compatibility envelope](references/compatibility-envelope.md) to expose mixed
producer, consumer, and deployment combinations.

### 3. Design safe intermediate states

Build the smallest ordered sequence that makes the new capability available,
allows controlled coexistence, moves consumers or data, and retires the old path.
Name states for the actual system rather than forcing generic labels.

For every state record preconditions, the change, valid old/new combinations,
verification, rollback, and exit criterion. Each state must be safe to pause in
and independently deployable when deployment is involved.

### 4. Plan data transition

When data changes, identify the source of truth, read and write rules per state,
transformation or backfill, idempotency, resumability, reconciliation, conflict
handling, load boundaries, and values the target cannot represent. Apply
[data transition checks](references/data-transition-checks.md).

Route measured backfill or resource bottlenecks to `performance-investigation`;
retain only their resulting constraints in this plan.

### 5. Define transition evidence

Specify advance, hold, and stop conditions using consumer status, old-path usage,
data reconciliation, error or divergence signals, compatibility tests, observation
windows, and accountable approval. Absence of reported errors is not proof.

### 6. Mark rollback limits

Classify each state as fully reversible, reversible only before data movement,
recoverable through a forward correction, or irreversible. Do not equate a code
revert with restoration of transformed data.

### 7. Gate retirement and hand off

Retire old behavior only after known consumers have moved, old-path usage is
absent for the required window, ownership and documentation are current, and no
supported rollback still depends on it. Choose one state:

- `READY TO RETIRE`
- `HOLD`
- `MORE EVIDENCE REQUIRED`
- `DECISION REQUIRED`

Hand each implementation step to `safe-code-change` and each completed diff to
`fact-based-code-review`. This skill owns the state sequence, not implementation
or general release approval.

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

Each state must use `### State name` followed by `Preconditions`, `Change`,
`Valid combinations`, `Verification`, `Rollback`, and `Exit criterion` fields.
