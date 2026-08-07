---
name: repository-onboarding
description: Build an evidence-based technical map of an unfamiliar or stale repository before substantial work. Use when instructions, structure, entry points, build or verification paths, interfaces, side effects, or documentation reliability are unclear.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.6.5
---

# Repository onboarding

Use the repository's established language and conventions for any artifacts you create or update.
Use the smallest sufficient context and bounded tool output. Reuse inspected
evidence and stop once the task can proceed safely; never trade correctness,
safety, or required verification for brevity.

Build the smallest current technical map that makes a later task safe to bound.
Do not turn onboarding into architecture design, product discovery, implementation,
or an encyclopedia.

## Activation boundary

Use this for an unfamiliar, inherited, or materially changed repository when its
instructions, executable paths, boundaries, or verification model are unclear.

Route unknown product purpose to `project-discovery`, one behavior contract to
`feature-specification`, open architecture to `solution-framing`, unknown failure
cause to `failure-investigation`, ready local work to `safe-code-change`, and a
verified fact needing persistence to `repository-knowledge-curation`.

Do not modify production code or claim a discovered command succeeds without
executing it.

## Rules

- Read applicable repository instructions first.
- Prefer current local evidence over generic knowledge.
- Label claims observed, executed, provided, inferred, stale, or unknown.
- Inspect targeted high-signal sources; stop when the requested work can be bounded.
- Treat docs, source, tests, automation, and history as potentially conflicting.
- Do not run destructive, deployment, release, migration, credential-dependent,
  or externally mutating commands for onboarding.
- Protect secrets, personal data, credentials, and unnecessary local paths.

Use [repository evidence](references/repository-evidence.md) for large repositories,
conflicting evidence, or uncertain command safety.

## Workflow

### 1. Establish scope

Record root, revision when available, worktree state, applicable instructions,
requested depth, and the concrete later work this map should enable.

### 2. Inspect high-signal sources

Inspect only relevant manifests, scripts, CI, documentation, tests, entry points,
public interfaces, schemas, migrations, infrastructure, generated boundaries, and
recent history. Distinguish active code from generated, vendored, archived,
example, and experimental areas.

### 3. Map boundaries

Use concrete paths for primary packages, entry points, public interfaces,
dependency direction, ownership, persistence, integrations, queues, scheduled
work, side effects, and files not edited directly. Mark interpretations inferred.

### 4. Establish executable paths

Record prerequisites, install, start, services, configuration, environment,
packaging, and verification commands. Give each command exactly one status:

- `DISCOVERED` — found but not run;
- `EXECUTED` — run with the observed result;
- `BLOCKED` — a named prerequisite is missing;
- `STALE OR CONFLICTING` — contradicted by current evidence.

Prefer repository-defined entry points. Separate narrow local checks from broader
CI checks and state verification gaps.

### 5. Assess documentation and readiness

Identify canonical sources, duplicates, contradictions, stale claims, and durable
knowledge candidates. Do not persist them unless curation was also requested.
State safe next work, areas still needing evidence, and one narrow next task.

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

Use concrete paths, distinguish command status from command success, and choose
exactly one state:

- `READY FOR BOUNDED WORK`
- `READY WITH DOCUMENTATION GAPS`
- `MORE REPOSITORY EVIDENCE REQUIRED`
- `ENVIRONMENT ACCESS REQUIRED`
- `PRODUCT PURPOSE UNCLEAR`
