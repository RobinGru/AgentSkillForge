from collections import Counter
from pathlib import Path

import yaml

from scripts.validate_repository import validate_skill

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "compatibility-migration" / "SKILL.md"
EVALS = ROOT / "evals" / "compatibility-migration.yaml"
REFERENCES = SKILL.parent / "references"
REQUIRED = {"positive": 5, "negative": 5, "conflict": 4, "output": 2, "adversarial": 2}
HEADINGS = [
    "## Migration target",
    "## Current contract",
    "## Consumers and owners",
    "## Compatibility envelope",
    "## Intermediate states",
    "## Data movement",
    "## Transition evidence",
    "## Rollback limits",
    "## Retirement conditions",
    "## Handoff state",
]
STATE_FIELDS = [
    "Preconditions",
    "Change",
    "Valid combinations",
    "Verification",
    "Rollback",
    "Exit criterion",
]


def load_cases() -> list[dict]:
    return yaml.safe_load(EVALS.read_text(encoding="utf-8"))["cases"]


def test_compatibility_migration_is_portable_and_at_most_180_lines() -> None:
    name, findings = validate_skill(SKILL)
    assert name == "compatibility-migration"
    assert not [finding for finding in findings if finding.level == "error"]
    assert len(SKILL.read_text(encoding="utf-8").splitlines()) <= 180


def test_compatibility_output_contract_is_exact_and_complete() -> None:
    text = SKILL.read_text(encoding="utf-8")
    section = text[text.index("## Output contract") :]
    headings = [line for line in section.splitlines() if line.startswith("## ")][1:]
    assert headings == HEADINGS
    assert all(field in section for field in STATE_FIELDS)


def test_compatibility_references_stay_within_declared_content_boundaries() -> None:
    assert {path.name for path in REFERENCES.iterdir()} == {
        "compatibility-envelope.md",
        "data-transition-checks.md",
    }
    envelope = (REFERENCES / "compatibility-envelope.md").read_text(encoding="utf-8").lower()
    for phrase in ("producer", "consumer", "version", "combination", "mixed", "owner"):
        assert phrase in envelope
    data = (REFERENCES / "data-transition-checks.md").read_text(encoding="utf-8").lower()
    for phrase in ("idempoten", "resume", "reconcil", "batch", "conflict", "code rollback", "data rollback"):
        assert phrase in data
    combined = envelope + data
    assert "release checklist" not in combined
    assert "incident communication" not in combined
    assert "```sql" not in combined


def test_compatibility_evals_meet_category_and_prompt_contract() -> None:
    cases = load_cases()
    counts = Counter(case["category"] for case in cases)
    assert len(cases) >= 18
    assert all(counts[category] >= minimum for category, minimum in REQUIRED.items())
    assert len({case["id"] for case in cases}) == len(cases)
    assert len({case["prompt"] for case in cases}) == len(cases)
    assert all(case.get("assertions") or case.get("forbidden_skills") for case in cases)
    required_cases = {
        "migration-conflict-security-token",
        "migration-conflict-review-step",
        "migration-adversarial-unsupported-zero-usage",
        "migration-adversarial-unrun-tests",
    }
    assert required_cases <= {case["id"] for case in cases}


def test_compatibility_evals_enforce_strategy_and_composition_routing() -> None:
    cases = {case["id"]: case for case in load_cases()}
    assert cases["migration-negative-strategy-choice"]["expected_skills"] == ["solution-framing"]
    assert "compatibility-migration" in cases["migration-negative-local-config"]["forbidden_skills"]
    assert cases["migration-conflict-backfill-performance"]["expected_skills"] == [
        "compatibility-migration",
        "performance-investigation",
    ]
    assert cases["migration-conflict-interface-coexistence"]["expected_skills"] == [
        "compatibility-migration",
        "product-interface-engineering",
    ]
