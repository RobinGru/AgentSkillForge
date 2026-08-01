from collections import Counter
from pathlib import Path
from typing import Any, cast

import yaml

from scripts.validate_repository import validate_skill

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "session-handoff" / "SKILL.md"
EVALS = ROOT / "evals" / "session-handoff.yaml"
REQUIRED = {"positive": 5, "negative": 5, "conflict": 3, "output": 2, "adversarial": 2}
HEADINGS = [
    "## Continuation objective",
    "## Source artifacts",
    "## Repository state",
    "## Completed and active work",
    "## Evidence and checks",
    "## Open decisions and unknowns",
    "## Risks and constraints",
    "## Next safe action",
    "## Handoff state",
]
STATES = [
    "READY TO CONTINUE",
    "DECISION REQUIRED",
    "MORE EVIDENCE REQUIRED",
    "ENVIRONMENT ACCESS REQUIRED",
    "EXTERNAL DEPENDENCY PENDING",
    "NO SAFE CONTINUATION STATE",
]


def load_cases() -> list[dict[str, Any]]:
    data = yaml.safe_load(EVALS.read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    cases = data.get("cases")
    assert isinstance(cases, list)
    assert all(isinstance(case, dict) for case in cases)
    return cast(list[dict[str, Any]], cases)


def output_headings(text: str) -> list[str]:
    start = text.index("## Output contract")
    return [line for line in text[start:].splitlines() if line.startswith("## ")][1:]


def test_session_handoff_is_portable_and_compact() -> None:
    name, findings = validate_skill(SKILL)
    assert name == "session-handoff"
    assert not [finding for finding in findings if finding.level == "error"]
    assert len(SKILL.read_text(encoding="utf-8").splitlines()) <= 180


def test_session_handoff_has_exact_output_contract_and_states() -> None:
    text = SKILL.read_text(encoding="utf-8")
    assert output_headings(text) == HEADINGS
    for state in STATES:
        assert f"`{state}`" in text
    assert "exactly one bounded action" in text
    assert "exactly one allowed state" in text


def test_session_handoff_evals_cover_boundaries() -> None:
    cases = load_cases()
    counts = Counter(case["category"] for case in cases)
    assert len(cases) >= 18
    assert all(counts[category] >= minimum for category, minimum in REQUIRED.items())
    assert len({case["id"] for case in cases}) == len(cases)
    assert len({case["prompt"] for case in cases}) == len(cases)
    assert all(case.get("assertions") or case.get("forbidden_skills") for case in cases)


def test_session_handoff_evals_route_near_misses_and_combinations() -> None:
    cases = {case["id"]: case for case in load_cases()}
    assert cases["handoff-negative-completed"]["forbidden_skills"] == ["session-handoff"]
    assert cases["handoff-negative-specification"]["expected_skills"] == ["feature-specification"]
    assert cases["handoff-conflict-investigation"]["expected_skills"] == [
        "failure-investigation",
        "session-handoff",
    ]
    assert cases["handoff-conflict-lifecycle"]["expected_skills"] == [
        "feature-lifecycle",
        "session-handoff",
    ]
