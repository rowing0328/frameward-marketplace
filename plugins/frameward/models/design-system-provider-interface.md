# Design System Provider Interface

A Frameward provider turns screen intent into implementation rules.

## Required provider sections

```yaml
name:
detection:
installationPolicy:
componentPolicy:
tokenPolicy:
layoutPolicy:
themePolicy:
agentDocsPolicy:
mcpPolicy:
versionPolicy:
riskNotes:
```

## Provider lifecycle

1. Detect
2. Select mode
3. Load documentation
4. Map layout regions to provider primitives
5. Map changes to provider components and tokens
6. Check provider-specific anti-patterns
7. Explain user-facing result in plain language

## Provider modes

- `native`: use the project’s own system
- `reference`: use guidance only
- `adapter`: directly use installed provider
- `bootstrap`: install provider with approval
- `mcp`: query provider docs through MCP with approval
