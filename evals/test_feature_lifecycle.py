from collections import Counter
from pathlib import Path
from typing import Any, cast

import yaml

from scripts.validate_repository import validate_skill

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "feature-lifecycle" / "SKILL.md"
EVALS = ROOT / "evals" / "feature-lifecycle.yaml"
REFERENCE = SKILL.parent / "references" / "artifact-templates.md"
HEADINGS = [
    "## Lifecycle update",
    "## Evidence",
    "## Updated artifacts",
    "## Next safe action",
    "## Lifecycle state",
]
STATES = ["PROPOSED", "READY", "IN PROGRESS", "BLOCKED", "VERIFICATION", "DONE", "ABANDONED"]
REQUIRED = {"positive": 5, "negative": 5, "conflict": 4, "output": 2, "adversarial": 4}


def load_cases() -> list[dict[str, Any]]:
    data = yaml.safe_load(EVALS.read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    cases = data.get("cases")
    assert isinstance(cases, list)
    assert all(isinstance(case, dict) for case in cases)
    return cast(list[dict[str, Any]], cases)


def output_headings(text: str) -> list[str]:
    section = text.split("## Output contract", 1)[1]
    return [line for line in section.splitlines() if line.startswith("## ")]


def test_feature_lifecycle_is_portable_and_has_a_bounded_ledger() -> None:
    name, findings = validate_skill(SKILL)
    text = SKILL.read_text(encoding="utf-8")

    assert name == "feature-lifecycle"
    assert not [finding for finding in findings if finding.level == "error"]
    assert len(text.splitlines()) <= 160
    assert "revision-bound lifecycle record" in text
    assert "project-management system" in text
    assert "`feature-specification`" in text
    assert "`session-handoff`" in text
    assert "`compatibility-migration`" in text
    assert "`adversarial-deep-review`" in text
    assert REFERENCE.is_file()
    reference = REFERENCE.read_text(encoding="utf-8")
    assert "## Canonical implementation record" in reference
    assert "## Feature index" in reference
    assert "## Handoff boundary" in reference


def test_feature_lifecycle_output_contract_and_state_guards_are_exact() -> None:
    text = SKILL.read_text(encoding="utf-8")

    assert output_headings(text) == HEADINGS
    assert all(f"`{state}`" in text for state in STATES)
    assert "verified_revision` equals `observed_revision" in text
    assert "exactly one safe next action" in text


def test_feature_lifecycle_evals_cover_boundaries_and_evidence() -> None:
    cases = load_cases()
    counts = Counter(case["category"] for case in cases)
    by_id = {case["id"]: case for case in cases}

    assert all(counts[category] >= minimum for category, minimum in REQUIRED.items())
    assert len({case["id"] for case in cases}) == len(cases)
    assert len({case["prompt"] for case in cases}) == len(cases)
    assert all(case.get("assertions") or case.get("forbidden_skills") for case in cases)
    assert by_id["lifecycle-positive-cross-session"]["expected_skills"] == ["feature-lifecycle"]
    assert by_id["lifecycle-negative-small-change"]["expected_skills"] == ["safe-code-change"]
    assert "feature-lifecycle" in by_id["lifecycle-negative-small-change"]["forbidden_skills"]
    assert by_id["lifecycle-conflict-handoff"]["expected_skills"] == [
        "feature-lifecycle",
        "session-handoff",
    ]
    assert by_id["lifecycle-conflict-adversarial-review"]["expected_skills"] == [
        "adversarial-deep-review",
        "feature-lifecycle",
    ]
    assert "refuses unsupported DONE state" in by_id["lifecycle-adversarial-false-done"]["assertions"]
