from pathlib import Path
from typing import Any, cast

import yaml

from scripts.validate_repository import validate_skill

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "specialized" / "vue-sfc-decomposition" / "SKILL.md"
EVALS = ROOT / "evals" / "vue-sfc-decomposition.yaml"


def test_vue_decomposition_skill_is_portable() -> None:
    name, findings = validate_skill(SKILL)
    assert name == "vue-sfc-decomposition"
    assert not [item for item in findings if item.level == "error"]
    assert len(SKILL.read_text(encoding="utf-8").splitlines()) <= 220


def test_vue_decomposition_evals_cover_seam_selection() -> None:
    data = yaml.safe_load(EVALS.read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    raw_cases = data.get("cases")
    assert isinstance(raw_cases, list)
    assert all(isinstance(case, dict) for case in raw_cases)
    cases = {case["id"]: case for case in cast(list[dict[str, Any]], raw_cases)}
    assert "vue-sfc-decomposition" in cases["vue-visual-sections"]["expected_skills"]
    assert "vue-sfc-decomposition" in cases["vue-reusable-form-logic"]["expected_skills"]
    assert "vue-sfc-decomposition" in cases["vue-api-mapping-and-cache"]["expected_skills"]
    assert "vue-sfc-decomposition" in cases["vue-long-but-stable"]["forbidden_skills"]


def test_vue_skill_protects_reactivity_and_cleanup() -> None:
    text = SKILL.read_text(encoding="utf-8").lower()
    assert "reactivity" in text
    assert "cleanup" in text
    assert "one seam per patch" in text
