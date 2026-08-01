---
name: feature-lifecycle
description: Keep a compact, revision-bound record for one substantial feature that spans sessions or agents. Use only when durable coordination is needed beyond a single bounded change.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.6.3
---

# Feature lifecycle

Use the repository's established language and conventions for any artifacts you create or update.


Keep one small record for a feature that must survive across sessions. This is
not a project-management system, task list, transcript, or replacement for
Git, tests, issues, review, or CI.

## Use it when

- one independently verifiable feature spans sessions, agents, or dependencies;
- the repository has no more suitable system of record.

Do not use it for a one-session change, a generic status report, or unclear
product requirements. Use the other specialist skill for product definition,
technical decisions, implementation proof, migrations, or transient handoffs.

## Record

Use the repository convention. Otherwise create:

```text
docs/features/<feature-id>/implementation.md
```

Keep the record compact and include only:

```markdown
# <feature-id> — <feature name>

- State: PROPOSED | READY | IN PROGRESS | BLOCKED | VERIFICATION | DONE | ABANDONED
- Specification: MISSING | DRAFT | READY
- Decision: NOT REQUIRED | PENDING | READY
- Observed revision: <full SHA or reason unavailable>
- Verified revision: <full SHA or reason unavailable>
- Scope: <affected areas>; non-goals: <important exclusions>
- Evidence: <criterion> — <direct proof and result>
- Blocker: <condition and resolver, or none>
- Next action: <one bounded action and expected result>
```

Link an existing specification or decision; do not copy it. Keep transient
worktree details in a handoff, not in this record.

## State rules

- `PROPOSED` or `READY`: readiness is incomplete or the first step is known and unblocked.
- `IN PROGRESS`: implementation or verification is actively observed.
- `BLOCKED`: the next action is prevented; name the resolver.
- `VERIFICATION`: implementation appears complete, but final evidence is missing.
- `DONE`: all criteria have current direct proof, required checks passed on the
  final revision, and `Observed revision` equals `Verified revision`.
- `ABANDONED`: an authorized owner stopped or replaced the feature.

Never infer state from a checkbox, commit message, silence, or elapsed time.
Reconcile the record with the current repository before changing it. Move the
state backward when the evidence or scope is stale. `DONE` does not mean
approved, merged, deployed, released, or accepted by stakeholders.

## Update procedure

1. Confirm the feature ID and inspect the current record, linked artifacts,
   revision, relevant code, tests, and repository status.
2. Mark readiness, scope, evidence, blockers, and revisions from observed facts.
3. Record only evidence or decisions that change the state or next action.
4. Map each acceptance criterion to direct proof and its revision.
5. Set exactly one bounded next action with its expected result.
6. Recheck links, the final diff, and executed checks; state unrun checks.

## Output contract

Use exactly these headings:

```markdown
## Lifecycle update
## Evidence
## Updated artifacts
## Next safe action
## Lifecycle state
```

Report the previous and current state, observed evidence and checks, changed
artifacts, exactly one next action, and exactly one current state. Keep stale
evidence and unrun checks explicit.
