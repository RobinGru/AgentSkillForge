---
name: feature-lifecycle
description: Maintain one compact, revision-bound status record for a substantial feature across sessions. Use for durable readiness, evidence, blockers, and next action; do not plan tasks, execute work, or replace specialist proof.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.6.5
---

# Feature lifecycle

Use the repository's established language and conventions for any artifacts you create or update.
Use the smallest sufficient context and bounded tool output. Reuse inspected
evidence and stop once the task can proceed safely; never trade correctness,
safety, or required verification for brevity.

Keep a compact, revision-bound record across sessions. This is not a
project-management system, task list, transcript, delivery loop, or replacement for Git,
tests, review, or CI.

Use `feature-delivery` for sequential task coordination and specialist skills for
decisions, implementation, review, migration, or proof.

## Record

Follow repository convention; otherwise maintain:

```text
docs/features/<feature-id>/implementation.md
```

```markdown
# <feature-id> — <feature name>
- State: PROPOSED | READY | IN PROGRESS | BLOCKED | VERIFICATION | DONE | ABANDONED
- Specification: MISSING | DRAFT | READY
- Decision: NOT REQUIRED | PENDING | READY
- Observed revision: <full SHA or reason unavailable>
- Verified revision: <full SHA or reason unavailable>
- Scope: <affected areas>; non-goals: <exclusions>
- Tasks: <link and compact state summary, or not created>
- Evidence: <criterion> — <direct proof and result>
- Blocker: <condition and resolver, or none>
- Next action: <one bounded action and expected result>
```

Link, never copy, `specification.md`, `tasks.md`, and decisions. They own behavior
and task state; this record owns feature revision and evidence summary.
`docs/features/index.md` remains a compact projection.

## State rules

- `PROPOSED`: behavior, direction, or readiness is incomplete.
- `READY`: one known unblocked next action exists.
- `IN PROGRESS`: one sequential task is active.
- `BLOCKED`: a named condition prevents the next action; name its resolver.
- `VERIFICATION`: implementation exists but final evidence is missing.
- `DONE`: all criteria have current direct proof, required checks passed on the
  final revision, and `Observed revision` equals `Verified revision`.
- `ABANDONED`: an authorized owner stopped or replaced the feature.

Never infer state from checkboxes, commits, silence, or time. Reconcile current
repository facts first and move state backward when evidence is stale. `DONE`
does not imply approval, merge, deployment, release, or stakeholder acceptance.

## Update procedure

1. Inspect current record, links, revision, relevant code, tests, and status.
2. Update readiness, scope, evidence, blockers, and revisions from observed facts.
3. Map criteria to direct proof and revision.
4. Set exactly one bounded next action with expected result.
5. Refresh only this feature's index row.
6. Verify links, final diff, executed checks, and explicit unrun checks.

Do not select or execute tasks. `feature-delivery` may persist supported task
results; the specialist's direct proof remains authoritative.

## Output contract

```markdown
## Lifecycle update
## Evidence
## Updated artifacts
## Next safe action
## Lifecycle state
```

Report previous and current state, evidence, changed artifacts, exactly one next
action, and one current state. Keep stale evidence and unrun checks explicit.
