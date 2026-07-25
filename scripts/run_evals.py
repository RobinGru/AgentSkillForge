#!/usr/bin/env python3
"""Validate the static skill-evaluation manifest.

This command checks coverage declarations only. It does not execute an agent or
claim runtime portability.
"""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

import yaml

REQUIRED = {"positive": 5, "negative": 5, "conflict": 3, "output": 2, "adversarial": 1}
PREFIXES = {"sf", "sc", "cr", "ui", "pi", "vue"}


def validate_manifest(path: Path) -> list[str]:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        return [f"could not read manifest: {error}"]
    if not isinstance(data, dict) or not isinstance(data.get("cases"), list):
        return ["manifest must contain a cases list"]

    cases = data["cases"]
    identifiers = [case.get("id") for case in cases if isinstance(case, dict)]
    errors: list[str] = []
    if len(cases) < 96:
        errors.append(f"expected at least 96 cases, found {len(cases)}")
    if len(identifiers) != len(cases) or any(not isinstance(item, str) or not item for item in identifiers):
        errors.append("every case must have a non-empty string id")
    elif len(set(identifiers)) != len(identifiers):
        errors.append("case ids must be unique")

    for prefix in PREFIXES:
        skill_cases = [case for case in cases if isinstance(case, dict) and str(case.get("id", "")).startswith(f"{prefix}-")]
        counts = Counter(case.get("category") for case in skill_cases)
        for category, minimum in REQUIRED.items():
            if counts[category] < minimum:
                errors.append(f"{prefix}: expected {minimum} {category} cases, found {counts[category]}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=Path("evals/manifest.yaml"))
    args = parser.parse_args()
    errors = validate_manifest(args.manifest)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Static eval manifest coverage is valid; runtime agent evaluation is not performed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
