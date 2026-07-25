from collections import Counter
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "evals" / "manifest.yaml"
SKILLS = {
    "sf": "solution-framing",
    "sc": "safe-code-change",
    "cr": "evidence-led-code-review",
    "ui": "product-interface-engineering",
    "pi": "performance-investigation",
    "vue": "vue-sfc-decomposition",
}
REQUIRED_CATEGORIES = {
    "positive": 5,
    "negative": 5,
    "conflict": 3,
    "output": 2,
    "adversarial": 1,
}


def test_eval_manifest_has_minimum_coverage_per_skill() -> None:
    cases = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))["cases"]
    assert len(cases) >= 96
    ids = [case["id"] for case in cases]
    assert len(ids) == len(set(ids))

    for prefix in SKILLS:
        counts = Counter(case["category"] for case in cases if case["id"].startswith(f"{prefix}-"))
        for category, minimum in REQUIRED_CATEGORIES.items():
            assert counts[category] >= minimum


def test_eval_manifest_covers_expected_and_forbidden_activation() -> None:
    cases = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))["cases"]
    for prefix, skill in SKILLS.items():
        skill_cases = [case for case in cases if case["id"].startswith(f"{prefix}-")]
        assert any(skill in case.get("expected_skills", []) for case in skill_cases)
        assert any(skill in case.get("forbidden_skills", []) for case in skill_cases)
