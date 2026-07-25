#!/usr/bin/env python3
"""Install portable skill directories into Zed's shared skill directory."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def repository_root() -> Path:
    return Path(__file__).resolve().parents[1]


def default_source() -> Path:
    return repository_root() / "skills"


def default_target() -> Path:
    return Path.home() / ".agents" / "skills"


def available_skills(source: Path) -> dict[str, Path]:
    if not source.is_dir():
        raise ValueError(f"skill source directory does not exist: {source}")
    return {
        path.name: path
        for path in sorted(source.iterdir())
        if path.is_dir() and (path / "SKILL.md").is_file()
    }


def install_skills(source: Path, target: Path, names: list[str] | None, force: bool) -> list[Path]:
    skills = available_skills(source.resolve())
    selected = sorted(names or skills)
    unknown = sorted(set(selected) - set(skills))
    if unknown:
        raise ValueError("unknown skill name(s): " + ", ".join(unknown))

    target = target.resolve()
    target.mkdir(parents=True, exist_ok=True)
    installed: list[Path] = []
    for name in selected:
        origin = skills[name].resolve()
        destination = target / name
        if destination.exists() and not force:
            raise FileExistsError(f"destination already exists: {destination}; rerun with --force to replace it")
        if destination.exists():
            shutil.rmtree(destination)
        shutil.copytree(origin, destination)
        installed.append(destination)
    return installed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=default_source(), help="directory containing skill folders")
    parser.add_argument("--target", type=Path, default=default_target(), help="Zed shared skill directory")
    parser.add_argument("--skill", dest="skills", action="append", help="skill name to install; repeat for more than one")
    parser.add_argument("--force", action="store_true", help="replace selected existing skill directories")
    args = parser.parse_args()

    try:
        installed = install_skills(args.source, args.target, args.skills, args.force)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    for path in installed:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
