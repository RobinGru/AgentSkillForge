---
name: repository-knowledge-curation
description: Classify and persist verified repository-specific knowledge in the smallest canonical artifact. Use after onboarding, investigation, implementation, review, or correction when a durable fact may belong in AGENTS.md, architecture, testing, an accepted decision record, or a scoped learning; avoid transcripts, speculation, and duplicate context.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.6.4
---

# Repository knowledge curation

Use the repository's established language and conventions for any artifacts you create or update.

Turn a verified repository-specific finding into a small, maintainable knowledge
change. Improve future retrieval without growing a permanent context dump or
creating a second source of truth.

## Activation boundary

Use this skill when:

- repository onboarding found durable guidance worth preserving;
- an investigation established a reusable cause, constraint, or safe procedure;
- implementation or review exposed stale or contradictory documentation;
- a maintainer correction should survive beyond the current conversation;
- an accepted technical decision needs to be recorded or linked;
- an existing learning should be promoted, narrowed, superseded, or retired.

Do not use this skill for:

- unverified observations, speculative advice, or generic ecosystem knowledge;
- product behavior contracts: use `feature-specification`;
- unresolved consequential choices: use `solution-framing`;
- feature progress or revision-bound evidence: use `feature-lifecycle`;
- transient worktree or continuation state: use `session-handoff`;
- implementation, failure diagnosis, or code review itself;
- routine activity logs, chat transcripts, or raw command output.

This skill may document an accepted decision. It must not make an unresolved
architecture or delivery decision on its own.

## Core rules

- Inspect existing instructions and documentation before creating a new file.
- Persist only observed, executed, provided, or explicitly accepted knowledge.
- Keep one canonical home for each fact; link instead of copying.
- Prefer the narrowest durable scope and the smallest useful change.
- Keep `AGENTS.md` short, actionable, and broadly relevant to its scope.
- Put explanation and detailed evidence in focused documents loaded on demand.
- Preserve dates, revisions, versions, environments, and owners only when they
  affect validity or re-verification.
- Remove or mark superseded claims when adding a replacement.
- Do not create empty documentation directories, empty indexes, or generic files
  without a current knowledge candidate.
- Do not weaken executable safeguards by replacing tests, automation, or policy
  checks with prose.

Consult [knowledge placement](references/knowledge-placement.md) whenever the
correct destination or promotion path is uncertain.

## Workflow

### 1. Define the knowledge candidate

State the smallest reusable claim, why it matters again, its evidence, scope,
owner when known, and conditions that could make it false.

Separate the durable fact from the story of how it was discovered. A failed
attempt belongs only when it prevents a likely repeated mistake and has a
verified explanation.

### 2. Inspect current knowledge

Search applicable instruction files, architecture and testing documents,
decision records, learning records, code-local documentation, specifications,
and related indexes.

Identify:

- the current canonical source, if one exists;
- duplicate or conflicting statements;
- the repository's naming and storage convention;
- narrower scopes or existing links that should be preserved;
- whether the candidate is already enforced by code, tests, automation, or
  configuration.

### 3. Classify the destination

Choose exactly one primary destination:

- `AGENTS.md` — a concise instruction or pointer needed across many tasks in its
  scope;
- architecture — durable structure, boundary, dependency direction, ownership,
  interface, data flow, or invariant;
- testing — verified commands, environments, fixtures, test selection,
  evidence expectations, or known verification limitations;
- decision — an accepted consequential choice, its context, alternatives,
  consequences, status, and verification obligations;
- learning — a verified repository-specific finding that is reusable but
  narrower, less stable, or not yet a general rule;
- another canonical source — code-local contract, feature specification,
  lifecycle record, operational runbook, or repository-defined equivalent;
- no durable update — transient, duplicated, obvious, unverified, or unlikely to
  be reused.

If a consequential choice is not accepted, stop and hand it to
`solution-framing`. Do not disguise a recommendation as a decision record.

### 4. Choose the curation action

Choose one action:

- create a focused record;
- update the current canonical record;
- promote a learning into a stable rule;
- demote an over-broad rule into scoped documentation;
- merge duplicates into one canonical source;
- supersede or retire stale knowledge;
- make no durable change.

Use the repository convention. When none exists and persistence is justified,
use only the needed fallback location:

```text
AGENTS.md
docs/architecture/
docs/testing/
docs/decisions/
docs/learnings/
```

Do not establish this whole structure for one fact.

### 5. Write the minimal durable change

Write for later retrieval:

- lead with the fact, rule, or decision;
- state scope and exceptions;
- include the direct command, path, interface, or evidence needed to apply it;
- include rationale only where omission would invite a wrong choice;
- include a re-verification condition for version- or environment-sensitive
  knowledge;
- link to the authoritative detail instead of duplicating it.

For `AGENTS.md`, prefer a short directive and a pointer. Do not add repository
summaries, session history, broad style advice, or detailed architecture that is
already discoverable elsewhere.

### 6. Reconcile conflicts and lifecycle

Update or remove contradicted statements in the same scope. Preserve a clear
supersession link when history remains useful. Do not silently rewrite an
accepted decision; retain its prior status and record the new accepted decision
according to repository convention.

Promote a learning only when its scope and stability are established. Retire or
narrow knowledge when its evidence no longer applies.

### 7. Verify the documentation change

Verify that:

- every new claim is supported and correctly scoped;
- links and referenced paths resolve locally;
- commands are labelled accurately as executed or merely documented;
- no conflicting active statement remains in the inspected scope;
- the chosen destination is discoverable from existing indexes or instructions
  when discovery would otherwise be unlikely;
- no temporary state, secret, personal data, or unnecessary local path was
  persisted;
- the final diff contains only the justified knowledge change.

Run only proportionate, non-destructive checks. A documentation change does not
prove the underlying behavior unless that behavior was directly verified.

## Output contract

Return exactly these headings:

```markdown
## Knowledge candidate
## Evidence and scope
## Placement decision
## Documentation change
## Conflicts and retirements
## Verification
## Handoff state
```

Requirements:

- `Knowledge candidate` states one reusable claim, not a session summary.
- `Evidence and scope` distinguishes observed, executed, provided, accepted,
  stale, and unknown information and states validity limits.
- `Placement decision` names exactly one primary destination and explains why
  the other likely destinations are not canonical.
- `Documentation change` lists created, updated, promoted, demoted, merged,
  superseded, retired, or unchanged artifacts.
- `Conflicts and retirements` names resolved and unresolved contradictions; use
  `None observed` only after the applicable scope was searched.
- `Verification` lists only checks actually performed and any remaining gap.
- `Handoff state` contains exactly one allowed state and its factual basis.

Choose one handoff state:

- `CURATED`
- `NO DURABLE UPDATE`
- `MORE EVIDENCE REQUIRED`
- `DECISION REQUIRED`
- `CANONICAL OWNER REVIEW REQUIRED`

The curation is complete when the fact has one discoverable canonical home, its
scope and evidence are explicit, stale duplicates are handled, and permanent
instructions remain smaller rather than merely more comprehensive.
