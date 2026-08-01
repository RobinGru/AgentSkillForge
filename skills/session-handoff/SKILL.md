---
name: session-handoff
description: Create a compact, verified continuation record for unfinished repository work when another session or developer must resume from preserved local state, evidence, and one safe next action.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.6.2
---

# Session handoff

Use the repository's established language and conventions for any artifacts you create or update.


Preserve actionable state for unfinished repository work. This is a continuation
record, not a transcript, retrospective, specification, or implementation plan.

For a tracked feature, `feature-lifecycle` owns durable feature state while this
skill owns transient worktree state. Reference the canonical lifecycle record and
fold durable facts found after resumption back into it; do not duplicate the diff
or staged-state details there.

## Activation boundary

Use this skill when concrete work is unfinished and another session, agent, or
developer will continue it; context may be lost; work pauses on a decision,
dependency, access request, or external result; or important local state is not
already preserved by durable artifacts.

Do not use it for completed work, generic summaries, or work already captured
completely by durable repository artifacts. Do not implement changes or resolve
open product or architecture decisions while recording the state.

## Workflow

### 1. Define the continuation objective

State the narrow task to continue. Reference the active issue, specification,
decision, review, or investigation when available; label an inferred objective
as `Inferred`.

### 2. Inspect current state

Inspect the branch and current revision; staged, unstaged, untracked, renamed,
and deleted files; current diff; relevant recent commits; referenced artifacts;
and commands or checks already executed. Use repository state, not conversation
memory. Do not expose secrets, credentials, personal data, or unnecessary local
paths.

### 3. Reference sources of truth

Name or link artifacts that own important information, such as issues,
specifications, decisions, reports, diffs, or generated outputs. Do not duplicate
their full content; record only the interpretation needed to continue correctly.

### 4. Classify the work

Separate work into `Durably completed`, `Completed but fragile`, `In progress`,
`Attempted and rejected`, and `Not started`. For each active change, state its
purpose and whether it is preserved in a commit, worktree, stash, artifact, or
not at all.

### 5. Record evidence

Record only checks and observations that actually occurred. Distinguish current
worktree evidence from older results that may be stale, checks not run, and checks
blocked by missing access or environment. Include exact commands when they aid
continuation and summarize large outputs.

### 6. Preserve unresolved conditions

List decisions, unknowns, risks, missing access, external dependencies, and
conflicts that can change the next action. For each, state what would resolve it.

### 7. Define one safe next action

Give exactly one bounded action, its prerequisite, the file, command, artifact, or
question involved, and the observable result that determines the following step.
Do not write vague instructions such as “continue implementation.”

### 8. Validate the handoff

Compare the record with the current repository state. Verify locally inspectable
references, remove duplicated or stale information, preserve unverified claims as
unverified, and keep unresolved decisions unresolved. Choose exactly one state:

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

`Repository state` must say whether the work is committed and, when available,
name the branch, revision, staged state, unstaged state, and untracked files.
`Next safe action` must contain one concrete action and its expected observable
result. `Handoff state` must contain exactly one allowed state and its factual
basis.
