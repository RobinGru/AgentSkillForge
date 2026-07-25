from collections import Counter
from pathlib import Path

import yaml

from scripts.validate_repository import validate_skill

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "failure-investigation" / "SKILL.md"
EVALS = ROOT / "evals" / "failure-investigation.yaml"
REFERENCES = SKILL.parent / "references"
REQUIRED = {"positive": 5, "negative": 5, "conflict": 4, "output": 2, "adversarial": 2}
HEADINGS = [
    "## Failure signal",
    "## Evidence inventory",
    "## Reproduction status",
    "## Causal boundary",
    "## Competing explanations",
    "## Discriminating checks",
    "## Supported cause",
    "## Unresolved conditions",
    "## Recommended guard",
    "## Handoff state",
]


def load_cases() -> list[dict]:
    return yaml.safe_load(EVALS.read_text(encoding="utf-8"))["cases"]


def output_headings(text: str) -> list[str]:
    start = text.index("## Output contract")
    return [line for line in text[start:].splitlines() if line.startswith("## ")][1:]


def test_failure_investigation_is_portable_and_at_most_180_lines() -> None:
    name, findings = validate_skill(SKILL)
    assert name == "failure-investigation"
    assert not [finding for finding in findings if finding.level == "error"]
    assert len(SKILL.read_text(encoding="utf-8").splitlines()) <= 180


def test_failure_investigation_has_exact_output_headings() -> None:
    assert output_headings(SKILL.read_text(encoding="utf-8")) == HEADINGS


def test_failure_references_stay_within_declared_content_boundaries() -> None:
    assert {path.name for path in REFERENCES.iterdir()} == {
        "evidence-strength.md",
        "intermittent-failures.md",
    }
    evidence = (REFERENCES / "evidence-strength.md").read_text(encoding="utf-8").lower()
    for phrase in ("observed", "reproduced", "provided", "inferred", "unknown", "contradict", "not run"):
        assert phrase in evidence
    intermittent = (REFERENCES / "intermittent-failures.md").read_text(encoding="utf-8").lower()
    for phrase in ("timing", "order", "shared state", "random", "environment", "external", "resource"):
        assert phrase in intermittent
    combined = evidence + intermittent
    assert "curl " not in combined
    assert "```python" not in combined
    assert "```bash" not in combined


def test_failure_evals_meet_category_and_prompt_contract() -> None:
    cases = load_cases()
    counts = Counter(case["category"] for case in cases)
    assert len(cases) >= 18
    assert all(counts[category] >= minimum for category, minimum in REQUIRED.items())
    assert len({case["id"] for case in cases}) == len(cases)
    assert len({case["prompt"] for case in cases}) == len(cases)
    assert all(case.get("assertions") or case.get("forbidden_skills") for case in cases)
    assert "failure-conflict-review-followup" in {case["id"] for case in cases}


def test_failure_evals_enforce_routing_boundaries() -> None:
    cases = {case["id"]: case for case in load_cases()}
    assert cases["failure-negative-known-null-cause"]["expected_skills"] == ["safe-code-change"]
    assert cases["failure-negative-latency-regression"]["expected_skills"] == ["performance-investigation"]
    assert "failure-investigation" in cases["failure-negative-review-fix"]["forbidden_skills"]
    assert cases["failure-conflict-interface-followup"]["expected_skills"] == [
        "failure-investigation",
        "product-interface-engineering",
    ]
    assert cases["failure-conflict-vue-followup"]["expected_skills"] == [
        "failure-investigation",
        "vue-sfc-decomposition",
    ]
