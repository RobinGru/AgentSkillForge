#!/usr/bin/env python3
"""Validate the portable skill package structure and skill documents."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import yaml

ALLOWED_FRONTMATTER = {
    "name",
    "description",
    "license",
    "compatibility",
    "metadata",
    "allowed-tools",
}
CLIENT_SPECIFIC_FIELDS = {"disable-model-invocation"}
TARGET_SKILLS = frozenset(
    {
        "solution-framing",
        "safe-code-change",
        "fact-based-code-review",
        "product-interface-engineering",
        "performance-investigation",
        "vue-sfc-decomposition",
        "failure-investigation",
        "security-boundary-analysis",
        "compatibility-migration",
    }
)
NAME_PATTERN = re.compile(r"^[a-z0-9-]{1,64}$")
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
FORBIDDEN_REFERENCES = re.compile(
    r"/review|/ship|security-auditor|test-engineer", re.IGNORECASE
)
PLACEHOLDER = re.compile(r"\b(?:TODO|TBD)\b|\bplaceholder\b", re.IGNORECASE)
TESTS_PASSED = re.compile(r"\btests? passed\b", re.IGNORECASE)
HEADING = re.compile(r"^(#{1,6})\s+\S.*$", re.MULTILINE)
FENCED_CODE = re.compile(r"^```.*?^```[ \t]*$", re.MULTILINE | re.DOTALL)


@dataclass(frozen=True)
class Finding:
    level: str
    path: Path
    message: str


def parse_frontmatter(path: Path, text: str) -> tuple[dict[str, Any] | None, str | None]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return None, "missing opening frontmatter delimiter"

    try:
        end = lines.index("---", 1)
    except ValueError:
        return None, "missing closing frontmatter delimiter"

    try:
        data = yaml.safe_load("\n".join(lines[1:end]))
    except yaml.YAMLError as error:
        return None, f"invalid YAML frontmatter: {error}"

    if not isinstance(data, dict):
        return None, "frontmatter must be a mapping"
    if "---" in lines[end + 1 :]:
        return None, "multiple frontmatter blocks are not allowed"
    return data, None


def is_relative_target(target: str) -> bool:
    parsed = urlparse(target)
    return not parsed.scheme and not target.startswith("#") and not target.startswith("/")


def validate_links(path: Path, text: str) -> list[Finding]:
    findings: list[Finding] = []
    for target in MARKDOWN_LINK.findall(text):
        target = target.split("#", 1)[0].strip()
        if not target or not is_relative_target(target):
            continue
        if not (path.parent / target).exists():
            findings.append(Finding("error", path, f"missing relative link target: {target}"))
    return findings


def has_empty_section(text: str) -> bool:
    text = FENCED_CODE.sub("", text)
    headings = list(HEADING.finditer(text))
    for index, heading in enumerate(headings):
        next_heading = headings[index + 1] if index + 1 < len(headings) else None
        section_end = next_heading.start() if next_heading else len(text)
        if text[heading.end() : section_end].strip():
            continue
        if next_heading and len(next_heading.group(1)) > len(heading.group(1)):
            continue
        return True
    return False


def validate_skill(path: Path) -> tuple[str | None, list[Finding]]:
    findings: list[Finding] = []
    text = path.read_text(encoding="utf-8")
    frontmatter, error = parse_frontmatter(path, text)
    if error:
        return None, [Finding("error", path, error)]
    assert frontmatter is not None

    for key in frontmatter:
        if key in CLIENT_SPECIFIC_FIELDS:
            findings.append(Finding("error", path, f"client-specific field: {key}"))
        elif key not in ALLOWED_FRONTMATTER:
            findings.append(Finding("error", path, f"unsupported frontmatter field: {key}"))

    name = frontmatter.get("name")
    if not isinstance(name, str) or not NAME_PATTERN.fullmatch(name):
        findings.append(Finding("error", path, "name must match lowercase letters, digits, and hyphens (max 64)"))
        name = None

    description = frontmatter.get("description")
    if not isinstance(description, str) or not description.strip() or len(description) > 1024:
        findings.append(Finding("error", path, "description must be non-empty and at most 1024 characters"))

    metadata = frontmatter.get("metadata")
    if metadata is not None and (
        not isinstance(metadata, dict)
        or any(not isinstance(key, str) or not isinstance(value, str) for key, value in metadata.items())
    ):
        findings.append(Finding("error", path, "metadata keys and values must be strings"))

    if "allowed-tools" in frontmatter:
        findings.append(Finding("warning", path, "allowed-tools requires an explicit portability justification"))

    line_count = len(text.splitlines())
    if line_count > 500:
        findings.append(Finding("error", path, f"SKILL.md exceeds 500 lines ({line_count})"))
    elif line_count >= 300:
        findings.append(Finding("warning", path, f"SKILL.md is long ({line_count} lines)"))

    if has_empty_section(text):
        findings.append(Finding("error", path, "contains an empty heading section"))

    findings.extend(validate_links(path, text))
    if re.search(r"references/[^\s/)]+/", text):
        findings.append(Finding("error", path, "reference paths may be only one level below references/"))
    if FORBIDDEN_REFERENCES.search(text):
        findings.append(Finding("error", path, "contains a forbidden persona or slash-command reference"))
    if PLACEHOLDER.search(text):
        findings.append(Finding("error", path, "contains a TODO, TBD, or placeholder"))
    if TESTS_PASSED.search(text):
        findings.append(Finding("error", path, "contains an unverified static 'tests passed' claim"))
    return name, findings


def readme_skill_names(readme: Path) -> set[str]:
    if not readme.exists():
        return set()
    return set(re.findall(r"`skills/([a-z0-9-]+)/`", readme.read_text(encoding="utf-8")))


def validate_repository(root: Path, skills_dir: Path) -> list[Finding]:
    findings: list[Finding] = []
    skills_root = root / skills_dir
    if not skills_root.is_dir():
        return [Finding("error", skills_root, "skills directory does not exist")]

    names: dict[str, Path] = {}
    for legacy_file in sorted(root.rglob("SKILL.md")):
        if not legacy_file.is_relative_to(skills_root):
            findings.append(Finding("error", legacy_file, "skill files must be located under skills/"))
            _, legacy_findings = validate_skill(legacy_file)
            findings.extend(legacy_findings)

    for directory in sorted(path for path in skills_root.iterdir() if path.is_dir()):
        skill_files = list(directory.glob("SKILL.md"))
        if len(skill_files) != 1:
            findings.append(Finding("error", directory, "skill directory must contain exactly one SKILL.md"))
            continue
        name, skill_findings = validate_skill(skill_files[0])
        findings.extend(skill_findings)
        if name is None:
            continue
        if directory.name != name:
            findings.append(Finding("error", directory, f"directory name must match skill name '{name}'"))
        if name in names:
            findings.append(Finding("error", directory, f"duplicate skill name '{name}' also used by {names[name]}"))
        names[name] = directory

    documented = readme_skill_names(root / "README.md")
    actual = set(names)
    if actual != TARGET_SKILLS:
        findings.append(
            Finding("error", skills_root, f"target skills differ: expected={sorted(TARGET_SKILLS)}, actual={sorted(actual)}")
        )
    if documented != actual:
        findings.append(
            Finding("error", root / "README.md", f"README skills inventory differs: documented={sorted(documented)}, actual={sorted(actual)}")
        )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--skills-dir", type=Path, default=Path("skills"))
    args = parser.parse_args()

    try:
        findings = validate_repository(args.root.resolve(), args.skills_dir)
    except Exception as error:  # noqa: BLE001  # pragma: no cover - preserves the documented exit contract
        print(f"internal validator error: {error}", file=sys.stderr)
        return 2

    for finding in findings:
        print(f"{finding.level.upper()}: {finding.path}: {finding.message}")
    return 1 if any(finding.level == "error" for finding in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
