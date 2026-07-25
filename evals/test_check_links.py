from pathlib import Path

from scripts.check_links import check_markdown_file


def test_valid_local_file_and_anchor_pass(tmp_path: Path) -> None:
    document = tmp_path / "guide.md"
    document.write_text("# Guide\n\n[Section](#section)\n\n## Section\n", encoding="utf-8")

    assert check_markdown_file(document, external=False) == []


def test_code_examples_do_not_create_link_findings(tmp_path: Path) -> None:
    document = tmp_path / "guide.md"
    document.write_text("`[Example](missing.md)`\n\n```md\n[Example](missing.md)\n```\n", encoding="utf-8")

    assert check_markdown_file(document, external=False) == []


def test_missing_target_and_absolute_path_fail(tmp_path: Path) -> None:
    document = tmp_path / "guide.md"
    document.write_text("[Missing](missing.md)\n[Root](/etc/passwd)\n", encoding="utf-8")

    findings = check_markdown_file(document, external=False)

    assert any("missing local target" in finding.message for finding in findings)
    assert any("absolute path" in finding.message for finding in findings)


def test_missing_same_file_anchor_fails(tmp_path: Path) -> None:
    document = tmp_path / "guide.md"
    document.write_text("# Guide\n\n[Missing](#missing)\n", encoding="utf-8")

    findings = check_markdown_file(document, external=False)

    assert any("missing anchor" in finding.message for finding in findings)
