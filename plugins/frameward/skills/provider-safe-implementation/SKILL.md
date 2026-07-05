---
name: provider-safe-implementation
description: Use while editing UI so changes follow the selected project-native or approved provider rules.
---

# provider-safe-implementation

## Goal

Ensure implementation follows provider-specific rules.

## When to use

Use immediately before and during code edits.

## Process

1. Load active provider state.
2. Read provider component and token policy.
3. Avoid hardcoded styles.
4. Avoid duplicate components.
5. Verify imports and props from docs or local examples.
6. Record provider assumptions.

## Output

```md
### Active provider
-

### Rules followed
-

### Components used
-

### Tokens/styles used
-

### Deviations
-
```

## User-language rule

Do not expose expert UI/UX terminology to non-expert users. Translate internal findings into plain language.
