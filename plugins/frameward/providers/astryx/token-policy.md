# Astryx Token Policy

Use Astryx tokens and CSS custom properties instead of hardcoded values.

## Avoid

```tsx
style={{ color: '#fff', marginTop: 16 }}
```

## Prefer

- Astryx component props
- token-backed StyleX or Tailwind utilities
- CSS custom properties from the active theme
- spacing/radius/color values provided by the system

## Rule

Do not turn Frameward ratio guidance into raw pixel magic numbers. Convert ratio suggestions into Astryx-safe values.
