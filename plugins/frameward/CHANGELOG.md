# Changelog

## 0.1.0 - Scaffold hardening

### Changed

- Reframed the repository as a clean Frameward v0.1 scaffold.
- Improved README onboarding for new users, Codex usage, loop gates, modes, and optional Astryx support.
- Aligned the hook loop with the eight Frameward gates: intent, language, layout, system, ratio, implementation, quality, and explanation.
- Added `balanced` and `hybrid-strict` mode support while keeping `advisory` as the safe default.
- Made strict hook behavior gate-specific instead of globally aggressive.
- Strengthened dependency-install and Astryx MCP safeguards so they require explicit user approval.
- Improved skill descriptions so Codex can select skills more reliably.
- Expanded scaffold validation to check plugin paths, hook paths, hook Python syntax, skill frontmatter, gate config, loop modes, schema JSON, and Astryx defaults.
- Added Korean local plugin installation documentation.
- Added Korean internal architecture documentation for early users.
- Added new-project UI foundation docs, workflow, template, and model.
- Added a lightweight reference-analysis skill, model, and template for safely learning from reference screens without copying brand-specific or unsupported details.

### Notes

Astryx remains optional, disabled by default, and does not become a Frameward dependency.

## 0.0.1 - Initial scaffold

### Added

- Frameward brand and core philosophy
- Codex plugin manifest
- Hook-based Frameward Loop
- Plain-language client policy
- Layout region and layout ratio models
- Design-system provider layer
- Optional Astryx provider
- Astryx install, detection, component, token, layout, theme, agent-docs, MCP, and version policies
- Provider detection skill
- Astryx adapter skill
- Initial schemas, templates, workflows, and examples

### Notes

Astryx is included as an optional provider. It is not enabled by default and must not be installed or configured without explicit approval.
