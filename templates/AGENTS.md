# AGENTS.md

## Language

Always answer the user in German. Be concise and explicit.

## Before acting

1. Inspect the repository, relevant files, current diff, and tests.
2. Use `codebase-memory-mcp` for structure, symbols, dependencies, decisions, and known risks.
3. Verify critical MCP findings in current files.
4. Select the smallest applicable skill.

## Skill routing

- unclear project goal → `project-discovery`
- non-trivial feature without clear behavior → `feature-specification`
- substantial feature needing durable revision-bound coordination → `feature-lifecycle`
- unclear technical direction → `solution-framing`
- unknown failure cause → `failure-investigation`
- small understood change → `safe-code-change`
- UI or accessibility work → `product-interface-engineering`
- large Vue or Nuxt component decomposition → `vue-sfc-decomposition`
- measured performance issue → `performance-investigation`
- staged migration → `compatibility-migration`
- explicit threat model → `security-boundary-analysis`
- concrete diff or PR review → `fact-based-code-review`
- explicit deep review of a concrete high-risk change → `adversarial-deep-review`
- unfinished work that another session must resume → `session-handoff`

For trivial, low-risk edits, work directly without creating extra process.

## Engineering rules

- Human owns product intent, architecture, review, risk, and irreversible actions.
- Prefer correctness, simplicity, readability, and consistency.
- No speculative abstractions.
- Make the smallest coherent local change.
- Do not hide unexpected failures with broad catches or silent fallbacks.
- Never weaken tests just to make them pass.
- If instructions conflict with project facts or invariants, report the conflict.

## Write-Then-Verify

For every durable change:

`Read → Write → Re-read → Inspect diff → Run direct proof → Report`

Never claim a file, test, status, or memory update without verification.
