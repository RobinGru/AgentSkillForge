---
name: solution-framing
description: Select a defensible technical or delivery direction for one consequential decision after product intent is known. Use when viable approaches differ materially in interfaces, ownership, cost, risk, compatibility, or reversibility and need an inspectable decision brief.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.6.4
---

# Solution framing

Use the repository's established language and conventions for any artifacts you create or update.
Use the smallest sufficient context and bounded tool output. Reuse inspected
evidence and stop once the task can proceed safely; never trade correctness,
safety, or required verification for brevity.

Turn one uncertain consequential choice into a bounded, evidence-linked decision.
Do not disguise discovery or implementation planning as a decision.

## Activation boundary

Use when implementation or delivery direction is ambiguous, crosses boundaries,
has materially different viable options, or is expensive to reverse.

Do not use for initial product direction, one capability's behavior contract, an
accepted decision, a fully bounded local change, code review, or unmeasured
performance diagnosis.

## Rules

- Inspect project facts before asking questions.
- Label material claims observed, provided, assumed, or unknown.
- Ask only for information that can change or safely block the decision.
- Prefer the smallest reversible option that satisfies known obligations.
- Do not present estimates, assumptions, or unrun checks as facts.
- Do not implement before the handoff permits it.

## Workflow

### 1. Frame and bound

State affected users or systems, current and desired conditions, in-scope work,
non-goals, constraints, interfaces, owners, assumptions, and blockers. Use
[risk and reversibility](references/risk-and-reversibility.md) to decide whether
an unknown can remain an assumption.

### 2. Compare viable options

Compare only feasible options using problem-derived criteria such as safety,
compatibility, migration cost, reversibility, operational burden, and evidence
cost. Reject a hard-constraint violation directly. If one option remains, state
why comparison is unnecessary.

### 3. Decide and prove readiness

Use the [decision brief template](assets/solution-brief-template.md) and
[decision record fields](references/decision-record.md). Link facts to the choice,
state consequences, mitigations, acceptance checks, and blockers.

For tracked work, `feature-lifecycle` may link the brief; this brief remains
authoritative. Choose exactly one handoff:

- **Ready to implement**
- **Research required**
- **Decision required**
- **Split required**

## Output contract

Return exactly these headings:

```markdown
## Decision
## Facts
## Assumptions
## Boundaries
## Selected approach
## Rejected approaches
## Risks and mitigations
## Acceptance checks
## Open blockers
## Handoff state
```

Every heading must be substantive, uncertainty labelled, rejected options
reasoned, and the handoff one of the four allowed values.
