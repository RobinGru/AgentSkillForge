from pathlib import Path

import yaml

from scripts.validate_repository import validate_skill

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "product-interface-engineering" / "SKILL.md"
EVALS = ROOT / "evals" / "product-interface-engineering.yaml"


def test_interface_skill_is_portable() -> None:
    name, findings = validate_skill(SKILL)
    assert name == "product-interface-engineering"
    assert not [item for item in findings if item.level == "error"]
    assert len(SKILL.read_text(encoding="utf-8").splitlines()) <= 250


def test_interface_evals_cover_boundaries() -> None:
    cases = {case["id"]: case for case in yaml.safe_load(EVALS.read_text(encoding="utf-8"))["cases"]}
    assert "product-interface-engineering" in cases["interface-checkout-form"]["expected_skills"]
    assert "product-interface-engineering" in cases["interface-backend-nontrigger"]["forbidden_skills"]
    assert "product-interface-engineering" in cases["interface-vue-structural-nonprimary"]["forbidden_skills"]
