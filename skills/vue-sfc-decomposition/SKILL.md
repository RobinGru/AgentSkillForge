---
name: vue-sfc-decomposition
description: Refactor a Vue single-file component by characterizing behavior, selecting one fact-based responsibility seam, preserving reactive and lifecycle semantics, and verifying the bounded extraction. Use for an observed Vue or Nuxt component decomposition problem.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.2.0-beta.1
---

# Vue SFC decomposition

Decompose a Vue component only to solve an observed responsibility, maintenance,
or testability problem. Choose the extraction boundary from behavior and
ownership, not component length alone.

## Use this skill when

- A Vue single-file component mixes separable visual, reactive, I/O, domain, or
  browser-integration responsibilities and that mix causes a concrete problem.
- A bounded refactor must preserve component behavior while making one concern
  independently testable or reusable.

## Do not use this skill when

- A component is merely long but has no observed change, ownership, or
  testability problem.
- Work changes user interaction or visual behavior rather than preserving it.
  Use an interface-engineering workflow for that scope.
- A measured performance investigation has not established a structural Vue
  cause. Investigate the performance signal before extracting code.

## Workflow

### 1. Characterize

Record Vue and Nuxt versions, Composition or Options API, TypeScript use, public
props, emits, slots, exposed values, router, store, data-query use, watchers,
lifecycle hooks, browser or DOM dependencies, and available test coverage. Read
nearby conventions before selecting a new location.

### 2. Protect

List behavior that must not change: rendered output, events, network calls,
loading and failure states, side-effect order, unmount cleanup, route or URL
behavior, and SSR or hydration when relevant. If practical coverage is absent,
add a characterization test or reproducible manual check before the extraction.

### 3. Choose one seam

Choose the smallest responsibility boundary supported by facts:

| Observed responsibility | Preferred boundary |
| --- | --- |
| Self-contained visual region | Child component |
| Reusable reactive behavior | Composable |
| Remote I/O or transport mapping | Existing query, service, or repository layer |
| Shared application state | Existing store |
| Pure calculation or formatting | Plain TypeScript module |
| Domain rule | Domain module |
| Local open or closed UI state | Keep in component |
| Browser or DOM integration | Focused composable with cleanup |

Do not create a central composable by default. Use
[Nuxt boundaries](references/nuxt-boundaries.md) when Nuxt runtime behavior is
in scope.

### 4. Extract

Make one seam per patch. Retain public APIs unless the task explicitly changes
them. Preserve ref, computed, and readonly semantics; avoid destructuring that
breaks reactivity. Retain watcher flush and immediate behavior, lifecycle order,
cleanup, and error handling. Do not combine UI redesign or domain-rule changes
with the extraction.

### 5. Observe

Run targeted tests and type checks where available. Check rendered output,
events, API-call count, watcher and lifecycle behavior, and cleanup. Check SSR
and hydration if the component participates in server rendering. Record checks
not run and why.

### 6. Continue deliberately

After a verified extraction, select the next seam from the remaining observed
problem. Stop only when an architectural decision, missing information, or user
approval is needed; do not stop merely because one seam was extracted.

## Output contract

Report `Characterization`, `Protected behavior`, `Selected seam`, `Patch`,
`Facts`, `Remaining risks`, and `Next seam`. State unknown framework or
runtime facts. For each selected seam, explain why the responsibility belongs
there and why alternatives were not chosen.
