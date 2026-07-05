# Astryx Provider

Astryx is an optional Frameward provider.

Frameward may use Astryx in four modes:

| Mode | Meaning |
|---|---|
| reference | Use Astryx principles as guidance only; do not install or import packages. |
| adapter | Use Astryx directly because it is already installed. |
| bootstrap | Propose installing Astryx in a suitable React project after explicit approval. |
| mcp | Query Astryx documentation through MCP after explicit approval. |

## Positioning

Frameward is not an Astryx wrapper. Frameward decides what the screen needs; Astryx can provide implementation primitives when appropriate.

## Default

Astryx is disabled by default in `.frameward/config.example.json`.
