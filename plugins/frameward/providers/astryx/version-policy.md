# Astryx Version Policy

Astryx is a fast-moving design system and may change while in beta.

## Policy

- Detect installed version from `package.json`.
- Prefer installed docs generated from that version.
- Do not assume props from memory.
- Re-run agent docs after a version bump.
- Record supported versions in provider state.

## Default scaffold support

```json
{
  "supportedVersions": ["0.1.x"],
  "versionPolicy": "pin-and-detect"
}
```
