# Example performance budgets

These are examples, not universal requirements. Repository or product budgets
take precedence.

## How to define a local budget

Write a budget as a named journey or operation, population, environment or load,
metric, threshold, measurement method, owner, and response when breached. Tie it
to a user outcome or operating constraint rather than a generic framework rule.

## Example formats

- `Search results, authenticated mobile field cohort: p75 interaction delay
  remains within product target; alert when two consecutive windows exceed it.`
- `Invoice import with stated fixture and worker count: peak resident memory
  stays below allocated worker limit; fail load check when exceeded.`
- `Order lookup under agreed concurrency: p95 operation latency and error rate
  remain within service objective; inspect queue time on alert.`

Validate thresholds with product owners and operating constraints before making
them a gate. Revisit them when workload, devices, or service objectives change.
