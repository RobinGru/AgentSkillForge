---
name: fact-based-code-review
description: Review a concrete diff or changed-file set for integration readiness. Use when relevant effects can be traced; separate observed defects and risks from missing facts and preferences, then return actionable findings plus one evidence-based decision.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.6.5
---

# Fact-based code review

Use the repository's established language and conventions for any artifacts you create or update.
Use the smallest sufficient context and bounded tool output. Reuse inspected
evidence and stop once the task can proceed safely; never trade correctness,
safety, or required verification for brevity.

Review a concrete change against intended behavior and repository evidence. Never
turn missing context into forced approval or rejection.

## Activation boundary

Use when a diff, patch, PR, or changed-file set exists and needs findings or an
integration decision. Do not use without a concrete change, for implementation,
or as a performance investigation.

## Workflow

### 1. Establish intent and scope

Inspect the supplied change, specification or issue, relevant tests, and runnable
checks. Identify intended behavior, contracts to preserve, affected users or
systems, and missing context. If intent cannot be established, return `BLOCKED`.

### 2. Trace relevant effects

Follow only affected interfaces and callers, data transformations, persistence,
side effects, failure and recovery paths, authorization, configuration, and
material runtime effects. Do not apply irrelevant review lenses.

Label supporting claims `Observed`, `Reproduced`, `Required`, `Inferred`, or
`Unverified`.

### 3. Write actionable findings

Create a finding only for a located defect or risk, or precisely bounded missing
information. Classify type as `Defect`, `Risk`, `Missing information`,
`Maintainability concern`, or `Preference`; severity as `Blocker`, `Major`,
`Moderate`, or `Minor`; confidence as `High`, `Medium`, or `Low`. Preferences
cannot block integration.

```markdown
### [Severity] Title
- Type:
- Location:
- Supporting details:
- Affected behavior:
- Impact:
- Confidence:
- Recommended correction:
- Verification:
```

### 4. Decide

Choose one:

- `APPROVE` — evidence supports integration and no blocker remains;
- `COMMENT` — only non-required observations remain;
- `REQUEST CHANGES` — a supported concern requires action;
- `BLOCKED` — required intent or evidence is unavailable.

## Output contract

Return `Scope`, `Intent`, `Facts considered`, `Findings`, `Checks not run`, and
`Decision`. Include every finding field, the decision's factual basis, and
remaining uncertainty. Never claim an unrun check.
