---
name: security-boundary-analysis
description: Build an evidence-based threat model. Use only for an explicitly authorized scope; map trust transitions, protected values, realistic attacker capabilities, abuse chains, controls, and residual uncertainty without reviewing a diff or implementing controls.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.6.4
---

# Security boundary analysis

Use the repository's established language and conventions for any artifacts you create or update.

Connect realistic attacker capabilities to concrete trust transitions and
verifiable controls. Avoid generic security checklists.

## Activation boundary

Use only for an explicitly requested and authorized threat model, abuse-path,
trust-boundary, or security model covering consequential identities, inputs,
data, capabilities, or actions.

Use `fact-based-code-review` for a finished diff, `safe-code-change` for a known
control, `solution-framing` for architecture choice, and
`product-interface-engineering` for visible consent or recovery behavior. Do not
exploit systems, broaden scope, change production, or issue a merge verdict.

## Workflow

### 1. Fix scope and evidence

Record objective, authorized systems and paths, exposure, roles, exclusions, and
missing access. Stop active investigation outside that boundary. Derive sources,
destinations, identities, permissions, validation, persistence, and crossings
from repository or provided evidence; mark unsupported topology unknown.

### 2. Model values and capabilities

Prioritize confidentiality, integrity, availability, credentials, artifacts,
audit and recovery data, and consequential actions. Describe attacker
capabilities and explicit limitations. For agents, tools, sandboxes, generated
configuration, or external outputs, use
[agentic boundaries](references/agentic-boundaries.md). Separate context influence
from file, process, network, credential, and tool side effects.

### 3. Construct and prioritize abuse chains

Connect entry condition, trust transition, control weakness or assumption,
attacker action, affected value, and concrete impact. Distinguish untrusted data
from instructions. Reject generic threats not tied to scoped evidence.

For each chain, state prerequisites, controls, likelihood, impact, uncertainty,
and the strongest risk-reducing observation. Use
[risk reasoning](references/risk-reasoning.md); avoid unsupported numeric precision.

### 4. Define controls and handoff

Separate evidenced, required, compensating, and owner-decided controls. Each
obligation names transition, placement, protection, and verification signal.

Choose exactly one state:

- `READY FOR SECURITY-AWARE IMPLEMENTATION`
- `SECURITY DECISION REQUIRED`
- `MORE SYSTEM EVIDENCE REQUIRED`
- `SCOPE NOT AUTHORIZED`
- `IMMEDIATE RISK ESCALATION`

Send selected controls to `safe-code-change` and later diffs to
`fact-based-code-review`.

## Output contract

Use these exact headings in this order:

```markdown
## Authorized scope
## System evidence
## Trust transitions
## Protected values
## Attacker capabilities
## Capability and side-effect inventory
## Abuse chains
## Existing controls
## Required controls
## Residual uncertainty
## Handoff state
```

Each chain uses `### Title` with `Entry condition`, `Trust transition`,
`Attacker action`, `Affected value`, `Existing control`, `Control gap`, `Impact`,
`Likelihood`, `Confidence`, and `Verification`.
