from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILLS = sorted((ROOT / "skills").glob("*/*/SKILL.md"))
STANDARD_RULE = (
    "Use the repository's established language and conventions for any artifacts "
    "you create or update."
)


def test_every_distributed_skill_is_compact_and_non_redundant() -> None:
    assert len(SKILLS) == 17

    for path in SKILLS:
        text = path.read_text(encoding="utf-8")
        assert len(text.splitlines()) <= 120, path
        assert text.count(STANDARD_RULE) == 1, path
        assert "## Capability disclosure" not in text, path


def test_skill_descriptions_are_bounded_routing_contracts() -> None:
    for path in SKILLS:
        frontmatter = text_frontmatter(path)
        description = frontmatter.get("description")
        assert isinstance(description, str), path
        assert 40 <= len(description) <= 420, path
        assert "Use " in description or "Use when" in description or "Use only" in description, path


def text_frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    raw = text.split("---", 2)[1]
    data = yaml.safe_load(raw)
    assert isinstance(data, dict)
    return data
