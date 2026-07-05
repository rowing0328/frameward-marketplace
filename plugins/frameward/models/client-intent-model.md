# Client Intent Model

The client intent model translates natural language into actionable UI work.

## Inputs

- User phrase
- Screen type
- Project context
- Existing design system
- Risk level

## Intent categories

| User wording | Likely internal intent |
|---|---|
| “better” | broad visual and usability improvement |
| “cleaner” | reduce clutter, improve grouping and spacing |
| “modern” | update rhythm, surfaces, typography, interaction states |
| “trustworthy” | consistency, clarity, reduced visual noise |
| “easier” | clarify next step, reduce friction |
| “mobile feels bad” | responsive order, touch targets, sticky actions |
| “confusing” | layout, labels, feedback, next action visibility |

## Confidence

Every interpretation should have a confidence level:

- High: user asked for a specific change.
- Medium: common phrase with clear likely meaning.
- Low: broad change with unclear screen purpose.

Low confidence does not always require blocking. Use conservative defaults unless the task is high risk.
