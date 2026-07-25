**English** · [Deutsch](README.de.md)

# AgentSkillForge

[![Validate](https://github.com/RobinGru/AgentSkillForge/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/RobinGru/AgentSkillForge/actions/workflows/validate.yml)
[![CodeQL](https://github.com/RobinGru/AgentSkillForge/actions/workflows/codeql.yml/badge.svg?branch=main)](https://github.com/RobinGru/AgentSkillForge/actions/workflows/codeql.yml)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](pyproject.toml)

Portable instruction packages that help AI coding assistants make careful changes and explain their work clearly.

[Explore skills](#skill-catalog) · [Install with Zed](#quick-start) · [Contribute](CONTRIBUTING.md)

> [!WARNING]
> AgentSkillForge is in beta. The package version is `0.2.0b1`; all six skill documents use `0.2.0-beta.1`. Repository checks cover structure, local links, packaging, and static activation cases. They do not execute agent models or prove compatibility with every client. A formal maintenance policy and release cadence are not documented.

## What is AgentSkillForge?

AgentSkillForge is a collection of small, reusable instruction packages for AI coding assistants. Each package describes a task type, the evidence to gather, the decisions to make, and how to report the result.

Packages are plain Markdown directories centred on `SKILL.md`, so they are not tied to a single client. This repository documents installation for Zed; other clients need their own documented way to load compatible skill directories.

## Why use it?

- **Focused guidance:** Choose a skill for the task instead of using one generic workflow.
- **Evidence before assumptions:** Skills distinguish observed facts, inferences, and checks that were not run.
- **Portable packages:** Copy a complete skill directory to a compatible client without a required Python runtime.
- **Checked distribution:** Repository automation validates structure, links, tests, static eval cases, and package contents.

## Skill Catalog

Choose the skill that matches the task—not merely a word in the prompt.

| Skill | When to use it | Example |
|---|---|---|
| [`skills/solution-framing/`](skills/solution-framing/) | The direction is unclear or a decision has meaningful trade-offs. | “Which migration approach is safest?” |
| [`skills/safe-code-change/`](skills/safe-code-change/) | You need a small, understood change or bug fix. | “Fix this reproducible validation error.” |
| [`skills/evidence-led-code-review/`](skills/evidence-led-code-review/) | A change is ready for review and needs an evidence-based assessment. | “Review this pull request before merging.” |
| [`skills/product-interface-engineering/`](skills/product-interface-engineering/) | A screen, form, interaction, accessibility, or responsive behavior needs work. | “Make this checkout form usable on mobile.” |
| [`skills/performance-investigation/`](skills/performance-investigation/) | You have a measured latency, throughput, or memory problem to investigate. | “Why did this endpoint become slower?” |
| [`skills/vue-sfc-decomposition/`](skills/vue-sfc-decomposition/) | A Vue or Nuxt component needs to be split without changing behavior. | “Separate this large Vue SFC into maintainable parts.” |

Read a package’s `SKILL.md` before using it. Keep its complete directory, including any `references/` and `assets/`, because the package may link to them.

## Quick Start

Install Git and Python 3.11 or newer before using the Zed installer. It installs all skills into Zed’s shared `~/.agents/skills` directory.

<details>
<summary>macOS, Linux, or WSL</summary>

```sh
git clone https://github.com/RobinGru/AgentSkillForge.git AgentSkillForge
cd AgentSkillForge
python3 scripts/install_zed_skills.py
```

</details>

<details>
<summary>Windows PowerShell</summary>

```powershell
git clone https://github.com/RobinGru/AgentSkillForge.git AgentSkillForge
cd AgentSkillForge
py scripts\install_zed_skills.py
```

</details>

Start a new agent session after installation. The installer stops rather than replacing an existing skill directory.

## Installation

### Portable core

Copy or reference the desired `skills/<name>/` directory using your client’s documented mechanism. AgentSkillForge does not claim a universal install path or automatic-discovery convention.

### Zed

Install only one skill when you do not need the full catalog:

```sh
python3 scripts/install_zed_skills.py --skill performance-investigation
```

Repeat `--skill` to install several packages. Use `--target` when Zed uses a different skill directory.

> [!CAUTION]
> `--force` deletes and recreates every selected target directory. Review local edits first; the installer does not merge files.

See the [complete Zed installation guide](docs/clients/zed.md) for selected skills, custom targets, updates, verification, and uninstallation.

## Using skills together

A common sequence is:

1. Use `solution-framing` when an important direction is still unclear.
2. Use `performance-investigation` when you have a measured performance problem.
3. Use `safe-code-change` to make a focused change.
4. Use `evidence-led-code-review` to review the completed change.

Your AI client decides when to load an installed skill. Each package also defines the type of response the assistant should produce.

## Compatibility

| Area | Supported or required |
|---|---|
| Skill format | Markdown `SKILL.md` packages with relative local references |
| Agent clients | Clients that can load compatible skill directories; exact support depends on client configuration |
| Documented integration | Zed with agent skills enabled |
| Python | 3.11 or newer for the Zed installer, packaging, and repository checks |
| Package runtime | No importable Python module; the wheel distributes skills and support files as data |

The skill documents themselves do not require Python. Python is used by the installer and repository tooling.

## Quality and development

The **Validate** workflow runs the repository checks below. **CodeQL** analyzes the Python tooling for supported security issues.

```sh
python -m pip install -e ".[dev]"
python scripts/validate_repository.py
python scripts/check_links.py
pytest
python scripts/run_evals.py
python scripts/check_distribution.py
```

These commands validate skill metadata and layout, local Markdown links, installer and packaging behavior, static eval-manifest coverage, and distributed wheel contents.

> [!NOTE]
> `python scripts/run_evals.py` validates static case declarations; it does not run an agent or establish runtime portability. Check external HTTP links explicitly with `python scripts/check_links.py --external`.

<details>
<summary>Project structure</summary>

```text
.
├── skills/                     # Portable skill packages
├── evals/                      # Static cases and repository tests
├── scripts/                    # Validation, packaging, and Zed installer tools
├── docs/clients/zed.md         # Zed integration guide
├── .github/workflows/          # Automation workflows
├── CONTRIBUTING.md             # Contribution and clean-room rules
├── pyproject.toml              # Python tooling and package metadata
├── README.md                   # English documentation
├── README.de.md                # German documentation
└── LICENSE                     # Apache License 2.0
```

The Python wheel is a data distribution, not an application or importable SDK. It places the README, skill packages, references, Zed guide, and installer below `share/agent-skill-forge/`.

</details>

## Contributing

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. New or changed skill behavior must preserve portable metadata and valid local references, follow the clean-room process, and update the relevant evals and output-contract checks.

## Security and support

Treat third-party skills as untrusted instructions. Inspect their content, provenance, links, and dependencies before installation. Do not grant tools, credentials, or filesystem access solely because a skill document requests them.

Report potential security vulnerabilities through GitHub’s private vulnerability reporting. Do not publish sensitive details in a public issue. Use [GitHub Issues](https://github.com/RobinGru/AgentSkillForge/issues) for public bug reports and questions.

## License and notices

AgentSkillForge is distributed under the [Apache License 2.0](LICENSE). Review [NOTICE](NOTICE) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) before redistribution.
