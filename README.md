**English** · [Deutsch](README.de.md)

# AgentSkillForge

![AgentSkillForge banner](assets/github-banner.jpg)

[![Validate](https://github.com/RobinGru/AgentSkillForge/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/RobinGru/AgentSkillForge/actions/workflows/validate.yml)
[![Runtime evals](https://github.com/RobinGru/AgentSkillForge/actions/workflows/runtime-evals.yml/badge.svg?branch=main)](https://github.com/RobinGru/AgentSkillForge/actions/workflows/runtime-evals.yml)
[![CodeQL](https://github.com/RobinGru/AgentSkillForge/actions/workflows/codeql.yml/badge.svg?branch=main)](https://github.com/RobinGru/AgentSkillForge/actions/workflows/codeql.yml)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](pyproject.toml)

Reusable Agent Skills that help AI coding assistants make careful changes and explain their work clearly.

[Explore skills](#skill-catalog) · [Install with Zed or Codex](#quick-start) · [Use the all-in-one template](#all-in-one-project-guidance) · [Contribute](CONTRIBUTING.md)

> [!NOTE]
> Static repository checks run for every pull request. Deterministic runtime-contract checks exercise the eval runner, while authenticated Codex smoke tests and Zed interactive checks are opt-in release evidence. See the [compatibility and maintenance policy](docs/compatibility.md) for the supported-client matrix and its explicit limits.

## What is AgentSkillForge?

AgentSkillForge is a collection of small, reusable Agent Skills for AI coding assistants. Each skill describes a task type, the facts to gather, the decisions to make, and how to report the result.

Agent Skills are plain Markdown directories centred on `SKILL.md`, so they are not tied to a single client. This repository provides documented installers for Zed and Codex; other clients need their own documented way to load compatible skill directories.

## Why use it?

- **Focused guidance:** Choose a skill for the task instead of using one generic workflow.
- **Facts before assumptions:** Skills distinguish observed facts, inferences, and checks that were not run.
- **Portable Agent Skills:** Copy a complete skill directory to a compatible client without a required Python runtime.
- **Checked distribution:** Repository automation validates structure, links, tests, static eval cases, and package contents.

## All-in-one project guidance

Don't want to choose among many skills or deal with a complex installation? Use [`templates/AGENTS-AIO.md`](templates/AGENTS-AIO.md), the compact all-in-one option.

Copy it into your project root as `AGENTS.md`. It provides general guidance for product fit, accessibility, security, verification, and review priorities without requiring a particular agent client.

```sh
cp templates/AGENTS-AIO.md /path/to/your-project/AGENTS.md
```

Add project-specific rules to the copied template, not to the distributed skills.

## Skill Catalog

Start with the sentence that best describes your task. The second column tells you when to pick a skill. The last column tells you when another skill is a better fit. You do not need to understand every technical term to make a good first choice.

> **Source layout vs. installation:** The categories only organize this repository. After installation, every skill is directly in `<target>/<skill-name>/`.

### Core workflow

Use these skills for everyday repository work: getting to know a project, making a small change, saving useful knowledge, or continuing interrupted work.

| Skill | Use it when | Use a different skill when |
|---|---|---|
| [`repository-onboarding`](skills/core/repository-onboarding/) | You need to understand an unfamiliar project before making bigger changes. | You first need to find out what the product should do (`project-discovery`), or you are investigating a broken feature (`failure-investigation`). |
| [`repository-knowledge-curation`](skills/core/repository-knowledge-curation/) | You have confirmed a useful fact about the repository and want to save it in the right place. | The information is only a guess, temporary, or still needs a decision. |
| [`safe-code-change`](skills/core/safe-code-change/) | You know what should change and where to change it safely. | You do not yet know why something is broken (`failure-investigation`), or old and new versions must work together during a rollout (`compatibility-migration`). |
| [`session-handoff`](skills/core/session-handoff/) | You need to leave clear notes so someone can safely continue unfinished work. | You need to track a larger feature over several sessions (`feature-lifecycle`). |

### Planning and coordination

Use these skills before coding when you need to decide what to build, how it should work, or how to deliver a larger change safely.

| Skill | Use it when | Use a different skill when |
|---|---|---|
| [`project-discovery`](skills/planning/project-discovery/) | The product is new or unclear: you do not yet know the users, goals, or first useful version. | You already know the product goal and need to describe one feature in detail (`feature-specification`). |
| [`feature-specification`](skills/planning/feature-specification/) | A planned feature needs clear rules: what users can do, what happens in each situation, and how to tell it works. | You still need to decide what the product should achieve (`project-discovery`) or how to build it (`solution-framing`). |
| [`solution-framing`](skills/planning/solution-framing/) | You know the goal but must choose an important technical approach. | The approach is already chosen and old and new versions must work side by side (`compatibility-migration`). |
| [`compatibility-migration`](skills/planning/compatibility-migration/) | You are changing an API, data format, or system and old and new versions must work together for a while. | You still need to choose the overall approach (`solution-framing`) or only need to make one safe local change (`safe-code-change`). |
| [`feature-lifecycle`](skills/planning/feature-lifecycle/) | A larger feature needs one short, up-to-date record across several sessions or people. | You only need to hand over unfinished work once (`session-handoff`). |

### Quality, investigation, and review

Use these skills to understand a problem, measure performance, check security risks, or review a finished change. They help you gather facts before deciding what to do next.

| Skill | Use it when | Use a different skill when |
|---|---|---|
| [`failure-investigation`](skills/quality/failure-investigation/) | Something is broken and you do not know why. | The problem is speed, memory use, or resource use (`performance-investigation`). Once you know the fix, use `safe-code-change`. |
| [`performance-investigation`](skills/quality/performance-investigation/) | The application is too slow or uses too much memory or other resources, and you can measure it. | You are investigating another kind of failure (`failure-investigation`). If you only hear “make it faster,” measure first. |
| [`security-boundary-analysis`](skills/quality/security-boundary-analysis/) | You need to check who can access what, how an attacker could misuse it, and which protections are needed. | You only need a normal review of code changes (`fact-based-code-review`). |
| [`fact-based-code-review`](skills/quality/fact-based-code-review/) | You want a practical review of a concrete set of code changes before merging. | You explicitly need an especially tough review of a high-risk change (`adversarial-deep-review`). |
| [`adversarial-deep-review`](skills/quality/adversarial-deep-review/) | You explicitly need to challenge a risky change: failures, misuse, recovery, parallel work, and operations. | You need the normal merge review (`fact-based-code-review`); use this skill to add risk findings to that review. |

### Specialized engineering

Use these skills when the task is specifically about a user interface or a Vue/Nuxt component.

| Skill | Use it when | Use a different skill when |
|---|---|---|
| [`product-interface-engineering`](skills/specialized/product-interface-engineering/) | You change something users see or use: a page, form, navigation, error message, accessibility behavior, or mobile layout. | The work is only on the backend, or you are reorganizing code without changing what users experience. |
| [`vue-sfc-decomposition`](skills/specialized/vue-sfc-decomposition/) | A Vue or Nuxt component has become hard to maintain and can be split into clear smaller responsibilities. | You are changing what users see or how the interface behaves (`product-interface-engineering`). |

Read a skill’s `SKILL.md` before using it. Keep the whole skill directory, including `references/` and `assets/`, because the skill may link to them.

## Quick Start

Install Git and Python 3.11 or newer before using an installer. The Zed and Codex wrappers both install all skills into the shared `~/.agents/skills` directory.

<details>
<summary>macOS, Linux, or WSL</summary>

```sh
git clone https://github.com/RobinGru/AgentSkillForge.git AgentSkillForge
cd AgentSkillForge
python3 scripts/install_zed_skills.py  # or: scripts/install_codex_skills.py
```

</details>

<details>
<summary>Windows PowerShell</summary>

```powershell
git clone https://github.com/RobinGru/AgentSkillForge.git AgentSkillForge
cd AgentSkillForge
py scripts\install_zed_skills.py  # or: scripts\install_codex_skills.py
```

</details>

Start a new agent session after installation. The installer stops rather than replacing an existing skill directory.

## Installation

### Portable core

Copy or reference the desired categorized source directory using your client’s documented mechanism. AgentSkillForge does not claim a universal install path or automatic-discovery convention.

### Flat ZIP bundle

Build a manually installable bundle from a source checkout:

```sh
python3 scripts/build_skill_bundle.py
```

It creates `dist/agent-skill-forge-skills.zip`. Extract its contents directly into your client skill directory, such as `~/.agents/skills`; each top-level directory is one complete skill. Do not copy the categorized `core/`, `planning/`, `quality/`, or `specialized/` source directories into that target.

### Zed and Codex

Use the client wrapper to install only one skill when you do not need the full catalog:

```sh
python3 scripts/install_zed_skills.py --skill performance-investigation
python3 scripts/install_codex_skills.py --skill performance-investigation
```

Both wrappers delegate to the same installer and default to `~/.agents/skills`. Repeat `--skill` to install several skills. Use `--target` to install into another client or repository skill directory.

> [!CAUTION]
> `--force` deletes and recreates every selected target directory. Review local edits first; the installer does not merge files.

See the complete [Zed](docs/clients/zed.md) and [Codex](docs/clients/codex.md) installation guides for selected skills, custom targets, updates, verification, and uninstallation.

## Using skills together

Common sequences are:

- Unfamiliar repository: `repository-onboarding` establishes a technical working map before substantial work; hand verified reusable facts to `repository-knowledge-curation` when they need a canonical durable home.
- New product: `project-discovery` establishes the product boundary and capability map, then `feature-specification` defines one capability before technical planning or implementation.
- Multi-session feature delivery: `feature-specification` owns the behavior contract; use `solution-framing` for consequential technical choices, `feature-lifecycle` for the durable revision-bound record, `safe-code-change` for each bounded work unit, and `session-handoff` only when unfinished concrete work must be resumed.

- Unknown non-performance failure: `failure-investigation` establishes a supported cause and safe change boundary, then `safe-code-change` implements the fix, and `fact-based-code-review` reviews it.
- Measured latency, throughput, memory, or resource problem: use `performance-investigation`, not `failure-investigation`; hand an understood change to `safe-code-change`, then use `fact-based-code-review`.
- Multi-step migration: `solution-framing` chooses the direction only when it is still open, `compatibility-migration` defines authoritative coexistence and retirement states, `feature-lifecycle` may link their feature-level evidence, and `safe-code-change` implements each local step.
- Explicit threat model: `security-boundary-analysis` defines trust transitions, abuse paths, and control obligations. Follow with `solution-framing` for architecture choices, `product-interface-engineering` for visible permission or recovery interactions, or `compatibility-migration` for staged coexistence; keep each output separate.
- High-risk change: use `adversarial-deep-review` only for an explicit deep assessment of a concrete change, then hand its evidence to `fact-based-code-review` for the sole merge decision. A tracked feature may link the resulting evidence in `feature-lifecycle` without transferring either review responsibility.

Your AI client decides when to load an installed skill. Descriptions are routing guidance, not guaranteed host behavior. Static and runtime-contract checks provide bounded evidence only; do not infer universal portability or reliable automatic activation from installation alone. See the [compatibility matrix](docs/compatibility.md).

## Optional repository instructions

[`templates/AGENTS.md`](templates/AGENTS.md) is an opinionated routing template for this catalog with a compact write-then-verify rule. Copy it only when German responses and `codebase-memory-mcp` are intended; otherwise adapt or remove those requirements first.


## Compatibility

| Area | Supported or required |
|---|---|
| Agent Skill format | Markdown `SKILL.md` directories with relative local references |
| Agent clients | Supported: Codex CLI and Zed, subject to the documented evidence level; other compatible clients are unverified |
| Documented integration | Zed with agent skills enabled; Codex CLI and Codex IDE extension; see [compatibility policy](docs/compatibility.md) |
| Python | 3.11 or newer for the Zed/Codex installers, packaging, and repository checks |
| Package runtime | No importable Python module; the wheel distributes Agent Skills and support files as data |

The skill documents themselves do not require Python. Python is used by the installer and repository tooling.

## Quality and development

The **Validate** workflow runs the repository checks below. **CodeQL** analyzes the Python tooling for supported security issues.

```sh
python -m pip install -e ".[dev]"
python scripts/validate_repository.py
python scripts/check_links.py
pytest
python scripts/run_evals.py
python scripts/run_runtime_evals.py --client fixture --fixture-response "Behavior contract. Scope, interaction state, validation error, and verification plan. Baseline evidence and hypothesis experiment. Finding and verification gap. Trust boundary and abuse path threat. Observed revision in the canonical record and next safe action. Repository identity, structure and boundaries, discovered command, and verification model. Knowledge candidate and placement decision."
python scripts/check_distribution.py
```

These commands validate skill metadata and layout, local Markdown links, installer and packaging behavior, static eval-manifest and runtime-contract declarations, deterministic contract execution, and distributed wheel contents.

> [!NOTE]
> The `fixture` client tests the runtime-eval mechanism without executing an agent. Authenticated Codex model execution is an explicit release check, not a pull-request gate. Its invocation, output artifact, client/model version, privacy implications, and limits are documented in the [compatibility policy](docs/compatibility.md). Check external HTTP links explicitly with `python scripts/check_links.py --external`.

<details>
<summary>Project structure</summary>

```text
.
├── skills/                     # Portable Agent Skills
├── evals/                      # Static cases, runtime contracts, client matrix, and tests
├── scripts/                    # Validation, runtime eval, packaging, and installer tools
├── docs/                       # Client guides and compatibility policy
├── templates/                  # Optional repository instruction templates
│   ├── AGENTS.md               # German skill routing and verification
│   └── AGENTS-AIO.md           # General all-in-one quality guidance
├── .github/workflows/          # Automation workflows
├── CONTRIBUTING.md             # Contribution and clean-room rules
├── pyproject.toml              # Python tooling and package metadata
├── README.md                   # English documentation
├── README.de.md                # German documentation
└── LICENSE                     # Apache License 2.0
```

The Python wheel is a data distribution, not an application or importable SDK. It places the README, Agent Skills, references, client guides, and installers below `share/agent-skill-forge/`.

</details>

## Contributing

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. New or changed skill behavior must preserve portable metadata and valid local references, follow the clean-room process, and update the relevant evals and output-contract checks.

## Security and support

Treat third-party skills as untrusted instructions. Inspect their content, provenance, links, and dependencies before installation. Do not grant tools, credentials, or filesystem access solely because a skill document requests them.

Report potential security vulnerabilities through GitHub’s private vulnerability reporting. Do not publish sensitive details in a public issue. Use [GitHub Issues](https://github.com/RobinGru/AgentSkillForge/issues) for public bug reports and questions.

## License and notices

AgentSkillForge is distributed under the [Apache License 2.0](LICENSE). Review [NOTICE](NOTICE) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) before redistribution.
