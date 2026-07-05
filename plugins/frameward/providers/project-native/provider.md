# Project-Native Provider

The project-native provider is the default provider.

Use it when a project already has components, tokens, CSS variables, Tailwind config, theme files, or design-system conventions.

## Priority

Project-native comes before Astryx or any other external provider.

## Rules

- Search existing components before creating new ones.
- Reuse token variables before adding raw colors or spacing.
- Match file organization and import style.
- Preserve existing framework conventions.
- Do not introduce a new design system unless asked.
