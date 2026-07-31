# Install in Codex

This guide adds the portable skill directories to Codex's user skill location.
It does not modify the portable `SKILL.md` files or require client-specific
fields in them.

## Prerequisites

- Codex CLI or the Codex IDE extension.
- Python 3.11 or newer.
- A local clone of this repository, or an installed wheel containing its
  `share/agent-skill-forge/` directory.

Codex loads user skills from `~/.agents/skills`, the same shared location used
by Zed. On Windows this normally resolves to
`C:\\Users\\<your-user>\\.agents\\skills`. Codex also scans repository-level
`.agents/skills` directories; use `--target` to install there instead.

## Install all skills

From the repository root:

### Windows PowerShell

```powershell
py scripts\install_codex_skills.py
```

### macOS, Linux, or WSL

```sh
python3 scripts/install_codex_skills.py
```

The command prints each installed directory. It refuses to replace an existing
skill directory.

## Install or update selected skills

Install one selected skill:

```sh
python3 scripts/install_codex_skills.py --skill failure-investigation
```

Install a related workflow set:

```sh
python3 scripts/install_codex_skills.py --skill project-discovery --skill feature-specification
```

Replace only a selected existing skill directory:

```sh
python3 scripts/install_codex_skills.py --skill compatibility-migration --force
```

`--force` deletes and recreates each selected destination directory. Review any
local edits in that directory before using it.

## Custom location

Install skills for one repository:

```sh
python3 scripts/install_codex_skills.py --target /path/to/repository/.agents/skills
```

On Windows PowerShell, for example:

```powershell
py scripts\install_codex_skills.py --target "$PWD\.agents\skills"
```

## Confirm in Codex

Codex detects skill changes automatically. If installed skills do not appear,
restart Codex. In Codex CLI or the IDE extension, use `/skills` or type `$` to
inspect or explicitly invoke a skill. Confirm that the installed directory
contains `SKILL.md` and any `references/` or `assets/` files.

Visibility verifies installation only. It does not prove which skill Codex will
choose for a prompt.

## Uninstall

Remove only the desired `<skill-name>` directory from `~/.agents/skills` or the
repository-level `.agents/skills` directory. Do not remove unrelated skills.
