---
name: safe-code-change
description: Make a bounded code change with an explicit behavior contract and proportionate verification. Run a direct proof before editing, repeat it afterward, and report remaining uncertainty.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.5.0
---

# Safe code change

Make a small, understood change and prove its intended effect without expanding
the task into redesign or broad refactoring.

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

Use the narrowest direct proof before and after the patch.

The pre-change proof establishes the baseline. The post-change proof repeats the
same behavior path against the final worktree.

## Workflow

### 1. Inspect the boundary

Read:

- affected implementation;
- nearest relevant tests;
- public callers and contracts at risk;
- closest established repository pattern;
- current diff and repository instructions.

Expand inspection only for demonstrated dependencies or side effects.

### 2. Define the behavior contract

Before editing, record:

- current observable behavior;
- intended observable behavior;
- behavior that must remain unchanged;
- interfaces, data, permissions, callers, and side effects at risk;
- direct success signal;
- non-goals.

A behavior-preserving refactor must name the observable contract it preserves.

Route unresolved product or architecture decisions before editing.

### 3. Establish the baseline proof

Choose the narrowest procedure that directly exercises the behavior contract.

Examples include a targeted test, controlled command, local request, browser
scenario, integration fixture, or output comparison.

Run it before editing and record:

- invocation or procedure;
- expected pre-change result;
- observed result;
- whether it directly checks the contract;
- relevant environment or fixture.

For a defect or intentional behavior change, the baseline should demonstrate the
current wrong or missing behavior.

For a behavior-preserving refactor, it should demonstrate the behavior that must
remain stable.

When no direct proof is possible, state the exact limitation. Route to
`failure-investigation` when that gap prevents a safe local change.

### 4. Apply the patch

Make the smallest coherent change that satisfies the behavior contract.

Preserve unrelated behavior, existing public contracts, error paths, repository
conventions, and user work already present.

Keep unrelated cleanup, speculative abstractions, broad renaming, test weakening,
and formatting churn outside the patch.

Reassess the task when the required boundary expands materially.

### 5. Repeat the direct proof

Run the same proof against the final patch.

Record:

- expected post-change result;
- observed result;
- whether the original symptom is corrected or preserved behavior remains;
- whether the same proof was repeated.

When the proof itself must change, explain why and show that the replacement
would still distinguish the original state.

### 6. Run proportionate checks

Run checks justified by the boundary and risk:

1. nearest targeted tests;
2. affected integration tests;
3. type and static analysis;
4. lint and formatting;
5. affected build;
6. broader suites when warranted.

A broad passing suite does not replace a failed or missing direct proof.

Mark results obtained before later edits as stale unless repeated.

### 7. Inspect the final diff

Confirm that:

- every changed line supports the behavior contract;
- no unrelated user work was overwritten;
- temporary diagnostics and fixtures are removed;
- tests were not weakened;
- generated or lock-file changes are justified;
- the direct proof ran against the final worktree;
- no unexpected file remains modified.

### 8. Report

Report the change, preserved contract, pre-change proof, post-change proof,
additional checks, gaps, risks, and intentionally untouched areas.

Use one verdict:

- `PROVED`
- `PARTIALLY PROVED`
- `NOT PROVED`

## Output contract

Use these exact headings:

```markdown
## Change
## Behavior contract
## Baseline proof
## Post-change proof
## Additional checks
## Checks not run
## Remaining risks
## Intentionally untouched
## Verification verdict
```

`Baseline proof` must include:

```markdown
- Invocation or procedure:
- Expected pre-change result:
- Observed pre-change result:
- Direct behavior signal: Yes | No
- Environment or fixture:
```

`Post-change proof` must include:

```markdown
- Invocation or procedure:
- Expected post-change result:
- Observed post-change result:
- Same proof repeated: Yes | No
```

`Verification verdict` must contain exactly one allowed verdict and its factual
basis.

The change is complete when the behavior contract is explicit, the final patch
stays within the understood boundary, the direct proof has been repeated or its
gap is explicit, and remaining uncertainty is not presented as success.
