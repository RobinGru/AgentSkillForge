# Web performance signals

Use browser measurements to describe an observed user journey, not to assign
blame to one subsystem.

## Evidence to collect

- Route, action, device class, connection conditions, and release identifier.
- Field telemetry when available: distribution, sample count, affected cohort,
  and time window.
- Lab trace for a reproducible path: CPU and network settings, cache state,
  device profile, and run count.
- Main-thread tasks, network timings, rendering work, and assets relevant to
  the reported delay.

Field data describes what users experienced. Lab data helps repeat and isolate
a path. Compare like with like; a synthetic desktop trace cannot prove a mobile
field improvement.

## Useful measures

For responsiveness, correlate an input with its handler, queued work, rendering,
and visible update. For loading, separate server response, transfer, parsing,
and rendering. When reporting Core Web Vitals, preserve their documented meaning
and cite the [official Web Vitals guidance](https://web.dev/articles/vitals).

Do not treat one score, trace, or isolated run as a universal diagnosis. Do not
use Time to Interactive as a current target metric.

## Question before changing code

What trace difference would show that main-thread work, transfer size, server
latency, or rendering is dominant for this journey? Collect that evidence before
choosing an optimization.
