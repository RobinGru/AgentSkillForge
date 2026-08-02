# Compatibility envelope

Define which old and new combinations are supported during a migration.

## Producer and consumer matrix

List each producer and consumer contract version. For every pairing, mark it
supported, temporarily supported, unsupported, or unknown, and cite the evidence
behind the classification.

## Version tolerance

Record how each side handles missing, additional, renamed, reordered, or changed
values. Include protocol negotiation, defaulting, feature detection, and failure
behavior only when they are evidenced requirements or implementation facts.

## Mixed deployments

Describe valid behavior when instances, jobs, regions, clients, or services run
different versions. Include ordering constraints and the effect of retries,
queued work, caches, and delayed consumers when relevant.

## Ownership and time bounds

Assign an owner to every consumer group and compatibility exception. Record the
latest supported transition date, observation window, and escalation path. A
calendar date alone does not prove a consumer has migrated.

## Envelope decision

State the invariants that every supported combination must preserve. Any unknown
combination blocks a destructive step unless its impossibility is established or
an accountable owner explicitly resolves the risk.
