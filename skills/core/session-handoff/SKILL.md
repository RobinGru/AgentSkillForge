---
name: session-handoff
description: Preserve a compact verified continuation record for unfinished repository work. Use when a later session or developer must resume from current worktree state, evidence, blockers, and exactly one safe next action.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.6.5
---

# Session handoff

Use the repository's established language and conventions for any artifacts you create or update.
Use the smallest sufficient context and bounded tool output. Reuse inspected
evidence and stop once the task can proceed safely; never trade correctness,
safety, or required verification for brevity.

Preserve actionable transient state for unfinished work. Do not create a
transcript, retrospective, specification, or implementation plan.

For tracked work, `feature-lifecycle` owns durable feature status; this skill owns
current worktree continuation state. Link rather than duplicate durable artifacts.

## Activation boundary

Use when concrete work is unfinished and a later session or developer must
continue after context loss, a decision, dependency, access request, or external
result. Do not use for completed work, generic summaries, or state already fully
captured by durable artifacts. Do not implement or resolve open decisions while
recording the handoff.

## Workflow

### 1. Establish objective and sources

State the narrow continuation objective. Link the owning issue, specification,
decision, review, investigation, lifecycle record, or generated artifact. Mark an
inferred objective `Inferred`; do not copy authoritative content.

### 2. Inspect current repository state

Inspect branch, revision, staged, unstaged, untracked, renamed and deleted files,
diff, relevant commits, and checks already run. Use repository facts, not memory.
Exclude secrets, personal data, credentials, and unnecessary local paths.

### 3. Classify work and evidence

Separate `Durably completed`, `Completed but fragile`, `In progress`, `Attempted
and rejected`, and `Not started`. For active changes, state purpose and whether
preserved in commit, worktree, stash, artifact, or nowhere.

Record only observed checks. Distinguish current evidence, stale results, checks
not run, and checks blocked by environment or access.

### 4. Preserve blockers and next action

List only decisions, unknowns, risks, access gaps, dependencies, and conflicts
that can change continuation; name each resolver. Give exactly one bounded action,
its prerequisite, concrete file, command, artifact, or question, and expected
observable result. Never write “continue implementation.”

### 5. Validate

Compare the record with current repository state, verify local references, remove
duplicates and stale claims, and keep uncertainty explicit. Choose exactly one
allowed state:

- `READY TO CONTINUE`
- `DECISION REQUIRED`
- `MORE EVIDENCE REQUIRED`
- `ENVIRONMENT ACCESS REQUIRED`
- `EXTERNAL DEPENDENCY PENDING`
- `NO SAFE CONTINUATION STATE`

## Output contract

Use these exact headings in this order:

```markdown
## Continuation objective
## Source artifacts
## Repository state
## Completed and active work
## Evidence and checks
## Open decisions and unknowns
## Risks and constraints
## Next safe action
## Handoff state
```

State commit status and available branch, revision, staged, unstaged, and untracked
state. `Next safe action` contains one action and result; `Handoff state` contains
exactly one allowed state with factual basis.
