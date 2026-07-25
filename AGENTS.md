# Repository development rules

## Scope

This repository distributes portable AgentSkillForge packages. `AGENTS.md` governs
repository development only; distributed skills must not depend on it at runtime.

## Rules

1. Keep skills portable across agent clients. Do not add client-specific
   metadata, tool names, slash commands, or runtime assumptions.
2. Do not claim a validation, measurement, review, or test result unless it
   was actually run and its result observed.
3. Keep Markdown links and referenced local files valid. Update or remove
   references in the same change that changes their targets.
4. Follow the clean-room process: derive replacement skills from neutral
   requirements, not by copying protected source text or structure.
5. Make small, focused patches. Do not delete legacy files until their
   validated replacements are ready.
6. Add or update required evals for every skill behavior, trigger boundary,
   and output contract that changes.
7. Do not modify user files outside the requested scope. Preserve existing
   uncommitted work unless the user explicitly asks otherwise.
8. Run the closest relevant repository checks before reporting work complete;
   report checks that are not run and why.
