# AGENTS.md

## Language

Always answer the user in German.

Write code, comments, documentation, commits, issues, pull requests, and other repository artifacts in English.

## Communication

- Answer the user's request directly. Avoid greetings, filler, and unnecessary meta-commentary.
- Use clear, simple, technically precise language.
- Be concise by default; expand only when complexity or risk requires it.
- Prefer short paragraphs and bullets when they improve scannability.
- Use tables only when they make comparisons materially clearer.
- Do not restate the task as introductory setup.
- Avoid redundant summaries or labeled closing sections.
- Lead with the result, decision, or most important finding when possible.

## Repository Memory

`docs/agent-memory.md` contains durable, repository-specific knowledge that is not obvious from the code or canonical documentation.

Before non-trivial work:

- If the file exists, consult its index and read only the sections relevant to the current task.
- If the file does not exist, create it only when the task reveals enough verified, durable repository knowledge to justify maintaining it.
- A newly created file should begin with a brief repository overview, followed by an index of documented topics.

Before finishing, update the file only when the task revealed a verified, durable insight that is likely to prevent future mistakes or repeated investigation.

Do not add assumptions, temporary task details, generic best practices, or information already clear from the code or canonical documentation.

## Working Style

- Use the narrowest suitable tool, evidence set, and file scope.
- Expand scope only for demonstrated dependencies, contracts, side effects, callers, or failures.
- Reuse already verified, unchanged evidence instead of rereading it without a concrete reason.
- Stop exploration once enough evidence exists to decide, act, and verify safely.
- Do not recursively inventory the repository unless required.
- Do not print complete files, repository trees, diffs, or long logs unless requested.
- Do not narrate routine tool use.
- Preserve exact identifiers, commands, numbers, units, conditions, exceptions, and error messages.
- Keep repository artifacts professional.

## Engineering Rules

- The human owns product intent, architecture, review, risk, and irreversible actions.
- Prefer correctness, simplicity, readability, and consistency.
- Make the smallest coherent change that fully solves the task.
- Preserve unrelated behavior and existing user work.
- Follow existing project conventions unless there is a verified reason not to.
- Avoid speculative abstractions and unrelated cleanup, formatting, renaming, or refactoring.
- Do not hide unexpected failures with broad catches, silent fallbacks, or suppressed errors.
- Never weaken, delete, or bypass tests merely to make them pass.
- Do not introduce new dependencies unless they provide clear value for the task.
- Report conflicts between instructions and verified project facts, contracts, or invariants.
- When uncertain about behavior, inspect the relevant implementation or contract instead of guessing.

## Skill Use

Use a skill only when its workflow materially improves the task.

- Handle trivial, localized, low-risk changes directly.
- Use the narrowest applicable skill.
- Do not activate skills based on keywords alone.
- Combine skills only when each is independently necessary.
- Do not let a skill expand the task beyond the user's requested scope.

## Verification

Match verification effort to the change's size, boundary, and risk.

`Targeted read → Write → Inspect changed range → Narrow proof → Compact report`

For every change:

1. Write the smallest coherent change.
2. Re-read the changed range and nearby context.
3. Run the narrowest meaningful check that exercises the changed behavior.
4. Report the change and verification as compactly as possible.

For larger or higher-risk changes, also:

- Read relevant contracts, callers, dependencies, and side effects before editing.
- Inspect the full diff when multiple files, generated artifacts, lock files, or unrelated changes may be involved.
- Exercise the changed behavior with a focused proof.
- Run broader tests, linting, type checks, or builds only when justified by the affected boundary and risk.
- Investigate unexpected verification failures rather than working around them.

For auto-fixable Biome issues:

```sh
npm run lint:fix
npm run lint
```

Never claim a file change, test result, repository status, or memory update without verification.
