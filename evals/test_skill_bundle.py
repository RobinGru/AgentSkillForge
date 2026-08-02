import zipfile
from pathlib import Path

from scripts.build_skill_bundle import build_bundle
from scripts.install_skills import available_skills

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills"


def test_flat_skill_bundle_contains_each_complete_skill_directory(tmp_path: Path) -> None:
    output = tmp_path / "agent-skill-forge-skills.zip"

    built = build_bundle(SOURCE, output)

    assert built == sorted(available_skills(SOURCE))
    with zipfile.ZipFile(output) as archive:
        members = set(archive.namelist())
    assert {f"{name}/SKILL.md" for name in built} <= members
    assert not any(member.startswith(("core/", "planning/", "quality/", "specialized/")) for member in members)
    assert "repository-onboarding/references/repository-evidence.md" in members
    assert "solution-framing/assets/solution-brief-template.md" in members


def test_installer_discovers_nested_source_and_installs_flat_target(tmp_path: Path) -> None:
    skills = available_skills(SOURCE)

    assert skills["safe-code-change"] == SOURCE / "core" / "safe-code-change"
    assert skills["security-boundary-analysis"] == SOURCE / "quality" / "security-boundary-analysis"
