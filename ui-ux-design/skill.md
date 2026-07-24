---
name: ui-ux-design
description: Design, review, or improve digital interfaces that are clear, distinctive, accessible, and production-ready. Automatically use when a task materially affects how users perceive, understand, navigate, or interact with an interface—even when the request is phrased as building, styling, refactoring, polishing, reviewing, or fixing frontend code. Covers visual hierarchy, layout, typography, color, components, content, interaction states, responsiveness, accessibility, and design-system consistency. Infer the relevant surface, mode, and constraints from the brief, files, screenshots, and codebase. Prevent generic AI-template output. Do not use for backend-only work with no user-facing effect.
disable-model-invocation: false
---

# UI/UX Design

Create interfaces that fit the product, help users complete the right task, and remain robust in real use. Avoid design that is merely attractive, fashionable, or plausibly generated.

## Applicability

Use this skill when the requested work changes at least one of these:

- what users notice first
- how information is grouped or understood
- how users navigate, decide, enter data, or complete actions
- visual language, layout, typography, color, spacing, or components
- interaction feedback, states, responsiveness, or accessibility
- consistency with an existing product or design system

Infer applicability from the task and available artifacts. The user does not need to mention “design,” “UI,” or “UX.”

Do not use it as the primary guide for backend-only logic, infrastructure, database design, authentication, or non-visual refactoring.

## Operating mode

Detect the required mode automatically:

- **Create:** establish structure and direction for new UI.
- **Reshape:** improve an existing interface without losing product intent.
- **Implement:** translate a brief, reference, or design into production UI.
- **Review:** identify UX, visual, accessibility, and consistency problems.
- **Fix:** make the smallest change that resolves a focused UI issue.

Scale the process to the task. Do not produce a design manifesto for a small fix.

## Core rules

1. **The brief wins.** Follow explicit product, brand, platform, and user constraints.
2. **Derive, do not decorate.** Base hierarchy, density, type, color, imagery, and motion on the subject, audience, content, and user job.
3. **Reuse before inventing.** Inspect existing components, tokens, patterns, content, and conventions first.
4. **Structure before styling.** Resolve information architecture, priority, grouping, and actions before visual polish.
5. **One clear direction.** Use a coherent design thesis; do not combine unrelated trends.
6. **Accessibility is a floor.** Use semantic structure, visible focus, keyboard support, readable contrast, meaningful labels, and reduced motion.
7. **Real states matter.** Include relevant loading, empty, error, success, disabled, long-content, permission, and destructive states.
8. **Content is interface.** Use specific labels, helpful errors, realistic content, and clear actions. Do not invent fake metrics or meaningless copy.
9. **Verify the result.** Render or inspect when possible; test relevant states, breakpoints, input methods, and project checks.

## Anti-slop test

“AI slop” is not a fixed visual style. It is design that appears finished but is generic, weakly justified, repetitive, or disconnected from the product.

Before finalizing, remove or justify:

- layouts that could fit almost any product
- card, bento, hero, dashboard, or sidebar patterns used by reflex
- decorative gradients, glass, glow, blobs, noise, oversized type, or motion without product meaning
- excessive containers, rounded rectangles, badges, dividers, icons, or empty space
- safe typography and palette choices with no subject-specific rationale
- repeated visual emphasis that leaves no clear priority
- decorative data, fake testimonials, fake activity, or placeholder content presented as real
- inaccessible controls, missing states, clipped focus, or fragile responsive behavior

A familiar pattern is acceptable when it is the clearest solution. Distinctiveness must not reduce usability.

## Workflow

### 1. Understand

Identify or infer:

- subject, audience, primary user job, and context
- content and actions that matter most
- platform, framework, component system, and constraints
- relevant states, accessibility needs, and reference material

Make the smallest safe assumption when details are missing. Ask only when a decision would materially change the product direction.

### 2. Inspect

For existing work, review nearby UI, components, tokens, styles, naming, responsive patterns, and tests before proposing changes.

### 3. Define

For substantial work, state briefly:

- design thesis
- information hierarchy and layout logic
- visual system or existing tokens to use
- one justified signature element, if appropriate
- key states and responsive behavior

Skip or compress this for focused fixes.

### 4. Execute

- use semantic, maintainable, project-native implementation
- prefer composition and existing primitives
- keep component APIs minimal and typed when applicable
- support keyboard, touch, screen readers, and relevant themes
- preserve existing behavior unless the request changes it
- avoid unnecessary dependencies and animation

### 5. Critique

Check hierarchy, comprehension, density, alignment, typography, semantic color, consistency, responsive behavior, states, focus, contrast, and motion. Make at least one refinement when a material issue is found.

### 6. Verify

Run available lint, type, test, build, accessibility, and visual checks relevant to the change. State precisely what could not be verified.

## Output

Match the output to the request:

- **Design request:** concise rationale, structure or wireframe, system decisions, states, and implementation guidance.
- **Implementation request:** make the changes, then summarize files and verification.
- **Review request:** prioritize findings by user impact; include concrete corrections.
- **Prompt request:** produce a reusable prompt that tells the target model to infer context, follow the existing system, cover states, and run the anti-slop test.

Keep final responses concise. Show quality through the result, not through lengthy explanation.

## Completion check

The work is complete when:

- the primary user job and action are clear
- the interface feels specific to its product and context
- information hierarchy and interaction states are coherent
- existing system conventions are reused or deviations are justified
- accessibility and responsive behavior are covered
- decorative or generic elements have been removed or earned
- relevant verification passes, or limitations are stated
