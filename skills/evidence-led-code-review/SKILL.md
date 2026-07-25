---
name: evidence-led-code-review
description: Review a concrete code change by tracing its relevant effects and separating observed defects, risks, missing evidence, and preferences. Use when a diff or changed files can be inspected.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.2.0-beta.1
---

# Evidence-led code review

Review a proposed change against its intended behavior and evidence available
in the repository. Do not turn unknown context into a forced approval or
rejection.

## Use this skill when

- A diff, patch, pull request, or changed-file set is available.
- The change needs an integration decision or actionable findings.
- Tests, configuration, interfaces, or runtime effects can be inspected.

## Do not use this skill when

- No concrete change is available.
- The request is to implement rather than assess a change.
- The primary question is a measured performance investigation.

## Workflow

### 1. Scope

Record supplied files or diff, available specification or issue, existing
tests, and checks that can actually run. State any missing review context.

### 2. Reconstruct intent

Identify intended behavior change, contracts that should remain stable,
affected users or systems, and success criteria. If intent cannot be inferred,
record the review as blocked rather than inventing a verdict.

### 3. Trace change effects

Follow only paths relevant to the change:

- public interfaces and callers;
- added, removed, or transformed data;
- side effects and persistence or migration paths;
- failures and recovery behavior;
- authorization boundaries;
- runtime or resource impact.

Do not apply irrelevant lenses by default.

### 4. Classify evidence

Label each claim with one status:

- **Observed:** directly present in code, configuration, or supplied artifact.
- **Reproduced:** demonstrated by an executed test or controlled run.
- **Required:** imposed by the stated contract or authoritative requirement.
- **Inferred:** reasoned from available facts but not directly observed.
- **Unverified:** cannot be confirmed with available evidence.

### 5. Write findings

Use a finding only when it has a location or a precisely bounded missing
context. Classify type as **Defect**, **Risk**, **Missing evidence**,
**Maintainability concern**, or **Preference**. Use severity **Blocker**,
**Major**, **Moderate**, or **Minor**. Preferences cannot block integration.

```markdown
### [Severity] Title

- Type:
- Location:
- Evidence:
- Affected behavior:
- Impact:
- Confidence:
- Recommended correction:
- Verification:
```

Set confidence to High, Medium, or Low. Mark unexecuted checks as unverified.

### 6. Decide

Choose one decision:

- **APPROVE:** evidence supports integration and no blocking finding remains.
- **COMMENT:** observations or suggestions do not require a change.
- **REQUEST CHANGES:** a supported defect, risk, or missing evidence requires action.
- **BLOCKED:** required intent or review context is unavailable.

## Output contract

Return sections named `Scope`, `Intent`, `Evidence considered`, `Findings`,
`Checks not run`, and `Decision`. Every finding must include all template
fields. The decision must name its evidence basis and remaining uncertainty.
