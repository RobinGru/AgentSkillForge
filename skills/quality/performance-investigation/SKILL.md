---
name: performance-investigation
description: Investigate a measured latency, responsiveness, throughput, memory, or resource concern. Use when a comparable baseline can be established; test bounded hypotheses with discriminating experiments and retain changes only with proportionate regression protection.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.6.5
---

# Performance investigation

Use the repository's established language and conventions for any artifacts you create or update.
Use the smallest sufficient context and bounded tool output. Reuse inspected
evidence and stop once the task can proceed safely; never trade correctness,
safety, or required verification for brevity.

Treat performance work as measurement-driven investigation, not an optimization
list. Do not change behavior before evidence identifies a plausible bottleneck.

## Activation boundary

Use for a repeatable slow path, monitored regression, breached budget or SLO,
resource exhaustion, planned demand against a limit, or an available trace,
profile, metric, or reproducible workload.

Without a signal, affected journey, or target, define a measurement plan instead.
Do not optimize a suspected asset, query, cache, framework, or structure without
evidence connecting it to the measured concern.

## Workflow

### 1. Define signal and baseline

Record affected operation, impact, users or systems, frequency, onset, signal
source, and reason it matters. Do not infer cause from symptom.

Make measurements comparable: environment, revision, dataset, load, tool,
sampling, primary and side metrics, and limits. Separate lab from field data and
retain enough evidence to repeat the comparison.

### 2. Partition and hypothesize

Divide the path into observable relevant portions such as network, server,
queueing, storage, serialization, cache, client main thread, rendering,
concurrency, or collection. Record unknown portions. Use
[web signals](references/web-signals.md) or
[backend signals](references/backend-signals.md) when applicable.

Keep bounded hypotheses supported by current measurements.

### 3. Run discriminating experiments

Apply [experiment design](references/experiment-design.md): change one material
variable, predict a result that differs if the hypothesis is false, and preserve
comparable conditions. Record expected and actual results. Do not implement a
suspected fix before the experiment distinguishes it from alternatives.

### 4. Decide and guard

Retain, revert, or continue based on observed results. Any retained change needs
comparable before-and-after primary metrics plus relevant side effects. Add a
proportionate regression test, budget, telemetry, alert, load test, or documented
manual check. Local budgets override
[example budgets](references/example-budgets.md).

## Output contract

Report `Signal`, `Baseline`, `Partition`, `Hypotheses`, `Experiments`, `Decision`,
`Before and after`, `Guard`, and `Limits`. Each experiment states hypothesis,
supporting facts, smallest discriminating check, expected and actual result,
decision, and next evidence if inconclusive.

Label claims measured, observed, inferred, or unknown. Never claim improvement
without comparable before-and-after evidence. See
[investigation examples](references/investigation-examples.md) for patterns, not
universal advice.
