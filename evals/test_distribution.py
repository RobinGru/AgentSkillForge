import tomllib
import zipfile
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
        "feature-lifecycle",
        "solution-framing",
        "failure-investigation",
        "safe-code-change",
        "fact-based-code-review",
        "adversarial-deep-review",
        "product-interface-engineering",
        "performance-investigation",
        "compatibility-migration",
        "security-boundary-analysis",
        "vue-sfc-decomposition",
        "session-handoff",
    }
    assert all(f"`{skill}`" in text for skill in skills)
    assert "workflow-navigator" not in text
    assert "For trivial, low-risk edits, work directly" in text
    assert "Read → Write → Re-read → Inspect diff → Run direct proof → Report" in text


def test_distribution_metadata_lists_every_skill_document() -> None:
    metadata = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    tool = metadata.get("tool")
    assert isinstance(tool, dict)
    setuptools = tool.get("setuptools")
    assert isinstance(setuptools, dict)
    data_files = setuptools.get("data-files")
    assert isinstance(data_files, dict)
    groups: dict[str, list[str]] = {}
    for group, files in data_files.items():
        assert isinstance(group, str)
        assert isinstance(files, list)
        assert all(isinstance(file, str) for file in files)
        groups[group] = [file for file in files if isinstance(file, str)]
    listed = {Path(item) for files in groups.values() for item in files if item.startswith("skills/")}
    assert listed == expected_skill_files(ROOT)
    assert groups["share/agent-skill-forge"] == ["README.md", "THIRD_PARTY_NOTICES.md", "docs/compatibility.md"]
    assert groups["share/agent-skill-forge/clients/codex"] == ["docs/clients/codex.md"]
    assert groups["share/agent-skill-forge/clients/zed"] == ["docs/clients/zed.md"]
    assert groups["share/agent-skill-forge/scripts"] == [
        "scripts/install_skills.py",
        "scripts/install_zed_skills.py",
        "scripts/install_codex_skills.py",
    ]
    assert groups["share/agent-skill-forge/templates"] == ["templates/AGENTS.md"]


def test_missing_skill_files_reports_missing_wheel_members(tmp_path: Path) -> None:
    wheel = tmp_path / "empty.whl"

    with zipfile.ZipFile(wheel, "w"):
        pass
    assert missing_skill_files(ROOT, wheel) == expected_skill_files(ROOT)
    assert missing_support_files(wheel) == {
        "share/agent-skill-forge/compatibility.md",
        "share/agent-skill-forge/clients/codex/codex.md",
        "share/agent-skill-forge/clients/zed/zed.md",
        "share/agent-skill-forge/scripts/install_skills.py",
        "share/agent-skill-forge/scripts/install_zed_skills.py",
        "share/agent-skill-forge/scripts/install_codex_skills.py",
        "share/agent-skill-forge/templates/AGENTS.md",
    }
