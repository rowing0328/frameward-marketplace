# Astryx Install Policy

Do not install Astryx without explicit user approval.

## Suitable for bootstrap mode

- React project
- no mature project-native design system
- user wants a strong UI foundation
- dependency additions are allowed

## Not suitable

- Vue, Svelte, native mobile, or non-React projects
- mature existing design system
- user did not approve dependency changes
- project cannot use StyleX/CSS custom properties approach

## Suggested install command after approval

```bash
npm install @astryxdesign/core @astryxdesign/theme-neutral @astryxdesign/cli
npx astryx init --features agents --agent codex
```

After installation, read generated agent docs before writing Astryx code.
