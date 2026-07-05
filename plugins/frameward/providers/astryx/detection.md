# Astryx Detection

Detect Astryx by checking:

- `package.json` dependencies:
  - `@astryxdesign/core`
  - `@astryxdesign/cli`
  - `@astryxdesign/theme-*`
- imports from `@astryxdesign/core/*`
- global CSS imports:
  - `@astryxdesign/core/reset.css`
  - `@astryxdesign/core/astryx.css`
  - `@astryxdesign/theme-*/theme.css`
- generated agent docs mentioning Astryx
- MCP config containing `https://astryx.atmeta.com/mcp`

If installed, set provider mode to `adapter`. If not installed, use `reference` unless the user approves bootstrap.
