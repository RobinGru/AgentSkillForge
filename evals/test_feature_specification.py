from collections import Counter
from pathlib import Path
from typing import Any, cast

import yaml

from scripts.validate_repository import validate_skill

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "feature-specification" / "SKILL.md"
EVALS = ROOT / "evals" / "feature-specification.yaml"
HEADINGS = [
    "## Capability and actor",
    "## Scope and dependencies",
    "## Behavior and rules",
    "## Permissions and data",
    "## States and edge cases",
    "## Acceptance criteria",
    "## Traceability",
    "## Assumptions and blockers",
    "## Handoff state",
]


def load_cases() -> list[dict[str, Any]]:
    data = yaml.safe_load(EVALS.read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    cases = data.get("cases")
    assert isinstance(cases, list)
    assert all(isinstance(case, dict) for case in cases)
    return cast(list[dict[str, Any]], cases)


def test_feature_specification_is_portable_and_compact() -> None:
    name, findings = validate_skill(SKILL)
    assert name == "feature-specification"
    assert not [finding for finding in findings if finding.level == "error"]
    text = SKILL.read_text(encoding="utf-8")
    assert len(text.splitlines()) <= 160
    assert "one substantial product capability" in text
    assert "small, understood change" in text
    assert "`feature-lifecycle`" in text


def test_feature_specification_output_contract_is_exact() -> None:
    section = SKILL.read_text(encoding="utf-8").split("## Output contract", 1)[1]
    assert [line for line in section.splitlines() if line.startswith("## ")] == HEADINGS


def test_feature_specification_evals_cover_behavior_boundaries() -> None:
    cases = load_cases()
    counts = Counter(case["category"] for case in cases)
    assert counts == {"positive": 5, "negative": 5, "conflict": 5, "output": 2, "adversarial": 2}
    by_id = {case["id"]: case for case in cases}
    assert len(by_id) == len(cases)
    assert all(case.get("assertions") or case.get("forbidden_skills") for case in cases)
    assert by_id["specification-positive-permissions"]["expected_skills"] == [
        "feature-specification"
    ]
    assert "feature-specification" in by_id["specification-negative-product-unclear"]["forbidden_skills"]
    assert "feature-specification" in by_id["specification-negative-architecture"]["forbidden_skills"]
    assert by_id["specification-negative-implement"]["expected_skills"] == ["safe-code-change"]
    assert "feature-specification" in by_id["specification-negative-implement"]["forbidden_skills"]
    assert by_id["specification-conflict-ui"]["expected_skills"] == [
        "feature-specification",
        "product-interface-engineering",
    ]
    assert by_id["specification-conflict-lifecycle"]["expected_skills"] == [
        "feature-specification",
        "feature-lifecycle",
    ]
