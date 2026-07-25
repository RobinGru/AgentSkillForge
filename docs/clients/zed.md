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

## Install or update selected skills

Install one skill:

```sh
python3 scripts/install_zed_skills.py --skill performance-investigation
```

Install several skills:

```sh
python3 scripts/install_zed_skills.py --skill safe-code-change --skill vue-sfc-decomposition
```

Replace only the selected existing skill directories:

```sh
python3 scripts/install_zed_skills.py --skill safe-code-change --force
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
target printed by the installer. Each skill directory must retain its `SKILL.md`
and any `references/` or `assets/` files.

## Uninstall

Remove the desired `<skill-name>` directory from the configured skill directory.
For the default location, remove only paths such as
`~/.agents/skills/performance-investigation`; do not remove unrelated skills.
