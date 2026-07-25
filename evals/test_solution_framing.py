from pathlib import Path

import yaml

from scripts.validate_repository import validate_skill


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "solution-framing" / "SKILL.md"
EVALS = ROOT / "evals" / "solution-framing.yaml"
REQUIRED_HEADINGS = [
    "## Decision",
    "## Evidence",
    "## Assumptions",
    "## Boundaries",
    "## Selected approach",
    "## Rejected approaches",
    "## Risks and mitigations",
    "## Acceptance evidence",
    "## Open blockers",
    "## Handoff state",
]


def test_solution_framing_is_portable_and_within_limit() -> None:
    name, findings = validate_skill(SKILL)

    assert name == "solution-framing"
    assert not [finding for finding in findings if finding.level == "error"]
    assert len(SKILL.read_text(encoding="utf-8").splitlines()) <= 220


def test_solution_framing_template_has_an_objective_contract() -> None:
    template = (SKILL.parent / "assets" / "solution-brief-template.md").read_text(encoding="utf-8")

    assert all(heading in template for heading in REQUIRED_HEADINGS)


def test_solution_framing_eval_manifest_covers_required_boundaries() -> None:
    data = yaml.safe_load(EVALS.read_text(encoding="utf-8"))
    cases = {case["id"]: case for case in data["cases"]}

    assert len(cases) == 6
    assert "solution-framing" in cases["solution-framing-auth-ambiguity"]["expected_skills"]
    assert "solution-framing" in cases["solution-framing-integration-boundaries"]["expected_skills"]
    assert "solution-framing" in cases["solution-framing-spacing-nontrigger"]["forbidden_skills"]
    assert "solution-framing" in cases["solution-framing-accepted-plan-nontrigger"]["forbidden_skills"]
    assert cases["solution-framing-ui-composition"]["expected_skills"] == [
        "solution-framing",
        "product-interface-engineering",
    ]
    assert cases["solution-framing-performance-routing"]["expected_skills"] == [
        "performance-investigation"
    ]
