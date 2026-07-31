**English** · [Deutsch](README.de.md)

# AgentSkillForge

![AgentSkillForge banner](assets/github-banner.jpg)

[![Validate](https://github.com/RobinGru/AgentSkillForge/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/RobinGru/AgentSkillForge/actions/workflows/validate.yml)
[![Runtime evals](https://github.com/RobinGru/AgentSkillForge/actions/workflows/runtime-evals.yml/badge.svg?branch=main)](https://github.com/RobinGru/AgentSkillForge/actions/workflows/runtime-evals.yml)
[![CodeQL](https://github.com/RobinGru/AgentSkillForge/actions/workflows/codeql.yml/badge.svg?branch=main)](https://github.com/RobinGru/AgentSkillForge/actions/workflows/codeql.yml)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](pyproject.toml)

Reusable Agent Skills that help AI coding assistants make careful changes and explain their work clearly.

[Explore skills](#skill-catalog) · [Install with Zed or Codex](#quick-start) · [Contribute](CONTRIBUTING.md)

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

## Skill Catalog

Choose the skill that matches the task—not merely a word in the prompt.

| Skill | When to use it | Example |
|---|---|---|
| [`skills/project-discovery/`](skills/project-discovery/) | A new or unclear product needs users, outcomes, boundaries, and an initial capability map. | “Define the smallest useful first release for this product.” |
| [`skills/feature-specification/`](skills/feature-specification/) | One substantial capability needs observable rules, states, permissions, and acceptance criteria. | “Specify retry and denial behavior for file import.” |
| [`skills/solution-framing/`](skills/solution-framing/) | The direction is unclear or a decision has meaningful trade-offs. | “Which migration approach is safest?” |
| [`skills/safe-code-change/`](skills/safe-code-change/) | You need a small, understood change or bug fix. | “Fix this reproducible validation error.” |
| [`skills/fact-based-code-review/`](skills/fact-based-code-review/) | A change is ready for review and needs a fact-based assessment. | “Review this pull request before merging.” |
| [`skills/adversarial-deep-review/`](skills/adversarial-deep-review/) | An explicitly requested deep review of a concrete high-risk change needs evidence-backed stress scenarios. | “Adversarially review this payment retry diff.” |
| [`skills/product-interface-engineering/`](skills/product-interface-engineering/) | A screen, form, interaction, accessibility, or responsive behavior needs work. | “Make this checkout form usable on mobile.” |
| [`skills/performance-investigation/`](skills/performance-investigation/) | You have a measured latency, throughput, or memory problem to investigate. | “Why did this endpoint become slower?” |
| [`skills/vue-sfc-decomposition/`](skills/vue-sfc-decomposition/) | A Vue or Nuxt component needs to be split without changing behavior. | “Separate this large Vue SFC into maintainable parts.” |
| [`skills/failure-investigation/`](skills/failure-investigation/) | A non-performance test, build, runtime, integration, or data failure has an unknown cause or safe change boundary. | “Find why this integration fails before proposing a fix.” |
| [`skills/security-boundary-analysis/`](skills/security-boundary-analysis/) | An explicit security or threat-modeling task needs trust transitions, abuse paths, controls, and residual uncertainty. | “Threat-model this webhook ingestion boundary.” |
| [`skills/compatibility-migration/`](skills/compatibility-migration/) | An agreed direction requires old and new behavior to coexist safely across multiple steps or consumers. | “Plan a compatible multi-release API migration.” |
| [`skills/session-handoff/`](skills/session-handoff/) | Unfinished repository work must be resumed by another session or developer from verified local state. | “Record the current worktree and the one safe next action.” |

Read a skill’s `SKILL.md` before using it. Keep its complete directory, including any `references/` and `assets/`, because the skill may link to them.

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

Copy or reference the desired `skills/<name>/` directory using your client’s documented mechanism. AgentSkillForge does not claim a universal install path or automatic-discovery convention.

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

- New product: `project-discovery` establishes the product boundary and capability map, then `feature-specification` defines one capability before technical planning or implementation.

- Unknown non-performance failure: `failure-investigation` establishes a supported cause and safe change boundary, then `safe-code-change` implements the fix, and `fact-based-code-review` reviews it.
- Measured latency, throughput, memory, or resource problem: use `performance-investigation`, not `failure-investigation`; hand an understood change to `safe-code-change`, then use `fact-based-code-review`.
- Multi-step migration: `solution-framing` chooses the direction only when it is still open, `compatibility-migration` defines safe coexistence and retirement states, and `safe-code-change` implements each local step.
- Explicit threat model: `security-boundary-analysis` defines trust transitions, abuse paths, and control obligations. Follow with `solution-framing` for architecture choices, `product-interface-engineering` for visible permission or recovery interactions, or `compatibility-migration` for staged coexistence; keep each output separate.
- High-risk change: use `adversarial-deep-review` only for an explicit deep assessment of a concrete change, then hand its evidence to `fact-based-code-review` for the merge decision.

Your AI client decides when to load an installed skill. Descriptions are routing guidance, not guaranteed host behavior. Static and runtime-contract checks provide bounded evidence only; do not infer universal portability or reliable automatic activation from installation alone. See the [compatibility matrix](docs/compatibility.md).

## Optional repository instructions

[`templates/AGENTS.md`](templates/AGENTS.md) is an opinionated repository-root template that routes work across this catalog and defines a compact write-then-verify rule. Copy it to a target repository only when German responses and `codebase-memory-mcp` are intended; otherwise adapt or remove those requirements first. Project-specific rules should be added in the copied file, not in the distributed skills.

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
python scripts/run_runtime_evals.py --client fixture --fixture-response "Behavior contract. Verification plan. Baseline evidence and hypothesis experiment. Finding and verification gap. Trust boundary and abuse path threat."
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
├── templates/AGENTS.md         # Optional repository instructions
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
