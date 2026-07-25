# Runtime routing report: 0.3.0-beta.1

## Status

**Overall status: NOT RUN**

This document is a reproducible manual test protocol, not evidence of a completed
runtime evaluation. No host/model combination has been executed for this report.
Every actual-load and result field therefore remains `NOT RUN`. The
`0.3.0-beta.1` release remains blocked until required runs are observed, recorded,
and satisfy the release gate below.

Static repository evals do not execute an agent and cannot substitute for this
report. Results from one host or model must not be generalized to untested
clients, versions, configurations, or model families.

## Run metadata

Create one metadata record and one result table per host/model run. Do not replace
`NOT RUN` with an expectation or inference.

| Field | Recorded value |
|---|---|
| Run ID | NOT RUN |
| Date and time (UTC) | NOT RUN |
| Operator | NOT RUN |
| Repository revision/tag | NOT RUN |
| Host | NOT RUN |
| Host version | NOT RUN |
| Model provider | NOT RUN |
| Model family and exact version | NOT RUN |
| Skill installation method | NOT RUN |
| Installed skill source/ref/tree SHA | NOT RUN |
| Installed skill set | NOT RUN |
| Agent configuration/instructions | NOT RUN |
| Tool permissions | NOT RUN |
| Conversation reset between cases | NOT RUN |
| Raw transcript location | NOT RUN |
| Known host/model dependencies | NOT RUN |

Required coverage is the documented Zed path plus a second compatible host when
practically available, and at least two model families or materially different
model versions when supported. Any unavailable dimension must be recorded as
`NOT RUN` with a reason; it remains unconfirmed.

## Reproduction procedure

1. Check out and record the exact `0.3.0-beta.1` candidate revision.
2. Install all nine skill directories using the recorded installation method.
3. Record host, host version, exact model, configuration, permissions, and skill
   provenance before prompting.
4. Start a clean agent session for every case. Do not add routing hints beyond
   the prompt in the matrix.
5. Submit the prompt verbatim and capture the raw transcript plus any host UI,
   logs, or metadata that identifies loaded skills.
6. Record `Actual loaded skill(s)` only from observable host evidence. If the host
   does not expose loading, record `UNOBSERVABLE`, not a guess.
7. Classify each case: `PASS`, `FALSE POSITIVE`, `FALSE NEGATIVE`,
   `UNEXPECTED MULTIPLE`, `UNOBSERVABLE`, or `NOT RUN`.
8. For a failure, preserve evidence, correct the relevant discovery description,
   add a static regression case, and rerun the affected contrast pair and the
   full matrix on every previously tested host/model combination.

`False positive` means an unexpected skill loaded. `False negative` means an
expected skill did not load. `Unexpected multiple` means more than the allowed
sequence or combination loaded for the initial task. A later handoff is not an
initial multi-activation.

## Minimal contrast matrix

Each adjacent pair changes the decisive routing signal. These 36 cases cover each
new skill against each of the six pre-existing catalog skills.

| ID | Boundary | Prompt | Expected initial skill(s) | Actual loaded skill(s) | Result | FP | FN | Unexpected multiple | Evidence/transcript |
|---|---|---|---|---|---|---|---|---|---|
| FI-SC-1 | failure vs safe change | A validation test fails only after the full suite. Find the cause before changing code. | `failure-investigation` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| FI-SC-2 | failure vs safe change | The validation test fails because the confirmed null guard is missing. Add that local guard. | `safe-code-change` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| FI-FR-1 | failure vs review | An integration fails after an update and the cause is unknown. Investigate it. | `failure-investigation` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| FI-FR-2 | failure vs review | A proposed integration fix diff is ready. Review it before merge. | `fact-based-code-review` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| FI-PI-1 | failure vs performance | The endpoint returns 500 for one dataset and the cause is unknown. Investigate it. | `failure-investigation` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| FI-PI-2 | failure vs performance | The endpoint p95 rose from 200 ms to 800 ms. Investigate it. | `performance-investigation` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| FI-SF-1 | failure vs framing | The selected queue design drops jobs intermittently. Establish why before proposing a change. | `failure-investigation` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| FI-SF-2 | failure vs framing | Choose between a queue and a database outbox; the direction is still open. | `solution-framing` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| FI-PIE-1 | failure vs interface | The checkout submit action sometimes creates no order. Find the cause before redesigning anything. | `failure-investigation` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| FI-PIE-2 | failure vs interface | Redesign checkout submit, error, and retry states for mobile accessibility. | `product-interface-engineering` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| FI-VUE-1 | failure vs Vue decomposition | This Vue component throws only after route reuse. Establish the cause before editing it. | `failure-investigation` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| FI-VUE-2 | failure vs Vue decomposition | This working Vue component is too large. Split it without changing behavior. | `vue-sfc-decomposition` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| SBA-SC-1 | security vs safe change | Threat-model the upload boundary, including attacker capabilities and abuse paths. | `security-boundary-analysis` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| SBA-SC-2 | security vs safe change | The upload limit is already specified. Add the local size validation. | `safe-code-change` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| SBA-FR-1 | security vs review | Build a threat model for the webhook trust transition before implementation. | `security-boundary-analysis` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| SBA-FR-2 | security vs review | Review this webhook verification diff for correctness and security issues. | `fact-based-code-review` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| SBA-PI-1 | security vs performance | Map abuse paths and controls for unauthenticated expensive search requests. | `security-boundary-analysis` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| SBA-PI-2 | security vs performance | Search p95 is 1.2 seconds under measured load. Find the bottleneck. | `performance-investigation` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| SBA-SF-1 | security vs framing | Identify trust transitions and control obligations for the proposed plugin system. | `security-boundary-analysis` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| SBA-SF-2 | security vs framing | Choose between in-process and isolated plugins using the stated security constraints. | `solution-framing` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| SBA-PIE-1 | security vs interface | Threat-model account recovery, including abuse chains and required controls. | `security-boundary-analysis` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| SBA-PIE-2 | security vs interface | Design the visible account-recovery consent, error, and success states. | `product-interface-engineering` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| SBA-VUE-1 | security vs Vue decomposition | Threat-model the trust transition from untrusted rich text into this Vue renderer. | `security-boundary-analysis` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| SBA-VUE-2 | security vs Vue decomposition | Split this working rich-text Vue renderer into smaller components without behavior changes. | `vue-sfc-decomposition` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| CM-SC-1 | migration vs safe change | Plan old and new event schemas to coexist across producers and consumers, including retirement criteria. | `compatibility-migration` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| CM-SC-2 | migration vs safe change | The coexistence plan is approved. Add the specified dual-read branch for this step. | `safe-code-change` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| CM-FR-1 | migration vs review | Define safe states and rollback boundaries for the multi-release API migration. | `compatibility-migration` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| CM-FR-2 | migration vs review | Review the completed first API-migration step before merge. | `fact-based-code-review` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| CM-PI-1 | migration vs performance | Plan compatible old/new table coexistence and retirement across deployments. | `compatibility-migration` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| CM-PI-2 | migration vs performance | The migration backfill throughput fell by 60 percent. Investigate the measured regression. | `performance-investigation` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| CM-SF-1 | migration vs framing | The target API is chosen. Plan compatible consumer transitions over three releases. | `compatibility-migration` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| CM-SF-2 | migration vs framing | Choose REST or event delivery for the replacement API; the direction is open. | `solution-framing` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| CM-PIE-1 | migration vs interface | Plan old and new authentication flows to coexist while clients migrate. | `compatibility-migration` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| CM-PIE-2 | migration vs interface | Design the user-visible reauthentication and recovery states for the new flow. | `product-interface-engineering` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| CM-VUE-1 | migration vs Vue decomposition | Plan old and new component APIs to coexist while downstream consumers migrate. | `compatibility-migration` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| CM-VUE-2 | migration vs Vue decomposition | Split this working Vue SFC internally without changing its public API. | `vue-sfc-decomposition` | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |

## Boundary summary

Complete this table separately for each run only after all relevant cases have
observable results.

| New-skill boundary | Cases | Observed result | Notes |
|---|---:|---|---|
| `failure-investigation` vs `safe-code-change` | 2 | NOT RUN | NOT RUN |
| `failure-investigation` vs `fact-based-code-review` | 2 | NOT RUN | NOT RUN |
| `failure-investigation` vs `performance-investigation` | 2 | NOT RUN | NOT RUN |
| `failure-investigation` vs `solution-framing` | 2 | NOT RUN | NOT RUN |
| `failure-investigation` vs `product-interface-engineering` | 2 | NOT RUN | NOT RUN |
| `failure-investigation` vs `vue-sfc-decomposition` | 2 | NOT RUN | NOT RUN |
| `security-boundary-analysis` vs `safe-code-change` | 2 | NOT RUN | NOT RUN |
| `security-boundary-analysis` vs `fact-based-code-review` | 2 | NOT RUN | NOT RUN |
| `security-boundary-analysis` vs `performance-investigation` | 2 | NOT RUN | NOT RUN |
| `security-boundary-analysis` vs `solution-framing` | 2 | NOT RUN | NOT RUN |
| `security-boundary-analysis` vs `product-interface-engineering` | 2 | NOT RUN | NOT RUN |
| `security-boundary-analysis` vs `vue-sfc-decomposition` | 2 | NOT RUN | NOT RUN |
| `compatibility-migration` vs `safe-code-change` | 2 | NOT RUN | NOT RUN |
| `compatibility-migration` vs `fact-based-code-review` | 2 | NOT RUN | NOT RUN |
| `compatibility-migration` vs `performance-investigation` | 2 | NOT RUN | NOT RUN |
| `compatibility-migration` vs `solution-framing` | 2 | NOT RUN | NOT RUN |
| `compatibility-migration` vs `product-interface-engineering` | 2 | NOT RUN | NOT RUN |
| `compatibility-migration` vs `vue-sfc-decomposition` | 2 | NOT RUN | NOT RUN |

## Run summary fields

| Metric | Value |
|---|---|
| Cases executed | NOT RUN |
| Cases passed | NOT RUN |
| False positives | NOT RUN |
| False negatives | NOT RUN |
| Unexpected multiple activations | NOT RUN |
| Unobservable cases | NOT RUN |
| Systematic trigger conflicts | NOT RUN |
| Description corrections made | NOT RUN |
| Static regression cases added | NOT RUN |
| Overall run verdict | NOT RUN |

## GitHub CLI and provenance gate

**Status: PARTIAL.** GitHub CLI `2.96.0` was used on 2026-07-25.

| Check | Result | Evidence |
|---|---|---|
| `gh skill publish --dry-run` | PASS | Completed successfully from the repository root. |
| Tag protection | WARNING | CLI reported no active tag-protection rulesets. |
| Preview each new skill at the release tag | NOT RUN | The candidate files do not yet exist at a published tag or commit. |
| Local installation of all nine skills | PASS | `gh skill install . --from-local --all --dir build/gh-skill-local` copied every skill and reference file. |
| Local installed-copy provenance | PASS | Every installed `SKILL.md` received the expected `metadata.github.local-path` value. |
| Pinned installation by tag or SHA | NOT RUN | The candidate files do not yet exist at a published tag or commit. |
| Source provenance fields | PASS | Repository search found no installation-injected `metadata.github-*` fields. |
| Remote installed-copy provenance | NOT RUN | Requires the pinned installation above. |

Before release, complete `gh skill preview` for each new skill, perform a pinned
`gh skill install`, and verify the installed provenance. A changed preview
interface or external CLI failure must be recorded with exact version and output;
it does not count as a successful gate.

## Release gate

Release remains **BLOCKED — NOT RUN** until:

- the GitHub CLI and provenance gate above has completed successfully;
- every required host/model run has complete metadata and preserved evidence;
- all 36 cases have observed, classifiable results;
- no known systematic trigger conflict remains;
- every false trigger has caused a discovery-description correction and a new
  static regression case, followed by reruns; and
- untested hosts and models remain explicitly unconfirmed.

Passing runtime and GitHub CLI gates permit runtime claims only for the exact
recorded host, version, model,
configuration, installation, and revision. It does not establish general runtime
portability.
