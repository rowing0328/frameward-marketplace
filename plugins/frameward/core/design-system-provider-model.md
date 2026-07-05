# Design System Provider Model

Frameward separates UI judgment from UI implementation.

```text
Frameward decides what should improve.
Providers decide how that improvement should be expressed in a specific design system.
```

## Provider priority

1. Project-native components and tokens
2. Provider already installed in the project
3. Provider explicitly requested by the user
4. Reference-only guidance

## First-class providers

- `project-native`
- `astryx`
- `shadcn`
- `tailwind`
- `mui`

Only `project-native` and `astryx` are fully scaffolded in this version.

## Provider responsibilities

A provider must define:

- Detection
- Installation policy
- Component usage
- Token/styling policy
- Layout policy
- Accessibility assumptions
- Version policy
- Agent documentation policy

## Non-negotiable rules

- Do not add dependencies without explicit approval.
- Do not replace a mature project-native design system unless asked.
- Do not invent component props when provider docs are available.
- Do not expose provider internals to the user unless needed.
