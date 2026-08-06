---
name: vue-sfc-decomposition
description: Refactor a Vue or Nuxt single-file component by selecting one evidence-based responsibility seam, preserving public, reactive, lifecycle, SSR, and cleanup behavior, and verifying the bounded extraction. Use only for an observed decomposition problem.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.6.4
---

# Vue SFC decomposition

Use the repository's established language and conventions for any artifacts you create or update.
Use the smallest sufficient context and bounded tool output. Reuse inspected
evidence and stop once the task can proceed safely; never trade correctness,
safety, or required verification for brevity.

Decompose only to solve an observed responsibility, maintenance, reuse, or
testability problem. Component length alone is not evidence.

## Activation boundary

Use when a Vue SFC mixes separable visual, reactive, I/O, domain, state, or
browser responsibilities and that mix causes a concrete problem. Do not use for
UI behavior changes or speculative performance refactors.

## Workflow

### 1. Characterize and protect

Record Vue/Nuxt versions, API style, TypeScript, props, emits, slots, exposed
values, router, store, queries, watchers, lifecycle, DOM dependencies, SSR, and
tests. Read nearby conventions.

Define behavior to preserve: output, events, requests, states, side-effect order,
reactivity, watcher timing, lifecycle, cleanup, routes, SSR, and hydration. Add a
characterization check before extraction when practical coverage is absent.

### 2. Choose one seam

Select the smallest fact-supported boundary:

- self-contained visual region → child component;
- reusable reactive behavior → composable;
- transport mapping → existing query, service, or repository layer;
- shared state → existing store;
- pure calculation → TypeScript module;
- domain rule → domain module;
- local UI state → keep local;
- browser integration → focused composable with cleanup.

Do not centralize by default. Use
[Nuxt boundaries](references/nuxt-boundaries.md) for runtime-sensitive scope.

### 3. Extract and verify

Make one seam per patch. Preserve public APIs unless explicitly changed. Retain
ref, computed, readonly, watcher, lifecycle, error, and cleanup semantics; avoid
destructuring that breaks reactivity. Do not combine redesign or domain changes.

Run targeted tests and type checks. Verify output, events, request counts,
watchers, lifecycle, cleanup, and SSR/hydration when applicable. Record unrun
checks and risk.

### 4. Continue deliberately

After a verified extraction, choose another seam only if the observed problem
remains and no decision, evidence, or approval blocker exists. Never extract
solely to reduce line count.

## Output contract

Report `Characterization`, `Protected behavior`, `Selected seam`, `Patch`,
`Facts`, `Remaining risks`, and `Next seam`. Explain why the responsibility
belongs at the selected boundary and why relevant alternatives were rejected.
