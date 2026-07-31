from collections import Counter
from pathlib import Path

import yaml

from scripts.run_evals import (

    LEGACY_MANIFEST_REQUIRED,
    NEW_SKILLS,
    SKILL_EVAL_SPECS,
    validate_eval_suite,
)

ROOT = Path(__file__).resolve().parents[1]
EVAL_DIR = ROOT / "evals"
MANIFEST = EVAL_DIR / "manifest.yaml"


def load_cases(path: Path) -> list[dict]:
    return yaml.safe_load(path.read_text(encoding="utf-8"))["cases"]


def test_eval_suite_uses_canonical_dynamic_coverage() -> None:
    assert validate_eval_suite(MANIFEST) == []

    manifest_cases = load_cases(MANIFEST)
    expected_minimum = sum(
        sum(LEGACY_MANIFEST_REQUIRED.values()) if spec.legacy_manifest_matrix else 3
        for spec in SKILL_EVAL_SPECS.values()
    )
    assert len(manifest_cases) >= expected_minimum

    for skill, spec in SKILL_EVAL_SPECS.items():
        detailed_cases = load_cases(EVAL_DIR / f"{skill}.yaml")
        assert len(detailed_cases) >= spec.detailed_minimum
        if spec.legacy_manifest_matrix:
            counts = Counter(
                case["category"]
                for case in manifest_cases
                if case["id"].startswith(f"{spec.prefix}-")
            )
            assert all(
                counts[category] >= minimum
                for category, minimum in LEGACY_MANIFEST_REQUIRED.items()
            )


def test_manifest_preserves_catalog_routing_and_compact_new_skill_contrasts() -> None:
    cases = load_cases(MANIFEST)
    for skill, spec in SKILL_EVAL_SPECS.items():
        skill_cases = [case for case in cases if case["id"].startswith(f"{spec.prefix}-")]
        assert any(skill in case.get("expected_skills", []) for case in skill_cases)
        if skill not in NEW_SKILLS:
            assert any(skill in case.get("forbidden_skills", []) for case in skill_cases)

        if skill in NEW_SKILLS:
            assert len(skill_cases) >= 3
            contrasted = {
                forbidden
                for case in skill_cases
                for forbidden in case.get("forbidden_skills", [])
            }
            assert set(SKILL_EVAL_SPECS) - {skill} <= contrasted


def test_manifest_and_detailed_eval_prompts_are_globally_unique() -> None:
    manifest_prompts = [case["prompt"] for case in load_cases(MANIFEST)]
    detailed_prompts = [
        case["prompt"]
        for skill in SKILL_EVAL_SPECS
        for case in load_cases(EVAL_DIR / f"{skill}.yaml")
    ]
    assert len(manifest_prompts) == len(set(manifest_prompts))
    assert len(detailed_prompts) == len(set(detailed_prompts))
    assert set(manifest_prompts).isdisjoint(detailed_prompts)
