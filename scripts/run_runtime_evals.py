#!/usr/bin/env python3
"""Run declared runtime skill contracts through a configured agent-client adapter.

The command evaluates explicit response contracts. It assesses routing only when
an adapter supplies reliable selected-skill metadata; otherwise routing is
reported as not available and does not make a response-contract run pass or fail.
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
from typing import cast

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


def load_yaml(path: Path) -> object:
    try:
        return cast(object, yaml.safe_load(path.read_text(encoding="utf-8")))
    except (OSError, yaml.YAMLError) as error:
        raise ValueError(f"could not read {path}: {error}") from error


def as_mapping(value: object) -> dict[str, object] | None:
    if not isinstance(value, dict):
        return None
    mapping = cast(dict[object, object], value)
    if not all(isinstance(key, str) for key in mapping):
        return None
    return cast(dict[str, object], mapping)


def object_list(value: object) -> list[object] | None:
    if not isinstance(value, list):
        return None
    return cast(list[object], value)


def string_list(value: object) -> list[str] | None:
    items = object_list(value)
    if items is None or not all(isinstance(item, str) for item in items):
        return None
    return cast(list[str], items)



def load_cases(path: Path) -> list[RuntimeCase]:
    data = as_mapping(load_yaml(path))
    raw_cases = object_list(data.get("cases")) if data is not None else None
    if data is None or data.get("version") != 1 or raw_cases is None:
        raise ValueError(f"{path} must contain version: 1 and a cases list")

    cases: list[RuntimeCase] = []
    identifiers: set[str] = set()
    for value in raw_cases:
        raw_case = as_mapping(value)
        if raw_case is None:
            raise ValueError(f"{path} cases must be mappings")
        identifier, prompt, expect = raw_case.get("id"), raw_case.get("prompt"), as_mapping(raw_case.get("expect"))
        if not isinstance(identifier, str) or not identifier or identifier in identifiers:
            raise ValueError(f"{path} case ids must be unique non-empty strings")
        if not isinstance(prompt, str) or not prompt:
            raise ValueError(f"{path}:{identifier} prompt must be a non-empty string")
        if expect is None:
            raise ValueError(f"{path}:{identifier} must declare an expect mapping")
        required = string_list(expect.get("required_patterns", []))
        prohibited = string_list(expect.get("prohibited_patterns", []))
        expected_skills = string_list(raw_case.get("expected_skills", []))
        forbidden_skills = string_list(raw_case.get("forbidden_skills", []))
        if any(value is None for value in (required, prohibited, expected_skills, forbidden_skills)):
            raise ValueError(f"{path}:{identifier} skill names and patterns must be string lists")
        assert required is not None and prohibited is not None
        assert expected_skills is not None and forbidden_skills is not None
        if not all(pattern for pattern in [*required, *prohibited]):
            raise ValueError(f"{path}:{identifier} patterns must be non-empty strings")
        for pattern in [*required, *prohibited]:
            try:
                _ = re.compile(pattern)
            except re.error as error:
                raise ValueError(f"{path}:{identifier} invalid pattern {pattern!r}: {error}") from error
        identifiers.add(identifier)
        cases.append(
            RuntimeCase(
                identifier=identifier,
                prompt=prompt,
                expected_skills=tuple(expected_skills),
                forbidden_skills=tuple(forbidden_skills),
                required_patterns=tuple(required),
                prohibited_patterns=tuple(prohibited),
            )
        )
    return cases


def load_client(path: Path, client_id: str) -> dict[str, object]:
    data = as_mapping(load_yaml(path))
    clients = object_list(data.get("clients")) if data is not None else None
    if data is None or data.get("version") != 1 or clients is None:
        raise ValueError(f"{path} must contain version: 1 and a clients list")
    for value in clients:
        client = as_mapping(value)
        if client is not None and client.get("id") == client_id:
            return client
    raise ValueError(f"unknown client: {client_id}")


def validate_client(client: dict[str, object]) -> list[str]:
    errors: list[str] = []
    mode = client.get("mode")
    if mode not in {"command", "manual-smoke"}:
        errors.append("mode must be command or manual-smoke")
    if not isinstance(client.get("supported"), bool):
        errors.append("supported must be a boolean")
    if mode == "command":
        command = string_list(client.get("command"))
        if not command:
            errors.append("command clients need a non-empty string command list")
    if "require_metadata" in client and not isinstance(client["require_metadata"], bool):
        errors.append("require_metadata must be a boolean")
    required_environment = string_list(client.get("required_environment", []))
    if required_environment is None or not all(required_environment):
        errors.append("required_environment must be a list of environment variable names")
    return errors


def expand_command(command: list[str], values: dict[str, str]) -> list[str]:
    return [part.format_map(values) for part in command]


def assess_response(case: RuntimeCase, response: str) -> dict[str, object]:
    missing = [pattern for pattern in case.required_patterns if not re.search(pattern, response)]
    prohibited = [pattern for pattern in case.prohibited_patterns if re.search(pattern, response)]
    return {"passed": not missing and not prohibited, "missing_patterns": missing, "prohibited_matches": prohibited}


def assess_routing(case: RuntimeCase, selected_skills: tuple[str, ...] | None) -> dict[str, object]:
    if selected_skills is None:
        return {"status": "not_available", "selected_skills": []}
    missing = [skill for skill in case.expected_skills if skill not in selected_skills]
    prohibited = [skill for skill in case.forbidden_skills if skill in selected_skills]
    return {
        "status": "passed" if not missing and not prohibited else "failed",
        "selected_skills": list(selected_skills),
        "missing_expected_skills": missing,
        "selected_forbidden_skills": prohibited,
    }


def run_case(client: dict[str, object], case: RuntimeCase, fixture_response: str | None, skills_source: Path) -> dict[str, object]:
    with tempfile.TemporaryDirectory(prefix="agent-skill-eval-") as directory:
        workdir = Path(directory)
        installed = install_skills(skills_source, workdir / ".agents" / "skills", None, force=False)
        prompt_file, response_file = workdir / "prompt.txt", workdir / "response.txt"
        _ = prompt_file.write_text(case.prompt, encoding="utf-8")
        values = {
            "prompt": case.prompt,
            "prompt_file": str(prompt_file),
            "response_file": str(response_file),
            "fixture_response": fixture_response or "",
        }
        command = string_list(client.get("command"))
        if not command:
            raise ValueError("command clients need a non-empty string command list")
        command = expand_command(command, values)
        completed = subprocess.run(command, cwd=workdir, text=True, capture_output=True, timeout=120, check=False)
        response = response_file.read_text(encoding="utf-8") if response_file.is_file() else completed.stdout
        response_contract = assess_response(case, response)
        routing_assessment = assess_routing(case, selected_skills=None)
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
            "response_contract": response_contract,
            "routing_assessment": routing_assessment,
            "passed": completed.returncode == 0 and bool(response.strip()) and response_contract["passed"],
        }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument("--cases", type=Path, default=Path("evals/runtime.yaml"))
    _ = parser.add_argument("--clients", type=Path, default=Path("evals/clients.yaml"))
    _ = parser.add_argument("--client", required=True)
    _ = parser.add_argument("--skills-source", type=Path, default=Path("skills"))
    _ = parser.add_argument("--output", type=Path)
    _ = parser.add_argument("--client-version", help="recorded client version for this run")
    _ = parser.add_argument("--model", help="recorded model identifier for this run")
    _ = parser.add_argument("--fixture-response", help="response used only by the deterministic fixture client")

    class Arguments(argparse.Namespace):
        cases: Path = Path("evals/runtime.yaml")
        clients: Path = Path("evals/clients.yaml")
        client: str = ""
        skills_source: Path = Path("skills")
        output: Path | None = None
        client_version: str | None = None
        model: str | None = None
        fixture_response: str | None = None

    args = parser.parse_args(argv, namespace=Arguments())

    try:
        cases, client = load_cases(args.cases), load_client(args.clients, args.client)
        errors = validate_client(client)
        if errors:
            raise ValueError(f"{args.client}: " + "; ".join(errors))
        if client["mode"] == "manual-smoke":
            raise ValueError(f"{args.client} is manual-smoke only; follow its client guide")
        required_environment = string_list(client.get("required_environment", []))
        assert required_environment is not None
        missing_environment = [name for name in required_environment if not os.environ.get(name)]
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
        "response_contract_passed": all(result["passed"] for result in results),
        "routing_assessment": "not_available",
        "passed": all(result["passed"] for result in results),
        "results": results,
    }
    serialized = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        _ = args.output.write_text(serialized, encoding="utf-8")
    print(serialized)
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
