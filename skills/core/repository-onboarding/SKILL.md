---
name: repository-onboarding
description: Establish an evidence-based technical map of an unfamiliar, inherited, or stale repository before substantial work. Use when repository instructions, structure, build and run paths, verification commands, system boundaries, interfaces, or documentation reliability are unclear; do not use to define product purpose or choose architecture.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.6.4
---

# Repository onboarding

Use the repository's established language and conventions for any artifacts you create or update.

Build a compact technical working map from current repository evidence. The map
must help a later task start safely without turning repository onboarding into an
exhaustive architecture exercise, implementation plan, or generated encyclopedia.

## Activation boundary

Use this skill when:

- entering an unfamiliar, inherited, or materially changed repository;
- repository instructions are absent, contradictory, or likely stale;
- the correct build, run, test, lint, type, or packaging paths are unclear;
- module boundaries, entry points, public interfaces, data stores, or side
  effects must be located before work can be bounded;
- a repository needs evidence for a concise agent or developer onboarding guide.

Route elsewhere when:

- users, outcomes, product scope, or repository purpose are unresolved:
  `project-discovery`;
- one capability needs observable rules and acceptance criteria:
  `feature-specification`;
- a consequential technical direction is still open: `solution-framing`;
- a concrete failure has an unknown cause: `failure-investigation`;
- a small understood change is ready: `safe-code-change`;
- verified knowledge is ready to be persisted:
  `repository-knowledge-curation`.

Do not modify production code, select architecture, or claim that discovered
commands work merely because they appear in documentation or configuration.

## Core rules

- Read applicable repository instructions before interpreting other files.
- Prefer current, local, inspectable evidence over generic ecosystem knowledge.
- Distinguish observed, executed, provided, inferred, stale, and unknown claims.
- Use targeted inspection before broad traversal; stop when the working map is
  sufficient for the stated task.
- Treat documentation, source, tests, automation, and history as evidence that
  may disagree, not as automatically consistent truth.
- Do not run destructive, deployment, release, migration, credential-dependent,
  or externally mutating commands merely to learn the repository.
- Do not expose secrets, personal data, credentials, or unnecessary local paths.
- Keep permanent instructions minimal. Recommend detailed knowledge for
  on-demand documentation rather than expanding a root instruction file.

Consult [repository evidence](references/repository-evidence.md) when evidence
conflicts, command safety is uncertain, or the repository is large.

## Workflow

### 1. Establish scope and instruction precedence

Identify the repository root, current revision when available, worktree state,
applicable instruction files, requested onboarding depth, and the concrete work
this map should enable.

Record whether the repository is new to the agent, genuinely undocumented, or
only missing evidence for one area. Do not re-document established facts without
need.

### 2. Inventory high-signal evidence

Inspect the smallest useful set of:

- root files and directory names;
- package, dependency, workspace, and lock manifests;
- build, task, and developer scripts;
- continuous-integration and release configuration;
- existing architecture, operations, contribution, and testing documents;
- test layout, fixtures, examples, and executable entry points;
- public interfaces, schemas, migrations, infrastructure, and generated-code
  boundaries relevant to the task;
- recent history only when it resolves ownership, convention, or drift.

Do not infer an active technology solely from a file extension or unused
configuration. Note generated, vendored, archived, example, and experimental
areas separately.

### 3. Map structure and boundaries

Describe only boundaries that are supported by repository evidence:

- primary packages, applications, services, libraries, or workspaces;
- entry points and public interfaces;
- dependency direction and ownership boundaries;
- persistence, external integrations, queues, scheduled work, and other side
  effects;
- generated artifacts and files that should not be edited directly;
- areas where the boundary remains ambiguous.

Use concrete paths. Label architectural interpretations as inferred until an
authoritative artifact or maintainer confirms them.

### 4. Establish build and runtime paths

Identify prerequisites, dependency installation, local startup, required
services, configuration sources, environment assumptions, and packaging or
artifact production.

For each important command, record one status:

- `DISCOVERED` — present in a current repository source but not executed;
- `EXECUTED` — run in the current environment with the observed result;
- `BLOCKED` — not runnable because a named prerequisite is missing;
- `STALE OR CONFLICTING` — contradicted by another current source or result.

Prefer repository-defined entry points over reconstructed commands.

### 5. Establish the verification model

Locate the narrowest checks for a local change and the broader checks used by
continuous integration. Identify test layers, selection mechanisms, fixtures,
external dependencies, static analysis, formatting, generated checks, and known
verification gaps.

Do not treat the existence of a test directory or workflow as evidence that it
currently succeeds. Record commands actually executed separately from commands
only discovered.

### 6. Assess documentation reliability

Identify canonical sources, duplicated guidance, missing links, contradictions,
stale claims, and large instruction files that mix durable rules with narrative
or temporary state.

Classify each useful documentation candidate as one of:

- `AGENTS.md` instruction;
- architecture knowledge;
- testing knowledge;
- accepted decision record;
- scoped learning;
- no durable update.

Do not persist these candidates during onboarding unless the user explicitly
requested both onboarding and curation. Otherwise hand them to
`repository-knowledge-curation`.

### 7. Bound readiness

State what a later agent can safely do, what still requires evidence, which
areas should not be touched yet, and the narrowest next task that the map enables.
Do not convert missing product purpose into a technical assumption.

## Output contract

Return exactly these headings:

```markdown
## Repository identity
## Instructions and sources of truth
## Structure and boundaries
## Build and runtime
## Verification model
## Interfaces, data, and side effects
## Risks, contradictions, and unknowns
## Knowledge candidates
## Handoff state
```

Requirements:

- `Repository identity` states the repository purpose only when observed or
  provided and names the inspected revision or its absence.
- `Instructions and sources of truth` names applicable instruction files and
  distinguishes authoritative, supporting, conflicting, and stale sources.
- `Structure and boundaries` uses concrete paths and labels inferences.
- `Build and runtime` and `Verification model` give each important command one
  of the four command statuses and include observed results only for executed
  commands.
- `Knowledge candidates` classifies each proposed durable fact without editing
  documentation or duplicating its full content.
- `Handoff state` contains exactly one allowed state and its factual basis.

Choose one handoff state:

- `READY FOR BOUNDED WORK`
- `READY WITH DOCUMENTATION GAPS`
- `MORE REPOSITORY EVIDENCE REQUIRED`
- `ENVIRONMENT ACCESS REQUIRED`
- `PRODUCT PURPOSE UNCLEAR`

The onboarding is complete when the map is sufficient to bound the next task,
commands are not overstated, contradictions remain visible, and no inferred
architecture is presented as established fact.
