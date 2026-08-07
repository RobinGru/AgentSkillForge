---
name: adversarial-deep-review
description: Adversarially assess a concrete high-risk code change. Use only when deep review is explicitly requested or proportionate; test evidence-backed failure, abuse, compatibility, recovery, concurrency, and operational scenarios without implementing or deciding merge readiness.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.6.4
---

# Adversarial deep review

Use the repository's established language and conventions for any artifacts you create or update.
Use the smallest sufficient context and bounded tool output. Reuse inspected
evidence and stop once the task can proceed safely; never trade correctness,
safety, or required verification for brevity.

Challenge assumptions that make a concrete high-risk change safe. Produce risk
evidence for later ordinary review; do not edit code or make the merge decision.

## Activation boundary

Use only when a patch, PR, diff, or changed-file set exists and deep adversarial
assessment is explicitly requested or proportionate to hard-to-reverse material
risk such as authority, money, durable data, secrets, public contracts,
migrations, retries, concurrency, or irreversible external effects.

Use `fact-based-code-review` for routine review, `security-boundary-analysis` for
a system threat model without a diff, `failure-investigation` for an unexplained
observed failure, and `safe-code-change` for implementation. Large or unfamiliar
code alone is not a trigger.

## Rules

- A scenario is a test question, not a finding.
- Challenge behavior and assumptions, never people.
- Inspect only changed code and surrounding paths needed for relevant invariants.
- Label material claims `Observed`, `Reproduced`, `Required`, `Inferred`, or
  `Unverified`.
- Missing reproduction is not proof of safety.
- Do not run destructive, live, or unauthorized probes.

## Workflow

### 1. Establish risk basis

Record change, intent, affected users or systems, assets, side effects,
reversibility, available checks, and missing context. Route to ordinary review if
no concrete material risk remains.

### 2. Identify invariants

State relevant authorization, integrity, ordering, idempotency, durability,
compatibility, retry, timeout, cancellation, concurrency, rollback, compensation,
repair, audit, and containment obligations. Link each to evidence and its
protecting assumption or control.

### 3. Select and test scenarios

Prioritize 3–7 plausible scenarios by impact, irreversibility, propagation,
detectability, and control strength. Consider partial success, hostile input,
confused authority, version interaction, duplication, corruption, races, stale
state, rollout, observability, and recovery only when relevant.

Inspect the smallest evidence set and run only safe discriminating checks. Assign
one outcome: `SUPPORTED`, `REFUTED`, `UNRESOLVED`, or `BLOCKED`. An unrun check
cannot support or refute a scenario.

### 4. Retain concerns and recovery limits

Retain supported defects or risks and unresolved information that blocks a
responsible assessment. Classify type as `Defect`, `Risk`, `Missing information`,
or `Maintainability concern`; severity as `Blocker`, `Major`, `Moderate`, or
`Minor`; confidence as `High`, `Medium`, or `Low`. Preferences and generic advice
cannot block.

For each material concern, state blast radius, propagation, detection, safe stop,
rollback limits, compensation or repair, and recovery evidence.

### 5. Hand off

Choose one state:

- `NO MATERIAL ADVERSARIAL FINDINGS`
- `RESIDUAL RISK ACCEPTANCE REQUIRED`
- `MITIGATION REQUIRED`
- `MORE EVIDENCE REQUIRED`
- `ROUTE TO SECURITY BOUNDARY ANALYSIS`
- `ROUTE TO FAILURE INVESTIGATION`

Pass evidence to `fact-based-code-review` for the sole integration decision.
`feature-lifecycle` may link evidence for a tracked feature.

## Output contract

Use these exact headings in this order:

```markdown
## Review scope
## Risk basis
## Intent and critical invariants
## Assumptions under attack
## Scenario register
## Verification record
## Adversarial findings
## Checks not run
## Blast radius and recovery
## Residual uncertainty
## Handoff state
```

Each scenario includes lens, preconditions, trigger, stressed invariant, failure
mechanism, affected path, evidence needed, plausibility, outcome, and verification.
Each retained finding includes severity, type, location, supporting details,
affected behavior, impact, confidence, mitigation, and verification. Stop before
implementation or merge decision.
