---
name: astryx-adapter
description: Use only when a React project already uses Astryx or the user explicitly approves Astryx support.
---

# astryx-adapter

## Goal

Apply Frameward improvements using Astryx only when it is already installed or explicitly approved.

## When to use

Use only when Astryx is installed in the project or explicitly approved as a provider.

## Process

1. Confirm provider mode: reference, adapter, bootstrap, or mcp.
2. Read local Astryx agent docs or CLI docs before writing Astryx code. Use MCP docs only after explicit approval.
3. Choose a frame-first layout.
4. Use Astryx components when available.
5. Use token-safe styling.
6. Avoid raw divs, style={{}}, hardcoded colors, and invented props.
7. Explain the result in plain language.

## Output

```md
### Astryx mode
-

### Docs checked
-

### Components selected
-

### Token/styling policy
-

### Layout policy
-

### User-facing explanation
-
```

## User-language rule

Do not expose expert UI/UX terminology to non-expert users. Translate internal findings into plain language.

## Safety

Do not install Astryx or enable Astryx MCP without explicit approval.
