from pathlib import Path
from typing import Any, cast

import yaml

from scripts.validate_repository import validate_skill

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "core" / "safe-code-change" / "SKILL.md"
EVALS = ROOT / "evals" / "safe-code-change.yaml"


def test_safe_code_change_is_portable_and_compact() -> None:
    name, findings = validate_skill(SKILL)

    assert name == "safe-code-change"
    assert not [finding for finding in findings if finding.level == "error"]
    text = SKILL.read_text(encoding="utf-8")
    assert len(text.splitlines()) <= 220
    assert "`feature-lifecycle`" in text


def test_safe_code_change_evals_cover_triggers_and_routing() -> None:
    data = yaml.safe_load(EVALS.read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    raw_cases = data.get("cases")
    assert isinstance(raw_cases, list)
    assert all(isinstance(case, dict) for case in raw_cases)
    cases = {case["id"]: case for case in cast(list[dict[str, Any]], raw_cases)}

    assert "safe-code-change" in cases["safe-code-change-local-bugfix"]["expected_skills"]
    assert "safe-code-change" in cases["safe-code-change-small-refactor"]["expected_skills"]
    assert "safe-code-change" in cases["safe-code-change-review-nontrigger"]["forbidden_skills"]
    assert cases["safe-code-change-performance-routing"]["expected_skills"] == [
        "performance-investigation"
    ]
    assert cases["safe-code-change-vue-composition"]["expected_skills"] == [
        "vue-sfc-decomposition",
        "safe-code-change",
    ]
    assert cases["safe-code-change-lifecycle-composition"]["expected_skills"] == [
        "safe-code-change",
        "feature-lifecycle",
    ]
