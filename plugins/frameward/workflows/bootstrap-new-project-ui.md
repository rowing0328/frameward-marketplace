# Workflow: Bootstrap New Project UI

Use this when the user asks Frameward to create a first screen or UI foundation for a brand-new project, or for a project that has no mature UI rules yet.

This workflow does not install dependencies. It may evaluate providers, including Astryx, but provider installation and MCP activation require explicit user approval.

## Process

1. Confirm this is a new project or a project without mature UI rules.
2. Identify the product type, primary users, and first representative screen.
3. Write a minimal UI foundation brief before implementation.
4. Check whether a provider is already present in the project.
5. Compare provider-neutral, project-native, and explicitly approved provider paths.
6. Evaluate Astryx as a candidate only; do not install Astryx or enable Astryx MCP.
7. Select the safest path and explain the reason in plain language.
8. Define loading, empty, error, disabled, and success states before implementation.
9. Define mobile, tablet, and desktop behavior before implementation.
10. Implement only after the foundation is clear.
11. Explain what foundation decisions were made and what remains open.

## Provider Decision Rules

- Use project-native rules if they already exist.
- Use provider-neutral rules when the project has no mature UI system.
- Use Astryx directly only when it is already installed or explicitly approved.
- Propose Astryx bootstrap only when the project is React-based, lacks mature UI rules, and the user approves dependency changes.
- Do not enable MCP without explicit approval.

## Required Output

```md
### New project status
-

### Primary user and first screen
-

### UI foundation summary
-

### Provider decision
-

### Astryx candidate evaluation
-

### States and screen sizes covered
-

### Plain-language explanation
-
```
