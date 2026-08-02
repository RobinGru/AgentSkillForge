from pathlib import Path
from typing import Any, cast

import yaml

from scripts.validate_repository import validate_skill

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "quality" / "fact-based-code-review" / "SKILL.md"
EVALS = ROOT / "evals" / "fact-based-code-review.yaml"


def test_review_skill_is_portable() -> None:
    name, findings = validate_skill(SKILL)

    assert name == "fact-based-code-review"
    assert not [finding for finding in findings if finding.level == "error"]
    assert len(SKILL.read_text(encoding="utf-8").splitlines()) <= 220


def test_review_evals_cover_fact_boundaries() -> None:
    data = yaml.safe_load(EVALS.read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    raw_cases = data.get("cases")
    assert isinstance(raw_cases, list)
    assert all(isinstance(case, dict) for case in raw_cases)
    cases = {case["id"]: case for case in cast(list[dict[str, Any]], raw_cases)}

    assert len(cases) == 5
    assert "REQUEST CHANGES" in cases["review-data-loss"]["assertions"][0]
    assert "APPROVE" in cases["review-small-correct-change"]["assertions"][0]
    assert "BLOCKED" in cases["review-api-break-without-spec"]["assertions"][0]
    assert "Preference" in cases["review-style-preference"]["assertions"][0]
    assert "Missing information" in cases["review-unverified-performance-claim"]["assertions"][0]
