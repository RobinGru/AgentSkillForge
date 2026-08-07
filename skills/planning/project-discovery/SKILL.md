---
name: project-discovery
description: Define an evidence-based product direction and initial capability map for a new or purpose-unclear repository. Use before feature specification or technical design when users, outcomes, first-release scope, non-goals, constraints, or success signals are unresolved.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.6.5
---

# Project discovery

Use the repository's established language and conventions for any artifacts you create or update.
Use the smallest sufficient context and bounded tool output. Reuse inspected
evidence and stop once the task can proceed safely; never trade correctness,
safety, or required verification for brevity.

Turn an idea or unclear repository into a bounded product brief and prioritized
capability map. Do not choose architecture or implement.

## Activation boundary

Use when product purpose, users, outcomes, scope, constraints, non-goals, or
success signals are unknown or disputed. Use `feature-specification` when one
known capability only needs behavior, `solution-framing` when product direction
is accepted and a technical choice remains, and specialist skills for delivery.

## Rules

- Inspect existing product artifacts and behavior before asking questions.
- Separate observed, provided, inferred, assumed, and unknown claims.
- Ask only questions that can change scope, priority, or viability.
- Prefer the smallest coherent useful release.
- Do not invent users, research, baselines, targets, constraints, or approval.

## Workflow

### 1. Establish problem and users

Inventory current evidence, intent, contradictions, and missing decisions. State
the undesirable condition, primary actors, jobs, costly failures, and desired end
condition without prescribing a solution.

### 2. Bound outcomes

Record in-scope outcomes, explicit non-goals, hard constraints, data and permission
concerns, integrations, operating context, reversible assumptions, and known
owners. For each outcome, define an observable signal, source, horizon, and owner;
keep missing baselines or targets unknown.

### 3. Build the initial capability map

List independently understandable capabilities and prioritize only the first
coherent release. Keep this brief-local product index minimal:

```markdown
| ID | Feature | Status | Spec |
|---|---|---|---|
```

Use `Idea`, `Ready`, `In Progress`, and `Done`. This map supports product
prioritization only; it is not `docs/features/index.md` and does not track
implementation. Hand a selected capability to `feature-specification`, which
creates its canonical specification and compact feature-index entry. Use
`feature-lifecycle` only when durable revision-bound status is needed.

### 4. Obtain product decision

Present the brief for human review. Drafts, silence, and agent recommendations are
not approval. After approval, identify the first capability to specify.

## Output contract

Return exactly these headings:

```markdown
## Product problem
## Users and jobs
## Outcomes and success signals
## Scope, non-goals, and constraints
## Repository evidence and uncertainty
## Initial capability map
## Recommended first capability
## Open decisions
## Handoff state
```

Choose one state: `READY FOR FEATURE SPECIFICATION`, `PRODUCT DECISION REQUIRED`,
`MORE EVIDENCE REQUIRED`, or `ALREADY INITIALIZED`.
