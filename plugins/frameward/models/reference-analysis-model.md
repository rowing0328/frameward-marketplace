# Reference Analysis Model

The reference analysis model helps Frameward learn from example screens without copying them blindly.

It is used only when a user provides a reference screen, screenshot, site, Figma note, existing UI, or manual example.

## Purpose

Frameward should turn reference input into practical guidance:

```text
visible fact
  -> safe learning
  -> target screen area
  -> existing project rule
  -> quality check
```

This keeps the work grounded in what can be seen while preserving the current project's own UI rules.

## Fields

### Reference Source

Records where the reference came from.

- `source`: screenshot, URL, Figma note, existing UI, manual description, or mixed.
- `providedBy`: user, local project, public source, or unknown.
- `confidence`: high, medium, or low.
- `relevantParts`: page frame, navigation, content area, cards, forms, buttons, lists, states, or other named areas.

### Visible Fact

Records what is visible before interpretation.

Examples:

- The primary action appears in the first screen.
- Cards use short titles and one supporting line.
- Dense lists collapse into grouped rows on smaller screens.
- Error text appears directly under the input.

### Interpretation

Explains why a visible fact may matter.

Examples:

- The first action is easy to find.
- Related information is grouped clearly.
- Mobile users can scan the list before opening details.
- The form keeps the problem close to the field.

### Safe Adoption

Defines what Frameward can learn from the reference.

Examples:

- Use a similar order of information.
- Keep the main action visible near the relevant content.
- Use short helper text for complex choices.
- Keep state messages close to the element they explain.

### Forbidden Carryover

Defines what Frameward must not copy.

Examples:

- Logos and brand marks.
- Product-specific claims.
- Certification, security, or authority signals.
- Copy that implies unsupported proof.
- Layout details that conflict with the current project.

### Target Application Area

Names where the safe learning may apply.

Allowed values:

- `page_frame`
- `navigation`
- `content_sections`
- `cards`
- `lists_tables`
- `forms`
- `buttons`
- `state_views`
- `mobile_behavior`

### Existing Project Rule

Records what local rule should stay in charge.

Examples:

- Existing button component.
- Existing spacing scale.
- Existing type sizes.
- Existing color roles.
- Existing form state pattern.
- Existing mobile breakpoint behavior.

### Quality Check

Defines what must be checked before implementation is considered ready.

Required checks when relevant:

- Mobile layout keeps the important action reachable.
- Keyboard focus is visible.
- Loading, empty, and error states remain clear.
- Text fits without overlapping.
- The implementation follows existing components and style rules.

## Completion Criteria

A reference analysis is complete when it identifies:

- the reference source and confidence,
- visible facts,
- safe learnings,
- items not to copy,
- target screen areas,
- existing project rules to preserve,
- checks to run before implementation.
