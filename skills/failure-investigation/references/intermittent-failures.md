# Intermittent failure checks

Use these categories to form checks, not as a presumption of cause.

## Timing and concurrency

Vary scheduling pressure, concurrency, timeouts, clocks, and synchronization one
factor at a time. Look for races, stale reads, and assumptions about completion.

## Order dependence

Compare isolated execution with different preceding operations. Track setup,
teardown, caches, globals, and process lifetime.

## Shared state

Inspect mutable fixtures, files, databases, queues, ports, environment variables,
and reused workers. Verify ownership and cleanup rather than assuming isolation.

## Random inputs

Capture seeds and generated values. Reduce a failing input while retaining the
failure, and distinguish input sensitivity from timing sensitivity.

## Environment and version drift

Compare runtime, dependency, operating-system, locale, timezone, feature flag,
configuration, and build artifact versions using recorded values.

## External services

Record request identity, retry behavior, remote responses, quotas, and service
state. Do not replay destructive calls without authorization.

## Resource limits

Check exhaustion only as a functional failure condition. If the primary concern
is measured consumption or performance, hand off to `performance-investigation`.
