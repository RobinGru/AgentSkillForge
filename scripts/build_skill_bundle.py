#!/usr/bin/env python3
"""Build a flat ZIP bundle containing every portable skill directory."""

from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path

if __package__ is None:  # Direct execution as `python scripts/build_skill_bundle.py`.
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from install_skills import available_skills
else:  # pragma: no cover - exercised through package imports in tests.
    from .install_skills import available_skills


def build_bundle(source: Path, output: Path) -> list[str]:
    skills = available_skills(source.resolve())
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, directory in sorted(skills.items()):
            for path in sorted(directory.rglob("*")):
                if path.is_file():
                    archive.write(path, Path(name) / path.relative_to(directory))
    return sorted(skills)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument("--source", type=Path, default=Path(__file__).resolve().parents[1] / "skills")
    _ = parser.add_argument("--output", type=Path, default=Path("dist") / "agent-skill-forge-skills.zip")
    args = parser.parse_args()
    skills = build_bundle(args.source, args.output)
    print(f"Built {args.output} with {len(skills)} flat skill directories.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
