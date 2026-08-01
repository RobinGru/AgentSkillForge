# Feature lifecycle artifact templates

Load this reference only when creating or repairing lifecycle artifacts. Adapt
paths to an equivalent repository convention without changing ownership: the
implementation record is canonical; the index is navigational; handoffs own
transient worktree state.

## Canonical implementation record

```markdown
# Implementation: <feature-id> — <feature name>

## Lifecycle
- State: <PROPOSED | READY | IN PROGRESS | BLOCKED | VERIFICATION | DONE | ABANDONED>
- Last updated: <YYYY-MM-DD>
- Observed revision: `<full SHA or not available with reason>`
- Verified revision: `<full SHA or not available with reason>`

## Readiness
- Specification: <MISSING | DRAFT | READY>
- Technical decision: <NOT REQUIRED | PENDING | READY>
- Implementation plan: <MISSING | READY>

## Objective
Implement the observable behavior defined in `spec.md`.

## Scope
- Affected areas: <paths, components, or interfaces>
- Non-goals: <material exclusions>

## Implementation plan
- [ ] <bounded step and observable completion>

## Acceptance evidence
| Criterion | Relevant area | Direct proof | Result | Revision |
|---|---|---|---|---|
| AC-1 | `path/...` | `test or procedure` | Pending | `not available` |

## Active work units
Omit unless work is parallelized.

| Unit | Non-overlapping scope | Branch/worktree | Base revision | Owner | State |
|---|---|---|---|---|---|
| W-1 | <scope> | `<name>` | `<SHA>` | <owner> | PLANNED |

## Decisions, blockers, and risks
- <condition and what resolves it>

## Verification
| Check | Command or procedure | Result | Revision | Date |
|---|---|---|---|---|
| Direct proof | `<command>` | Not run | `not available` | <YYYY-MM-DD> |

## Next safe action
<One bounded action, prerequisite, and expected observable result.>
```

Remove unsupported empty sections instead of writing generic assurances.

## Feature index

```markdown
# Feature index

| ID | Feature | State | Specification | Implementation | Observed revision | Updated | Blocker |
|---|---|---|---|---|---|---|---|
| F-001 | File import | IN PROGRESS | `F-001-file-import/spec.md` | `F-001-file-import/implementation.md` | `abc1234` | 2026-08-02 | — |
```

The index must not introduce facts absent from the canonical record. It is
separate from the brief-local capability map produced by `project-discovery`.
When the record and index differ, inspect the repository and repair both in the
same lifecycle update.

## Parallel-work constraints

Create work units only when scopes are independently safe and expected evidence
is clear. Do not assign overlapping write scopes without explicit coordination.
Record completion evidence per unit; never infer feature completion from one unit.

## Handoff boundary

A handoff references the canonical record and adds only continuation facts such
as branch, current revision, staged or unstaged files, local diff, fragile state,
executed checks, unresolved conditions, and one safe next action. After resuming,
fold durable evidence into the canonical record and supersede the handoff according
to repository convention.
