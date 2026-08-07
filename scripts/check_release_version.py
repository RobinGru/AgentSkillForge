#!/usr/bin/env python3
"""Ensure a release tag matches the package and skill document versions."""

from __future__ import annotations

import argparse
import re
import sys
import tomllib
from pathlib import Path
from typing import cast

PACKAGE_VERSION = re.compile(
    r"^(?P<release>\d+(?:\.\d+)*)(?:(?P<pre>a|b|rc)(?P<number>\d+))?$"
)
SKILL_VERSION = re.compile(r"(?m)^  version:\s*['\"]?(?P<version>[^'\"\s]+)['\"]?\s*$")
RELEASE_TAG = re.compile(r"^\d+\.\d+\.\d+$")
PRE_RELEASE_LABEL = {"a": "alpha", "b": "beta", "rc": "rc"}


def expected_skill_version(package_version: str) -> str:
    """Convert the package's PEP 440 version to the skill metadata form."""
    match = PACKAGE_VERSION.fullmatch(package_version)
    if match is None:
        raise ValueError(f"unsupported package version: {package_version}")

    label = match.group("pre")
    if label is None:
        return match.group("release")
    return f"{match.group('release')}-{PRE_RELEASE_LABEL[label]}.{match.group('number')}"


def check_release_version(root: Path, tag: str) -> list[str]:
    """Return mismatches between a release tag, package version, and skill versions."""
    with (root / "pyproject.toml").open("rb") as file:
        metadata = cast(object, tomllib.load(file))
    if not isinstance(metadata, dict):
        raise TypeError("pyproject.toml must contain a project table")
    metadata = cast(dict[str, object], metadata)
    project = metadata.get("project")
    if not isinstance(project, dict):
        raise TypeError("pyproject.toml project must be a table")
    project = cast(dict[str, object], project)
    package_version = project.get("version")
    if not isinstance(package_version, str):
        raise TypeError("pyproject.toml project.version must be a string")

    expected_tag = package_version
    findings: list[str] = []
    if RELEASE_TAG.fullmatch(tag) is None:
        findings.append(f"release tag {tag!r} must match MAJOR.MINOR.PATCH")
    if tag != expected_tag:
        findings.append(f"release tag {tag!r} does not match package version {expected_tag!r}")

    expected_version = expected_skill_version(package_version)
    for path in sorted((root / "skills").rglob("SKILL.md")):
        match = SKILL_VERSION.search(path.read_text(encoding="utf-8"))
        actual_version = match.group("version") if match else None
        if actual_version != expected_version:
            findings.append(f"{path.relative_to(root)} has version {actual_version!r}; expected {expected_version!r}")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument("tag", help="Release tag, for example 0.4.0")

    class Arguments(argparse.Namespace):
        tag: str = ""

    args = parser.parse_args(namespace=Arguments())

    findings = check_release_version(Path(__file__).resolve().parents[1], args.tag)
    if findings:
        print("Release version validation failed:", file=sys.stderr)
        print(*findings, sep="\n", file=sys.stderr)
        return 1

    print(f"Release version validation passed for {args.tag}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
