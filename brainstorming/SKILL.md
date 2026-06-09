---
name: brainstorming
description: "Use this before substantial creative or design-sensitive software work: new features, new components, behavior changes, architecture changes, broad refactors, or unclear implementation requests. Scales from a lightweight clarification pass for small tasks to a full collaborative design process for complex work."
---

# Brainstorming Ideas Into Designs

## Overview

Turn an idea or implementation request into a clear, validated design before writing code.

This skill helps an agent avoid premature implementation by first understanding the user's intent, the current project context, the constraints, and the success criteria. It is especially useful when the work is ambiguous, product-facing, architectural, risky, or likely to affect multiple parts of the codebase.

Use the smallest version of this process that is sufficient for the task. Do not turn obvious, low-risk edits into a long design exercise.

## When to Use This Skill

Use the **full brainstorming process** when the request involves one or more of the following:

- A new feature, screen, workflow, API, component, integration, or user-facing behavior
- A significant behavior change whose impact is not fully specified
- Architecture, data model, state management, authentication, permissions, performance, security, or deployment implications
- Multiple plausible implementation approaches
- Unclear requirements, constraints, acceptance criteria, or non-goals
- A change that may affect several files, modules, teams, users, or downstream systems
- A request where implementing the wrong thing would be costly

Use the **lightweight process** when the request is small and mostly clear, for example:

- A localized bug fix
- A copy, style, or configuration change
- A small UI adjustment with obvious scope
- A straightforward implementation with clear acceptance criteria
- A mechanical refactor that does not change behavior

Skip this skill when the user has already provided a complete design, implementation plan, and acceptance criteria, unless contradictions or risks are visible.

## Process Selection

Before starting, choose one of three modes.

### 1. Lightweight Clarification

Use this for small, low-risk, mostly clear changes.

Do the following:

1. Inspect the relevant project context.
2. Restate the goal in one or two sentences.
3. Identify the likely files, components, or systems affected.
4. Ask at most one clarifying question only if the answer would materially change the implementation.
5. State the minimal intended approach.
6. Proceed if the task is sufficiently clear.

Do not force a long design discussion for simple work.

### 2. Focused Design

Use this for medium-complexity work where the goal is understandable but the implementation needs design judgment.

Do the following:

1. Inspect the current project state.
2. Ask targeted questions, preferably one at a time.
3. Clarify success criteria, constraints, and non-goals.
4. Present two or three implementation approaches with trade-offs.
5. Recommend one approach and explain why.
6. Produce a concise design summary before implementation.

### 3. Full Collaborative Design

Use this for broad, ambiguous, risky, or architectural work.

Do the following:

1. Inspect the current project state in depth.
2. Build a shared understanding of the user's goal.
3. Ask questions incrementally until requirements and constraints are clear enough.
4. Explore alternatives and trade-offs.
5. Present the recommended design in digestible sections.
6. Validate the design with the user before implementation.
7. Document the validated design if the project or user expects design artifacts.

## Understanding the Idea

Start by checking the current project context before asking unnecessary questions. Review relevant files, documentation, conventions, tests, recent commits, issue descriptions, or existing patterns when available.

Clarify the following:

- Purpose: What problem should this solve?
- Users: Who uses this, and in what situation?
- Current behavior: What exists today?
- Desired behavior: What should change?
- Constraints: Technical, product, legal, security, performance, compatibility, time, or team constraints
- Success criteria: How will we know the work is done?
- Non-goals: What should explicitly not be included?
- Failure cases: What can go wrong, and how should the system respond?

Prefer multiple-choice questions when they reduce effort for the user. Use open-ended questions when the design space is genuinely broad.

Default to one question per message for complex discovery. For simple or time-sensitive work, it is acceptable to ask a small grouped set of questions if that is clearly more efficient.

## Exit Criteria for Discovery

Move from discovery to design only when the following are sufficiently clear:

- The user goal is understood.
- The main user or system flows are known.
- The in-scope and out-of-scope items are identified.
- Key constraints and risks are known or explicitly marked as assumptions.
- The affected components, files, APIs, or data structures are roughly identified.
- The expected success criteria or acceptance tests are defined.
- There is enough information to compare implementation approaches.

If some information is missing but not critical, proceed with explicit assumptions instead of blocking progress.

## Exploring Approaches

Present two or three realistic approaches when there is meaningful design choice.

For each approach, cover:

- What the approach is
- Why it might be attractive
- Main trade-offs
- Risks or hidden costs
- Testing implications
- Migration or rollout implications, if relevant

Lead with the recommended option. Explain why it best balances simplicity, maintainability, risk, and user value.

Use YAGNI aggressively. Remove nice-to-have features unless they directly support the stated goal or reduce clear future risk.

## Presenting the Design

When the design is ready, present it in small sections. For full collaborative design, keep each section around 200–300 words and validate after each section. For focused design, a shorter consolidated design is usually enough.

Cover the areas that matter for the task:

- Architecture and boundaries
- Components, modules, or services touched
- Data model, state, and data flow
- API or interface changes
- UI and user interaction, if applicable
- Permissions, privacy, and security considerations
- Error handling and edge cases
- Performance and scalability considerations, if relevant
- Observability, logging, or analytics, if relevant
- Accessibility and internationalization, if relevant
- Compatibility, migration, rollout, and rollback, if relevant
- Testing strategy

Be explicit about assumptions. Separate confirmed requirements from recommendations.

## Documentation

Create a design document when one of the following is true:

- The user asks for a design document.
- The change is broad, risky, architectural, or likely to be revisited later.
- The repository has an established design-doc or planning convention.
- The design needs handoff to another agent or human implementer.

Use this path unless the project uses a different convention:

```text
docs/plans/YYYY-MM-DD-<topic>-design.md
```

A good design document should include:

- Summary
- Goals
- Non-goals
- Current state
- Proposed design
- Alternatives considered
- Risks and mitigations
- Testing strategy
- Rollout or migration plan, if relevant
- Open questions

Do not automatically commit the document unless the user explicitly asked for commits or the repository workflow clearly expects it. If committing is appropriate, use a clear commit message and include only the relevant design artifact.

If a writing or style-improvement skill is available, use it to make the document concise and readable.

## Implementation Handoff

Before implementation, ensure the user or project workflow is ready for code changes.

For larger work:

1. Confirm that the design is accepted or note the accepted assumptions.
2. Create an implementation plan.
3. Use an isolated branch or worktree when appropriate.
4. Break the work into small, testable steps.
5. Keep the implementation aligned with the agreed design.

For small work:

1. State the minimal approach.
2. Implement directly if the request is clear.
3. Test the changed behavior.

## Key Principles

- **Scale the process to the task.** Full brainstorming is valuable for complex work but wasteful for trivial edits.
- **Understand before building.** Avoid coding before the goal, scope, and constraints are clear enough.
- **Ask useful questions.** Ask only questions whose answers could change the design or implementation.
- **Prefer clarity over ceremony.** Use lightweight clarification when a long design process would slow the user down.
- **Explore real alternatives.** Compare approaches when meaningful choices exist.
- **Recommend clearly.** Do not just list options; explain which one should be used and why.
- **YAGNI ruthlessly.** Avoid speculative features and abstractions.
- **Validate incrementally.** Check the design with the user before major implementation work.
- **Document when valuable.** Write durable design docs for complex or risky changes, not for every tiny edit.
- **Commit intentionally.** Never commit automatically unless the user or workflow clearly calls for it.
- **Make assumptions visible.** If moving forward with incomplete information, say what is assumed.
- **Design for failure.** Consider errors, edge cases, rollback, and tests before implementation.
