# Risk reasoning

Prioritize abuse chains with explicit reasoning rather than unsupported scores.

## Likelihood

Describe the access, knowledge, timing, user interaction, and environmental
conditions an attacker needs. Use qualitative terms only after stating those
conditions. Reduce likelihood when an evidenced control blocks a required step.

## Impact

Name the affected value and concrete consequence: exposure, unauthorized change,
loss of service, fraudulent action, lost auditability, persistent access, or
unsafe recovery. Bound scope by tenants, records, systems, duration, and
recoverability where evidence permits.

## Existing controls

Count a control only when its location and behavior are evidenced. State which
step it prevents, detects, limits, or helps recover from, and identify its
verification signal. Planned controls do not reduce current risk.

## Ranking changes

Record observations that would materially raise or lower priority, such as public
exposure, stronger identity proof, narrower permissions, rate limits, immutable
artifacts, monitoring coverage, or reliable recovery.

## Missing deployment information

Do not invent network placement, identity providers, secret handling, tenancy, or
operator practice. Mark the affected likelihood or impact as uncertain and ask
for the smallest fact needed to refine it. Escalate only when the plausible
high-impact path is credible under the known scope.
