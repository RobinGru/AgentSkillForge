---
name: solution-framing
description: Establish a defensible direction for an unclear or consequential software decision before implementation. Use when goals, boundaries, interfaces, ownership, risks, or non-goals need an explicit decision record.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.2.0-beta.1
---

# Solution framing

Turn an uncertain technical request into a bounded decision that another
person or agent can inspect and act on. The result is a decision brief, not an
implementation plan disguised as discovery.

## Use this skill when

Use this skill when one or more of these conditions apply:

- The requested outcome or expected behavior is ambiguous.
- The work crosses system boundaries, interfaces, or ownership lines.
- Several feasible directions have materially different costs or risks.
- Choosing the wrong direction would make later work expensive to undo.
- Constraints, non-goals, risks, or acceptance checks are absent.

## Do not use this skill when

Do not use this skill for a fully specified local change, a typo or isolated
configuration value, a request with an accepted decision brief, or a code
review with a known change set. Route a performance symptom without a baseline
to a performance investigation instead.

## Operating rules

- Inspect available project facts before asking for information.
- Label each important statement as observed, provided, assumed, or unknown.
- Ask only for information that can change the decision or prevent unsafe work.
- Prefer a reversible, smaller direction when it satisfies the stated need.
- Do not present an assumption, estimate, or unrun check as facts.
- Do not begin implementation until the handoff outcome permits it.

## Workflow

### 1. Frame the problem

State the requested change without prescribing a solution. Identify the
affected users or systems, the observed starting condition, and the desired
end condition. If any of these are unknown, record that uncertainty.

**Exit:** a one-paragraph problem statement that can be disproved or refined.

### 2. Bound the decision

List in-scope work, excluded work, hard constraints, reversible assumptions,
blockers, and affected interfaces. Use
[`risk-and-reversibility.md`](references/risk-and-reversibility.md) to assess
whether a missing fact blocks progress or can remain an assumption.

**Exit:** a bounded decision surface with explicit ownership and dependencies.

### 3. Compare options when needed

Compare only genuinely viable options. Use criteria that arise from the
problem, such as safety, compatibility, migration cost, reversibility,
operational burden, or time to confirm key facts. An option may be rejected
without a full comparison when it violates a hard constraint.

**Exit:** a concise comparison or a reason why only one viable direction
exists.

### 4. Decide in a brief

Create the decision brief using
[`solution-brief-template.md`](assets/solution-brief-template.md). Every
required heading must be present. Link facts to the choice, separate
assumptions from facts, and state how acceptance will be demonstrated. Consult
[`decision-record.md`](references/decision-record.md) for field definitions.

**Exit:** a complete decision brief with no unlabelled uncertainty.

### 5. Choose a handoff state

Choose exactly one result:

- **Ready to implement:** scope, constraints, owner, and acceptance checks
  are sufficient.
- **Research required:** a named unknown prevents a safe decision.
- **Decision required:** a stakeholder must choose among stated trade-offs.
- **Split required:** independent decisions should be resolved separately.

## Output contract

Return one decision brief with these exact headings:

1. `## Decision`
2. `## Facts`
3. `## Assumptions`
4. `## Boundaries`
5. `## Selected approach`
6. `## Rejected approaches`
7. `## Risks and mitigations`
8. `## Acceptance checks`
9. `## Open blockers`
10. `## Handoff state`

A brief is complete only when every heading has substantive content, each
claim is labelled as observed, provided, assumed, or unknown; rejected
options have a reason, and the handoff state is one of the four allowed values.

## References

- [Decision record fields](references/decision-record.md)
- [Risk and reversibility guide](references/risk-and-reversibility.md)
- [Decision brief template](assets/solution-brief-template.md)
