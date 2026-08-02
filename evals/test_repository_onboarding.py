from collections import Counter
from pathlib import Path
from typing import Any, cast

import yaml

from scripts.validate_repository import validate_skill

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "core" / "repository-onboarding" / "SKILL.md"
EVALS = ROOT / "evals" / "repository-onboarding.yaml"
HEADINGS = [
    "## Repository identity", "## Instructions and sources of truth",
    "## Structure and boundaries", "## Build and runtime", "## Verification model",
    "## Interfaces, data, and side effects", "## Risks, contradictions, and unknowns",
    "## Knowledge candidates", "## Handoff state",
]


def load_cases() -> list[dict[str, Any]]:
    data = yaml.safe_load(EVALS.read_text(encoding="utf-8"))
    assert isinstance(data, dict) and isinstance(data.get("cases"), list)
    return cast(list[dict[str, Any]], data["cases"])


def test_repository_onboarding_is_portable_and_evidence_based() -> None:
    name, findings = validate_skill(SKILL)
    text = SKILL.read_text(encoding="utf-8")
    assert name == "repository-onboarding"
    assert not [finding for finding in findings if finding.level == "error"]
    assert len(text.splitlines()) <= 240
    assert (SKILL.parent / "references" / "repository-evidence.md").is_file()
    assert all(status in text for status in ("`DISCOVERED`", "`EXECUTED`", "`BLOCKED`", "`STALE OR CONFLICTING`"))


def test_repository_onboarding_output_contract_is_exact() -> None:
    section = SKILL.read_text(encoding="utf-8").split("## Output contract", 1)[1]
    assert [line for line in section.splitlines() if line.startswith("## ")] == HEADINGS


def test_repository_onboarding_evals_cover_boundaries() -> None:
    cases = load_cases()
    counts = Counter(case["category"] for case in cases)
    assert len(cases) == 18
    assert counts == {"positive": 5, "negative": 5, "conflict": 3, "output": 2, "adversarial": 3}
    by_id = {case["id"]: case for case in cases}
    assert len(by_id) == len(cases)
    assert by_id["onboarding-positive-unfamiliar"]["expected_skills"] == ["repository-onboarding"]
    assert "repository-onboarding" in by_id["onboarding-negative-failure"]["forbidden_skills"]
    assert by_id["onboarding-conflict-curate"]["expected_skills"] == ["repository-onboarding", "repository-knowledge-curation"]
