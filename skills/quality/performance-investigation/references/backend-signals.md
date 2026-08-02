# Backend performance signals

Map an operation from arrival through completion so latency, capacity, and
resource use are distinguishable.

## Facts to collect

- Operation name, status outcome, request shape, tenant or cohort where safe,
  and time window.
- Latency distribution and throughput under a stated load profile.
- Queue wait, service time, downstream calls, database or storage timing, and
  retry or error rates when available.
- CPU, memory, connection-pool use, garbage collection, saturation, and bounded
  traces or profiles.

Keep request timing separate from background work when they use different
queues, hosts, or resource limits. A higher percentile can come from waiting,
contention, downstream delay, or work duration; measure the relevant segment.

## Question before changing code

Which timing segment changes when load rises, and which small test can separate
queueing from slow service, storage, or a downstream dependency?
