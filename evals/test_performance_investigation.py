from pathlib import Path
from typing import Any, cast

import yaml

from scripts.validate_repository import validate_skill

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "performance-investigation" / "SKILL.md"
EVALS = ROOT / "evals" / "performance-investigation.yaml"
REFERENCES = SKILL.parent / "references"


def test_performance_skill_is_portable() -> None:
    name, findings = validate_skill(SKILL)
    assert name == "performance-investigation"
    assert not [item for item in findings if item.level == "error"]
    assert len(SKILL.read_text(encoding="utf-8").splitlines()) <= 220


def test_performance_references_cover_required_facts() -> None:
    required = {
        "web-signals.md",
        "backend-signals.md",
        "experiment-design.md",
        "example-budgets.md",
        "investigation-examples.md",
    }
    assert required <= {path.name for path in REFERENCES.iterdir()}
    budgets = (REFERENCES / "example-budgets.md").read_text(encoding="utf-8").lower()
    assert "not universal requirements" in budgets
    examples = (REFERENCES / "investigation-examples.md").read_text(encoding="utf-8").lower()
    for signal in ("queueing", "vue", "memory spike"):
        assert signal in examples


def test_performance_evals_cover_trigger_boundaries() -> None:
    data = yaml.safe_load(EVALS.read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    raw_cases = data.get("cases")
    assert isinstance(raw_cases, list)
    assert all(isinstance(case, dict) for case in raw_cases)
    cases = {case["id"]: case for case in cast(list[dict[str, Any]], raw_cases)}
    assert "performance-investigation" in cases["performance-inp-regression"]["expected_skills"]
    assert "performance-investigation" in cases["performance-no-signal"]["expected_skills"]
    assert "performance-investigation" in cases["performance-image-optimization-nontrigger"]["forbidden_skills"]
    assert "vue-sfc-decomposition" in cases["performance-vue-input-lag"]["forbidden_skills"]
