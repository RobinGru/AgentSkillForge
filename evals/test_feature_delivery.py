from collections import Counter
from pathlib import Path
from typing import Any, cast

import yaml

from scripts.validate_repository import validate_skill

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "planning" / "feature-delivery" / "SKILL.md"
EVALS = ROOT / "evals" / "feature-delivery.yaml"
HEADINGS = [
    "## Delivery update",
    "## Task evidence",
    "## Updated artifacts",
    "## Next task or stop reason",
    "## Delivery state",
]
STATES = ["PROPOSED", "READY", "IN PROGRESS", "BLOCKED", "VERIFICATION", "DONE", "ABANDONED"]


def load_cases() -> list[dict[str, Any]]:
    data = yaml.safe_load(EVALS.read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    cases = data.get("cases")
    assert isinstance(cases, list)
    assert all(isinstance(case, dict) for case in cases)
    return cast(list[dict[str, Any]], cases)


def test_feature_delivery_is_portable_and_strictly_sequential() -> None:
    name, findings = validate_skill(SKILL)
    text = SKILL.read_text(encoding="utf-8")

    assert name == "feature-delivery"
    assert not [finding for finding in findings if finding.level == "error"]
    assert len(text.splitlines()) <= 180
    assert "same agent" in text
    assert "Never use parallel agents" in text
    assert "at most one task may be `IN PROGRESS`" in text
    assert "Do not stop merely because one task" in text


def test_feature_delivery_contract_and_state_guards_are_exact() -> None:
    text = SKILL.read_text(encoding="utf-8")
    section = text.split("## Output contract", 1)[1]

    assert [line for line in section.splitlines() if line.startswith("## ")] == HEADINGS
    assert all(f"`{state}`" in text for state in STATES)
    assert "dependencies are `DONE`" in text
    assert "direct proof" in text
    assert "failed verification" in text


def test_feature_delivery_evals_cover_sequential_boundaries() -> None:
    cases = load_cases()
    counts = Counter(case["category"] for case in cases)
    by_id = {case["id"]: case for case in cases}

    assert all(counts[category] >= minimum for category, minimum in {
        "positive": 2, "negative": 2, "conflict": 2, "output": 1, "adversarial": 2
    }.items())
    assert len(by_id) == len(cases)
    assert len({case["prompt"] for case in cases}) == len(cases)
    assert all(case.get("assertions") or case.get("forbidden_skills") for case in cases)
    assert by_id["delivery-negative-single-change"]["expected_skills"] == ["safe-code-change"]
    assert "feature-delivery" in by_id["delivery-negative-single-change"]["forbidden_skills"]
    assert "refuses parallel agents" in by_id["delivery-adversarial-parallel"]["assertions"]
