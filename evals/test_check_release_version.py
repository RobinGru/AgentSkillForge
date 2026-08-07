from pathlib import Path

from scripts.check_release_version import check_release_version, expected_skill_version


def write_repository(root: Path, package_version: str, skill_version: str) -> None:
    (root / "skills" / "example").mkdir(parents=True)
    (root / "pyproject.toml").write_text(
        f"[project]\nversion = {package_version!r}\n", encoding="utf-8"
    )
    (root / "skills" / "example" / "SKILL.md").write_text(
        f"---\nmetadata:\n  version: {skill_version}\n---\n", encoding="utf-8"
    )


def test_expected_skill_version_converts_prerelease_versions() -> None:
    assert expected_skill_version("1.2.3") == "1.2.3"
    assert expected_skill_version("1.2.3b4") == "1.2.3-beta.4"
    assert expected_skill_version("1.2.3rc1") == "1.2.3-rc.1"


def test_release_version_validation_accepts_matching_versions(tmp_path: Path) -> None:
    write_repository(tmp_path, "1.2.3", "1.2.3")

    assert check_release_version(tmp_path, "1.2.3") == []


def test_release_version_validation_checks_nested_skills(tmp_path: Path) -> None:
    write_repository(tmp_path, "1.2.3", "1.2.3")
    nested_skill = tmp_path / "skills" / "core" / "nested" / "SKILL.md"
    nested_skill.parent.mkdir(parents=True)
    nested_skill.write_text("---\nmetadata:\n  version: 1.2.2\n---\n", encoding="utf-8")

    findings = check_release_version(tmp_path, "1.2.3")

    assert any("skills/core/nested/SKILL.md has version" in finding for finding in findings)


def test_release_version_validation_rejects_non_semver_tags(tmp_path: Path) -> None:
    write_repository(tmp_path, "1.2.3", "1.2.3")

    for tag in ("v1.2.3", "1.2", "1.2.3.4", "1.2.3-beta.1", "release-1.2.3"):
        findings = check_release_version(tmp_path, tag)
        assert any("must match MAJOR.MINOR.PATCH" in finding for finding in findings)


def test_release_version_validation_reports_package_and_skill_mismatches(tmp_path: Path) -> None:
    write_repository(tmp_path, "1.2.3b4", "1.2.3-beta.3")

    findings = check_release_version(tmp_path, "1.2.3")

    assert any("does not match package version" in finding for finding in findings)
    assert any("has version" in finding for finding in findings)
