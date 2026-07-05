---
name: design-system-provider-detection
description: Use before UI edits to decide whether to follow project-native UI rules, existing Astryx usage, or another approved provider.
---

# design-system-provider-detection

## Goal

Select the safest design-system provider before UI implementation.

## When to use

Use before design-system-audit and before any component changes.

## Process

1. Inspect package dependencies.
2. Search for local UI components and tokens.
3. Detect Astryx, shadcn/ui, MUI, Tailwind, or custom systems.
4. Prefer project-native provider.
5. If Astryx is present, mark mode as adapter.
6. If Astryx is absent, do not install it; mark reference mode unless user approves.
7. Record provider state.

## Output

```md
### Detected providers
-

### Active provider
-

### Provider mode
-

### Evidence
-

### Safe implementation rule
-

### Approval needed
-
```

## User-language rule

Do not expose expert UI/UX terminology to non-expert users. Translate internal findings into plain language.
