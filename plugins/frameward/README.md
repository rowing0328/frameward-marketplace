# Frameward

Frameward is an open-source, agent-native UI improvement framework for Codex.

It helps Codex turn vague screen feedback like “make this page better”, “make it cleaner”, “make it easier to use”, or “make it more modern” into a clear improvement loop: understand the request, map the screen, follow the project’s existing UI rules, make conservative changes, check the result, and explain the work in plain language.

Frameward is not a UI component library. It is not an Astryx wrapper. It is a hook-guided way to help Codex improve screens without forcing users to learn design vocabulary.

## Who It Is For

Frameward is for product teams, maintainers, designers, and developers who want Codex to handle unclear screen feedback more reliably.

Users can say things like:

- “이 화면 좀 더 좋게 해줘.”
- “뭔가 촌스러워요.”
- “더 깔끔하게 만들어주세요.”
- “모바일에서 불편해요.”
- “어디를 눌러야 할지 모르겠어요.”
- “This settings page feels confusing.”

Frameward turns that into practical work without asking the user to name formal design concepts.

## Why It Avoids Jargon

Most users describe the problem in everyday language. Frameward keeps that language intact.

Codex may reason internally about layout, states, spacing, and quality, but user-facing answers should say things like:

- what users should notice first
- the most important button
- where the screen feels crowded
- where users might get stuck
- the project’s existing color, spacing, and text rules
- checking mobile, tablet, and desktop

This keeps the final explanation useful to people who care about the screen but do not speak in specialist terms.

## The Frameward Loop

Frameward uses eight gates to keep Codex from jumping straight into random visual changes.

1. **Intent Gate**: understand what the user probably wants.
2. **Language Gate**: keep user-facing explanations plain.
3. **Layout Gate**: identify the main screen areas and what each one is for.
4. **System Gate**: inspect the project’s existing components, colors, spacing, and text rules.
5. **Ratio Gate**: check whether spacing and sizing feel balanced without forcing rigid math.
6. **Implementation Gate**: make small, safe changes that match the interpreted goal.
7. **Quality Gate**: check mobile behavior, keyboard/focus, empty/loading/error states, and important actions.
8. **Explanation Gate**: explain what changed and why in plain language.

## Using It With Codex

Install or load this repository as a local Codex plugin, then ask Codex to use Frameward on UI work.

Example prompts:

```text
Use Frameward to improve this screen. The user only said “make it cleaner,” so infer a safe direction, preserve the project’s existing UI rules, and explain the result plainly.
```

```text
Use Frameward to audit this settings page. Tell me where people may get stuck and suggest conservative improvements.
```

```text
Use Frameward with Astryx only if this project already uses Astryx. Do not install Astryx or enable MCP unless I explicitly approve it.
```

## Modes

Frameward defaults to `advisory` mode. This is the safest starting point because hooks add helpful context but avoid blocking normal work.

Modes are configured in `.frameward/config.json` or copied from `.frameward/config.example.json`:

```json
{
  "enforcementMode": "advisory"
}
```

Available modes:

- `advisory`: adds guidance and reminders, with minimal interference.
- `balanced`: stays quiet for non-UI tasks, warns more clearly for likely UI edits, and blocks dependency installs or external provider activation unless explicitly approved.
- `hybrid-strict`: uses strict checks for likely UI edits and final quality/explanation checks, while avoiding unrelated work.
- `strict`: blocks likely UI edits when pre-edit gates are missing and can continue a turn when final checks are missing.

Strict behavior is gate-specific. It is not meant to block every command or force a heavy process onto non-UI tasks.

## Providers

Frameward is framework-agnostic. It should use the project’s existing UI system first.

Provider priority:

1. Project-native components and styling rules.
2. A provider already installed in the project.
3. A provider explicitly requested by the user.
4. Reference-only guidance.

Included provider docs:

- `project-native`: existing project components and styling.
- `astryx`: optional provider for React projects.
- `shadcn`, `tailwind`, `mui`: placeholder provider shells for future expansion.

## Astryx

Astryx is optional. Frameward must not install Astryx, enable Astryx MCP, or migrate a project to Astryx without explicit user approval.

Frameward documents four Astryx modes:

- **Reference mode**: learn from Astryx guidance without installing anything.
- **Adapter mode**: use Astryx because the project already uses it.
- **Bootstrap mode**: propose Astryx for a new React project only after approval.
- **MCP mode**: connect Astryx documentation through MCP only after approval.

Frameward is not an Astryx wrapper. Astryx is one optional provider among others.

## Repository Structure

```text
frameward/
  .codex-plugin/       Codex plugin manifest
  .frameward/          Example project configuration
  core/                Principles, decision order, language rules, loop gates
  docs/                Human-readable design and architecture docs
  models/              Framework models used by skills and hooks
  providers/           UI provider adapters and policies
  ratio-profiles/      Screen-specific spacing and sizing guidance
  skills/              Codex skills
  workflows/           End-to-end workflows
  hooks/               Codex lifecycle hooks
  schemas/             JSON schemas for internal state and reports
  templates/           Report and checklist templates
  examples/            Example requests and outcomes
  assets/              Plugin assets
```

## Design Documentation

Frameward currently keeps its internal design documentation in Korean for the primary early users:

- [로컬 플러그인 설치](./docs/local-plugin-install.ko.md)
- [Frameward 내부 설계](./docs/architecture.ko.md)
- [새 프로젝트 UI 흐름](./docs/new-project-flow.ko.md)

## Validation

Run the scaffold validator after edits:

```bash
python3 tools/validate_scaffold.py
```

The validator checks plugin metadata, hook configuration, Python hook syntax, skill metadata, schemas, example config safety, and Astryx defaults.

## Roadmap

### v0.1

- Frameward identity and loop gates
- Plain-language policy
- Codex plugin manifest
- Conservative hook loop
- Provider layer with project-native first
- Astryx as an optional provider
- Initial skills, schemas, templates, workflows, and examples

### v0.2

- Provider detection tests
- More framework-specific examples for React, Next.js, and Vite
- Expanded shadcn, Tailwind, and MUI provider docs
- Stronger examples for mobile and data-heavy screens
