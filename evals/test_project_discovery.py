from collections import Counter
from pathlib import Path
from typing import Any, cast

import yaml

from scripts.validate_repository import validate_skill

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "planning" / "project-discovery" / "SKILL.md"
EVALS = ROOT / "evals" / "project-discovery.yaml"
HEADINGS = [
    "## Product problem",
    "## Users and jobs",
    "## Outcomes and success signals",
    "## Scope, non-goals, and constraints",
    "## Repository evidence and uncertainty",
    "## Initial capability map",
    "## Recommended first capability",
    "## Open decisions",
    "## Handoff state",
]


def load_cases() -> list[dict[str, Any]]:
    data = yaml.safe_load(EVALS.read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    cases = data.get("cases")
    assert isinstance(cases, list)
    assert all(isinstance(case, dict) for case in cases)
    return cast(list[dict[str, Any]], cases)


def test_project_discovery_is_portable_and_compact() -> None:
    name, findings = validate_skill(SKILL)
    assert name == "project-discovery"
    assert not [finding for finding in findings if finding.level == "error"]
    text = SKILL.read_text(encoding="utf-8")
    assert len(text.splitlines()) <= 160
    assert "| ID | Feature | Status | Spec |" in text
    assert all(status in text for status in ("Idea", "Ready", "In Progress", "Done"))
    assert "it is not `docs/features/index.md`" in text
    assert "`feature-specification`" in text
    assert "`feature-lifecycle`" in text


def test_project_discovery_output_contract_is_exact() -> None:
    section = SKILL.read_text(encoding="utf-8").split("## Output contract", 1)[1]
    assert [line for line in section.splitlines() if line.startswith("## ")] == HEADINGS


def test_project_discovery_evals_cover_behavior_boundaries() -> None:
    cases = load_cases()
    counts = Counter(case["category"] for case in cases)
    assert counts == {"positive": 5, "negative": 5, "conflict": 5, "output": 2, "adversarial": 2}
    by_id = {case["id"]: case for case in cases}
    assert len(by_id) == len(cases)
    assert all(case.get("assertions") or case.get("forbidden_skills") for case in cases)
    assert by_id["discovery-positive-new-product"]["expected_skills"] == ["project-discovery"]
    assert "project-discovery" in by_id["discovery-negative-one-feature"]["forbidden_skills"]
    assert "project-discovery" in by_id["discovery-negative-technical-choice"]["forbidden_skills"]
    assert by_id["discovery-negative-local-fix"]["expected_skills"] == ["safe-code-change"]
    assert any(
        "minimal feature index" in assertion
        for assertion in by_id["discovery-output-brief"]["assertions"]
    )
    assert by_id["discovery-conflict-then-specify"]["expected_skills"] == [
        "project-discovery",
        "feature-specification",
    ]
    assert by_id["discovery-conflict-lifecycle"]["expected_skills"] == [
        "project-discovery",
        "feature-lifecycle",
    ]
