# Astryx MCP Policy

Astryx MCP is optional.

Do not enable MCP automatically.

## Example MCP config

```json
{
  "mcpServers": {
    "astryx": {
      "type": "url",
      "url": "https://astryx.atmeta.com/mcp"
    }
  }
}
```

## Use MCP when

- the user approves external documentation lookup,
- Astryx provider is enabled,
- accurate component documentation is needed.

## Do not use MCP when

- the project policy forbids external tools,
- the user has not approved it,
- project-native design system is enough.
