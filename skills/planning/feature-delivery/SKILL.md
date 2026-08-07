---
name: feature-delivery
description: Deliver one tracked feature through its bounded ready tasks, strictly sequentially in the same agent. Use when implementation spans multiple specialist work units; select one task, apply its specialist contract, persist evidence, and continue until a stop condition applies.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.6.5
---

# Feature delivery

Use the repository's established language and conventions for any artifacts you create or update.
Use the smallest sufficient context and bounded tool output. Reuse inspected
evidence and stop once the task can proceed safely; never trade correctness,
safety, or required verification for brevity.

Coordinate one feature's technical tasks. Never use parallel agents, delegate
concurrent work, or execute tasks concurrently.

## Responsibility boundary

- `feature-specification` owns behavior and `specification.md`.
- `feature-lifecycle` owns revision-bound `implementation.md` status.
- `feature-delivery` owns technical task selection and `tasks.md`.
- The named specialist skill owns each task's method and direct proof.
- `index.md` is only a compact projection.

Applying a specialist means the same agent follows that contract for one task,
then returns here. Use this for multi-task implementation or complete delivery;
not for one bounded change, specification, status-only updates, or unresolved
product or architecture decisions.

## Task record

Follow repository convention; otherwise maintain
`docs/features/<feature-id>/tasks.md`:

```markdown
## TASK-001 — <bounded outcome>
- State: PROPOSED | READY | IN PROGRESS | BLOCKED | VERIFICATION | DONE | ABANDONED
- Depends on: <task IDs or none>
- Skill: <specialist skill>
- Scope: <bounded files, components, or behavior>
- Acceptance criteria: <criterion IDs>
- Baseline proof: <direct pre-change procedure>
- Expected proof: <direct completion procedure>
- Evidence: <observed result and revision, or none>
- Blocker: <condition and resolver, or none>
```

Keep stable task IDs and full task detail out of the index.

## State rules

A task is `READY` only when dependencies are `DONE`, no decision is missing,
scope is bounded, criteria and direct proof are defined, and required safe access
exists.

- `PROPOSED`: incomplete or not executable.
- `READY`: every readiness condition holds.
- `IN PROGRESS`: the one selected task.
- `BLOCKED`: a named condition and resolver prevent progress.
- `VERIFICATION`: implementation exists but proof is missing or failed.
- `DONE`: implementation, direct proof, relevant checks, and final-revision
  reconciliation succeeded.
- `ABANDONED`: authorized stop or replacement; dependencies remain unsatisfied
  unless the plan removes them.

The rule is simple: at most one task may be `IN PROGRESS`. Never start a second
until the current task is `DONE`, `BLOCKED`, or `ABANDONED`. Never infer `DONE`
from code presence, checkboxes, stale evidence, or unrun tests.

## Sequential workflow

1. Reconcile `index.md`, `specification.md`, `implementation.md`, `tasks.md`,
   repository revision, status, implementation, and evidence. Treat the index as
   summary and move stale states backward.
2. Create or refine bounded technical tasks only when direction is known. Route a
   consequential unresolved choice to `solution-framing`.
3. Select exactly one executable `READY` task and mark only it `IN PROGRESS`.
4. In the same agent, apply its named specialist skill. Do not replace specialist
   rules with general delivery rules.
5. Record proof, checks, revision, blocker, and resulting task state. Failed
   verification remains `VERIFICATION` or `BLOCKED`; do not run dependents.
6. Update feature-level evidence in `implementation.md` and only this feature's
   compact row in `index.md`.
7. If complete delivery was requested, select the next `READY` task and continue.

Do not stop merely because one task, test, file change, specialist workflow, or
lifecycle update completed.

## Stop conditions

Stop only for `PRODUCT DECISION REQUIRED`, `SPLIT REQUIRED`, an unresolved safe
blocker, missing access, an unauthorized destructive or irreversible action,
failed verification after bounded correction attempts, specification/repository
contradiction, no executable `READY` task, or all tasks completed.

A blocked task does not prevent a later independent `READY` task; execution still
remains sequential.

## Output contract

```markdown
## Delivery update
## Task evidence
## Updated artifacts
## Next task or stop reason
## Delivery state
```

Report one active or just-completed task, observed proof, changed artifacts, next
task or exact stop reason, and one feature state. Never imply parallel execution
or unsupported completion.
