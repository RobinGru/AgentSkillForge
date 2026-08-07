---
name: repository-knowledge-curation
description: Persist one verified repository-specific fact in its smallest canonical artifact. Use after evidence-producing work when durable guidance, architecture, testing knowledge, an accepted decision, or a scoped learning must be updated without duplicating context.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.6.4
---

# Repository knowledge curation

Use the repository's established language and conventions for any artifacts you create or update.
Use the smallest sufficient context and bounded tool output. Reuse inspected
evidence and stop once the task can proceed safely; never trade correctness,
safety, or required verification for brevity.

Turn one verified reusable finding into the smallest durable documentation change.
Do not create a transcript, context dump, or second source of truth.

## Activation boundary

Use this after onboarding, investigation, implementation, review, or maintainer
correction when a supported fact should outlive the current session.

Do not use it for speculation, generic ecosystem advice, unresolved decisions,
feature status, transient worktree state, implementation, diagnosis, or review.
Route those to `solution-framing`, `feature-lifecycle`, `session-handoff`, or the
relevant specialist skill.

## Rules

- Persist only observed, executed, provided, or explicitly accepted knowledge.
- Inspect existing instructions and documentation before creating an artifact.
- Keep one canonical home per fact; update or link instead of copying.
- Prefer the narrowest scope and smallest useful change.
- Do not replace executable safeguards with prose.
- Mark or remove superseded claims in the same scope.
- Keep secrets, personal data, temporary state, and unnecessary local paths out.

Use [knowledge placement](references/knowledge-placement.md) when destination or
promotion is uncertain.

## Workflow

### 1. Define the candidate

State one reusable claim, its evidence, scope, value, owner when known, and the
condition that would require re-verification. Exclude discovery history unless a
verified failed approach prevents a likely repeated mistake.

### 2. Find the canonical home

Inspect applicable instructions, architecture, testing, decisions, learnings,
code-local contracts, feature artifacts, and indexes. Identify duplicates,
conflicts, existing enforcement, and repository conventions.

Choose exactly one primary destination:

- `AGENTS.md` for a short broadly applicable directive or pointer;
- architecture for structure, boundaries, interfaces, ownership, or invariants;
- testing for verified commands, fixtures, environments, and evidence limits;
- decision for an accepted consequential choice and its consequences;
- learning for a narrower verified repository-specific fact;
- another established canonical source;
- no durable update when the candidate is transient, duplicated, obvious, or
  insufficiently supported.

An unresolved consequential choice goes to `solution-framing`.

### 3. Apply one curation action

Create, update, promote, demote, merge, supersede, retire, or make no durable
change. Follow repository conventions; otherwise create only the one needed
location under `AGENTS.md` or `docs/{architecture,testing,decisions,learnings}/`.

Lead with the fact. State scope, exceptions, direct paths or commands, and only
the rationale needed to avoid misuse. Link authoritative detail.

### 4. Reconcile and verify

Resolve conflicting active statements in the inspected scope. Preserve decision
history when required. Verify claim support, scope, links, discoverability,
command labels, absence of sensitive or transient data, and the final diff.
Documentation alone does not prove underlying behavior.

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

Name one primary destination, only checks actually run, remaining conflicts, and
exactly one state:

- `CURATED`
- `NO DURABLE UPDATE`
- `MORE EVIDENCE REQUIRED`
- `DECISION REQUIRED`
- `CANONICAL OWNER REVIEW REQUIRED`

Complete only when the fact has one discoverable canonical home, supported scope,
and no ignored active duplicate.
