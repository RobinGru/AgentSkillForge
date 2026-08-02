# Data transition checks

Use these checks when migration states move or reinterpret persisted data.

## Idempotency and resumption

Define stable work identity and the result of repeating a unit. Record checkpoints,
restart behavior, partial-write handling, and how concurrent live writes interact
with resumed work.

## Reconciliation

Specify counts, checksums, sampled comparisons, invariant queries, or domain-level
balances that can reveal omissions and divergence. Define tolerance, ownership,
and the action taken when reconciliation fails.

## Batch and load boundaries

Set bounded units, pacing, concurrency, stop signals, and operational windows.
Treat measured performance diagnosis as separate `performance-investigation`
work; carry its validated limits back into the migration plan.

## Conflicts and unrepresentable data

Define authority when old and new writes disagree. Quarantine or explicitly map
values the target cannot represent; do not silently discard them.

## Completion evidence

Require proof that the full intended population was considered, failed units were
resolved, live writes are covered, consumers use the target representation, and
the old path remains unused for the agreed observation window.

## Rollback distinction

Record code rollback and data rollback separately. A binary or deployment may be
reversible while transformed, deleted, or newly accepted data requires forward
repair or cannot be restored.
