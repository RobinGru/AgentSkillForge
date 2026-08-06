---
name: safe-code-change
description: Make one bounded, understood code change and prove its intended behavior. Use when the change boundary is known; run the narrowest direct proof before editing, repeat it on the final worktree, and report remaining uncertainty.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.6.4
---

# Safe code change

Use the repository's established language and conventions for any artifacts you create or update.

Implement one understood change without expanding into redesign or broad cleanup.

## Activation boundary

Use this for a reproducible local defect, deliberate bounded behavior change,
behavior-preserving refactor, proven investigation handoff, or one independently
safe migration step.

Route unknown cause or boundary to `failure-investigation`, unresolved product or
architecture to the relevant planning skill, multi-state coexistence to
`compatibility-migration`, and review-only or performance diagnosis elsewhere.

Within a tracked feature, `feature-lifecycle` stores feature-level evidence; this
skill remains authoritative for the patch and direct proof.

## Core rule

Run the narrowest direct proof before editing and repeat the same path against the
final worktree. A broad suite does not replace missing direct proof.

## Workflow

### 1. Bound the change

Inspect only affected implementation, nearest tests, relevant callers and
contracts, established local patterns, repository instructions, status, and diff.
Record internally:

- current and intended observable behavior;
- behavior that must remain unchanged;
- interfaces, data, permissions, callers, and side effects at risk;
- direct success signal and non-goals.

Stop or reroute when product intent, cause, or safe boundary remains unresolved.

### 2. Establish baseline proof

Run the smallest test, command, request, browser scenario, fixture, or comparison
that distinguishes current behavior from success. Record invocation, expected and
observed result, environment, and whether the signal is direct.

For a fix, demonstrate the defect when possible. For a refactor, demonstrate the
behavior to preserve. If no adequate proof exists, state the exact limitation.

### 3. Apply the patch

Make the smallest coherent change. Preserve unrelated behavior, public contracts,
error paths, repository conventions, tests, and existing user work. Exclude
speculative abstractions, unrelated cleanup, broad renaming, and formatting churn.
Reassess if the boundary expands materially.

### 4. Repeat proof and checks

Repeat the direct proof on the final worktree. If it changes, explain why the
replacement still distinguishes the original state. Then run only proportionate
checks: nearest tests, affected integration, static analysis, lint, build, and
broader suites only when risk justifies them. Results become stale after later
edits.

### 5. Inspect and report

Confirm every changed line supports the contract, tests were not weakened,
temporary diagnostics are gone, generated changes are justified, and no unrelated
work was overwritten. Report only paths, decisive evidence, checks, and risk.

## Output contract

Use at most 6 lines and 100 words:

```markdown
Change: `<path>` — concise effect
Proof: `<command>` — before: …; after: …
Checks: `<command>` ✓
Risk: …
Result: PROVED | PARTIALLY PROVED | NOT PROVED
```

`Change`, `Proof`, and `Result` are required. Omit `Checks` or `Risk` when absent.
Use one line per field. Never claim an unrun check or unsupported success.
