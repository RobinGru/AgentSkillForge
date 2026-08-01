---
name: feature-lifecycle
description: Maintain a small, revision-bound lifecycle record for one substantial feature across sessions, agents, or dependent work units. Use when durable coordination is needed beyond a single session and the repository must preserve current state, evidence, blockers, and one safe next action.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.6.2
---

# Feature lifecycle

Maintain one compact, revision-bound lifecycle record so another agent can
reconcile a substantial feature and continue safely. This is not a
project-management system, transcript, implementation workflow, or replacement
for Git, tests, issues, review, or CI.

## Activation boundary

Use this skill when one independently verifiable feature needs durable
coordination across sessions, agents, dependencies, or non-overlapping work
units. Do not use it for one-session changes, generic status reports, or work
already fully owned by a current repository system of record.

Route product behavior to `feature-specification`, consequential technical
choices to `solution-framing`, bounded implementation to `safe-code-change`,
coexistence or mixed-version transitions to `compatibility-migration`, and fragile
or dirty worktree continuation to `session-handoff`.

## Ownership and artifacts

`feature-lifecycle` owns durable feature identity, readiness, state, linked source
artifacts, bounded plan, revision-bound evidence, durable blockers, and exactly
one safe next action. It links specifications and decisions without changing
them and never duplicates transient handoff details. For a migration, link the
migration artifact: it remains authoritative for compatibility, rollback, and
retirement. For a deep review, link its scenario evidence and resulting blocker;
`adversarial-deep-review` never sets lifecycle state or an integration decision.

Use the repository's equivalent convention or:

```text
docs/features/INDEX.md
 docs/features/<feature-id>/spec.md
 docs/features/<feature-id>/implementation.md
 docs/handoffs/<feature-id>.md
```

`implementation.md` is canonical; `INDEX.md` is a compact projection and must
agree with it. A handoff exists only for interrupted concrete work. Use
[artifact templates](references/artifact-templates.md) only when creating or
repairing these files.

## State model

Use exactly one state, derived from observed facts:

- `PROPOSED`: readiness is incomplete.
- `READY`: specification and required decisions are ready, boundary and planned
  proofs are known, and the first bounded step is unblocked.
- `IN PROGRESS`: implementation or verification work is observed and unblocked.
- `BLOCKED`: a named decision, access need, dependency, external result, or
  repository condition prevents the next action; record its resolver.
- `VERIFICATION`: implementation appears complete but final-revision evidence or
  required checks are incomplete.
- `DONE`: every criterion has current proof, required checks passed on the final
  revision, the final diff was inspected, no blocker remains, and
  `verified_revision` equals `observed_revision`.
- `ABANDONED`: an authorized owner explicitly stopped or replaced the feature.

Never infer progress, completion, or abandonment from a document, checkbox,
commit message, agent claim, silence, or elapsed time. Move backward when scope
or repository facts invalidate readiness or evidence. `DONE` does not imply
approval, merge, deployment, release, or stakeholder acceptance.

## Revision and readiness rules

Record a full commit SHA when practical:

- `observed_revision`: revision last reconciled with the record.
- `verified_revision`: revision supported by acceptance evidence and checks.

The record is stale when relevant repository state changed after
`observed_revision` or its claims no longer reconcile. Inspect current facts
before editing or changing state; keep dirty-worktree details in
`session-handoff`.

Track readiness separately:

```text
Specification: MISSING | DRAFT | READY
Technical decision: NOT REQUIRED | PENDING | READY
Implementation plan: MISSING | READY
```

## Workflow

1. Confirm one stable feature ID and independently verifiable capability.
2. Inspect index, specification, lifecycle record, decisions, issues, current
   revision, relevant code and tests, and any active handoff.
3. Create or reconcile `implementation.md`; mark stale or unsupported claims.
4. Apply readiness fields and state guards from current facts.
5. Keep bounded steps; complete one only when its observable result exists.
6. Map every acceptance criterion to direct proof, result, and revision.
7. For parallel units, record non-overlapping scope, expected evidence, base
   revision, owner, and branch or worktree; a completed unit is not a completed
   feature.
8. Record only decisions, blockers, and risks that change state or next action.
9. Define exactly one bounded next action, prerequisite, and expected result.
10. Update the index with the canonical record; use `session-handoff` for
    interrupted work and later fold durable facts back into the record.
11. Reconcile the final artifacts, revision, links, diff, and executed checks;
    leave unrun checks explicit.

## Output contract

Use exactly these headings:

```markdown
## Lifecycle update
## Evidence
## Updated artifacts
## Next safe action
## Lifecycle state
```

Report previous and current state with factual basis, only observed evidence and
executed checks, every changed lifecycle artifact, exactly one safe next action
with expected result, and exactly one allowed state. Keep stale evidence,
unsupported claims, and unrun checks explicit.
