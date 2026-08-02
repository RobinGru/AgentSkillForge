# Repository evidence

Use this guide to keep onboarding compact, current, and evidence-based.

## Claim status

| Status | Meaning |
| --- | --- |
| Observed | Directly visible in the current repository, worktree, or supplied artifact. |
| Executed | Observed by running a bounded command in the current environment. |
| Provided | Explicitly stated by the requester or an identified authoritative owner. |
| Inferred | A reasoned interpretation supported by evidence but not established. |
| Stale | Once supported but contradicted by a newer source, revision, or result. |
| Unknown | Material information that has not been established. |

Use a source path, command, revision, or owner when it helps another person
recheck the claim. A confident explanation is not stronger than inspectable
evidence.

## Evidence comparison

Evidence strength depends on the claim:

- For an executable command, a current execution result is stronger than a
  README example, while continuous-integration configuration is useful evidence
  of intended automation.
- For public behavior, current tests and interfaces are evidence; they do not
  automatically prove desired product intent.
- For architecture, code dependencies show current structure while an accepted
  decision may explain intended constraints. Record drift rather than choosing
  one silently.
- For ownership or policy, an identified maintainer or accepted repository
  artifact may be authoritative even when code cannot express the rule.
- Historical files and commits explain how the repository arrived here but are
  not automatically current instructions.

When sources conflict, name the conflict and the owner or check that can resolve
it.

## Safe inspection sequence

Start with high-signal, low-risk evidence:

1. applicable repository instructions and root documentation;
2. root tree, manifests, workspaces, and lock files;
3. task scripts and continuous-integration configuration;
4. tests, fixtures, examples, and executable entry points;
5. architecture, operations, schemas, migrations, and infrastructure relevant
   to the requested scope;
6. targeted source traversal and history only for unresolved boundaries.

Avoid recursive reading of generated, vendored, cache, artifact, dependency, and
large data directories unless the task specifically depends on them.

## Command safety

Before executing a discovered command, check whether it can:

- deploy, publish, release, migrate, delete, reset, seed, or modify remote state;
- access credentials, production data, paid services, or external systems;
- install unreviewed code or execute repository hooks;
- create large artifacts or materially alter the worktree.

Prefer read-only inspection and narrow local checks. A blocked or unsafe command
is a documented limitation, not an invitation to bypass safeguards.

## Signals of stale guidance

Treat guidance as suspect when:

- referenced paths, scripts, packages, or workflows no longer exist;
- lock files, manifests, and instructions name incompatible toolchains;
- continuous integration uses different commands from root documentation;
- a command fails before reaching the behavior it claims to verify;
- multiple instruction files state conflicting rules for the same scope;
- generated summaries contain technologies or boundaries unsupported by current
  files;
- temporary work, milestone state, or session history appears in permanent
  repository instructions.

## Minimal-context rule

Repository onboarding should produce a map, not a dump. Keep only facts that
change how later work is located, bounded, executed, or verified. Place detailed
knowledge in focused documents that can be read on demand, and reserve permanent
instruction files for short, actionable rules and pointers.
