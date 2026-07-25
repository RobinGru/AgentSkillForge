---
name: product-interface-engineering
description: Engineer user-facing interface changes around a concrete user job, existing product patterns, complete interaction states, and proportionate verification. Use for UI flows, components, accessibility, or responsive behavior.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.4.0
---

# Product interface engineering

Build or review interfaces by making user task, interaction behavior, states,
and verification explicit. Reuse product conventions before introducing a new
visual pattern.

## Use this skill when

- A screen, component, flow, accessibility behavior, or responsive interaction changes.
- Users must make a decision, enter data, recover from failure, or complete an action.

## Do not use this skill when

- Work is backend-only or has no user-facing effect.
- A structural component refactor preserves interaction and visual behavior.
- An exact token or alignment correction has no behavior impact; use local scope only.

## Scope

Choose `local` for isolated adjustment, `flow` for bounded journey, or
`systemic` for reusable or cross-screen change. Increase verification depth only
when scope or risk requires it.

## Workflow

### 1. User job

Identify actor, concrete goal, decision or action supported, and costly errors.
Mark missing product knowledge as unknown; do not fabricate research.

### 2. Existing system

Inspect nearby components, tokens, content conventions, routes, state patterns,
supported platforms, tests, and stories. Retain established patterns when they
serve job.

### 3. Interaction contract

Specify primary action, inputs, outcomes, errors, cancellation, resumption, and
permission-limited behavior. State result users can safely expect.

### 4. State model

List relevant states: initial, pending, empty, partial, populated, invalid,
recoverable or terminal failure, success, disabled, permission-limited,
destructive confirmation, and offline when applicable. Define recovery for each
state that can fail.

### 5. Implementation

Use semantic elements and existing primitives. Keep component APIs minimal.
Support keyboard, touch, and assistive technology; account for responsive text,
layout, and localization. Do not invent production content or measurements.

### 6. Verification

Use [verification matrix](references/verification-matrix.md) to report checks.
Load [accessibility baseline](references/accessibility-baseline.md) and
[visual decision guidance](references/visual-system-decisions.md) when needed.

## Output contract

Report `Scope`, `User job`, `System facts`, `Interaction contract`, `State
model`, `Implementation`, `Checks`, and `Remaining risks`. Each check uses
Passed, Failed, Not run, or Not applicable. State unverified assumptions and
accessibility conflicts with closest usable alternative.
