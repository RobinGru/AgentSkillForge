---
name: security-boundary-analysis
description: Analyze an explicitly requested security or threat-modeling scope by mapping evidence-backed trust transitions, protected assets, realistic attacker capabilities, abuse paths, controls, and residual uncertainty. Do not use for generic code review, broad architecture summaries, or unspecific security advice.
license: Apache-2.0
compatibility: AgentSkillForge
metadata:
  version: 0.3.0-beta.1
---

# Security boundary analysis

Produce an evidence-based security model for an explicitly authorized scope.
Connect realistic attacker capabilities to concrete trust transitions and
verifiable control obligations rather than supplying a generic checklist.

## Activation boundary

Use this skill when the user explicitly requests a threat model, abuse-path
analysis, trust-boundary analysis, or a security model for authentication,
authorization, tenant isolation, untrusted inputs, uploads, webhooks, plugins,
agent tools, skill supply chains, secrets, sensitive data, money movement, or
irreversible actions.

Do not use it when:

- A finished diff merely needs review; use `fact-based-code-review` unless a
  security model is explicitly requested as its contract.
- A known local control only needs implementation; use `safe-code-change`.
- The request is generic security education, an architecture summary, or vague
  advice without a security decision.
- Architecture or product options must be selected; supply security constraints
  to `solution-framing` instead.
- The task only designs visible consent, permission, or recovery interactions;
  pass constraints to `product-interface-engineering`.

## Capability disclosure

- **Positive example:** Map trust transitions and abuse paths for a webhook that
  accepts externally signed events and writes tenant data.
- **Near non-trigger:** Review an authentication patch for correctness without a
  threat-model request; use `fact-based-code-review`.
- **Main output:** An authorized security-boundary model containing concrete
  abuse chains, control obligations, and residual uncertainty.
- **Explicit non-actions:** Do not exploit systems, change production, broaden
  authorization, choose general architecture, design UI, or issue a merge verdict.

## Workflow

### 1. Fix authorization and scope

Record the analysis objective, approved systems and paths, deployment exposure,
known roles, exclusions, and missing access. Stop active investigation outside
that boundary.

### 2. Derive trust transitions

Use repository evidence, configuration, and user-provided facts to map sources,
destinations, data or actions, identities, permissions, validation, persistence,
and process or network crossings. Mark unsupported topology as unknown.

### 3. Inventory protected values and capabilities

Prioritize confidentiality, integrity, availability, credentials, release
artifacts, audit data, recovery material, and consequential actions. Describe
attacker capabilities narrowly, including capabilities they do not possess.
Use [agentic boundaries](references/agentic-boundaries.md) when skills, agents,
tools, sandboxes, generated configuration, or external outputs are in scope.

Separate context influence from side effects. For file, process, network,
credential, and tool access, state whether the capability is declared, observed,
assumed, or unknown and whether it is temporary or persistent.

### 4. Construct abuse chains

For each credible chain connect an entry condition, trust transition, control
weakness or assumption, attacker action, affected value, and concrete impact.
Distinguish untrusted data from instructions, especially in agentic systems.
Avoid generic threats that cannot be tied to scoped evidence.

### 5. Reason about priority

For each chain, explain prerequisites, existing controls, likelihood, impact,
uncertainty, and the strongest risk-reducing observation. Apply
[risk reasoning](references/risk-reasoning.md); avoid numeric precision that the
evidence cannot support.

### 6. Define control obligations

Separate evidenced controls, required controls, compensating controls, and items
requiring an owner decision. Every obligation must identify its trust transition,
placement, intended protection, and verification signal.

### 7. Select the handoff

Choose exactly one state:

- `READY FOR SECURITY-AWARE IMPLEMENTATION`
- `SECURITY DECISION REQUIRED`
- `MORE SYSTEM EVIDENCE REQUIRED`
- `SCOPE NOT AUTHORIZED`
- `IMMEDIATE RISK ESCALATION`

Send selected controls to `safe-code-change`. Send a later implementation diff to
`fact-based-code-review`; do not make the merge decision here.

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

Each chain must use `### Title` followed by `Entry condition`, `Trust transition`,
`Attacker action`, `Affected value`, `Existing control`, `Control gap`, `Impact`,
`Likelihood`, `Confidence`, and `Verification` fields.
