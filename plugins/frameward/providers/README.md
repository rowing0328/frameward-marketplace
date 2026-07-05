# Providers

Providers adapt Frameward decisions to specific design systems.

Frameward always detects and respects the project-native design system first. External providers are optional.

## Included providers

- `project-native`: generic provider for existing project components and tokens.
- `astryx`: optional Astryx provider for React/StyleX projects or reference-only guidance.
- `shadcn`: placeholder provider shell for future expansion.
- `tailwind`: placeholder provider shell for future expansion.
- `mui`: placeholder provider shell for future expansion.

## Provider selection

```text
project-native > installed provider > explicitly requested provider > reference-only guidance
```

## Safety

Do not install dependencies, configure MCP, or migrate a UI library without explicit approval.
