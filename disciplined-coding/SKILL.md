---

name: disciplined-coding
description: Use when modifying code, fixing bugs, refactoring, implementing features, or reviewing completed coding work. Enforces evidence-based work, minimal diffs, systematic debugging, verification, and no guessing.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Disciplined Coding

Use this skill whenever code will be changed, debugged, refactored, or reviewed.

The goal is to make correct, small, evidence-based changes without guessing, overengineering, or touching unrelated code.

## Core Principles

* Evidence first: do not guess when facts can be checked.
* Read before editing: inspect relevant files, tests, configs, logs, and documentation before making changes.
* Smallest safe change: prefer focused, minimal diffs over broad rewrites.
* Follow the project: match existing architecture, naming, style, and conventions.
* Preserve behavior: do not change public APIs or existing behavior unless the task requires it.
* Verify before finishing: run the most relevant practical checks before declaring completion.
* Report honestly: clearly separate evidence, assumptions, conclusions, skipped checks, and remaining risks.

## No-Guessing Rules

When information is missing, do not invent it.

* If a fact can be checked in the repository, tools, logs, tests, documentation, or available context, check it before acting.
* Do not present unverified assumptions as facts.
* Do not apply speculative fixes without confirming the likely cause.
* Do not assume commands, APIs, file locations, configuration, business rules, or user intent when they can be discovered.
* If uncertainty remains after reasonable investigation, state the uncertainty explicitly and choose the safest limited action.
* Ask the user only when the missing information cannot be reasonably discovered from the available context.

## Workflow

### 1. Understand the Task

Before making changes:

* Identify the requested outcome.
* Determine whether the task is a feature, bugfix, refactor, cleanup, or review.
* Read the relevant source files, tests, configs, docs, and recent surrounding code.
* Find the nearest existing pattern before creating a new one.
* Identify constraints such as public APIs, compatibility, performance, security, data safety, and style conventions.

Do not edit until the relevant context has been inspected.

### 2. Establish Evidence

For bugs, failing tests, crashes, regressions, flaky behavior, or unexpected output:

* Locate the exact failure: error message, failing test, stack trace, log entry, incorrect output, or reproduction steps.
* Identify the smallest relevant code path.
* Reproduce the issue when practical.
* Form one hypothesis at a time.
* Confirm or disprove the hypothesis using code, tests, logs, or runtime behavior before changing code.
* Fix the root cause rather than masking the symptom.

For features, refactors, or cleanups:

* Identify the existing implementation style.
* Locate similar behavior and reuse the established pattern where appropriate.
* Confirm expected inputs, outputs, side effects, and error behavior.
* Determine whether tests, docs, types, or configuration need to change.

### 3. Plan the Smallest Useful Change

Before editing:

* Choose the smallest change that solves the task safely.
* Keep the diff focused on the requested outcome.
* Avoid unrelated refactors, formatting churn, renames, or reorganizations.
* Avoid new dependencies unless they are necessary and clearly justified.
* Avoid public API changes unless required.
* Consider edge cases, error paths, backward compatibility, security, and data integrity.

If the change is risky, reduce scope where possible and note the risk clearly.

### 4. Implement Carefully

While editing:

* Match existing code style, naming, structure, and abstractions.
* Keep behavior unchanged except where the task intentionally changes it.
* Handle relevant edge cases and error paths.
* Prefer clear, direct code over unnecessary abstraction.
* Do not remove or weaken tests, validation, error handling, security checks, or type checks to make the change pass.
* Do not hide errors unless graceful degradation is explicitly required.
* Do not introduce secrets, credentials, tokens, unsafe logging, or sensitive data exposure.

### 5. Verify

After editing, run the strongest relevant checks that are practical.

Prefer this order:

1. The previously failing test, command, or reproduction case
2. The nearest targeted test
3. Typecheck or lint
4. Build
5. Broader test suite

When updating behavior, add or update a regression check when practical.

If automated verification is not available, perform the strongest practical manual check.

If verification cannot be run, state:

* what was not run
* why it was not run
* what should be checked next

### 6. Review Before Finishing

Before declaring completion, review the change as if reviewing a pull request.

Check:

* Does the change solve the requested problem?
* Is the diff focused and minimal?
* Are unrelated changes avoided?
* Are existing conventions followed?
* Are edge cases and error paths handled?
* Are tests, types, lint, build, or manual checks updated or run where relevant?
* Are docs updated if behavior, usage, or configuration changed?
* Are security, privacy, data integrity, and compatibility risks considered?
* Are assumptions, skipped checks, and remaining risks clearly reported?

Do not call the work complete if a known serious issue remains unmentioned.

## Final Response Format

When finished, respond briefly with:

1. What changed
2. How it was verified
3. Assumptions, skipped checks, or remaining risks

Keep the final response concise, specific, and evidence-based.
