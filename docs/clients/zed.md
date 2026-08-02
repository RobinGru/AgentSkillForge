# Install in Zed

This guide adds the portable skill directories to Zed's shared agent-skill
location. It does not modify the portable `SKILL.md` files or require a
client-specific field in them.

## Prerequisites

- Zed with agent skills enabled in your configuration.
- Python 3.11 or newer.
- A local clone of this repository, or an installed wheel containing its
  `share/agent-skill-forge/` directory.

The default target is `~/.agents/skills`. On Windows this normally resolves to
`C:\\Users\\<your-user>\\.agents\\skills`. If your Zed configuration uses another
skill directory, pass it explicitly with `--target`.

## Install all skills

From the repository root:

### Windows PowerShell

```powershell
py scripts\install_zed_skills.py
```

### macOS, Linux, or WSL

```sh
python3 scripts/install_zed_skills.py
```

The command prints each installed directory. It refuses to replace an existing
skill directory.

## Manual ZIP installation

Build `dist/agent-skill-forge-skills.zip` from a source checkout with:

```sh
python3 scripts/build_skill_bundle.py
```

Extract the ZIP contents directly into the configured skill directory. Its top-level
entries are complete flat skill directories; do not extract them below a category
folder.

## Install or update selected skills

Install one selected skill:

```sh
python3 scripts/install_zed_skills.py --skill failure-investigation
```

Install a related workflow set:

```sh
python3 scripts/install_zed_skills.py --skill project-discovery --skill feature-specification
```

Replace only a selected existing skill directory:

```sh
python3 scripts/install_zed_skills.py --skill compatibility-migration --force
```

`--force` deletes and recreates each selected destination directory. Review any
local edits in that directory before using it.

## Custom location

```sh
python3 scripts/install_zed_skills.py --target /path/to/AgentSkillForge
```

On Windows PowerShell, for example:

```powershell
py scripts\install_zed_skills.py --target "$HOME\.agents\skills"
```

## Confirm in Zed

Start a new agent session after installation. If the skills are not visible,
restart Zed and confirm that its configured agent-skill directory matches the
target printed by the installer. For a selected installation, verify its printed
directories, for example `~/.agents/skills/project-discovery` or
`~/.agents/skills/feature-specification`. Each selected directory must retain its
`SKILL.md` and any `references/` or `assets/` files.

Visibility verifies installation only. It does not prove which skill Zed or its
configured model will load for a prompt. For releases, complete the documented
[Zed smoke checklist](../compatibility.md#zed-release-smoke-checklist) and record
its client version, configured model, prompts, and observed outcomes.

## Uninstall

Remove the desired `<skill-name>` directory from the configured skill directory.
For the default location, remove only paths such as
`~/.agents/skills/failure-investigation`; do not remove unrelated skills.
