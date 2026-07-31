#!/usr/bin/env python3
"""Run declared runtime skill contracts through a configured agent-client adapter.

The command validates only explicit response contracts. A passing run does not
prove model routing, semantic quality, or compatibility with untested clients.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import yaml

if __package__ is None:  # Direct execution as `python scripts/run_runtime_evals.py`.
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.install_skills import install_skills


@dataclass(frozen=True)
class RuntimeCase:
    identifier: str
    prompt: str
    expected_skills: tuple[str, ...]
    forbidden_skills: tuple[str, ...]
    required_patterns: tuple[str, ...]
    prohibited_patterns: tuple[str, ...]


def load_yaml(path: Path) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        raise ValueError(f"could not read {path}: {error}") from error


def load_cases(path: Path) -> list[RuntimeCase]:
    data = load_yaml(path)
    if not isinstance(data, dict) or data.get("version") != 1 or not isinstance(data.get("cases"), list):
        raise ValueError(f"{path} must contain version: 1 and a cases list")

    cases: list[RuntimeCase] = []
    identifiers: set[str] = set()
    for raw_case in data["cases"]:
        if not isinstance(raw_case, dict):
            raise ValueError(f"{path} cases must be mappings")
        identifier, prompt, expect = raw_case.get("id"), raw_case.get("prompt"), raw_case.get("expect")
        if not isinstance(identifier, str) or not identifier or identifier in identifiers:
            raise ValueError(f"{path} case ids must be unique non-empty strings")
        if not isinstance(prompt, str) or not prompt:
            raise ValueError(f"{path}:{identifier} prompt must be a non-empty string")
        if not isinstance(expect, dict):
            raise ValueError(f"{path}:{identifier} must declare an expect mapping")
        required, prohibited = expect.get("required_patterns", []), expect.get("prohibited_patterns", [])
        if not all(isinstance(pattern, str) and pattern for pattern in [*required, *prohibited]):
            raise ValueError(f"{path}:{identifier} patterns must be non-empty strings")
        for pattern in [*required, *prohibited]:
            try:
                re.compile(pattern)
            except re.error as error:
                raise ValueError(f"{path}:{identifier} invalid pattern {pattern!r}: {error}") from error
        identifiers.add(identifier)
        cases.append(
            RuntimeCase(
                identifier=identifier,
                prompt=prompt,
                expected_skills=tuple(raw_case.get("expected_skills", [])),
                forbidden_skills=tuple(raw_case.get("forbidden_skills", [])),
                required_patterns=tuple(required),
                prohibited_patterns=tuple(prohibited),
            )
        )
    return cases


def load_client(path: Path, client_id: str) -> dict[str, Any]:
    data = load_yaml(path)
    if not isinstance(data, dict) or data.get("version") != 1 or not isinstance(data.get("clients"), list):
        raise ValueError(f"{path} must contain version: 1 and a clients list")
    for client in data["clients"]:
        if isinstance(client, dict) and client.get("id") == client_id:
            return client
    raise ValueError(f"unknown client: {client_id}")


def validate_client(client: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    mode = client.get("mode")
    if mode not in {"command", "manual-smoke"}:
        errors.append("mode must be command or manual-smoke")
    if not isinstance(client.get("supported"), bool):
        errors.append("supported must be a boolean")
    if mode == "command":
        command = client.get("command")
        if not isinstance(command, list) or not command or not all(isinstance(item, str) for item in command):
            errors.append("command clients need a non-empty string command list")
    if "require_metadata" in client and not isinstance(client["require_metadata"], bool):
        errors.append("require_metadata must be a boolean")
    required_environment = client.get("required_environment", [])
    if not isinstance(required_environment, list) or not all(isinstance(name, str) and name for name in required_environment):
        errors.append("required_environment must be a list of environment variable names")
    return errors


def expand_command(command: list[str], values: dict[str, str]) -> list[str]:
    return [part.format_map(values) for part in command]


def assess_response(case: RuntimeCase, response: str) -> dict[str, Any]:
    missing = [pattern for pattern in case.required_patterns if not re.search(pattern, response)]
    prohibited = [pattern for pattern in case.prohibited_patterns if re.search(pattern, response)]
    return {"passed": not missing and not prohibited, "missing_patterns": missing, "prohibited_matches": prohibited}


def run_case(client: dict[str, Any], case: RuntimeCase, fixture_response: str | None, skills_source: Path) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="agent-skill-eval-") as directory:
        workdir = Path(directory)
        installed = install_skills(skills_source, workdir / ".agents" / "skills", None, force=False)
        prompt_file, response_file = workdir / "prompt.txt", workdir / "response.txt"
        prompt_file.write_text(case.prompt, encoding="utf-8")
        values = {
            "prompt": case.prompt,
            "prompt_file": str(prompt_file),
            "response_file": str(response_file),
            "fixture_response": fixture_response or "",
        }
        command = expand_command(client["command"], values)
        completed = subprocess.run(command, cwd=workdir, text=True, capture_output=True, timeout=120, check=False)
        response = response_file.read_text(encoding="utf-8") if response_file.is_file() else completed.stdout
        assessment = assess_response(case, response)
        return {
            "id": case.identifier,
            "installed_skills": [path.name for path in installed],
            "expected_skills": list(case.expected_skills),
            "forbidden_skills": list(case.forbidden_skills),
            "command": command,
            "exit_code": completed.returncode,
            "stdout": completed.stdout,
            "stderr": completed.stderr,
            "response": response,
            "assessment": assessment,
            "passed": completed.returncode == 0 and bool(response.strip()) and assessment["passed"],
        }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", type=Path, default=Path("evals/runtime.yaml"))
    parser.add_argument("--clients", type=Path, default=Path("evals/clients.yaml"))
    parser.add_argument("--client", required=True)
    parser.add_argument("--skills-source", type=Path, default=Path("skills"))
    parser.add_argument("--output", type=Path)
    parser.add_argument("--client-version", help="recorded client version for this run")
    parser.add_argument("--model", help="recorded model identifier for this run")
    parser.add_argument("--fixture-response", help="response used only by the deterministic fixture client")
    args = parser.parse_args(argv)

    try:
        cases, client = load_cases(args.cases), load_client(args.clients, args.client)
        errors = validate_client(client)
        if errors:
            raise ValueError(f"{args.client}: " + "; ".join(errors))
        if client["mode"] == "manual-smoke":
            raise ValueError(f"{args.client} is manual-smoke only; follow its client guide")
        missing_environment = [name for name in client.get("required_environment", []) if not os.environ.get(name)]
        if missing_environment:
            raise ValueError(f"{args.client} requires environment variable(s): {', '.join(missing_environment)}")
        if args.client == "fixture" and args.fixture_response is None:
            raise ValueError("fixture client requires --fixture-response")
        if client.get("require_metadata") and (not args.client_version or not args.model):
            raise ValueError(f"{args.client} requires --client-version and --model for release evidence")
        skills_source = args.skills_source.resolve()
        if not skills_source.is_dir():
            raise ValueError(f"skills source directory does not exist: {skills_source}")
    except ValueError as error:
        parser.error(str(error))

    results = [run_case(client, case, args.fixture_response, skills_source) for case in cases]
    report = {
        "format_version": 1,
        "client": args.client,
        "client_version": args.client_version,
        "model": args.model,
        "executed_at": datetime.now(UTC).isoformat(),
        "case_count": len(results),
        "passed": all(result["passed"] for result in results),
        "results": results,
    }
    serialized = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized, encoding="utf-8")
    print(serialized)
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
