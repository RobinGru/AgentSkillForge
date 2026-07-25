---
name: performance-investigation
description: Investigate a measured performance concern with a comparable baseline, bounded hypotheses, discriminating experiments, and proportionate regression protection. Use for observed latency, responsiveness, throughput, memory, or resource problems.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.2.0-beta.1
---

# Performance investigation

Treat performance work as an investigation, not a list of optimizations. Change
behavior only after measurements identify a plausible bottleneck and an experiment
can distinguish it from competing explanations.

## Use this skill when

- A user reports a repeatable slow path, monitoring detects a regression, or a
  service-level objective or agreed budget is breached.
- A planned load change, resource limit, or measured responsiveness issue needs
  a risk assessment.
- A profiling artifact, trace, metric, or reproducible workload can guide an
  investigation.

## Do not use this skill when

- Someone requests that code be faster but supplies no signal, affected journey,
  or target. Request those details and prepare a measurement plan instead.
- An asset, query, cache, or framework change is proposed without a measurement showing that
  it affects a measured problem.
- A structural refactor is the primary task. Use this skill only if measurement
  establishes a performance cause that the refactor must address.

## Workflow

### 1. Signal

Record the observed issue and its impact: affected journey or operation, users
or systems affected, frequency, onset, and reason it matters. Classify the signal
as user report, alert, regression, budget breach, reproducible slow journey,
resource exhaustion, or planned demand. Do not infer a cause from the symptom.

### 2. Baseline

Make measurements comparable. Record environment, build or revision, dataset,
load shape, tool, sampling method and count, primary metric, side metrics, and
known limits. State whether each result is lab data, field data, or both; do not
combine them as though they had identical conditions. Preserve enough raw output
or an accessible summary for another investigator to repeat the comparison.

### 3. Partition

Divide the affected path into observable portions before proposing a fix. Check
only portions relevant to the signal, such as network transfer, server time,
queueing, database or storage, serialization, cache behavior, client main
thread, rendering, assets, concurrency, or memory collection. Record unknown
portions explicitly.

Use [web signals](references/web-signals.md) or [backend signals](references/backend-signals.md)
when their scope matches the path.

### 4. Experiment

For each live hypothesis, use [experiment design](references/experiment-design.md).
Change one material variable, choose the smallest test that would produce a
different result if the hypothesis were false, and keep comparable conditions.
Do not rewrite a suspected N+1 query, render path, or cache layer before a
measurement can distinguish it from alternatives.

### 5. Decide and guard

Retain, revert, or continue investigating based on observed results, not
expectation. Any retained performance change needs before-and-after measurements
for the primary metric plus relevant side effects. Choose proportionate
protection: regression test, repository budget, telemetry, alert, load test, or
documented manual check. [Example budgets](references/example-budgets.md) help
format local targets; product and repository budgets take precedence.

## Output contract

Report `Signal`, `Baseline`, `Partition`, `Hypotheses`, `Experiments`,
`Decision`, `Before and after`, `Guard`, and `Limits`. For every experiment
include:

- hypothesis and its supporting facts;
- smallest discriminating experiment;
- expected and actual result;
- decision and next information needed, if inconclusive.

Label claims as measured, observed, inferred, or unknown. State measurement
limitations and unverified assumptions. Do not claim improvement without a
comparable before-and-after result.

## Investigation examples

See [investigation examples](references/investigation-examples.md) for small
API queueing, Vue input lag, and batch memory-spike investigations. They model
questions and experiments, not universal implementation advice.
