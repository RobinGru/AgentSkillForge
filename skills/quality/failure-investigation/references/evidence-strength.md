# Evidence strength

Use these labels consistently in a failure investigation:

- `Observed`: directly visible in a preserved artifact, output, or inspected state.
- `Reproduced`: observed again under recorded, repeatable conditions.
- `Provided`: reported by the user or another source but not independently checked.
- `Inferred`: a reasoned interpretation that fits current evidence.
- `Unknown`: material information is absent or cannot be verified.

## Conflicting evidence

Keep contradictory observations visible. Check whether they differ by revision,
environment, input, timing, or collection method before ranking either one. Do
not silently average incompatible evidence or select the result that favors a
preferred explanation.

## Discriminating checks

A useful check predicts materially different results for at least two live
explanations. Record its setup, changed variable, expected result per explanation,
possible side effects, and stopping condition. Prefer reversible checks with the
smallest relevant scope.

## Checks not run

Describe an unexecuted check as proposed, not passed. State why it was not run,
what access or condition is missing, and which uncertainty remains. A plausible
expected result is still an inference until observed.
