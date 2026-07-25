# Contributing

## Propose a skill from a problem

Start with the user problem, inputs, decisions, risks, facts, output, and
non-goals. Do not start from an imported skill, preferred workflow, or agent
client feature.

## Clean-room and licensing

Derive new content from neutral requirements. Do not copy source text, heading
order, distinctive examples, or code blocks from another skill. Do not import
content without a known compatible license and provenance.

## Package structure

```text
skills/<skill-name>/
├── SKILL.md
└── references/
    └── optional-reference.md
evals/<skill-name>.yaml
evals/test_<skill_name>.py
```

Use lowercase hyphenated names. Keep portable frontmatter limited to supported
fields and do not add client-specific metadata, tool names, commands, or runtime
assumptions. Keep referenced local files present and links relative.

## Required checks

Run the closest relevant checks before submitting:

```sh
python -m pip install -e ".[dev]"
python scripts/validate_repository.py
python scripts/check_links.py
python -m pytest -q evals
python scripts/run_evals.py
python scripts/check_distribution.py
```

Report commands actually run and their results. If a check cannot run, state why.

## Evals

Update per-skill evals and `evals/manifest.yaml` for every trigger boundary,
non-trigger, conflict, output contract, or adversarial behavior changed. Cover
positive and negative activation cases; never encode claims that require runtime
verification unless that verification is available.

## Review checklist

- Problem and non-goals are explicit.
- Skill is portable and contains no client-specific metadata or commands.
- Required output and uncertainty handling are testable.
- Links, references, and notices remain valid.
- Diff is focused and does not overwrite unrelated user work.
- Required checks and eval updates are present.

## Versioning

Use semantic versioning for releases: patch for corrections, minor for backward-
compatible skills or behavior, and major for incompatible trigger or output
contract changes. Root license and runtime portability gates must be satisfied
before a release claims full portability.
