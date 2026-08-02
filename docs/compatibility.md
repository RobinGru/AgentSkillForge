# Compatibility and maintenance policy

AgentSkillForge distributes portable Markdown skill directories. Portability means
that distributed skills avoid required client-specific metadata, commands, and
runtime dependencies. It does not mean every agent client or model will load or
route a skill identically.

## Support matrix

| Client | Support level | Evidence | Release expectation |
|---|---|---|---|
| Codex CLI | Supported when its configured version accepts `SKILL.md` directories | Installer tests; opt-in command smoke evals | Run the command smoke suite when credentials and a pinned CLI/model are available. |
| Zed | Supported for directory installation and interactive use | Installer tests; manual release smoke checklist | Complete the checklist below for a release that changes skills or client installation. |
| Other compatible clients | Community / unverified | Portable-package validation only | Document an adapter and add coverage before calling the client supported. |

The matrix applies to the current client versions configured by a release
operator. Client and model versions must be recorded with any runtime-eval
artifact; this repository does not claim compatibility with future versions.

## Checks

The repository has independent evidence layers:

1. **Static package checks** validate metadata, skill structure, links, wheel
   contents, installation, and eval declarations on every pull request.
2. **Deterministic runtime-contract checks** use the `fixture` client to prove
   that the contract runner and its assertions work. They do not execute a
   model.
3. **Codex command smoke checks** execute only when a release operator provides
   an authenticated Codex CLI environment and explicitly enables them with
   `AGENT_SKILLS_RUNTIME_EVALS=1`.
4. **Zed manual smoke checks** cover discovery and interactive use until Zed
   offers a stable headless agent interface suitable for automation.

A pass means only the declared response-contract assertions passed for the
recorded client, model, and prompt run. Routing is assessed separately only when
the client supplies reliable selected-skill metadata; otherwise it is reported
as not available. A pass does not prove semantic correctness or behavior for
clients or models outside that record.

## Run the command smoke suite

Install the project's development dependencies, make an authenticated `codex`
CLI available, then run:

```sh
AGENT_SKILLS_RUNTIME_EVALS=1 \
python scripts/run_runtime_evals.py \
  --client codex-cli \
  --client-version "$(codex --version)" \
  --model "<configured-model-id>" \
  --output artifacts/runtime-evals/codex-cli.json
```

Before each case, the adapter copies all skills to an isolated
`.agents/skills` directory in its temporary workspace. It then sends each prompt
to the configured client command and evaluates only the required and prohibited
regular-expression response contracts in `evals/runtime.yaml`. Its current
adapter does not provide selected-skill metadata, so routing is reported as not
available. The Codex adapter requires
a recorded client version and model identifier. Preserve the resulting JSON
artifact with the release record. The report contains the executed command and
response, so review it for sensitive data before publishing it.

`evals/clients.yaml` is the client-adapter registry. A command adapter receives
`{prompt}`, `{prompt_file}`, and `{response_file}` substitutions. It is executed
without a shell. Add a new client only with a documented, stable invocation and
a testable result channel. `manual-smoke` entries intentionally cannot be run by
the command runner.

## Zed release smoke checklist

1. Install skills into an empty temporary target with
   `python scripts/install_zed_skills.py --target <target>`.
2. Configure Zed to use that exact target and start a new agent session.
3. Confirm a skill directory, its `SKILL.md`, and linked `references/` or
   `assets/` files are visible to the client.
4. Run one positive prompt and one boundary prompt from `evals/runtime.yaml`.
5. Record the Zed version, configured model, date, prompts, and observed
   outcome in the release notes or attached release artifact.
6. Treat missing discovery, unreadable references, or an incorrect explicit
   invocation as a release blocker. Record ambiguous automatic routing as a
   compatibility limitation, not a passing result.

## Maintenance cadence

- Run static checks for every pull request.
- Run deterministic contract tests for every pull request.
- Run the Codex smoke suite before releases when the required credentials are
  available; otherwise document it as not run.
- Complete the Zed checklist for releases that change skill content, packaging,
  installation, or compatibility claims.
- Re-run relevant client checks after a documented client or model version
  change, and update this matrix if support changes.
