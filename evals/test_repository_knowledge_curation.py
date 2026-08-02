from collections import Counter
from pathlib import Path
from typing import Any, cast

import yaml

from scripts.validate_repository import validate_skill

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "core" / "repository-knowledge-curation" / "SKILL.md"
EVALS = ROOT / "evals" / "repository-knowledge-curation.yaml"
HEADINGS = [
    "## Knowledge candidate", "## Evidence and scope", "## Placement decision",
    "## Documentation change", "## Conflicts and retirements", "## Verification",
    "## Handoff state",
]


def load_cases() -> list[dict[str, Any]]:
    data = yaml.safe_load(EVALS.read_text(encoding="utf-8"))
    assert isinstance(data, dict) and isinstance(data.get("cases"), list)
    return cast(list[dict[str, Any]], data["cases"])


def test_repository_knowledge_curation_is_portable_and_canonical() -> None:
    name, findings = validate_skill(SKILL)
    text = SKILL.read_text(encoding="utf-8")
    assert name == "repository-knowledge-curation"
    assert not [finding for finding in findings if finding.level == "error"]
    assert len(text.splitlines()) <= 240
    assert (SKILL.parent / "references" / "knowledge-placement.md").is_file()
    assert "Choose exactly one primary destination" in text
    assert "`NO DURABLE UPDATE`" in text


def test_repository_knowledge_curation_output_contract_is_exact() -> None:
    section = SKILL.read_text(encoding="utf-8").split("## Output contract", 1)[1]
    assert [line for line in section.splitlines() if line.startswith("## ")] == HEADINGS


def test_repository_knowledge_curation_evals_cover_boundaries() -> None:
    cases = load_cases()
    counts = Counter(case["category"] for case in cases)
    assert len(cases) == 18
    assert counts == {"positive": 5, "negative": 5, "conflict": 3, "output": 2, "adversarial": 3}
    by_id = {case["id"]: case for case in cases}
    assert len(by_id) == len(cases)
    assert by_id["curation-positive-test-guide"]["expected_skills"] == ["repository-knowledge-curation"]
    assert "repository-knowledge-curation" in by_id["curation-negative-decision"]["forbidden_skills"]
    assert by_id["curation-conflict-onboarding"]["expected_skills"] == ["repository-onboarding", "repository-knowledge-curation"]
