from pathlib import Path
from typing import Any, cast

import yaml

from scripts.validate_repository import validate_skill

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "product-interface-engineering" / "SKILL.md"
EVALS = ROOT / "evals" / "product-interface-engineering.yaml"


def test_interface_skill_is_portable() -> None:
    name, findings = validate_skill(SKILL)
    assert name == "product-interface-engineering"
    assert not [item for item in findings if item.level == "error"]
    content = SKILL.read_text(encoding="utf-8")
    assert len(content.splitlines()) <= 250
    for signal in ("UI/UX", "frontend", "dialogs or modals", "keyboard", "responsive or mobile"):
        assert signal in content


def test_interface_evals_cover_boundaries() -> None:
    data = yaml.safe_load(EVALS.read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    raw_cases = data.get("cases")
    assert isinstance(raw_cases, list)
    assert all(isinstance(case, dict) for case in raw_cases)
    cases = {case["id"]: case for case in cast(list[dict[str, Any]], raw_cases)}
    assert "product-interface-engineering" in cases["interface-checkout-form"]["expected_skills"]
    assert "product-interface-engineering" in cases["interface-short-modal-de"]["expected_skills"]
    assert "product-interface-engineering" in cases["interface-responsive-navigation-de"]["expected_skills"]
    assert "product-interface-engineering" in cases["interface-figma-implementation"]["expected_skills"]
    assert "product-interface-engineering" in cases["interface-keyboard-focus"]["expected_skills"]
    assert "product-interface-engineering" in cases["interface-ui-debug-short"]["expected_skills"]
    assert "product-interface-engineering" in cases["interface-token-nontrigger"]["forbidden_skills"]
    assert "product-interface-engineering" in cases["interface-backend-nontrigger"]["forbidden_skills"]
    assert "product-interface-engineering" in cases["interface-vue-structural-nonprimary"]["forbidden_skills"]
