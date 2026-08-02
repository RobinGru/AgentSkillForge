from collections import Counter
from pathlib import Path
from typing import Any, cast

import yaml

from scripts.validate_repository import validate_skill

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "quality" / "security-boundary-analysis" / "SKILL.md"
EVALS = ROOT / "evals" / "security-boundary-analysis.yaml"
REFERENCES = SKILL.parent / "references"
REQUIRED = {"positive": 5, "negative": 5, "conflict": 4, "output": 2, "adversarial": 2}
HEADINGS = [
    "## Authorized scope",
    "## System evidence",
    "## Trust transitions",
    "## Protected values",
    "## Attacker capabilities",
    "## Capability and side-effect inventory",
    "## Abuse chains",
    "## Existing controls",
    "## Required controls",
    "## Residual uncertainty",
    "## Handoff state",
]
ABUSE_FIELDS = [
    "Entry condition",
    "Trust transition",
    "Attacker action",
    "Affected value",
    "Existing control",
    "Control gap",
    "Impact",
    "Likelihood",
    "Confidence",
    "Verification",
]


def load_cases() -> list[dict[str, Any]]:
    data = yaml.safe_load(EVALS.read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    cases = data.get("cases")
    assert isinstance(cases, list)
    assert all(isinstance(case, dict) for case in cases)
    return cast(list[dict[str, Any]], cases)


def test_security_boundary_analysis_is_portable_and_at_most_180_lines() -> None:
    name, findings = validate_skill(SKILL)
    assert name == "security-boundary-analysis"
    assert not [finding for finding in findings if finding.level == "error"]
    assert len(SKILL.read_text(encoding="utf-8").splitlines()) <= 180


def test_security_output_contract_is_exact_and_complete() -> None:
    text = SKILL.read_text(encoding="utf-8")
    section = text[text.index("## Output contract") :]
    headings = [line for line in section.splitlines() if line.startswith("## ")][1:]
    assert headings == HEADINGS
    assert all(field in section for field in ABUSE_FIELDS)


def test_security_references_stay_within_declared_content_boundaries() -> None:
    assert {path.name for path in REFERENCES.iterdir()} == {"agentic-boundaries.md", "risk-reasoning.md"}
    boundaries = (REFERENCES / "agentic-boundaries.md").read_text(encoding="utf-8").lower()
    for phrase in ("metadata", "repository", "credential", "sandbox", "persistent", "external", "provenance"):
        assert phrase in boundaries
    risk = (REFERENCES / "risk-reasoning.md").read_text(encoding="utf-8").lower()
    for phrase in ("likelihood", "impact", "existing control", "deployment", "uncertain"):
        assert phrase in risk
    combined = boundaries + risk
    assert "owasp top 10" not in combined
    assert "active exploit" not in combined
    assert "cvss" not in combined


def test_security_evals_meet_category_and_prompt_contract() -> None:
    cases = load_cases()
    counts = Counter(case["category"] for case in cases)
    assert len(cases) >= 18
    assert all(counts[category] >= minimum for category, minimum in REQUIRED.items())
    assert len({case["id"] for case in cases}) == len(cases)
    assert len({case["prompt"] for case in cases}) == len(cases)
    assert all(case.get("assertions") or case.get("forbidden_skills") for case in cases)
    required_cases = {
        "security-conflict-measured-dos",
        "security-adversarial-skill-secrets",
        "security-adversarial-unauthorized-system",
    }
    assert required_cases <= {case["id"] for case in cases}


def test_security_evals_enforce_explicit_scope_and_composition() -> None:
    cases = {case["id"]: case for case in load_cases()}
    assert "security-boundary-analysis" in cases["security-negative-auth-review"]["forbidden_skills"]
    assert cases["security-negative-provider-choice"]["expected_skills"] == ["solution-framing"]
    assert cases["security-conflict-control-implementation"]["expected_skills"] == [
        "security-boundary-analysis",
        "safe-code-change",
    ]
    assert cases["security-conflict-migration"]["expected_skills"] == [
        "security-boundary-analysis",
        "compatibility-migration",
    ]
