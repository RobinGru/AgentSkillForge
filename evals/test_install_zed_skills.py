from pathlib import Path

import pytest

from scripts.install_zed_skills import available_skills, install_skills

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills"


def test_zed_installer_copies_selected_skill_with_references(tmp_path: Path) -> None:
    installed = install_skills(SOURCE, tmp_path / "skills", ["solution-framing"], force=False)
    destination = installed[0]
    assert (destination / "SKILL.md").is_file()
    assert (destination / "references" / "decision-record.md").is_file()
    assert (destination / "assets" / "solution-brief-template.md").is_file()


@pytest.mark.parametrize(
    ("skill", "references"),
    [
        ("failure-investigation", {"evidence-strength.md", "intermittent-failures.md"}),
        ("security-boundary-analysis", {"agentic-boundaries.md", "risk-reasoning.md"}),
        ("compatibility-migration", {"compatibility-envelope.md", "data-transition-checks.md"}),
    ],
)
def test_zed_installer_copies_each_new_skill_with_references(
    tmp_path: Path, skill: str, references: set[str]
) -> None:
    destination = install_skills(SOURCE, tmp_path / skill, [skill], force=False)[0]
    assert (destination / "SKILL.md").is_file()
    assert references == {path.name for path in (destination / "references").iterdir()}


def test_zed_installer_copies_all_skills_and_new_references(tmp_path: Path) -> None:
    target = tmp_path / "all-skills"
    installed = install_skills(SOURCE, target, None, force=False)

    assert {path.name for path in installed} == set(available_skills(SOURCE))
    expected_references = {
        "failure-investigation": {"evidence-strength.md", "intermittent-failures.md"},
        "security-boundary-analysis": {"agentic-boundaries.md", "risk-reasoning.md"},
        "compatibility-migration": {"compatibility-envelope.md", "data-transition-checks.md"},
    }
    for skill, references in expected_references.items():
        destination = target / skill
        assert (destination / "SKILL.md").is_file()
        assert references == {path.name for path in (destination / "references").iterdir()}


def test_zed_installer_requires_force_before_replacement(tmp_path: Path) -> None:
    target = tmp_path / "skills"
    install_skills(SOURCE, target, ["safe-code-change"], force=False)
    with pytest.raises(FileExistsError):
        install_skills(SOURCE, target, ["safe-code-change"], force=False)
    install_skills(SOURCE, target, ["safe-code-change"], force=True)
    assert (target / "safe-code-change" / "SKILL.md").is_file()


def test_zed_installer_rejects_unknown_skill(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="unknown skill"):
        install_skills(SOURCE, tmp_path / "skills", ["missing-skill"], force=False)


def test_zed_installer_discovers_all_distributed_skills() -> None:
    assert set(available_skills(SOURCE)) == {
        "solution-framing",
        "safe-code-change",
        "fact-based-code-review",
        "product-interface-engineering",
        "performance-investigation",
        "vue-sfc-decomposition",
        "failure-investigation",
        "security-boundary-analysis",
        "compatibility-migration",
        "project-discovery",
        "feature-specification",
    }
