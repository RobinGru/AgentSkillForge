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

    assert "Use a skill only when its workflow materially improves the task" in text
    assert "Handle trivial, localized, low-risk changes directly" in text
    assert "Use the narrowest applicable skill" in text
    assert "Do not activate skills based on keywords alone" in text
    assert "Do not combine multiple skills unless each is independently necessary" in text
    assert "`feature-delivery`" in text
    assert "Never use parallel agents" in text
    assert "workflow-navigator" not in text
    assert "Targeted read → Write → Inspect changed range → Narrow proof → Compact report" in text


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
        "scripts/build_skill_bundle.py",
    ]
    assert groups["share/agent-skill-forge/templates"] == [
        "templates/AGENTS.md",
        "templates/AGENTS-AIO.md",
    ]


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
        "share/agent-skill-forge/scripts/build_skill_bundle.py",
        "share/agent-skill-forge/templates/AGENTS.md",
        "share/agent-skill-forge/templates/AGENTS-AIO.md",
    }
