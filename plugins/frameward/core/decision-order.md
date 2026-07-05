# Decision Order

Use this order for every Frameward task.

## 1. Is this a UI task?

Skip Frameward gates for pure backend, data, deployment, or documentation tasks unless the user explicitly requests UI review.

## 2. What does the user likely mean?

Translate vague language into a likely direction.

Examples:

- “cleaner” → reduce clutter, align spacing, improve grouping
- “modern” → simplify surfaces, improve typography rhythm, remove dated decoration
- “easier” → clarify next action, reduce steps, improve feedback
- “trustworthy” → consistency, calm spacing, stronger labels, fewer gimmicks

## 3. What is the screen type?

Examples:

- landing page
- dashboard
- form
- settings
- detail page
- list/table
- mobile screen
- modal
- card/component

## 4. What are the screen regions?

Find navigation, main content, supporting content, important buttons, feedback messages, overlays, and mobile-safe areas.

## 5. What design system exists?

Prefer:

1. Project-native system
2. Explicitly enabled provider
3. Reference-only provider guidance
4. Minimal changes without introducing a new system

## 6. Should Astryx be used?

Use Astryx only when:

- the project already uses Astryx,
- the user explicitly asks for Astryx,
- or the user approves adopting it.

Do not install or configure it silently.

## 7. What can be safely improved?

Vague requests default to safe improvements: spacing, grouping, labeling, visible important buttons, states, and mobile behavior.

## 8. How should the result be explained?

Translate technical changes into simple reasons:

- “I made the main action easier to find.”
- “I grouped related information so the screen feels less busy.”
- “I kept the project’s existing color and spacing rules.”
