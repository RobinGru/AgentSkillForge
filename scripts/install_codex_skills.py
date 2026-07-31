#!/usr/bin/env python3
"""Install portable skill directories into Codex's shared skill directory."""

from __future__ import annotations

from pathlib import Path

try:
    from .install_skills import main as install_main
except ImportError:  # Supports execution as a script from the repository root.
    from install_skills import main as install_main  # pyright: ignore[reportImplicitRelativeImport]


DEFAULT_TARGET = Path.home() / ".agents" / "skills"


def main() -> int:
    return install_main(DEFAULT_TARGET, "Codex")


if __name__ == "__main__":
    raise SystemExit(main())
