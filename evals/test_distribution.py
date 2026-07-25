from pathlib import Path

from scripts.check_distribution import expected_skill_files, missing_skill_files, missing_zed_support_files


ROOT = Path(__file__).resolve().parents[1]


def test_distribution_metadata_lists_every_skill_document() -> None:
    import tomllib

    metadata = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    groups = metadata["tool"]["setuptools"]["data-files"]
    listed = {Path(item) for files in groups.values() for item in files if item.startswith("skills/")}
    assert listed == expected_skill_files(ROOT)
    assert groups["share/agent-skill-forge/clients/zed"] == ["docs/clients/zed.md"]
    assert groups["share/agent-skill-forge/scripts"] == ["scripts/install_zed_skills.py"]


def test_missing_skill_files_reports_missing_wheel_members(tmp_path: Path) -> None:
    wheel = tmp_path / "empty.whl"
    import zipfile

    with zipfile.ZipFile(wheel, "w"):
        pass
    assert missing_skill_files(ROOT, wheel) == expected_skill_files(ROOT)
    assert missing_zed_support_files(wheel) == {
        "share/agent-skill-forge/clients/zed/zed.md",
        "share/agent-skill-forge/scripts/install_zed_skills.py",
    }
