---
name: failure-investigation
description: Diagnose an unexpected non-performance failure. Use when its cause or safe change boundary is unknown; establish a discriminating signal, test competing explanations, and hand off a supported cause or explicit evidence gap without implementing the fix.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.6.4
---

# Failure investigation

Use the repository's established language and conventions for any artifacts you create or update.
Use the smallest sufficient context and bounded tool output. Reuse inspected
evidence and stop once the task can proceed safely; never trade correctness,
safety, or required verification for brevity.

Establish why a non-performance failure occurs and where a later change is safe.
Diagnose only; do not implement the fix.

## Activation boundary

Use for unexpected test, build, runtime, integration, or data failures whose
mechanism or safe boundary is uncertain, including intermittent, order-dependent,
environment-specific, stateful, and concurrency-dependent failures.

Route measured latency, throughput, memory, or resource concerns to
`performance-investigation`; known local causes to `safe-code-change`; concrete
diffs to `fact-based-code-review`; open product or architecture to planning.

## Core rule

Establish a repeatable signal that detects the reported failure before elaborating
a causal theory. If no adequate signal is possible, name the missing evidence,
access, artifact, or environment and stop escalation.

## Workflow

### 1. Define and reproduce

Record actual versus expected behavior, impact, environment, revision, onset,
frequency, closest working comparison, and prior interventions. Label material
claims `Observed`, `Reproduced`, `Provided`, `Inferred`, or `Unknown`.

Build the smallest direct or justified proxy loop that distinguishes failure from
success. Record invocation, exact symptom, result, repeatability, duration,
environment, and whether it runs unattended. For intermittent failures, use
controlled repetitions and change one relevant variable at a time. Consult
[intermittent failures](references/intermittent-failures.md) when needed.

### 2. Reduce and locate

Reduce inputs, setup, state, dependencies, and steps while rerunning the loop.
Compare the failing and closest working cases. Find the earliest divergent state
and distinguish symptom location, first invalid state, and where its responsible
condition was introduced.

### 3. Test competing explanations

Keep multiple explanations consistent with evidence. For each, state support,
contradictions, a falsifiable prediction, and the smallest discriminating check.
Run safe checks; remove explanations contradicted by executed evidence. Use
[evidence strength](references/evidence-strength.md) to calibrate claims.

### 4. State cause and handoff

A supported cause connects mechanism, causal boundary, and demonstrated failure
signal, and explains the working comparison. Otherwise report a partial cause or
the exact missing link.

Define behavior to change and preserve, narrowest safe boundary, regression guard,
and contracts at risk. Hand supported work to `safe-code-change`.

Choose one state:

- `SUPPORTED CAUSE`
- `PARTIAL CAUSE`
- `MORE EVIDENCE REQUIRED`
- `ENVIRONMENT ACCESS REQUIRED`
- `ROUTE TO PERFORMANCE INVESTIGATION`
- `ROUTE TO SOLUTION FRAMING`

## Output contract

Use these exact headings:

```markdown
## Failure signal
## Diagnostic loop
## Evidence inventory
## Reproduction and reduction
## Causal boundary
## Competing explanations
## Discriminating checks
## Supported cause
## Unresolved conditions
## Recommended guard
## Safe change boundary
## Handoff state
```

`Diagnostic loop` includes invocation, exact symptom, direct or proxy signal,
current result, repeatability, duration, environment, and agent-runnability. Each
explanation includes support, contradictions, prediction, check, execution state,
and result. Match cause strength to evidence and stop before implementation.
