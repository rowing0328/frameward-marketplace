# Frameward Loop Gates

Frameward uses gates to keep Codex from skipping important UI work.

## Gates

### Intent Gate

Has the vague request been translated into a practical direction?

### Language Gate

Will the final explanation avoid unnecessary UX jargon?

### Layout Gate

Have the main screen areas been identified?

### System Gate

Has the existing design system been inspected?

### Ratio Gate

Has proportion and spacing rhythm been considered without forcing rigid math?

### Implementation Gate

Are changes small, safe, and aligned with the interpreted goal?

### Quality Gate

Have mobile, accessibility, and screen states been checked?

### Explanation Gate

Will the user understand what changed and why?

## Modes

### Advisory

Hooks provide extra context and warnings but do not aggressively block work.

### Balanced

Hooks stay quiet for non-UI tasks, warn more clearly for likely UI edits, and block dependency installs or external provider activation unless the user explicitly approves them.

### Hybrid-strict

Hooks use strict checks for likely UI edits and final quality/explanation checks, while still avoiding unrelated non-UI work.

### Strict

Hooks can deny likely UI edits when pre-edit gates are missing and can continue the turn when final language, quality, or explanation checks are missing. Strict checks are gate-specific; they are not a global block on every command.
