from pathlib import Path

from scripts.validate_repository import (
    TARGET_SKILLS,
    validate_repository,
    validate_skill,
)


def write_skill(root: Path, name: str, body: str) -> None:
    directory = root / "skills" / name
    directory.mkdir(parents=True)
    (directory / "SKILL.md").write_text(body, encoding="utf-8")


def test_valid_repository_passes(tmp_path: Path) -> None:
    for name in TARGET_SKILLS:
        write_skill(
            tmp_path,
            name,
            f"---\nname: {name}\ndescription: A portable example.\n---\n\n# Example\n\nUse this skill.\n",
        )
    inventory = "\n".join(f"`skills/{name}/`" for name in sorted(TARGET_SKILLS))
    (tmp_path / "README.md").write_text(inventory + "\n", encoding="utf-8")

    assert validate_repository(tmp_path, Path("skills")) == []


def test_skills_require_repository_language_and_conventions() -> None:
    required_rule = "Use the repository's established language and conventions for any artifacts you create or update."

    for name in TARGET_SKILLS:
        text = (Path(__file__).resolve().parents[1] / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
        assert required_rule in text


def test_extra_skill_is_an_error(tmp_path: Path) -> None:
    for name in TARGET_SKILLS | {"example-skill"}:
        write_skill(
            tmp_path,
            name,
            f"---\nname: {name}\ndescription: A portable example.\n---\n\n# Example\n\nUse this skill.\n",
        )
    inventory = "\n".join(f"`skills/{name}/`" for name in sorted(TARGET_SKILLS | {"example-skill"}))
    (tmp_path / "README.md").write_text(inventory + "\n", encoding="utf-8")

    findings = validate_repository(tmp_path, Path("skills"))

    assert any("target skills differ" in finding.message for finding in findings)



def test_legacy_skill_and_duplicate_frontmatter_are_errors(tmp_path: Path) -> None:
    path = tmp_path / "SKILL.md"
    path.write_text(
        "---\nname: example\ndescription: Example.\n---\n\n---\nname: example\n---\n",
        encoding="utf-8",
    )

    _, findings = validate_skill(path)
    (tmp_path / "skills").mkdir()
    (tmp_path / "README.md").write_text("", encoding="utf-8")
    repository_findings = validate_repository(tmp_path, Path("skills"))

    assert any("multiple frontmatter blocks" in finding.message for finding in findings)
    assert any("skill files must be located under skills/" in finding.message for finding in repository_findings)


def test_nested_headings_are_not_empty_sections(tmp_path: Path) -> None:
    path = tmp_path / "SKILL.md"
    path.write_text(
        "---\nname: example\ndescription: Example.\n---\n\n# Example\n\n## Workflow\n\n### Step\n\nContent.\n",
        encoding="utf-8",
    )

    _, findings = validate_skill(path)

    assert not any("empty heading section" in finding.message for finding in findings)


def test_headings_in_fenced_code_are_not_sections(tmp_path: Path) -> None:
    path = tmp_path / "SKILL.md"
    path.write_text(
        "---\nname: example\ndescription: Example.\n---\n\n# Example\n\nContent.\n\n```md\n## Empty example\n\n## Another example\n```\n",
        encoding="utf-8",
    )

    _, findings = validate_skill(path)

    assert not any("empty heading section" in finding.message for finding in findings)


def test_client_metadata_and_missing_link_are_errors(tmp_path: Path) -> None:
    write_skill(
        tmp_path,
        "example-skill",
        "---\nname: example-skill\ndescription: A portable example.\ndisable-model-invocation: false\n---\n\n# Example\n\n[Missing](missing.md)\n",
    )
    (tmp_path / "README.md").write_text("`skills/example-skill/`\n", encoding="utf-8")

    findings = validate_repository(tmp_path, Path("skills"))

    messages = [finding.message for finding in findings]
    assert any("client-specific field" in message for message in messages)
    assert any("missing relative link target" in message for message in messages)
