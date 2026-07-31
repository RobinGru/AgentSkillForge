from pathlib import Path

from scripts.check_distribution import (
    expected_skill_files,
    missing_skill_files,
    missing_support_files,
)

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "templates" / "AGENTS.md"


def test_repository_agents_template_has_the_compact_routing_contract() -> None:
    text = TEMPLATE.read_text(encoding="utf-8")
    skills = {
        "project-discovery",
        "feature-specification",
        "solution-framing",
        "failure-investigation",
        "safe-code-change",
        "fact-based-code-review",
        "product-interface-engineering",
        "performance-investigation",
        "compatibility-migration",
        "security-boundary-analysis",
        "vue-sfc-decomposition",
    }
    assert all(f"`{skill}`" in text for skill in skills)
    assert "workflow-navigator" not in text
    assert "For trivial, low-risk edits, work directly" in text
    assert "Read → Write → Re-read → Inspect diff → Run direct proof → Report" in text


def test_distribution_metadata_lists_every_skill_document() -> None:
    import tomllib

    metadata = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    groups = metadata["tool"]["setuptools"]["data-files"]
    listed = {Path(item) for files in groups.values() for item in files if item.startswith("skills/")}
    assert listed == expected_skill_files(ROOT)
    assert groups["share/agent-skill-forge/clients/zed"] == ["docs/clients/zed.md"]
    assert groups["share/agent-skill-forge/scripts"] == ["scripts/install_zed_skills.py"]
    assert groups["share/agent-skill-forge/templates"] == ["templates/AGENTS.md"]


def test_missing_skill_files_reports_missing_wheel_members(tmp_path: Path) -> None:
    wheel = tmp_path / "empty.whl"
    import zipfile

    with zipfile.ZipFile(wheel, "w"):
        pass
    assert missing_skill_files(ROOT, wheel) == expected_skill_files(ROOT)
    assert missing_support_files(wheel) == {
        "share/agent-skill-forge/clients/zed/zed.md",
        "share/agent-skill-forge/scripts/install_zed_skills.py",
        "share/agent-skill-forge/templates/AGENTS.md",
    }
