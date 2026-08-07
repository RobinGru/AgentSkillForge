#!/usr/bin/env python3
"""Check local Markdown links, assets, scripts, and same-file anchors."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlparse
from urllib.request import Request, urlopen

LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
HEADING_PATTERN = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)
FENCED_CODE_PATTERN = re.compile(r"^```.*?^```[ \t]*$", re.MULTILINE | re.DOTALL)
INLINE_CODE_PATTERN = re.compile(r"`[^`]*`")
EXCLUDED_DIRECTORIES = frozenset({".git", ".venv", "__pycache__", "build", ".pytest_cache", ".ruff_cache"})


@dataclass(frozen=True)
class Finding:
    path: Path
    message: str


def slugify(heading: str) -> str:
    normalized = heading.lower().strip()
    normalized = re.sub(r"[^\w\s-]", "", normalized, flags=re.UNICODE)
    return re.sub(r"[\s-]+", "-", normalized).strip("-")


def markdown_without_code(text: str) -> str:
    return INLINE_CODE_PATTERN.sub("", FENCED_CODE_PATTERN.sub("", text))


def anchors(text: str) -> set[str]:
    return {slugify(heading) for heading in HEADING_PATTERN.findall(markdown_without_code(text))}



def split_target(target: str) -> tuple[str, str | None]:
    path, separator, anchor = target.partition("#")
    return unquote(path), unquote(anchor) if separator else None


def is_external(target: str) -> bool:
    return urlparse(target).scheme in {"http", "https"}


def check_markdown_file(path: Path, external: bool) -> list[Finding]:
    findings: list[Finding] = []
    text = path.read_text(encoding="utf-8")
    for raw_target in LINK_PATTERN.findall(markdown_without_code(text)):
        target = raw_target.strip().strip("<>")
        if not target:
            findings.append(Finding(path, "empty link target"))
            continue
        if is_external(target):
            if external:
                findings.extend(check_external(path, target))
            continue
        if target.startswith("/"):
            findings.append(Finding(path, f"absolute path is not portable: {target}"))
            continue

        target_path, anchor = split_target(target)
        destination = path if not target_path else path.parent / target_path
        if not destination.exists():
            findings.append(Finding(path, f"missing local target: {target_path}"))
            continue
        if anchor:
            if destination.suffix.lower() != ".md":
                findings.append(Finding(path, f"anchor target is not Markdown: {target}"))
                continue
            available = anchors(destination.read_text(encoding="utf-8"))
            if slugify(anchor) not in available:
                findings.append(Finding(path, f"missing anchor: {target}"))
    return findings


def check_external(path: Path, target: str) -> list[Finding]:
    try:
        request = Request(target, method="HEAD", headers={"User-Agent": "agent-skill-forge-link-checker"})
        with urlopen(request, timeout=10) as response:
            if response.status >= 400:
                return [Finding(path, f"external link returned HTTP {response.status}: {target}")]
    except OSError as error:
        return [Finding(path, f"external link check failed for {target}: {error}")]
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--external", action="store_true", help="also check HTTP(S) links")
    args = parser.parse_args()

    root = args.root.resolve()
    findings: list[Finding] = []
    for path in sorted(root.rglob("*.md")):
        if not EXCLUDED_DIRECTORIES.intersection(path.relative_to(root).parts):
            findings.extend(check_markdown_file(path, args.external))

    for finding in findings:
        print(f"ERROR: {finding.path}: {finding.message}")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
