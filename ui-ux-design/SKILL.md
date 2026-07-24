---
name: ui-ux-design
description: "Design, review, or improve user-facing interfaces. Automatically use only when a task materially changes information architecture, interaction behavior, responsive behavior, accessibility, component patterns, or the visual system. For an explicitly requested isolated value, copy, alignment, or styling change, use Micro mode and do not broaden the scope. Do not use for backend-only work with no user-facing effect."
disable-model-invocation: false
---

# UI/UX Design

Create interfaces that help real users complete a defined task, fit the product and its constraints, meet measurable accessibility and quality requirements, and remain robust in production.

Do not substitute visual polish for product understanding. Do not present assumptions, simulated research, placeholder data, or unverified claims as facts.

## 1. Priority order

When requirements conflict, use this order:

1. User safety, accessibility, legal, privacy, and data-integrity requirements
2. Explicit product requirements and the primary user job
3. Existing design-system rules and established product behavior
4. Platform conventions and evidence-backed usability practices
5. Brand expression and visual preference

The brief does not override levels 1–2.

If a requested design would create a known accessibility, safety, privacy, or data-integrity failure:

- do not silently implement the failure;
- preserve the underlying intent with the closest compliant alternative;
- state the conflict and the alternative used;
- if exact reproduction is required for analysis or a non-production mock-up, isolate and label the non-compliant part and also provide a compliant production recommendation.

## 2. Applicability and scope control

Use this skill when the task materially changes at least one of the following:

- information architecture, hierarchy, grouping, or navigation;
- how users decide, enter data, recover from errors, or complete a task;
- interaction behavior, feedback, states, or permissions;
- responsive behavior or support for different input methods;
- accessibility semantics or operability;
- reusable component patterns, design tokens, or the product's visual system;
- a complete screen, flow, feature, or design review.

Do not automatically run the full workflow for:

- an exact single-value change such as `12px` to `16px`;
- a copy-only correction that does not change meaning or task flow;
- a local alignment, color-token, icon, or formatting fix with no new behavior;
- snapshot updates, dependency upgrades, or non-visual refactoring;
- backend-only logic, infrastructure, database work, or authentication internals with no interface impact.

If the user explicitly invokes this skill for such work, use **Micro mode** and keep the change local.

Do not broaden the task merely because a different design might be preferable. Preserve unrelated behavior and styling unless they create a blocker defined in this skill.

## 3. Operating modes

Choose the smallest mode that safely covers the task.

### Micro

Use for an exact, local change with no new structure or behavior.

- Inspect the affected component and its nearest dependencies.
- Implement the requested change without redesigning adjacent UI.
- Verify the local result and relevant project checks.
- Do not create a design thesis, research plan, or broad critique.

### Scoped

Use for one component, screen section, or bounded interaction flow.

- Confirm the user job, affected states, and acceptance criteria.
- Reuse the existing system before introducing a new pattern.
- Test the complete affected interaction, not only the default state.

### Substantial

Use for a new screen or flow, information-architecture change, new reusable pattern, redesign, or product-level review.

- Establish an evidence record, UX hypothesis, measurable success criterion, design rationale, validation plan, and verification matrix.
- Consider the end-to-end user journey and dependencies outside the visible screen.

Task labels such as **Create**, **Reshape**, **Implement**, **Review**, and **Fix** may be used within any appropriate scope mode.

## 4. Evidence, assumptions, and UX validity

### Evidence record

For Scoped and Substantial work, classify important inputs as:

- **Observed:** directly found in supplied files, code, screenshots, analytics, research, or the live product.
- **Provided:** explicitly stated by the user or product brief.
- **Inferred:** a reasonable conclusion supported by observed or provided evidence.
- **Unknown:** not established by available evidence.

Never convert an inference or unknown into a factual claim.

For each decision that materially affects the product direction, record the evidence or label the assumption. Examples include the primary audience, most common task, device context, frequency of use, business priority, and risk tolerance.

### Research integrity

Never invent or simulate:

- user interviews, quotes, observations, usability findings, or survey results;
- analytics, conversion rates, task success, drop-off, or performance data;
- accessibility audit results, browser test results, or assistive-technology results;
- testimonials, activity feeds, operational metrics, or production content.

When direct research or analytics are unavailable:

- state that they are unavailable;
- use the smallest reversible assumption needed to proceed;
- produce a validation plan instead of fabricated findings;
- distinguish proposed metrics from measured metrics.

### UX hypothesis and success measure

For Substantial work, define:

- **User:** the relevant user or role;
- **Job:** the concrete task or decision;
- **Problem evidence:** what indicates the current or expected problem;
- **Hypothesis:** the proposed change and expected user effect;
- **Primary measure:** one measurable user outcome;
- **Guardrails:** outcomes that must not worsen;
- **Validation method:** how the hypothesis can be tested.

Use this format:

> For [user] doing [job], changing [interface or behavior] should improve [measurable outcome] because [evidence or rationale]. Validate with [method]. Do not worsen [guardrail].

Suitable outcome measures include task completion, error rate, time on task, successful recovery, comprehension, support requests, abandonment, or accessibility defects. Do not use engagement as a default proxy when the user goal is completion or comprehension.

If no baseline or target is available, label the measure as **proposed** and do not invent a number.

### Proportionate validation

Select validation based on risk and uncertainty:

- **Low-risk local change:** targeted review and functional verification.
- **Moderate interaction change:** prototype or implementation test with representative tasks, plus analytics or support evidence when available.
- **High-risk, irreversible, regulated, financial, health, privacy, or destructive flow:** specialist review and representative-user validation before claiming production readiness.

Do not claim that a design is “validated” unless relevant evidence was actually collected. A heuristic review is not a usability test; an automated accessibility scan is not an accessibility audit.

## 5. Operational definitions

Use these definitions instead of vague quality language.

### Material

A change or issue is material when it can affect at least one of these outcomes:

- completion, comprehension, decision quality, or recovery for a real user task;
- accessibility, safety, privacy, legal compliance, or data integrity;
- behavior at a supported viewport, zoom level, locale, browser, platform, or input method;
- a declared performance budget or network-resilience requirement;
- consistency of a reusable component or pattern across more than one use;
- production reliability or maintainability beyond the edited line.

A purely aesthetic preference with no plausible effect on these outcomes is not material.

### Review severity and confidence

Use one severity and one confidence level for each review finding.

Severity:

- **Blocker:** prevents a core task or creates a safety, accessibility, privacy, legal, security, or data-integrity failure.
- **High:** seriously harms a common or important task and has no reasonable workaround.
- **Medium:** causes recurring confusion, delay, errors, or inconsistency, but a workaround exists.
- **Low:** creates localized friction or inconsistency without threatening task completion.

Confidence:

- **High:** directly reproduced, measured, or required by an applicable standard.
- **Medium:** strongly supported by observed evidence but not directly measured with users.
- **Low:** a plausible hypothesis that requires validation.

Do not present a Low-confidence preference as a defect.

### Product-specific

A result is product-specific when at least two material decisions can be traced to actual product evidence, such as the user job, content model, domain constraints, frequency of use, risk, platform, or existing system.

Fail condition: replacing the labels and logo would allow the same structure to fit an unrelated product with no meaningful change.

### Coherent

A result is coherent when hierarchy, component choice, density, typography, color, and motion support the same user priorities and interaction model.

Check:

- the primary task is identifiable without reading every element;
- each decision context has one clearly dominant action, unless actions are intentionally equal;
- emphasis levels match information priority;
- repeated elements behave and look consistently;
- exceptions are documented and justified.

### Justified or earned

An element is justified when it serves at least one stated function: comprehension, navigation, task completion, feedback, accessibility, risk reduction, meaningful brand recognition, or evidence-backed persuasion.

Use the removal test: if removing the element does not reduce one of those functions, remove it or simplify it.

### Distinctive

Distinctiveness is optional, not a completion requirement. It must come from product content, domain behavior, brand assets, or a relevant interaction—not arbitrary decoration.

A signature element is acceptable only when it:

- has a named purpose;
- does not reduce comprehension, accessibility, or performance;
- is not repeated so often that it competes with the primary task.

### Generic-output risk

A design has generic-output risk when it appears complete but is weakly tied to the product. Indicators include interchangeable layouts, reflexive card grids, decorative dashboards, fake data, excessive containers, arbitrary gradients, or repeated emphasis with no priority.

Do not use “AI slop” as the evaluation result. Report the specific observable problem and its user impact.

## 6. Core design rules

1. **Structure before styling.** Resolve priority, sequence, grouping, labels, actions, and states before decorative treatment.
2. **Reuse before inventing.** Inspect existing components, tokens, patterns, content, naming, and tests first.
3. **Content is interface.** Use concrete labels, realistic supplied content, helpful instructions, and actionable error messages.
4. **Real states are part of the design.** Include all relevant loading, empty, partial, error, success, disabled, offline, permission, long-content, and destructive states.
5. **Progressive disclosure over hidden complexity.** Show what is needed for the current decision and make secondary detail discoverable.
6. **Preserve user work.** Avoid data loss on validation errors, navigation, refresh, timeout, or retry whenever technically possible.
7. **Do not encode meaning by appearance alone.** Color, position, shape, animation, or iconography must not be the only carrier of essential information.
8. **Use familiar patterns when they are clearer.** Novelty is never a goal by itself.
9. **Prefer reversible decisions under uncertainty.** Avoid introducing a new component or visual language when a local composition solves the problem.
10. **No change is a valid review outcome.** Do not modify a design merely to demonstrate that a critique occurred.

## 7. Accessibility minimums

Unless the product has a stricter requirement, target **WCAG 2.2 Level AA** for web interfaces. For native platforms, follow the platform accessibility guidance and preserve equivalent outcomes.

A known failure on a core task is a release blocker unless the user explicitly requests a non-production analysis artifact and the failure is clearly documented.

### Semantics and assistive technology

- Use native semantic elements before custom roles.
- Every interactive element must expose an accessible name, role, state, and value where applicable.
- Preserve a logical heading structure, landmark structure, reading order, and focus order.
- Associate labels, descriptions, instructions, and errors programmatically with controls.
- Announce important asynchronous status changes without moving focus unnecessarily.
- Provide meaningful text alternatives for informative non-text content; use empty alternatives for purely decorative images.
- Do not place essential text in an image when normal text can provide the same presentation.

### Keyboard and focus

- All functionality must be operable by keyboard without a trap.
- Focus order must follow the task and visual reading sequence.
- Focus must remain visible and must not be fully obscured by sticky or overlay content.
- Use a clearly visible focus indicator. As a design default, target an indicator at least equivalent to a 2 CSS-pixel perimeter with at least 3:1 contrast against adjacent unfocused colors.
- Opening, closing, and returning from dialogs, menus, popovers, and disclosures must move or restore focus predictably.
- Do not trigger a context change merely on focus.

### Contrast and non-color cues

- Normal text: at least **4.5:1** contrast.
- Large text: at least **3:1** contrast.
- Essential component boundaries, states, focus indicators, and meaningful graphics: at least **3:1** against adjacent colors.
- Do not rely on color alone for errors, selection, status, links, or required fields.
- Disabled controls may use the WCAG exception, but their state and purpose must remain understandable.

### Target size and input

- Pointer targets must meet at least **24 × 24 CSS pixels**, including the WCAG spacing exceptions where applicable.
- Aim for **44 × 44 CSS pixels** for primary, frequent, touch-first, or safety-critical controls.
- Do not require hover, fine pointer control, multipoint gestures, device motion, or drag-only interaction when an equivalent simpler input can be provided.

### Reflow, zoom, and text adaptation

- Support text resize to **200%** without loss of content or functionality.
- Support reflow at a viewport equivalent to **320 CSS pixels** without two-dimensional scrolling, except for content that genuinely requires it, such as maps, large data tables, diagrams, or editing canvases.
- Do not lose content or functionality when users apply WCAG text-spacing overrides.
- Avoid fixed heights for text containers and controls that may contain translated, user-generated, or enlarged text.
- Prevent clipped focus indicators, labels, validation messages, and controls.

### Motion, time, and media

- Respect `prefers-reduced-motion` and remove non-essential motion for that preference.
- Do not use flashing content that creates a seizure risk.
- Provide pause, stop, extend, or disable controls for time limits and moving content when required.
- Provide captions, transcripts, audio description, or alternatives when required by the media and product context.

## 8. Responsive design, browser support, and input methods

### Responsive behavior

- Choose breakpoints from content and interaction constraints, not device names alone.
- Test the smallest supported width, a representative intermediate width, and a wide layout.
- Include long headings, long names, large numbers, validation messages, and unbroken strings.
- Preserve task order when columns collapse.
- Do not hide essential actions solely to make a layout fit.
- Make hover enhancements optional; the task must remain understandable and operable without hover.
- Account for software keyboards, safe areas, orientation changes, and viewport-resizing behavior when relevant.

### Browser and platform support

- Follow the repository's declared support matrix, `browserslist`, platform version, or product requirement.
- If none exists, document the assumption instead of claiming universal support.
- Where tools are available, smoke-test the current stable versions of Chromium, Firefox, and Safari for Substantial web changes.
- Use progressive enhancement and avoid a critical path that depends on an unsupported experimental feature without a fallback.
- State exactly which browsers, devices, or platforms were not tested.

### Input methods

Test interactions that are affected by the change with the relevant combination of:

- keyboard;
- touch;
- mouse or trackpad;
- screen reader or accessibility tree inspection;
- voice input or switch-access implications when the interaction uses custom controls, drag, gestures, or spatial input.

## 9. Internationalization and localization

Treat internationalization as a structural concern, not a final copy pass.

- Use the correct document or view language metadata.
- Format dates, times, numbers, currencies, names, addresses, and plural forms with locale-aware APIs.
- Do not concatenate translated sentence fragments.
- Avoid fixed widths and character-count assumptions.
- Prefer CSS logical properties where direction can change.
- Support right-to-left layout when required by the product; mirror directional UI only when the meaning should mirror.
- Test with the longest available locale or pseudo-localization. If neither exists, use approximately 30% text expansion as a heuristic and label it as such.
- Verify mixed-direction content, truncation, wrapping, form validation, and icon direction when RTL support is relevant.
- Do not claim localization quality without review by an appropriate language or locale expert.

## 10. Performance and network resilience

Follow existing product performance budgets first.

If no budget exists and the interface is web-based, use these default field targets for key user journeys:

- Largest Contentful Paint: **≤ 2.5 seconds**;
- Interaction to Next Paint: **≤ 200 milliseconds**;
- Cumulative Layout Shift: **≤ 0.1**;
- evaluate at the 75th percentile, separated for mobile and desktop, when real-user data is available.

Do not present a local Lighthouse or lab result as field performance. Label lab and field measurements separately.

For network-dependent UI:

- provide an immediate response to user input;
- show an honest loading or pending state;
- prevent accidental duplicate submission;
- preserve entered data on recoverable failure;
- provide timeout, retry, offline, and partial-data behavior when relevant;
- avoid layout shifts caused by late content;
- test at least one throttled mobile-network profile for Scoped or Substantial asynchronous flows when tooling is available;
- do not block the primary task on decorative assets, analytics, or non-essential third-party code.

## 11. Content, errors, and destructive actions

- Use labels that name the user action or destination.
- Keep instructions adjacent to the decision they affect.
- Explain errors in plain language, identify the affected field or action, preserve user input, and state how to recover.
- Use an error summary when multiple errors or long forms make individual errors difficult to find.
- Distinguish empty, zero, unavailable, filtered-out, loading, and error states.
- For destructive actions, match the safeguard to severity and reversibility: clear naming, confirmation for high-risk actions, undo where useful, and a visible result.
- Do not use dark patterns, disguised advertisements, forced continuity, hidden costs, confirm-shaming, obstructive cancellation, or misleading defaults.
- Do not fabricate urgency, scarcity, social proof, activity, testimonials, or metrics.

## 12. Generic-output test

Before finalizing Scoped or Substantial work, inspect each major region.

Remove, replace, or justify:

- a layout that would work unchanged for an unrelated product;
- card, bento, dashboard, hero, sidebar, or tab patterns used without an information or task rationale;
- gradients, glass effects, glow, blobs, noise, oversized type, or motion with no defined function;
- excessive containers, rounded rectangles, badges, dividers, icons, or empty space;
- placeholder or decorative data presented as real;
- repeated visual emphasis that obscures priority;
- an icon without a clear label where the meaning is not universally understood;
- an illustration or animation that delays, shifts, or competes with the primary task;
- a custom interaction that is less understandable or accessible than a native pattern.

For every retained non-essential visual element, be able to complete this sentence:

> This element helps [user] to [understand, decide, navigate, act, recover, or recognize the product] by [specific mechanism].

If the sentence cannot be completed with product evidence or a clear rationale, simplify or remove the element.

## 13. Workflow

### Step 1: Classify

Determine:

- scope mode: Micro, Scoped, or Substantial;
- task type: Create, Reshape, Implement, Review, or Fix;
- affected user job and risk level;
- required evidence and verification depth.

Do not expand a Micro task into a review unless a blocker is directly caused or exposed by the requested change.

### Step 2: Inspect

For existing work, inspect the relevant:

- component and neighboring flow;
- design tokens and component primitives;
- content model and real states;
- responsive patterns and themes;
- accessibility implementation;
- tests, linting, type checks, build scripts, browser matrix, and performance budgets.

Prefer the smallest relevant inspection area first. Expand only when dependencies or user impact require it.

### Step 3: Establish evidence and acceptance criteria

For Scoped work, state the user job, affected states, and concrete acceptance criteria.

For Substantial work, add:

- evidence record;
- UX hypothesis and primary measure;
- guardrails;
- validation plan;
- technical quality targets.

Ask a question only when the missing answer would materially change product direction or create unsafe rework. Otherwise, proceed with a clearly labeled reversible assumption.

### Step 4: Define the solution

For Scoped or Substantial work, state briefly:

- hierarchy and interaction logic;
- components and tokens to reuse;
- new pattern only if existing primitives cannot express the need;
- relevant states and recovery behavior;
- responsive and accessibility behavior;
- optional signature element and its purpose.

A design thesis, when useful, must use this concrete form:

> For [user] doing [job], prioritize [information or action] through [structure or interaction], while avoiding [known risk or tradeoff].

Do not use a slogan as a design thesis.

### Step 5: Execute

- Use semantic, maintainable, project-native implementation.
- Prefer composition and existing primitives.
- Keep component APIs minimal, typed where applicable, and consistent with the repository.
- Preserve unrelated behavior and public APIs.
- Avoid unnecessary dependencies and animation.
- Include relevant states in the implementation, not only in the explanation.
- Use real supplied content or clearly marked placeholders; never invent production data.

### Step 6: Critique against acceptance criteria

Evaluate observable properties, not taste alone:

- Can the intended user identify and complete the primary task?
- Does information order match task order?
- Are labels and outcomes unambiguous?
- Are all relevant states recoverable?
- Is the interaction operable with relevant input methods?
- Do measurable accessibility thresholds pass?
- Does the layout survive required widths, zoom, long content, and localization?
- Does each major visual element pass the product-specific and removal tests?
- Has the change introduced inconsistency or unnecessary scope?

Change the work only when a material issue is found. If no material issue is found, record that no refinement was necessary.

### Step 7: Verify

Run the required checks for the selected scope. Do not replace a failed or unavailable check with a claim based on visual inspection.

Report each check as:

- **Passed:** executed and met the stated criterion;
- **Failed:** executed and did not meet it;
- **Not run:** unavailable, out of scope, or blocked, with the reason;
- **Not applicable:** the criterion does not apply, with a brief reason when unclear.

## 14. Verification matrix

### Required for every implementation change

- inspect the final diff for unintended scope;
- run the repository's closest relevant formatter, lint, type, test, and build commands when they exist;
- verify the requested behavior or visual change directly;
- verify that no supplied content or data was fabricated or altered unintentionally;
- report checks that could not be run.

### Additional requirements for Micro changes

Run only checks affected by the change:

- local component or page inspection;
- targeted test or story when available;
- contrast check when a foreground, background, border, state, or focus color changes;
- keyboard/focus check when an interactive control changes;
- smallest supported width when spacing, sizing, wrapping, or positioning changes.

A Micro change is complete without a broader redesign review when these checks pass and no blocker is exposed.

### Additional requirements for Scoped changes

- test default, loading, empty, error, success, disabled, permission, destructive, and long-content states that apply;
- test keyboard operation and visible focus for affected interactions;
- run an automated accessibility scan when tooling exists, then manually inspect affected semantics and focus behavior;
- test at 200% text zoom and at 320 CSS-pixel-equivalent reflow where applicable;
- test smallest, intermediate, and wide layouts;
- test touch target size for affected controls;
- test one throttled network condition when the flow is asynchronous;
- verify the complete affected task, not only isolated components.

### Additional requirements for Substantial changes

- complete all Scoped checks;
- test the primary task end to end;
- test the declared browser/platform matrix where tools are available;
- test localization expansion and RTL when relevant;
- measure or estimate performance against the declared budget, clearly distinguishing field data, lab data, and unmeasured risk;
- provide a representative-user or specialist validation plan when validation was not possible;
- review privacy, destructive actions, permissions, data loss, and recovery paths;
- review consistency across all newly introduced reusable patterns.

### Release blockers

Do not describe work as production-ready while any known blocker remains:

- a build, type, lint, or relevant test failure caused by the change;
- a keyboard trap or inaccessible primary task;
- missing accessible name, role, state, label, or error association on a core control;
- required text or controls unavailable at supported width, zoom, or text spacing;
- contrast below the declared minimum on essential content or controls;
- data loss, duplicate destructive submission, misleading outcome, or unrecoverable error in the affected flow;
- fabricated production content, metrics, research, or verification claims;
- a critical browser/platform failure inside the declared support matrix;
- an unresolved safety, legal, privacy, or security conflict exposed by the interface.

## 15. Examples

### Example A: Exact spacing fix

**Request:** “Change the gap between these two controls from 12px to 16px.”

**Bad:** Redesign the section, add cards, change typography, and introduce new tokens.

**Good:** Use Micro mode, confirm whether an existing spacing token equals 16px, change only the relevant declaration, inspect wrapping at the smallest supported width, and run the closest relevant check.

### Example B: Analytics overview

**Bad:** Create twelve interchangeable metric cards, decorative charts, and invented percentages because dashboards conventionally look that way.

**Good:** Start from the decisions the user must make. Use only supplied metrics. Group information by decision or workflow, show data freshness and unavailable states, provide a table or drill-down where exact values matter, and avoid a chart when comparison is clearer in text or a table.

### Example C: Form validation

**Bad:** Use placeholder-only labels, mark errors with a red border, clear the form after failure, and show “Something went wrong.”

**Good:** Use persistent labels, programmatically associated instructions and errors, a plain-language recovery message, preserved input, focus or an error summary for multiple failures, and a retry path for network errors.

### Example D: Brand color conflict

**Request:** “Use the light brand yellow for body text on white.”

**Bad:** Follow the color request even though the contrast fails, or silently replace the brand color with an unrelated color.

**Good:** Explain that the requested foreground use fails the accessibility minimum, retain the yellow for a compliant non-text accent or darker background treatment, and use an approved darker brand tone for text.

### Example E: Product-specific landing page

**Bad:** Add a generic oversized headline, gradient orb, three benefit cards, fake testimonials, and an animated product mock-up unrelated to the actual workflow.

**Good:** Use the product's real task, evidence, screenshots, or supplied content. Show the most important outcome and the path to it, use specific proof only when supplied, and keep any visual signature subordinate to comprehension and performance.

### Example F: Review with no necessary change

**Bad:** Change radius, color, or spacing merely because a review was requested.

**Good:** If the component meets the acceptance criteria and no material problem is found, report that no design change is recommended and list the checks performed.

## 16. Output contract

Match the response to the task.

### Design request

Provide:

- scope mode and known constraints;
- user job and evidence/assumptions;
- structure and interaction logic;
- relevant states, accessibility, responsiveness, and content behavior;
- success measure and validation plan for Substantial work;
- concise rationale tied to evidence.

### Implementation request

Make the change, then report:

- what changed and where;
- any assumptions or intentional deviations;
- checks run with Passed, Failed, Not run, or Not applicable status;
- remaining blockers or risks.

### Review request

Prioritize findings by user impact and confidence. For each finding include:

- observed evidence;
- affected user/task;
- concrete impact;
- severity;
- correction;
- verification method.

Separate verified defects from hypotheses and preferences.

### Prompt request

Produce a reusable prompt that includes:

- activation and scope limits;
- evidence and anti-fabrication rules;
- measurable accessibility and quality thresholds;
- required states and validation;
- product-specific and generic-output tests;
- verification reporting.

## 17. Completion criteria

Work is complete only when all applicable statements are true:

- the scope mode matches the size and risk of the task;
- the primary user job and expected outcome are explicit or clearly labeled as assumptions;
- material decisions are traceable to evidence, constraints, or a documented hypothesis;
- the information hierarchy and interaction sequence support the task;
- relevant states, recovery paths, and destructive outcomes are covered;
- existing components and conventions are reused, or deviations are justified;
- applicable WCAG 2.2 AA thresholds and platform accessibility requirements are met;
- required responsive, zoom, text-spacing, localization, browser, input, performance, and network checks are addressed;
- no production data, research, metrics, testimonials, or test results were fabricated;
- generic or decorative elements have a defined function or were removed;
- required verification passed, or the result is clearly marked as incomplete with blockers and unrun checks;
- no unnecessary change was introduced merely to satisfy the process.
