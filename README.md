**English** · [Deutsch](README.de.md)

# AgentSkillForge

[![Validate](https://github.com/RobinGru/AgentSkillForge/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/RobinGru/AgentSkillForge/actions/workflows/validate.yml)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](pyproject.toml)

Clear, reusable instructions that help AI coding assistants work carefully and explain what they did.

[Zed installation](docs/clients/zed.md) · [Skill packages](skills/) · [Contributing](CONTRIBUTING.md)

> [!WARNING]
> AgentSkillForge is currently in beta. The package version is `0.2.0b1`, and all six skill documents use version `0.2.0-beta.1`. Repository checks cover structure, local links, packaging, and static activation cases; they do not execute agent models or prove compatibility with every client. No formal maintenance policy or release cadence is documented.

## About

AgentSkillForge is a collection of small instruction packages for AI coding assistants. Think of a skill as a checklist: it tells the assistant what kind of task it is handling, what to check first, and how to report the result.

For example, one skill helps an assistant plan a risky decision; another helps it fix a small bug; another checks a finished change. The packages are plain Markdown files, so they are not tied to one specific AI tool. Zed has a documented installer. Other tools need their own way to load skill folders.

## Highlights

- **Clear guidance:** Each skill says what it is for and when it is the wrong choice.
- **Honest results:** Skills ask the assistant to separate facts, guesses, and checks it did not run.
- **Useful together:** You can combine skills when a task needs more than one step, such as planning, changing code, and reviewing it.
- **Easy to move:** A skill is a folder of Markdown files that can be copied to a compatible AI tool.
- **Checked before release:** This repository includes automated checks for files, links, tests, and package contents.
- **Original content:** Contributors write new skills from the problem to solve instead of copying another skill.

## Quick Start

Install Git and Python 3.11 or newer before using the Zed installer. On macOS, Linux, or WSL:

```sh
git clone https://github.com/RobinGru/AgentSkillForge.git AgentSkillForge
cd AgentSkillForge
python3 scripts/install_zed_skills.py
```

On Windows PowerShell:

```powershell
git clone https://github.com/RobinGru/AgentSkillForge.git AgentSkillForge
cd AgentSkillForge
py scripts\install_zed_skills.py
```

The installer copies all skills to Zed's shared `~/.agents/skills` folder and prints the installed paths. Start a new agent session afterward. If a folder already exists, the installer stops instead of replacing it.

See the [complete Zed installation guide](docs/clients/zed.md) for selected skills, custom targets, updates, verification, and uninstallation.

## Skill Catalog

- [`skills/solution-framing/`](skills/solution-framing/) — Help the assistant choose a safe direction when the task is unclear or has important trade-offs.
- [`skills/safe-code-change/`](skills/safe-code-change/) — Help it make a small, understood code change and check that it works.
- [`skills/evidence-led-code-review/`](skills/evidence-led-code-review/) — Help it review a proposed code change and explain problems clearly.
- [`skills/product-interface-engineering/`](skills/product-interface-engineering/) — Help it improve screens, forms, accessibility, and responsive behavior that people use.
- [`skills/performance-investigation/`](skills/performance-investigation/) — Help it investigate a measured speed or memory problem before changing code.
- [`skills/vue-sfc-decomposition/`](skills/vue-sfc-decomposition/) — Help it split a difficult Vue or Nuxt component without changing its behavior.

Read a package's `SKILL.md` before using it. Keep its complete directory, including any `references/` and `assets/`, because the workflow may link to those files.

## Installation

### Portable core

Copy or reference the desired `skills/<name>/` directory using your agent client's documented mechanism. The repository does not claim a universal installation path or automatic discovery convention.

### Zed

The included installer supports Windows, macOS, Linux, and WSL paths through Python's filesystem APIs. Install one skill with:

```sh
python3 scripts/install_zed_skills.py --skill performance-investigation
```

Install several skills by repeating `--skill`. Use `--target` when Zed is configured for a different directory.

> [!CAUTION]
> `--force` deletes and recreates each selected destination directory. Review local edits before using it; the operation does not merge files.

## Usage

Pick the skill that matches the actual task. Do not choose one only because a prompt contains a matching word.

A common order is:

1. Use `solution-framing` when an important choice is still unclear.
2. Use `performance-investigation` when you have a real speed or memory problem to investigate.
3. Use `safe-code-change` to make a focused fix.
4. Use `evidence-led-code-review` to check the completed change.

Your AI tool decides when to load an installed skill. Each skill also explains the kind of answer the assistant should give.

## Requirements and Compatibility

| Area | Supported or required |
|---|---|
| Git | Required for the documented clone-based Quick Start |
| Skill format | Markdown `SKILL.md` packages with relative local references |
| Agent clients | Clients that can load compatible skill directories; exact support depends on client configuration |
| Documented integration | Zed with agent skills enabled |
| Python | 3.11 or newer for the Zed installer, packaging, and repository checks |
| CI environment | Python 3.12 on `ubuntu-latest` |
| Package runtime | No importable Python module; the wheel distributes skill and support files as data |

The skill documents themselves do not require a Python runtime. Python is used by the installer and repository tooling.

## Validation and Development

Install the development dependencies and run the checks used by the repository workflow:

```sh
python -m pip install -e ".[dev]"
python scripts/validate_repository.py
python scripts/check_links.py
pytest
python scripts/run_evals.py
python scripts/check_distribution.py
```

These commands cover:

- skill names, frontmatter, directory layout, relative references, and README inventory;
- local Markdown targets and anchors;
- validator, installer, packaging, and per-skill contract tests;
- static eval-manifest coverage for positive, negative, conflict, output, and adversarial cases;
- wheel contents for every distributed skill document and Zed support file.

`python scripts/run_evals.py` validates static case declarations only. It does not run an agent or establish runtime portability. External HTTP links are checked only when `python scripts/check_links.py --external` is run explicitly.

## Project Structure

```text
.
├── skills/                     # Portable skill packages
├── evals/                      # Static cases and repository tests
├── scripts/                    # Validation, packaging, and Zed installer tools
├── docs/clients/zed.md         # Zed integration guide
├── .github/workflows/          # Repository validation workflow
├── CONTRIBUTING.md             # Contribution and clean-room rules
├── pyproject.toml              # Python tooling and data-package metadata
├── README.md                   # English documentation
├── README.de.md                # German documentation
└── LICENSE                     # Apache License 2.0
```

The Python wheel is a data distribution, not an application or importable SDK. It places the README, skill packages, references, Zed guide, and installer below `share/agent-skill-forge/`.

## Documentation

- [Zed installation](docs/clients/zed.md)
- [Contribution guide](CONTRIBUTING.md)
- [Skill packages](skills/)
- [Static eval cases](evals/manifest.yaml)
- [Third-party notices](THIRD_PARTY_NOTICES.md)

## Contributing

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. New or changed skill behavior must keep portable metadata, preserve valid local references, follow the clean-room process, and update the relevant evals and output-contract checks.

## Security

Treat all third-party skills as untrusted instructions. Inspect their content, provenance, links, and dependencies before installation. Do not grant tools, credentials, or filesystem access solely because a skill document requests them.

This repository currently has no `SECURITY.md` or documented private vulnerability-reporting channel. Do not publish sensitive vulnerability details in a public issue.

## Support

No public support or bug-reporting channel is currently documented. GitHub Issue creation is restricted for this repository. Do not invent or use an unofficial contact; consult the repository page for any future maintainer-provided channel.

## License and Notices

AgentSkillForge is distributed under the [Apache License 2.0](LICENSE). Review [NOTICE](NOTICE) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) before redistribution.
