# Frameward Philosophy

Frameward exists for users who cannot precisely describe UI/UX.

The user should be allowed to speak naturally:

> “Make this screen better.”

Frameward converts that into a structured improvement loop:

```text
intent → layout → system → provider → ratio → implementation → quality → explanation
```

## Core belief

A coding agent should not decorate a screen randomly. It should first understand what the screen is for, what the user should notice, what action should be easy, and which project rules already exist.

## Plain language first

Frameward uses expert concepts internally, but final answers should be understandable to a non-designer.

Internal:

```text
Primary CTA prominence is weak.
```

Client-facing:

```text
The most important button is not easy to notice. I made it clearer what the user should do next.
```

## Design systems before taste

When a project already has a design system, Frameward follows it first. When a project does not, Frameward can suggest optional providers such as Astryx, but only with explicit approval for new dependencies.
