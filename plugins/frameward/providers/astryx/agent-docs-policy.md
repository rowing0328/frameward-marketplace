# Astryx Agent Docs Policy

Astryx component work requires current docs.

## Required before writing Astryx code

At least one of:

```bash
npx astryx init --features agents --agent codex
```

```bash
npx astryx component <Name> --dense
npx astryx docs tokens --dense
npx astryx docs layout --dense
```

Or an approved Astryx MCP lookup.

## Why

Agent docs prevent common mistakes:

- generic React fallbacks
- invented props
- incorrect import paths
- hardcoded values
- raw elements where components exist
