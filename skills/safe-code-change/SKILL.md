---
name: safe-code-change
description: Make a bounded code change with an explicit behavior contract and proportionate verification. Use for localized fixes or behavior-preserving refactors, not for broad design, review, or investigation work.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.3.0-beta.1
---

# Safe code change

Use this workflow for a small, understood change where safety comes from a
clear contract and direct proof, not from expanding the task into a broad
refactor.

## Use this skill when

- A localized defect has a reproducible symptom or clear expected behavior.
- A small refactor must preserve observable behavior.
- The likely files and affected boundary can be identified without a broad
  redesign or investigation.

## Do not use this skill when

- The request is only to review an existing change.
- A performance question needs measurement or bottleneck analysis.
- A component needs structural decomposition before a safe local patch exists.
- The outcome, scope, or ownership decision remains unclear.

## Workflow

### 1. Inspect

Read the affected code, its nearest tests, and the closest existing pattern.
Identify the narrowest change boundary and expand the inspection only when a
real dependency requires it.

### 2. Contract

Before editing, record:

- behavior that must remain unchanged;
- behavior that must change;
- public interfaces, data formats, or callers at risk;
- the smallest signal that will demonstrate success.

If the contract cannot be stated, stop and obtain the missing decision.

### 3. Patch

Make the smallest sufficient change. Preserve error paths and existing type,
language, and style conventions. Do not fold unrelated cleanup, speculative
abstractions, or an API redesign into the patch.

### 4. Prove

Choose only the checks justified by the change, in this order where relevant:

1. reproduce the original symptom or run the affected test;
2. run the nearest targeted test;
3. run type or lint checks;
4. build the affected artifact;
5. run a broader suite when the boundary or risk warrants it.

Record checks that were not run and why. A passing broad check does not replace
the direct behavior signal when one is available.

### 5. Report

Report the completed change, the proof obtained, unrun checks, remaining
risks, and deliberately untouched areas. Do not claim checks that did not run.

## Output contract

Use this format after the change:

```markdown
## Change

## Contract preserved

## Facts

## Checks not run

## Remaining risks

## Intentionally untouched
```

Each section must contain a concrete statement. If no risk, skipped check, or
untouched area applies, state that explicitly rather than omitting the section.
