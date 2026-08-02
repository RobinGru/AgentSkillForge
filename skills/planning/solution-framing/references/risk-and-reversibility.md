# Risk and reversibility guide

## Classify unknowns

Treat an unknown as a blocker when it affects safety, legal obligations, data
integrity, a public contract, an irreversible migration, or the feasibility of
the selected direction. Otherwise record it as a reversible assumption with a
specific validation step.

## Compare reversibility

When comparing options, consider:

- cost and time to undo the change;
- data conversion or compatibility commitments;
- blast radius across owners and systems;
- observability needed to detect failure;
- ability to deliver in a small, independently verifiable slice.

An option is not automatically preferred because it is reversible. It must
also satisfy the stated problem and hard constraints.
