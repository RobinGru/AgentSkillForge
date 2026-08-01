from collections import Counter
from pathlib import Path

import yaml

from scripts.validate_repository import validate_skill

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "adversarial-deep-review" / "SKILL.md"
EVALS = ROOT / "evals" / "adversarial-deep-review.yaml"
REQUIRED = {"positive": 5, "negative": 5, "conflict": 4, "output": 2, "adversarial": 2}
HEADINGS = [
    "## Review scope",
    "## Risk basis",
    "## Intent and critical invariants",
    "## Assumptions under attack",
    "## Scenario register",
    "## Verification record",
    "## Adversarial findings",
    "## Checks not run",
    "## Blast radius and recovery",
    "## Residual uncertainty",
    "## Handoff state",
]


def load_cases() -> list[dict]:
    return yaml.safe_load(EVALS.read_text(encoding="utf-8"))["cases"]


def test_adversarial_deep_review_has_portable_metadata() -> None:
    name, findings = validate_skill(SKILL)
    assert name == "adversarial-deep-review"
    assert not [finding for finding in findings if finding.level == "error"]


def test_adversarial_deep_review_has_exact_output_headings() -> None:
    text = SKILL.read_text(encoding="utf-8")
    section = text[text.index("## Output contract") :]
    assert [line for line in section.splitlines() if line.startswith("## ")][1:] == HEADINGS


def test_adversarial_deep_review_evals_meet_category_and_prompt_contract() -> None:
    cases = load_cases()
    counts = Counter(case["category"] for case in cases)
    assert len(cases) >= 18
    assert all(counts[category] >= minimum for category, minimum in REQUIRED.items())
    assert len({case["id"] for case in cases}) == len(cases)
    assert len({case["prompt"] for case in cases}) == len(cases)
    assert all(case.get("assertions") or case.get("forbidden_skills") for case in cases)


def test_adversarial_deep_review_enforces_critical_routing_boundaries() -> None:
    cases = {case["id"]: case for case in load_cases()}
    assert cases["adversarial-positive-payment-retry"]["expected_skills"] == [
        "adversarial-deep-review"
    ]
    assert cases["adversarial-negative-routine-review"]["expected_skills"] == [
        "fact-based-code-review"
    ]
    assert "adversarial-deep-review" in cases["adversarial-negative-routine-review"]["forbidden_skills"]
    assert cases["adversarial-negative-high-risk-ordinary-review"]["expected_skills"] == [
        "fact-based-code-review"
    ]
    assert cases["adversarial-negative-system-threat-model"]["expected_skills"] == [
        "security-boundary-analysis"
    ]
    assert cases["adversarial-negative-observed-failure"]["expected_skills"] == [
        "failure-investigation"
    ]
    assert cases["adversarial-conflict-review-handoff"]["expected_skills"] == [
        "adversarial-deep-review",
        "fact-based-code-review",
    ]
    assert cases["adversarial-conflict-security-contract"]["expected_skills"] == [
        "adversarial-deep-review",
        "security-boundary-analysis",
    ]
    assert "`feature-lifecycle`" in SKILL.read_text(encoding="utf-8")
    assert cases["adversarial-conflict-feature-lifecycle"]["expected_skills"] == [
        "adversarial-deep-review",
        "feature-lifecycle",
        "fact-based-code-review",
    ]
