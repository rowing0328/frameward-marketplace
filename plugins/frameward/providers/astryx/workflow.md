# Astryx Workflow

## Reference mode

1. Keep project dependencies unchanged.
2. Use Astryx principles: frame-first, tokens, components over primitives.
3. Implement with the project-native provider.

## Adapter mode

1. Confirm Astryx is installed.
2. Read generated agent docs or use the local CLI when available.
3. Use MCP only when the user has explicitly approved it.
4. Map Frameward regions to Astryx layout primitives.
5. Use components and token-safe styling.
6. Run Frameward quality checks.

## Bootstrap mode

1. Confirm React suitability.
2. Ask for explicit approval.
3. Install packages.
4. Run `npx astryx init --features agents --agent codex`.
5. Read docs.
6. Implement a small representative screen before wider migration.
