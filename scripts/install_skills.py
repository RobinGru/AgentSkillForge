#!/usr/bin/env python3
"""Install portable skill directories into a client skill directory."""

from __future__ import annotations

import argparse
import shutil
from collections.abc import Sequence
from pathlib import Path


def repository_root() -> Path:
    return Path(__file__).resolve().parents[1]


def default_source() -> Path:
    return repository_root() / "skills"


def available_skills(source: Path) -> dict[str, Path]:
    if not source.is_dir():
        raise ValueError(f"skill source directory does not exist: {source}")

    skills: dict[str, Path] = {}
    for skill_file in sorted(source.rglob("SKILL.md")):
        directory = skill_file.parent
        name = directory.name
        if name in skills:
            raise ValueError(f"duplicate skill name '{name}': {skills[name]} and {directory}")
        skills[name] = directory
    return skills


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
        _ = shutil.copytree(origin, destination)
        installed.append(destination)
    return installed


def main(default_target: Path, client_name: str, argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument("--source", type=Path, default=default_source(), help="directory containing skill folders")
    _ = parser.add_argument("--target", type=Path, default=default_target, help=f"{client_name} skill directory")
    _ = parser.add_argument("--skill", dest="skills", action="append", help="skill name to install; repeat for more than one")
    _ = parser.add_argument("--force", action="store_true", help="replace selected existing skill directories")

    class Arguments(argparse.Namespace):
        source: Path = default_source()
        target: Path = default_target
        skills: list[str] | None = None
        force: bool = False

    args = parser.parse_args(argv, namespace=Arguments())

    try:
        installed = install_skills(args.source, args.target, args.skills, args.force)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    for path in installed:
        print(path)
    return 0
