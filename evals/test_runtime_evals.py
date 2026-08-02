import json
from pathlib import Path

import pytest

from scripts.run_runtime_evals import (
    assess_response,
    assess_routing,
    load_cases,
    load_client,
    main,
    validate_client,
)

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "evals" / "runtime.yaml"
CLIENTS = ROOT / "evals" / "clients.yaml"
FIXTURE_RESPONSE = (
    "Behavior contract. Scope, interaction state, validation error, and verification plan. "
    "Baseline evidence and hypothesis experiment. Finding and verification gap. Trust boundary and abuse path threat. "
    "Observed revision in the canonical record and next safe action."
)


def test_runtime_cases_have_machine_checkable_contracts() -> None:
    cases = load_cases(CASES)

    assert len(cases) >= 4
    assert all(case.required_patterns for case in cases)
    assert all(case.expected_skills for case in cases)


def test_client_matrix_declares_command_and_manual_clients() -> None:
    fixture = load_client(CLIENTS, "fixture")
    codex = load_client(CLIENTS, "codex-cli")
    zed = load_client(CLIENTS, "zed")

    assert validate_client(fixture) == []
    assert validate_client(codex) == []
    assert validate_client(zed) == []
    assert zed["mode"] == "manual-smoke"


def test_response_assessment_reports_missing_and_prohibited_patterns() -> None:
    case = load_cases(CASES)[0]

    assessment = assess_response(case, "Tests passed.")

    assert not assessment["passed"]
    assert assessment["missing_patterns"]
    assert assessment["prohibited_matches"]


def test_routing_assessment_requires_selected_skill_metadata() -> None:
    case = load_cases(CASES)[0]

    unavailable = assess_routing(case, selected_skills=None)
    passed = assess_routing(case, selected_skills=case.expected_skills)
    failed = assess_routing(case, selected_skills=case.forbidden_skills)

    assert unavailable == {"status": "not_available", "selected_skills": []}
    assert passed["status"] == "passed"
    assert failed["status"] == "failed"


def test_fixture_client_runs_contracts_and_writes_report(tmp_path: Path) -> None:
    output = tmp_path / "runtime-report.json"

    result = main(
        [
            "--client",
            "fixture",
            "--fixture-response",
            FIXTURE_RESPONSE,
            "--output",
            str(output),
        ]
    )

    report = json.loads(output.read_text(encoding="utf-8"))
    assert isinstance(report, dict)
    results = report.get("results")
    assert isinstance(results, list)
    assert all(isinstance(case, dict) for case in results)
    assert result == 0
    assert report["passed"] is True
    assert report["response_contract_passed"] is True
    assert report["routing_assessment"] == "not_available"
    assert all(case["passed"] for case in results)
    assert all(case["response_contract"]["passed"] for case in results)
    assert all(case["routing_assessment"]["status"] == "not_available" for case in results)


def test_fixture_client_requires_explicit_response() -> None:
    with pytest.raises(SystemExit, match="2"):
        _ = main(["--client", "fixture"])


def test_codex_client_requires_recorded_release_metadata(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("AGENT_SKILLS_RUNTIME_EVALS", "1")

    with pytest.raises(SystemExit, match="2"):
        _ = main(["--client", "codex-cli"])
