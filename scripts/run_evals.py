#!/usr/bin/env python3
"""Validate static catalog and per-skill evaluation declarations.

This command checks declared coverage only. It does not execute an agent or
claim runtime routing behavior.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


if __package__ is None:  # Direct execution as `python scripts/run_evals.py`.
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.run_runtime_evals import as_mapping, load_cases as load_runtime_cases, object_list, string_list
from scripts.run_runtime_evals import load_yaml as load_runtime_yaml
from scripts.run_runtime_evals import validate_client


@dataclass(frozen=True)
class SkillEvalSpec:
    prefix: str
    detailed_minimum: int
    legacy_manifest_matrix: bool = False


SKILL_EVAL_SPECS = {
    "solution-framing": SkillEvalSpec("sf", 6, True),
    "safe-code-change": SkillEvalSpec("sc", 5, True),
    "fact-based-code-review": SkillEvalSpec("cr", 5, True),
    "product-interface-engineering": SkillEvalSpec("ui", 5, True),
    "performance-investigation": SkillEvalSpec("pi", 5, True),
    "vue-sfc-decomposition": SkillEvalSpec("vue", 5, True),
    "failure-investigation": SkillEvalSpec("fi", 18),
    "security-boundary-analysis": SkillEvalSpec("sec", 18),
    "compatibility-migration": SkillEvalSpec("cm", 18),
    "project-discovery": SkillEvalSpec("pd", 18),
    "feature-specification": SkillEvalSpec("fs", 18),
    "feature-lifecycle": SkillEvalSpec("fl", 20),
    "session-handoff": SkillEvalSpec("sh", 18),
    "adversarial-deep-review": SkillEvalSpec("adr", 18),
    "repository-knowledge-curation": SkillEvalSpec("rkc", 18),
    "repository-onboarding": SkillEvalSpec("rko", 18),
}
LEGACY_MANIFEST_REQUIRED = {
    "positive": 5,
    "negative": 5,
    "conflict": 3,
    "output": 2,
    "adversarial": 1,
}
NEW_SKILLS = {
    name for name, spec in SKILL_EVAL_SPECS.items() if not spec.legacy_manifest_matrix
}



def load_cases(path: Path) -> tuple[list[dict[str, object]], list[str]]:
    try:
        data = as_mapping(load_runtime_yaml(path))
    except ValueError as error:
        return [], [str(error)]
    raw_cases = object_list(data.get("cases")) if data is not None else None
    if data is None or raw_cases is None:
        return [], [f"{path} must contain a cases list"]
    cases = [as_mapping(case) for case in raw_cases]
    if any(case is None for case in cases):
        return [], [f"{path} cases must be mappings"]
    return [case for case in cases if case is not None], []



def validate_case_identity(cases: list[dict[str, object]], label: str) -> list[str]:
    errors: list[str] = []
    identifiers = [case.get("id") for case in cases]
    prompts = [case.get("prompt") for case in cases]
    if any(not isinstance(value, str) or not value.strip() for value in identifiers):
        errors.append(f"{label}: every case must have a non-empty string id")
    elif len(set(identifiers)) != len(identifiers):
        errors.append(f"{label}: case ids must be unique")
    if any(not isinstance(value, str) or not value.strip() for value in prompts):
        errors.append(f"{label}: every case must have a non-empty string prompt")
    elif len(set(prompts)) != len(prompts):
        errors.append(f"{label}: prompts must be unique")
    return errors


def validate_detailed_evals(eval_dir: Path) -> tuple[list[str], set[str]]:
    errors: list[str] = []
    prompts: set[str] = set()
    for skill, spec in SKILL_EVAL_SPECS.items():
        path = eval_dir / f"{skill}.yaml"
        cases, load_errors = load_cases(path)
        errors.extend(load_errors)
        if load_errors:
            continue
        errors.extend(validate_case_identity(cases, skill))
        if len(cases) < spec.detailed_minimum:
            errors.append(f"{skill}: expected at least {spec.detailed_minimum} detailed cases, found {len(cases)}")
        for case in cases:
            prompt = case.get("prompt")
            if isinstance(prompt, str):
                if prompt in prompts:
                    errors.append(f"detailed eval prompt is duplicated across skills: {prompt}")
                prompts.add(prompt)
    return errors, prompts


def validate_manifest(path: Path) -> list[str]:
    cases, errors = load_cases(path)
    if errors:
        return errors
    errors.extend(validate_case_identity(cases, "manifest"))

    expected_minimum = sum(
        sum(LEGACY_MANIFEST_REQUIRED.values()) if spec.legacy_manifest_matrix else 3
        for spec in SKILL_EVAL_SPECS.values()
    )
    if len(cases) < expected_minimum:
        errors.append(f"expected at least {expected_minimum} catalog cases, found {len(cases)}")

    for skill, spec in SKILL_EVAL_SPECS.items():
        skill_cases = [case for case in cases if str(case.get("id", "")).startswith(f"{spec.prefix}-")]
        if spec.legacy_manifest_matrix:
            counts = Counter(case.get("category") for case in skill_cases)
            for category, minimum in LEGACY_MANIFEST_REQUIRED.items():
                if counts[category] < minimum:
                    errors.append(f"{spec.prefix}: expected {minimum} {category} cases, found {counts[category]}")
        else:
            if len(skill_cases) < 3:
                errors.append(f"{spec.prefix}: expected at least 3 grouped catalog contrast cases")
            comparison_skills = set(SKILL_EVAL_SPECS) - {skill}
            contrasted = {
                other
                for case in skill_cases
                for other in (string_list(case.get("forbidden_skills", [])) or [])
                if other in comparison_skills
            }
            missing = sorted(comparison_skills - contrasted)
            if missing:
                errors.append(f"{spec.prefix}: missing catalog contrasts against {', '.join(missing)}")
    return errors


def validate_runtime_declarations(eval_dir: Path) -> list[str]:
    errors: list[str] = []
    try:
        cases = load_runtime_cases(eval_dir / "runtime.yaml")
    except ValueError as error:
        errors.append(str(error))
    else:
        if not cases:
            errors.append("runtime.yaml must declare at least one runtime case")

    try:
        clients = as_mapping(load_runtime_yaml(eval_dir / "clients.yaml"))
    except ValueError as error:
        errors.append(str(error))
        return errors
    raw_clients = object_list(clients.get("clients")) if clients is not None else None
    if clients is None or clients.get("version") != 1 or raw_clients is None:
        return [*errors, f"{eval_dir / 'clients.yaml'} must contain version: 1 and a clients list"]
    identifiers: set[str] = set()
    for value in raw_clients:
        client = as_mapping(value)
        identifier = client.get("id") if client is not None else None
        if not isinstance(identifier, str) or not identifier:
            errors.append("clients.yaml clients must have non-empty string ids")
            continue
        assert client is not None
        if identifier in identifiers:
            errors.append(f"clients.yaml duplicate client id: {identifier}")
        identifiers.add(identifier)
        errors.extend(f"{identifier}: {error}" for error in validate_client(client))
    if not {"codex-cli", "zed"} <= identifiers:
        errors.append("clients.yaml must declare codex-cli and zed clients")
    return errors


def validate_eval_suite(manifest: Path) -> list[str]:
    errors = validate_manifest(manifest)
    detailed_errors, detailed_prompts = validate_detailed_evals(manifest.parent)
    errors.extend(detailed_errors)
    errors.extend(validate_runtime_declarations(manifest.parent))
    manifest_cases, load_errors = load_cases(manifest)
    if not load_errors:
        duplicates = sorted(
            prompt
            for case in manifest_cases
            if isinstance(prompt := case.get("prompt"), str) and prompt in detailed_prompts
        )
        if duplicates:
            errors.append(f"manifest prompts duplicate detailed evals: {duplicates}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument("--manifest", type=Path, default=Path("evals/manifest.yaml"))

    class Arguments(argparse.Namespace):
        manifest: Path = Path("evals/manifest.yaml")

    args = parser.parse_args(namespace=Arguments())
    errors = validate_eval_suite(args.manifest)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Static eval coverage is valid; runtime agent evaluation was not performed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
