#!/usr/bin/env python3
"""Build a wheel and ensure it contains every distributed skill document."""

from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


def expected_skill_files(root: Path) -> set[Path]:
    return {path.relative_to(root) for path in (root / "skills").rglob("*.md")}


def wheel_path(directory: Path) -> Path:
    wheels = sorted(directory.glob("agent_skill_forge-*.whl"))
    if len(wheels) != 1:
        raise RuntimeError(f"expected one wheel, found {len(wheels)}")
    return wheels[0]


def wheel_members(wheel: Path) -> list[str]:
    with zipfile.ZipFile(wheel) as archive:
        return archive.namelist()


def missing_skill_files(root: Path, wheel: Path) -> set[Path]:
    members = wheel_members(wheel)
    prefix = "share/agent-skill-forge/"
    return {
        path
        for path in expected_skill_files(root)
        if not any(member.endswith(prefix + path.as_posix()) for member in members)
    }


def missing_support_files(wheel: Path) -> set[str]:
    required = {
        "share/agent-skill-forge/compatibility.md",
        "share/agent-skill-forge/clients/codex/codex.md",
        "share/agent-skill-forge/clients/zed/zed.md",
        "share/agent-skill-forge/scripts/install_skills.py",
        "share/agent-skill-forge/scripts/install_zed_skills.py",
        "share/agent-skill-forge/scripts/install_codex_skills.py",
        "share/agent-skill-forge/scripts/build_skill_bundle.py",
        "share/agent-skill-forge/templates/AGENTS.md",
        "share/agent-skill-forge/templates/AGENTS-AIO.md",
    }
    members = wheel_members(wheel)
    return {path for path in required if not any(member.endswith(path) for member in members)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument("--root", type=Path, default=Path.cwd())

    class Arguments(argparse.Namespace):
        root: Path = Path.cwd()

    args = parser.parse_args(namespace=Arguments())
    root = args.root.resolve()

    with tempfile.TemporaryDirectory(prefix="agent-skill-forge-wheel-") as output:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "wheel", "--no-deps", "--wheel-dir", output, "."],
            cwd=root,
            check=False,
        )
        if result.returncode:
            return result.returncode
        wheel = wheel_path(Path(output))
        missing = missing_skill_files(root, wheel)
        missing_support = missing_support_files(wheel)

    if missing or missing_support:
        for path in sorted(missing):
            print(f"ERROR: wheel is missing {path}")
        for path in sorted(missing_support):
            print(f"ERROR: wheel is missing {path}")
        return 1
    print("Wheel contains every distributed skill document and client support file.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
