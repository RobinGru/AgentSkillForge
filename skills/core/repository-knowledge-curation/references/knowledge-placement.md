# Knowledge placement

Use this guide to choose one canonical home and avoid permanent context growth.

## Placement matrix

| Destination | Use for | Keep out |
| --- | --- | --- |
| `AGENTS.md` | Short actionable instructions, mandatory repository entry points, hard constraints, and pointers needed across many tasks in the file's scope. | Repository encyclopedia, architecture narrative, session state, raw learnings, generic best practices, duplicated detail. |
| Architecture | Durable system structure, responsibilities, boundaries, dependency direction, public interfaces, data flow, ownership, and invariants. | Temporary plans, command logs, unresolved preferences, product acceptance criteria. |
| Testing | Verified test and validation commands, environment setup, fixtures, test data, suite selection, evidence expectations, and scoped limitations. | Claims that a command succeeds without execution, implementation plans, unexplained flaky symptoms. |
| Decision | An accepted consequential choice with context, considered options, decision owner or authority, consequences, status, and verification obligations. | Open recommendations, agent-selected architecture, routine local implementation details. |
| Learning | A verified repository-specific cause, pitfall, workaround, or discovery likely to matter again but not yet a broad stable rule. | Chat transcripts, guesses, one-off routine activity, unexplained failures, universal advice. |
| Another canonical source | Product behavior, symbol-local contracts, operational procedures, feature state, or other knowledge already owned by a repository-defined artifact. | Copies created only to make the information appear in another folder. |
| No durable update | Transient, obvious, duplicated, unverified, sensitive, or unlikely-to-recur information. | Knowledge whose absence creates a credible repeat failure. |

## Classification questions

Ask in this order:

1. Is the claim verified or explicitly accepted?
   - If no, gather evidence or keep it out of durable documentation.
2. Does another artifact already own this kind of truth?
   - If yes, update or link that artifact.
3. Is it an instruction needed for most work in a scope?
   - If yes, use a concise `AGENTS.md` directive or pointer.
4. Does it describe stable system structure or an invariant?
   - If yes, use architecture documentation.
5. Does it explain how repository behavior is verified?
   - If yes, use testing documentation.
6. Does it record a consequential choice that has been accepted?
   - If yes, use a decision record.
7. Is it a reusable, verified finding with narrower or uncertain longevity?
   - If yes, use a learning record.
8. Would future work find it naturally in code, tests, configuration, or an
   existing document without extra guidance?
   - If yes, prefer no durable update or a small pointer.

## Minimal record shapes

Follow repository conventions first. When none exist, include only fields that
preserve validity and retrieval.

### Architecture

- Statement or invariant
- Scope and affected boundaries
- Evidence or authoritative source
- Consequences for changes
- Exceptions or unknowns
- Last verified when time-sensitive

### Testing

- Purpose and scope
- Exact repository-defined command or procedure
- Required environment, services, fixtures, and data
- Expected evidence
- Selection or narrowing mechanism
- Known verified limitation
- Last verified when environment-sensitive

### Decision

- Status
- Decision question
- Context and constraints
- Considered viable options
- Accepted decision and authority
- Consequences and risks
- Verification or enforcement
- Supersedes or superseded by

An unresolved choice is not a decision record. Use `solution-framing` first.

### Learning

- Context
- Observed symptom or risk
- Evidence
- Verified cause
- Verified resolution or avoidance
- Failed approaches only when reusable
- Scope, versions, and environment
- Last verified
- Promotion or retirement condition

## Promotion and retirement

Promote a learning when repeated evidence establishes a broader stable rule:

- into `AGENTS.md` when it becomes a concise instruction required across many
  tasks;
- into architecture when it becomes a durable boundary or invariant;
- into testing when it becomes the standard verification procedure;
- into a decision record when an authorized consequential choice adopts it.

After promotion, replace duplicate learning text with a link or retire the record
according to repository convention.

Demote or retire knowledge when:

- its version, environment, path, interface, or dependency scope no longer
  applies;
- an accepted decision supersedes it;
- executable checks make the prose redundant;
- evidence cannot be reproduced;
- the statement is too broad for the facts that remain.

## Conflict handling

When documentation conflicts with code, tests, automation, or another document:

- do not silently choose the newest-looking source;
- state whether each source describes current behavior, intended behavior, or
  policy;
- identify the owner, direct check, or accepted decision needed to resolve the
  conflict;
- keep the contradiction visible when it cannot be resolved safely;
- avoid updating several files with the same unconfirmed interpretation.

## Context budget rule

Permanent instructions consume attention on every applicable task. Add an
`AGENTS.md` line only when its repeated benefit is greater than that permanent
cost. Detailed knowledge should remain in focused files that can be discovered
through a short pointer and loaded only when relevant.
