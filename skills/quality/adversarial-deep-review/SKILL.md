---
name: adversarial-deep-review
description: Challenge an explicitly requested, concrete high-risk code change with evidence-based failure, abuse, compatibility, recovery, concurrency, and operational scenarios. Use before the final normal review for an explicit deep adversarial assessment; do not use for routine review, implementation, a system threat model without a diff, or diagnosis of an observed failure.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.6.4
---

# Adversarial deep review

Use the repository's established language and conventions for any artifacts you create or update.


Assess a concrete high-risk change by systematically challenging the assumptions
that make it safe. Retain only findings and uncertainty that repository evidence
supports.

This skill produces risk evidence for a later ordinary review. It does not edit
code, make a merge decision, or claim that a change is universally safe.

## Activation boundary

Use this skill only when both conditions hold:

- a concrete patch, pull request, diff, or changed-file set is available; and
- an adversarial or deep assessment is explicitly requested, or the change has a
  material consequence that is difficult to prevent, detect, or reverse.

Material consequences can include authorization changes, money movement, durable
or regulated data, secrets, public contracts, migrations, retries, concurrency,
or irreversible external effects.

Use another skill when:

- a routine correctness and integration review is needed: `fact-based-code-review`;
- no concrete change exists and the concern is system-wide trust or abuse:
  `security-boundary-analysis`;
- an observed behavior has an unknown cause: `failure-investigation`;
- a measured resource or responsiveness issue needs diagnosis:
  `performance-investigation`;
- an approved compatibility transition needs sequencing: `compatibility-migration`;
- an understood correction must be implemented: `safe-code-change`.

Do not activate solely because code is large, unfamiliar, or security-related.

## Core rules

1. A scenario is a question to test, not a finding.
2. Challenge the behavior and its assumptions, never the people who wrote it.
3. Stay within the supplied change and only inspect surrounding code needed to
   establish an invariant, caller, side effect, control, or recovery path.
4. Mark material statements as `Observed`, `Reproduced`, `Required`, `Inferred`,
   or `Unverified`.
5. Do not treat a missing reproduction as proof of safety.
6. Do not run destructive, live, or unauthorized probes. Record their evidence
   gap and propose a safe alternative.

## Workflow

### 1. Establish scope and risk basis

Record the supplied change, stated intent, affected users or systems, critical
assets, side effects, reversibility, available checks, and missing context.

State why an adversarial assessment is proportionate. Route to ordinary review
when no concrete material risk basis remains.

### 2. Identify invariants and assumptions

Name behavior that must stay true, such as:

- authorization and trust transitions;
- data integrity, uniqueness, ordering, idempotency, and durability;
- interface compatibility and independently deployed callers;
- retry, timeout, cancellation, and partial-completion behavior;
- concurrency, time, stale state, and delivery ordering;
- rollback, compensation, repair, auditability, and containment.

For each material invariant, state the evidence that establishes it and the
assumption or control that protects it.

### 3. Select relevant scenarios

Choose only lenses relevant to the change:

- interruption, retry, partial success, and recovery;
- hostile input, confused authority, and privilege misuse;
- caller, schema, dependency, and version interactions;
- duplication, loss, corruption, stale state, and impossible state;
- races, reordering, expiry, and delayed delivery;
- observability, rollout, containment, and repair load.

Prioritize three to seven plausible scenarios by impact, irreversibility,
propagation, detectability, and strength of existing controls. Avoid invented
numeric scores.

### 4. Test each scenario against evidence

For each selected scenario, inspect the smallest relevant set of changed code,
callers, tests, configuration, persistence paths, and recovery mechanisms.

Run a targeted check only when it is safe, authorized, and can distinguish the
scenario. Assign exactly one outcome:

- `SUPPORTED`
- `REFUTED`
- `UNRESOLVED`
- `BLOCKED`

A check that was not run cannot support or refute a scenario. Refuted scenarios
remain in the record but do not become findings.

### 5. Retain material concerns

Retain only supported defects or risks, plus unresolved information that blocks a
responsible assessment. Classify each as `Defect`, `Risk`, `Missing information`,
or `Maintainability concern`; use `Blocker`, `Major`, `Moderate`, or `Minor`
severity and `High`, `Medium`, or `Low` confidence.

Do not promote a preference, generic advice, or an unverified scenario into a
blocking finding.

### 6. Assess recovery and handoff

For every material concern, identify affected users, data, services, or external
systems; propagation and detection paths; safe-stop behavior; rollback limits;
compensation or repair needs; and evidence that recovery works.

Choose one handoff state:

- `NO MATERIAL ADVERSARIAL FINDINGS`
- `RESIDUAL RISK ACCEPTANCE REQUIRED`
- `MITIGATION REQUIRED`
- `MORE EVIDENCE REQUIRED`
- `ROUTE TO SECURITY BOUNDARY ANALYSIS`
- `ROUTE TO FAILURE INVESTIGATION`

Pass the scenario record and retained findings to `fact-based-code-review` for
the sole final integration decision. For a tracked feature, `feature-lifecycle`
may link this evidence and record a resulting blocker or verification gap. Keep
analysis, implementation, lifecycle state, and merge decisions separate.

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

For every prioritized scenario, include:

```markdown
### Scenario title
- Lens:
- Preconditions:
- Trigger:
- Invariant under stress:
- Failure mechanism:
- Affected path:
- Evidence needed:
- Initial plausibility: High | Medium | Low
- Outcome: SUPPORTED | REFUTED | UNRESOLVED | BLOCKED
- Verification:
```

For every retained finding, include:

```markdown
### [Severity] Title
- Type:
- Location:
- Supporting details:
- Affected behavior:
- Impact:
- Confidence:
- Recommended mitigation:
- Verification:
```

The review is complete when the risk basis, scenarios, evidence, findings,
recovery limits, unrun checks, and one handoff state are explicit. Stop before
implementing or deciding whether to merge.
