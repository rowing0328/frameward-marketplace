# Astryx Component Policy

When using Astryx directly:

1. Read Astryx agent docs first.
2. Use local Astryx agent docs or CLI docs before writing component code. Use MCP docs only after explicit approval.
3. Do not guess import paths.
4. Do not invent props.
5. Prefer Astryx components for covered UI elements.
6. Avoid raw `div` structures when an Astryx layout or component exists.
7. Use components according to screen archetype.

## Frameward plain-language mapping

Internal:

```text
Use Button for the primary action.
```

Client-facing:

```text
I made the most important button easier to find and kept it consistent with the project’s UI library.
```
