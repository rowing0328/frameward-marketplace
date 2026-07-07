---
name: reference-analysis
description: Use when a user provides a reference screen, screenshot, site, Figma note, or example UI before improving a Frameward screen.
---

# reference-analysis

## Goal

Separate what Frameward can safely learn from a reference screen from what it should not copy.

Use this before implementation when the user provides a screenshot, site, Figma note, existing UI, or manually described example as a reference.

## When to use

Use this skill when:

- The user says to copy, follow, match, take inspiration from, benchmark, or compare a reference.
- The user provides screenshots, URLs, Figma notes, or example screens.
- A screen improvement depends on understanding which parts of a reference are useful.
- A new project needs a reference-informed first screen, but the project has its own product and UI rules.

Do not use this skill when:

- The user only asks to improve the current screen and provides no reference.
- The task is not UI-related.
- The user asks for a full static handoff package rather than a Frameward improvement pass.

## Process

1. Record the reference source and confidence.
2. Identify the reference parts that matter to the current task.
3. Separate visible facts from interpretation.
4. List what Frameward can learn from the reference.
5. List what Frameward must not copy.
6. Map safe learnings to target screen areas.
7. Preserve the current project's existing UI rules first.
8. Define checks to run before implementation.
9. Explain the result in plain language.

## Analysis fields

Use these fields unless the task needs a shorter answer.

```text
Reference summary
- Source:
- Confidence:
- Relevant parts:

Visible facts
- Screen structure:
- Information grouping:
- Important action:
- Text and density:
- States and feedback:

Safe to learn
- What can transfer:
- Why it helps:
- Target screen area:
- Existing project rule to preserve:
- Allowed adaptation:

Do not copy
- Brand-specific elements:
- Unsupported claims:
- Layout risks:
- Accessibility risks:
- Project mismatch:

Checks before implementation
- Mobile:
- Keyboard and focus:
- Loading, empty, and error states:
- Text fit:
- Existing component/style rules:

Plain-language summary
- Summary:
```

## Rules

- Do not implement code in this skill.
- Do not generate images in this skill.
- Do not install UI libraries in this skill.
- Do not activate external providers in this skill.
- Do not copy a reference screen wholesale.
- Do not carry over logos, official marks, certifications, security claims, customer claims, or authority signals without a source supplied by the user.
- Do not use expert terms in the final explanation when plain language is enough.
- Treat the project's existing components, colors, spacing, and text rules as the default.

## Output

Return a concise reference analysis that can be used by later Frameward skills.

End with one of these next-step recommendations:

- `Next: layout-region-mapping` when screen areas are still unclear.
- `Next: design-system-provider-detection` when the project UI system is unknown.
- `Next: design-system-audit` when the provider is known but local rules need inspection.
- `Next: screen-improvement-plan` when the reference analysis and local UI rules are clear.
