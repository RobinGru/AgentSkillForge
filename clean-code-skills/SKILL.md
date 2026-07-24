---
name: clean-code-skills
description: Use when writing, reviewing, or refactoring code to make it readable, maintainable, simple, testable, and easy to change.
disable-model-invocation: false
---

---
name: clean-code-skills
description: Use when writing, reviewing, or refactoring code to make it readable, maintainable, simple, testable, and easy to change.
---

# Maintainable Code Skill

## Goal

Produce code that is easy to read, easy to change, easy to test, and hard to misuse.

Prefer small, clear improvements over large rewrites. Preserve existing behavior unless the user explicitly asks for behavior changes.

## Core Principles

1. Make intent obvious.
2. Keep functions small and focused.
3. Use descriptive names.
4. Reduce nesting and branching.
5. Remove duplication.
6. Separate responsibilities.
7. Keep error handling explicit.
8. Prefer simple code over clever code.
9. Add tests for changed behavior.
10. Leave the code cleaner than before.

## When Writing Code

Before coding:

- Identify the smallest useful change.
- Reuse existing patterns in the project.
- Avoid introducing new abstractions unless they clearly reduce complexity.
- Do not change public APIs unless required.

While coding:

- Use meaningful names for variables, functions, classes, and files.
- Keep each function responsible for one clear task.
- Extract helper functions when a block has a clear separate purpose.
- Replace deeply nested logic with guard clauses where appropriate.
- Prefer straightforward control flow.
- Avoid hidden side effects.
- Avoid premature optimization.
- Keep comments rare and useful: explain why, not what.

After coding:

- Check whether the code is easier to read than before.
- Check whether edge cases are handled.
- Check whether tests should be added or updated.
- Mention any tradeoffs or assumptions.

## When Reviewing Code

Review for:

### Critical Issues

- Bugs or behavior changes
- Security risks
- Data loss risks
- Broken error handling
- Missing validation
- Race conditions or unsafe concurrency

### Maintainability Issues

- Unclear names
- Long functions or classes
- Too much nesting
- Duplicated logic
- Mixed responsibilities
- Hidden dependencies
- Overly clever abstractions
- Dead code
- Inconsistent style

### Test Issues

- Missing tests for changed behavior
- No boundary-case tests
- Tests that depend on implementation details
- Flaky or slow tests
- Unclear test names

## Refactoring Rules

When refactoring, follow this order:

1. Preserve behavior.
2. Add or identify tests if possible.
3. Rename unclear symbols.
4. Extract small helper functions.
5. Reduce nesting.
6. Remove duplication.
7. Simplify interfaces.
8. Delete unused code.
9. Re-run or suggest relevant tests.

Do not refactor unrelated areas unless they block the requested change.

## Output Format

When reviewing or refactoring, respond with:

### Summary

Briefly explain the main maintainability problem.

### Suggested Changes

List concrete changes, ordered by impact.

### Refactored Code

Provide the improved code when useful.

### Why This Is Better

Explain how the change improves readability, maintainability, testability, or safety.

### Tests

Mention tests added, tests to run, or missing test coverage.

## Style Preferences

- Prefer clear names over comments.
- Prefer composition over large inheritance hierarchies.
- Prefer explicit dependencies over global state.
- Prefer guard clauses over deeply nested `if` blocks.
- Prefer boring, predictable code.
- Avoid unnecessary frameworks, patterns, or abstractions.

## Constraints

- Do not invent requirements.
- Do not silently change behavior.
- Do not remove error handling.
- Do not ignore existing style.
- Do not produce huge rewrites when a small change is enough.
- If unsure, state the assumption and choose the safest minimal change.
