---
name: safe-code-change
description: Make a bounded code change with an explicit behavior contract and proportionate verification. Run a direct proof before editing, repeat it afterward, and report remaining uncertainty.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.6.4
---

# Safe code change

Use the repository's established language and conventions for any artifacts you create or update.

Make a small, understood change and prove its intended effect without expanding the task into redesign or broad refactoring.

## Activation boundary

Use this skill when:

- a localized defect has a reproducible symptom and known change boundary;
- a specific observable behavior must change;
- a small refactor must preserve behavior;
- an investigation has established the implementation boundary;
- one independently safe migration step is ready.

Route elsewhere when:

- the cause or safe boundary is unknown: `failure-investigation`;
- product behavior or architecture remains unresolved;
- several coordinated compatibility states are required:
  `compatibility-migration`;
- the task is only review or performance diagnosis.

## Core rule

Use the narrowest direct proof before and after the patch. The pre-change proof
establishes the baseline; the post-change proof repeats that path against the final worktree.

Minimize context and chat output throughout the task:
- read only targeted files and relevant line ranges;
- expand inspection only when evidence requires it;
- do not print complete files, complete diffs, directory trees, or successful
  command output into chat unless explicitly requested;
- retain only the command, exit status, and decisive output lines;
- summarize routine tool results in one short sentence or less.

## Workflow
### 1. Inspect the boundary

Read only the smallest relevant scope:

- affected implementation;
- nearest relevant tests;
- public callers and contracts at risk;
- closest established repository pattern;
- current diff and applicable repository instructions.

Expand inspection only for demonstrated dependencies or side effects. Do not
perform broad repository inventories, recursive scans, or unrelated file reads.

### 2. Define the behavior contract

Before editing, record internally:

- current observable behavior;
- intended observable behavior;
- behavior that must remain unchanged;
- interfaces, data, permissions, callers, and side effects at risk;
- direct success signal;
- non-goals.

Do not print the full contract into chat unless clarification is required or the
user explicitly requests it.

A behavior-preserving refactor must identify the observable contract it preserves.

Route unresolved product or architecture decisions before editing. Within a
tracked feature, `feature-lifecycle` records the resulting feature-level evidence;
this skill remains authoritative for the patch and direct proof.

### 3. Establish the baseline proof

Choose the narrowest procedure that directly exercises the behavior contract.

Examples include a targeted test, controlled command, local request, browser
scenario, integration fixture, or output comparison.

Run it before editing and retain:

- invocation or procedure;
- expected pre-change result;
- observed result;
- whether it directly checks the contract;
- relevant environment or fixture.

For a defect or intentional behavior change, the baseline should demonstrate the
current wrong or missing behavior.

For a behavior-preserving refactor, it should demonstrate the behavior that must
remain stable.

When no direct proof is possible, retain the exact limitation. Route to
`failure-investigation` when that gap prevents a safe local change.

Do not paste full logs. Keep only decisive failure or result lines.

### 4. Apply the patch

Make the smallest coherent change that satisfies the behavior contract.

Preserve unrelated behavior, existing public contracts, error paths, repository
conventions, and user work already present.

Keep unrelated cleanup, speculative abstractions, broad renaming, test weakening,
and formatting churn outside the patch.

Reassess the task when the required boundary expands materially.

Do not reproduce edited source code in chat unless explicitly requested.

### 5. Repeat the direct proof

Run the same proof against the final patch.

Retain:

- expected post-change result;
- observed result;
- whether the original symptom is corrected or preserved behavior remains;
- whether the same proof was repeated.

When the proof itself must change, explain why and confirm that the replacement
would still distinguish the original state.

Do not paste successful output. Report only the command and concise result.

### 6. Run proportionate checks

Run only checks justified by the boundary and risk:

1. nearest targeted tests;
2. affected integration tests;
3. type and static analysis;
4. lint and formatting;
5. affected build;
6. broader suites only when materially warranted.

A broad passing suite does not replace a failed or missing direct proof.

Mark results obtained before later edits as stale unless repeated.

Do not run broad suites by default for a localized low-risk change when a direct
targeted proof and nearest relevant checks are sufficient.

### 7. Inspect the final diff

Confirm internally that:

- every changed line supports the behavior contract;
- no unrelated user work was overwritten;
- temporary diagnostics and fixtures are removed;
- tests were not weakened;
- generated or lock-file changes are justified;
- the direct proof ran against the final worktree;
- no unexpected file remains modified.

Do not print the full diff. Mention only affected paths and material effects.

### 8. Report

Return only the minimum information needed to verify the result.

Do not:

- repeat code, diffs, file contents, commands, or routine process steps;
- reproduce successful tool output;
- explain routine successful checks;
- include unchanged behavior unless materially relevant;
- add introductions, summaries, recommendations, or follow-up offers;
- use tables;
- use code blocks unless explicitly requested.

Default maximum: 6 lines and 100 words.

## Output contract
Use exactly this compact structure:

```markdown
Change: `<path>` — knapper Effekt
Proof: `<command>` — vorher: …; nachher: …
Checks: `<command>` ✓
Risk: …
Result: PROVED | PARTIALLY PROVED | NOT PROVED
```

Rules:

- `Change`, `Proof`, and `Result` are always present.
- Omit `Checks` when no additional check was run.
- Omit `Risk` when no material uncertainty remains.
- Use one line per field.
- Mention multiple files or checks comma-separated.
- Never print a full diff, full file, long log, or large code block unless
  explicitly requested.
- Do not restate the behavior contract when the change description already makes
  it clear.
- Keep commands, paths, error text, and verdict tokens exact.
- `Result` contains exactly one allowed verdict and a short factual basis.
- If the user requests more detail, expand only the requested section.

Allowed verdicts:
- `PROVED`
- `PARTIALLY PROVED`
- `NOT PROVED`

The change is complete when the behavior contract is explicit internally, the
final patch stays within the understood boundary, the direct proof has been
repeated or its gap is explicit, and remaining uncertainty is not presented as
success.
