# AGENTS.md — All-in-One Quality Guidance

These instructions apply to every agent working in this repository. More specific instructions in nested `AGENTS.md` files take precedence.

## Language

- Respond in the repository's primary language.
- Infer it from the README, documentation, product copy, and existing communication.
- If the repository is multilingual or unclear, use the user's language.
- Preserve the language of each edited file unless the task explicitly requires translation.
- Write comments, documentation, errors, and user-facing text in the language and terminology already used nearby.

## Objective

Produce work that is specific to this product, native to this repository, easy to verify, and easy to maintain.

**Generic output can look plausible while skipping the decisions required for a correct, purposeful solution.**

Optimize for:

- user and product fit
- clear information hierarchy
- small, coherent changes
- maintainable architecture
- accessibility and security
- verified behavior rather than confident claims

## Working Method

Before changing code or design:

1. Read the relevant instructions, files, tests, components, styles, data models, and surrounding implementation.
2. Identify the user goal, acceptance criteria, constraints, edge cases, failure states, and trust boundaries.
3. Reuse existing patterns before introducing new ones.
4. State only necessary assumptions. Never invent requirements, product facts, metrics, testimonials, or user research.
5. Split non-trivial work into small, verifiable steps.

For a non-trivial implementation, establish a concise contract first:

- expected inputs and outputs
- valid and invalid states
- error behavior
- relevant edge cases
- authorization and security boundaries
- observable acceptance criteria

Implement and test against that contract.

## Design Rules

Derive the interface from the task and content, not from visual trends.

- Start with user flow, information architecture, and content priority.
- Use realistic copy and data shapes. Do not use meaningless statistics, filler copy, or fake social proof.
- Choose one intentional visual direction that fits the product, audience, and context.
- Create hierarchy with typography, spacing, alignment, scale, and contrast before adding containers or effects.
- Give each screen a clear primary purpose and action.
- Cover relevant states: loading, empty, error, success, disabled, validation, focus, and permission denied.
- Preserve user control. Do not hide important decisions behind unexplained automation.
- Use motion only for orientation, feedback, or state change, and respect `prefers-reduced-motion`.

Do not use these as automatic defaults:

- generic centered hero sections with gradient text, two CTAs, a dashboard mockup, and a logo cloud
- bento grids, excessive cards, or nested containers without structural purpose
- purple/cyan gradients, neon glow, glassmorphism, blur, blobs, or grain without product relevance
- excessive rounding, pills, shadows, borders, or decorative icon circles
- fully centered layouts with weak reading order
- decorative charts or metrics that support no decision
- default “tech” styling, trend fonts, or dark mode as substitutes for brand character
- vague AI marketing language such as “revolutionary,” “seamless,” “supercharge,” or “next-level”
- fabricated quotes, ratings, logos, customers, benchmarks, or trust signals

These elements are allowed only when they serve a clear product purpose and belong to a consistent system.

### Accessibility

- Prefer semantic HTML and native controls.
- Ensure complete keyboard operation and visible focus.
- Use real labels, useful validation messages, and appropriate autocomplete values.
- Maintain sufficient contrast; never rely on color alone.
- Make interactive targets reliably usable.
- Test narrow and wide layouts with long, short, empty, and missing content.
- Ensure links and buttons are distinguishable and functional.

## Code Rules

Make the smallest coherent change that fully solves the task.

- Follow the repository's structure, naming, typing, state management, styling, and error-handling conventions.
- Preserve public APIs and unrelated behavior unless the task requires a change.
- Extend existing abstractions before adding dependencies, global state, helper layers, or parallel architecture.
- Do not rewrite large areas merely because regeneration is easier.
- Remove code made obsolete by the change.

Do not ship:

- duplicated logic that should reuse or extend existing behavior
- oversized functions or components with mixed responsibilities
- premature abstractions, generic wrappers, or vague `Manager`, `Factory`, and `Utils` layers
- imprecise types such as `any` when a useful type is practical
- swallowed errors, silent `catch` blocks, or fabricated fallback results
- dead code, commented-out code, unresolved placeholders, or unexplained TODOs
- hard-coded secrets, tokens, sensitive data, or environment-specific values
- unvalidated external input, unsafe string construction, or client-only authorization
- dependencies for trivial behavior or dependencies added without inspection
- comments that restate obvious code or prose that disguises unclear implementation
- tests that mirror implementation details instead of observable behavior and edge cases
- mocks or fake backends presented as production-ready behavior

Understand every changed line. If a change cannot be explained, inspect more context or reduce its scope.

### Security

- Validate input at trust boundaries and encode output for its destination.
- Enforce authentication and authorization on the server.
- Keep secrets out of the repository and client bundles.
- Do not log credentials, tokens, personal data, or confidential content.
- Use parameterized database access and secure defaults.
- Bound file uploads, redirects, network targets, and resource consumption.
- Justify and inspect new or updated dependencies.

## Verification

Run every relevant repository-provided check that is available:

- focused unit, integration, and end-to-end tests
- type checking
- linting and formatting checks
- build
- security or dependency checks

Also verify:

- acceptance criteria and important edge cases
- loading, empty, error, recovery, and permission states where applicable
- no unintended behavior changes
- no unrelated edits, avoidable duplication, or unnecessary complexity
- no unnecessary requests, re-renders, bundle growth, layout shifts, or expensive hot-path work

Fix causes rather than suppressing failures. Do not weaken tests or disable rules merely to make checks pass.

For UI work, render and operate the application. Check at least one narrow and one wide viewport, keyboard navigation, focus, contrast, labels, long content, empty data, errors, reduced motion, clipping, overlap, layout shift, broken links, and unresponsive controls.

Never claim that an interface is polished, responsive, accessible, secure, or working based only on source inspection.

## Review Mode

Prioritize findings by impact:

1. broken behavior, security issues, or data loss
2. accessibility and usability failures
3. unclear flow or missing states
4. maintainability and structural problems
5. generic styling or unnecessary decoration

Report a small number of concrete findings. For each, include the location, impact, and direct correction. Do not replace useful review with a long list of cosmetic preferences.

## Completion

A task is complete only when the change:

- clearly belongs to this product rather than a generic template
- solves the stated user goal with clear content and hierarchy
- contains no fabricated facts, unfinished placeholders, or broken interactions
- respects repository conventions, accessibility, and security boundaries
- remains focused, understandable, and locally extensible
- passes all relevant checks that could be run

Finish with a concise report containing:

- what changed and why
- checks run and their results
- assumptions, skipped checks, and remaining risks

Never claim success without verifiable evidence.
