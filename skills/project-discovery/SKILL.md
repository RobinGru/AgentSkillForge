---
name: project-discovery
description: Establish an evidence-based product direction and initial capability map for a new, uninitialized, or purpose-unclear repository. Use before feature specification or technical design when users, outcomes, scope, non-goals, or success signals are not yet agreed.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.4.0
---

# Project discovery

Turn an idea or an unclear repository into a bounded product brief and a small,
prioritized capability map. Define the problem and desired outcomes without
choosing architecture or writing implementation code.

## Use this skill when

- A product or repository is being started.
- Existing code has no trustworthy statement of users, purpose, or scope.
- Product outcomes, non-goals, constraints, or success signals are disputed.
- A feature request cannot be assessed because the wider product boundary is
  missing.

## Do not use this skill when

- One known capability only needs observable behavior and acceptance criteria;
  use `feature-specification`.
- The product direction is accepted and only a technical choice remains; use
  `solution-framing`.
- The task is implementation, diagnosis, migration, review, or release work.

## Rules

- Inspect current product documents, code, tests, configuration, and history
  before asking questions.
- Separate observed facts, user-provided facts, inferences, assumptions, and
  unknowns.
- Ask only questions that can change scope, priority, or product viability.
- Prefer the smallest coherent useful outcome; keep future possibilities out of
  current scope.
- Do not invent research, baselines, users, constraints, or approval.
- Do not select detailed architecture or modify product code.

## Workflow

### 1. Inventory current evidence

Summarize observed capabilities, stated intent, contradictions, and missing
product decisions. Verify important claims against current repository sources.

### 2. Define the problem and users

State the undesirable current condition, affected primary actors, their concrete
jobs and costly failure modes, and the desired end condition. Keep the problem
separate from a proposed solution.

### 3. Bound the product

Record in-scope outcomes, explicit non-goals, hard constraints, data and
permission concerns, integrations, operational context, and reversible
assumptions. Name owners or decision makers when known.

### 4. Define success

For each desired outcome, identify an observable signal, source, time horizon,
and owner. Record missing baselines or targets as unknown rather than creating
numbers.

### 5. Build the initial capability map

List larger, independently understandable capabilities and prioritize only what
is needed for the first coherent useful release. Keep a single capability in the
brief; once several larger capabilities exist, maintain only this minimal index:

```markdown
| ID | Feature | Status | Spec |
|---|---|---|---|
```

Use `Idea`, `Ready`, `In Progress`, and `Done`. Do not introduce a larger status
machine unless the project demonstrates a need for one.

### 6. Obtain a product decision

Present the brief and map for human review. Do not treat a draft, silence, or
agent recommendation as approval. After approval, identify the first capability
that should receive a detailed specification.

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

Choose one handoff state: `READY FOR FEATURE SPECIFICATION`, `PRODUCT DECISION
REQUIRED`, `MORE EVIDENCE REQUIRED`, or `ALREADY INITIALIZED`.

The result is complete only when product facts and assumptions are distinct,
the first-release boundary is coherent, every capability has an observable
outcome, and no unresolved decision is represented as approved.
