# Investigation examples

These examples demonstrate collecting facts. They are not prescribed fixes.

## API latency with queueing

**Signal:** p95 export-start latency rises during a scheduled partner upload.

**Partition:** Separate queue wait, worker service time, database reads, and
partner calls for the same export type.

**Discriminating experiment:** Replay a representative upload in an isolated
environment with current worker count, then with one additional worker while
holding request rate and dataset fixed. If queue wait falls while service time
stays stable, capacity contention is supported; otherwise inspect service and
downstream segments.

## Vue interaction with a long main-thread task

**Signal:** Field data reports an interaction-delay regression after a filter
release on lower-powered devices.

**Partition:** Compare input event timing, synchronous handler work, reactive
updates, rendering, and network activity in a trace of the filter journey.

**Discriminating experiment:** In a controlled build, replace only the suspected
synchronous formatting step with a no-op for the same input sequence. A reduced
long task and response delay supports that step as a contributor; unchanged
traces point to another segment.

## Batch process with a memory spike

**Signal:** Nightly reconciliation workers restart after memory rises beyond
container allocation on the largest customer dataset.

**Partition:** Measure retained heap, allocation rate, batch size, queued items,
and storage-read duration across batch boundaries.

**Discriminating experiment:** Run the same fixture with half the batch size,
without changing concurrency or input ordering. A proportional peak-memory drop
supports batch residency as a cause; a flat peak suggests retained references or
another allocation source need profiling.
