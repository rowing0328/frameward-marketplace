# Frameward Agent Instructions

Frameward is a UI improvement framework for users who do not know UI/UX terminology.

## Prime directive

Do not require the user to know UI/UX.

When the user says something vague, translate it internally into practical UI work, then explain the result in plain language.

## Forbidden user-facing behavior

Avoid exposing these terms to non-expert users unless the user used them first:

- CTA
- conversion
- visual hierarchy
- information architecture
- cognitive load
- design token
- responsive QA
- affordance
- heuristic evaluation

Use plain equivalents:

- “the most important button”
- “what the user should notice first”
- “how the screen content is organized”
- “where the user gets stuck”
- “the project’s existing color, spacing, and text rules”
- “checking mobile, tablet, and desktop”

## Decision order

1. Understand what the user likely wants.
2. State safe assumptions in plain language.
3. Identify the screen type and main screen areas.
4. Detect the project’s design system.
5. Select a provider: project-native first, Astryx only if enabled or already present.
6. Plan small conservative changes.
7. Implement with existing components and tokens.
8. Check mobile behavior, keyboard/focus, empty/loading/error states.
9. Explain what changed and why in plain language.

## Astryx rule

Astryx is optional. Do not install it, enable its MCP server, or migrate a project to it without explicit user approval.

When Astryx is already installed, use its agent docs, CLI, or MCP context before writing Astryx component code.
