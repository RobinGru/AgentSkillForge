---
name: product-interface-engineering
description: Build, change, debug, or review user-facing UI/UX and frontend behavior. Use for pages, forms, dialogs or modals, navigation, validation, recovery, interaction states, accessibility, keyboard, focus, touch, and responsive or mobile layouts; exclude backend-only work and behavior-preserving refactors.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.6.5
---

# Product interface engineering

Use the repository's established language and conventions for any artifacts you create or update.
Use the smallest sufficient context and bounded tool output. Reuse inspected
evidence and stop once the task can proceed safely; never trade correctness,
safety, or required verification for brevity.

Make the user job, interaction contract, states, accessibility, and verification
explicit. Reuse established product patterns before introducing new ones.

## Activation boundary

Use when a user-facing screen, component, flow, decision, data entry, recovery,
accessibility behavior, or responsive interaction changes. Do not use for
backend-only work, behavior-preserving structural refactors, or isolated visual
token corrections without interaction impact.

Choose `local`, `flow`, or `systemic` scope. Increase verification only with scope
or risk.

## Workflow

### 1. Establish user and system facts

Identify actor, goal, supported decision or action, and costly errors. Inspect
nearby components, tokens, content, routes, state patterns, platforms, tests, and
stories. Mark missing product knowledge unknown; do not invent research.

### 2. Define interaction and states

Specify primary action, inputs, outcomes, validation, errors, cancellation,
resumption, permissions, and the result users can safely expect. Include only
relevant initial, pending, empty, partial, populated, invalid, recoverable,
terminal, success, disabled, permission-limited, destructive confirmation, and
offline states. Define recovery for each failure state.

### 3. Implement

Use semantic elements and established primitives. Keep component APIs minimal.
Support keyboard, touch, assistive technology, responsive text and layout, and
localization. Do not invent production content or measurements.

### 4. Verify

Use the [verification matrix](references/verification-matrix.md). Load the
[accessibility baseline](references/accessibility-baseline.md) and
[visual decision guidance](references/visual-system-decisions.md) when relevant.

## Output contract

Report `Scope`, `User job`, `System facts`, `Interaction contract`, `State model`,
`Implementation`, `Checks`, and `Remaining risks`. Mark each check `Passed`,
`Failed`, `Not run`, or `Not applicable`. State unverified assumptions and any
accessibility conflict with the closest usable alternative.
