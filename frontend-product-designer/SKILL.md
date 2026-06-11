---
name: frontend-product-design
description: Create distinctive, accessible, production-ready frontend UI. Use when building or reshaping user-facing components, pages, flows, design-system elements, responsive layouts, interaction states, visual polish, or frontend UI fixes.
allowed-tools: read_file write_file run_command list_files
---

# Skill: Frontend Product Design

## Purpose

Create frontend interfaces that feel specific to the product and are robust enough to ship. This skill combines two responsibilities:

1. **Design leadership:** choose a deliberate visual direction that fits the subject, audience, content, and product job instead of producing a generic attractive template.
2. **Frontend discipline:** implement that direction with existing system conventions, typed components, accessibility, responsive behavior, complete states, and verification.

The goal is not decoration. The goal is an interface that helps users do the right thing, feels like it belongs to this product, and survives real content, real devices, and real interaction.

## Use this skill when

Use this skill for:

- Building new user-facing UI components, pages, flows, or design-system variants.
- Implementing designs from Figma, Sketch, screenshots, images, sketches, or written briefs.
- Improving visual quality, hierarchy, spacing, typography, motion, responsiveness, or polish.
- Fixing visual bugs, accessibility issues, responsive problems, or broken interaction states.
- Refactoring frontend components for maintainability while preserving or improving UX.
- Adding transitions, micro-interactions, loading states, empty states, error states, or success states.

## Do not use this skill as the primary guide for

- Backend API design, database schema, infrastructure, authentication, authorization, or permissions.
- Major frontend architecture changes such as framework migrations or state-management overhauls.
- Brand strategy decisions that require stakeholder approval.
- Performance work that depends mainly on backend, infrastructure, CDN, image pipeline, or data-model changes.

If a UI task exposes one of these issues, solve the frontend-relevant part and clearly flag the separate product, design, backend, architecture, or infrastructure decision needed.

## Required context

Before building, identify or infer the following. Do not block on minor ambiguity; make the smallest reasonable assumption and continue unless the choice would materially change product direction.

- **Subject:** what the product, feature, page, or component is actually about.
- **Audience:** who will use it and what they understand, value, fear, or need to decide.
- **Single job:** the main thing the UI must help the user do.
- **Context:** where the UI sits in the product, how users arrive there, and what happens next.
- **Design reference:** Figma, Sketch, screenshot, image, existing screen, system primitive, or written brief.
- **Available context:** user preferences, project notes, previous design attempts, brand guidance, or product memory available in the current work context. Use these as hints, not as a reason to ignore the brief.
- **System constraints:** framework, component library, styling method, design tokens, naming conventions, theme support, browser support, and test setup.
- **Interaction requirements:** props, variants, states, validation, loading, empty, error, success, disabled, permissions, keyboard behavior, and edge cases.
- **Accessibility requirements:** semantic structure, focus behavior, keyboard navigation, screen-reader support, contrast, reduced motion, and WCAG target if specified.

## Non-negotiable principles

### 1. The brief wins

Follow explicit user, product, brand, and design requirements first. When the brief specifies a visual direction, implement that direction faithfully. When the brief leaves room, use that freedom to make choices specific to the subject instead of falling back to generic defaults.

### 2. Ground the design in the subject

Distinctive UI comes from the product's own world: its materials, language, workflows, artifacts, constraints, metaphors, and audience expectations. Derive palette, type, layout, iconography, motion, density, and copy from something true about the subject. Use real product content whenever possible; avoid lorem ipsum, fake metrics, and generic placeholder copy when the real content can be inferred or supplied.

### 3. Reuse the system before inventing

Inspect existing components, tokens, styles, patterns, naming conventions, and file structure before creating anything new. Prefer extending established primitives over introducing parallel abstractions. New primitives must solve a real gap.

### 4. Be opinionated, but spend boldness in one place

Every substantial design should have one memorable, justifiable signature element: one real aesthetic risk that fits the brief and can be explained. It may be a layout move, interaction, typographic treatment, visual metaphor, data presentation, or motion moment. Keep the surrounding system disciplined so the signature feels intentional rather than noisy.

### 5. Accessibility is a quality floor

Use semantic HTML first. Add ARIA only when it improves meaning or interaction. Preserve visible focus, logical keyboard navigation, readable contrast, screen-reader clarity, hit-target usability, and reduced-motion preferences. If a visual requirement conflicts with accessibility, flag the conflict and implement the closest accessible alternative.

### 6. Complete the real states

A polished UI includes the states users actually encounter: loading, skeleton, empty, partial data, long content, malformed content, error, validation error, success, disabled, hover, focus-visible, active, selected, expanded, collapsed, permission-limited, offline if relevant, and destructive-action confirmation.

### 7. Motion must earn its place

Use motion to clarify hierarchy, preserve continuity, provide feedback, or express the subject. Prefer one orchestrated moment over many scattered effects. Respect `prefers-reduced-motion`. Avoid motion that hides latency, harms comprehension, or makes the product feel generated.

### 8. Content is interface

UI copy is design material. Labels, headings, helper text, empty states, errors, toasts, and calls to action should help users understand what is happening and what to do next.

### 9. Verification is part of the work

The task is not complete when the UI compiles. It is complete when the interface works across relevant content, states, themes, breakpoints, input methods, accessibility checks, and validation commands.

## Workflow

### Step 1: Inspect and orient

1. Review nearby files and existing components before writing new code.
2. Identify the component library and styling conventions, such as shadcn, Radix, MUI, Tailwind, CSS modules, styled-components, vanilla CSS, or design tokens.
3. Locate existing examples of similar components, pages, states, tests, and Storybook stories.
4. Determine layout, theme, breakpoint, accessibility, naming, import, and state-management patterns.
5. Check package manager, scripts, test tools, browser targets, and whether visual tooling is available.
6. Note constraints that must not be broken.

### Step 2: Define the design direction

For substantial new UI or redesigns, create a compact design plan before implementation. For small component fixes, keep the plan brief and proportional.

Include:

- **Subject, audience, single job:** one sentence each.
- **Palette:** 4-6 named colors with hex values and a purpose for each. Prefer existing tokens when available; if introducing colors, map them to token roles.
- **Typography:** display, body, and optional utility/data roles, including type scale, weights, widths, spacing, and where each role appears. Choose type deliberately; do not default to the same pairings for every project.
- **Layout concept:** structure, spatial rhythm, hierarchy, density, and responsive behavior.
- **Signature element:** the one subject-specific design move the UI will be remembered by.
- **Motion concept:** where motion helps understanding, feedback, or atmosphere; otherwise keep it minimal.
- **Content voice:** how labels, headings, empty states, errors, and calls to action should sound.

For landing pages or major screens, treat the hero or first screen as the thesis of the experience: it should reveal the most characteristic thing about the subject, not just display a headline, metric, and generic gradient.

When the direction is not obvious, explore 2-3 short alternatives before choosing. Use compact notes or ASCII wireframes when layout comparison would help. Then select one direction and build consistently from it.

### Step 3: Run the anti-template critique

Before building, test the plan against common generic outputs.

Revise if the plan relies on unearned defaults such as:

- The common AI defaults: warm cream background with high-contrast serif and terracotta accent; near-black background with one acid-green or vermilion accent; or broadsheet-style hairline rules with dense newspaper columns. These can be valid only when the brief or subject truly calls for them.
- Decorative gradients with no product meaning.
- Generic card grids, bento layouts, or floating dashboards without a content reason.
- Numbered sections when the content is not a real sequence.
- Random glassmorphism, neon accents, oversized metrics, stock icons, decorative blobs, or noise overlays.
- Excessive animation that makes the UI feel generated rather than designed.
- A mismatch between vision and execution: maximalist directions need enough craft and detail to feel intentional; minimal directions need precision in spacing, type, rhythm, and interaction details.
- Safe typography and color choices that could fit almost any product.
- Structural devices, labels, dividers, or visual metaphors that decorate but do not explain.

Keep defaults only when they are genuinely the best answer for the brief. Otherwise, replace them with choices derived from the subject, audience, product task, and existing system.

### Step 4: Plan implementation with system discipline

Before editing files, decide:

1. Which existing components, tokens, hooks, utilities, and patterns to reuse.
2. Which files need to be created or changed.
3. What component API is needed and which props, variants, and events it should expose.
4. Which states and edge cases must be represented in code.
5. Which tests, stories, examples, or docs should be added.
6. Which validation commands will prove the work.

Prefer composition over large configuration objects. Keep APIs typed, minimal, and predictable.

### Step 5: Implement the UI

1. Use existing components and tokens wherever possible.
2. Follow the project's file structure, naming conventions, import style, and styling approach.
3. Keep styling predictable: avoid selector conflicts, accidental cascade overrides, and broad global rules.
4. Use semantic HTML as the foundation.
5. Implement keyboard behavior and focus management for interactive UI.
6. Support mouse, touch, keyboard, and screen-reader usage.
7. Handle responsive layouts for mobile, tablet, desktop, narrow containers, and wide containers.
8. Support light and dark themes if the product supports them.
9. Respect `prefers-reduced-motion` for nonessential movement.
10. Animate `transform` and `opacity` where possible; avoid layout-triggering animation unless there is a clear reason.
11. Avoid unnecessary dependencies, heavy animation libraries, large assets, or bundle growth unless justified by the brief and supported by the project.
12. Preserve existing behavior unless the request explicitly changes it.

### Step 6: Design the content, not just the container

Use these rules:

- Write from the user's side of the screen.
- Name things by what users recognize and control, not by internal implementation.
- Prefer specific language over clever language.
- Use active voice for actions.
- Use sentence case unless the product convention says otherwise.
- Keep action names consistent across buttons, dialogs, toasts, confirmations, and navigation.
- Make errors specific: say what happened and what the user can do next.
- Make empty states directional: explain what belongs here and provide the next useful action.
- Let each text element do one job: label, explain, warn, confirm, or guide.

### Step 7: Cover variants and states

For each component or screen, account for relevant combinations of:

- Default, hover, focus-visible, active, selected, disabled.
- Loading, skeleton, empty, populated, partial data, long data, malformed data.
- Error, validation error, warning, success, confirmation.
- Expanded, collapsed, modal open, modal closed, tooltip shown, menu shown.
- Mobile, tablet, desktop, narrow containers, wide containers.
- Light theme, dark theme, high-contrast needs where applicable.
- Mouse, touch, keyboard, and screen-reader usage.

Do not leave states to browser defaults unless those defaults are intentional, accessible, and visually consistent.

### Step 8: Add required artifacts

When the project supports them, include:

- Component files in the correct directory.
- TypeScript types for props and exported interfaces.
- Unit tests for logic, rendering, and critical user interactions.
- Integration or end-to-end tests for important flows when appropriate.
- Storybook stories or equivalent documentation for variants and states.
- Screenshots or visual snapshots when visual review tooling is available.
- Notes for intentional deviations from existing patterns.
- Brief design notes when a distinctive direction, visual risk, or important rejected default should be remembered by future maintainers.

Skip artifacts only when the repository clearly does not use them or the change is too small to justify them.

### Step 9: Critique after building

If visual tooling is available, render the UI and inspect screenshots before finalizing. Look for:

- Weak hierarchy or unclear primary action.
- Spacing drift, misalignment, cramped density, or inconsistent rhythm.
- Type choices that feel generic or mismatched to the subject.
- Color choices that do not map to semantic purpose.
- Decoration that does not help comprehension.
- Broken responsive behavior.
- Missing or inconsistent interaction states.
- Clipped focus rings or inaccessible contrast.
- Motion that feels scattered, slow, or gratuitous.

Make at least one refinement pass when the critique reveals a visible or usability issue.

## Verification checklist

Run the standard project validation commands. Prefer existing scripts over inventing new ones.

At minimum, verify:

- Lint passes.
- Type checks pass.
- Relevant tests pass.
- Build passes when appropriate for the task.
- The UI renders without console errors or warnings.
- The design matches the brief or reference at relevant breakpoints.
- Keyboard navigation works in a logical order.
- Focus states are visible and not clipped.
- Screen-reader names and roles are meaningful.
- Color contrast is acceptable; use axe, Lighthouse, or equivalent if available.
- Reduced-motion preferences are respected.
- Loading, empty, error, disabled, success, and long-content states work.
- Light and dark themes work if applicable.
- The component works in supported browsers or environments.

If validation cannot be run, state exactly why and what was checked manually instead.

## Completion criteria

A task using this skill is complete only when:

- The UI solves the user's stated job.
- The design direction is specific to the subject and not a generic template.
- Existing system conventions are respected or deviations are documented.
- Accessibility requirements are satisfied or conflicts are clearly flagged with an accessible alternative.
- Important states and variants are implemented.
- Responsive and theme behavior is correct.
- Required artifacts are added when the project supports them.
- Validation commands pass or failures are clearly explained as unrelated, pre-existing, or blocked by missing project context.

## Escalation rules

Escalate or explicitly flag the issue when:

- A design requirement conflicts with accessibility.
- The requested pattern contradicts established product conventions.
- The UI requires missing product decisions, such as pricing logic, permissions, compliance copy, destructive-action policy, legal copy, or brand approval.
- A change would require architecture, backend, authentication, authorization, data-model, or infrastructure work.
- Performance concerns appear, such as large bundle impact, expensive rendering, heavy media, or animation that cannot run smoothly on target devices.
- The implementation cannot be verified because the project lacks scripts, dependencies, assets, credentials, or runnable context.

When escalating, propose the safest useful frontend alternative instead of stopping abruptly.

## Final response format

When the task is done, respond with:

1. A concise summary of the implemented UI or design change.
2. The files changed or created.
3. The validation commands run and their results.
4. Any limitations, assumptions, or follow-up risks.

Do not include a long design manifesto in the final response unless the user asks for it. The work should show the design quality directly.
