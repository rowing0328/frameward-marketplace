---
name: state-coverage-check
description: Use when making sure a screen handles default, loading, empty, error, disabled, and success states.
---

# state-coverage-check

## Goal

Prevent UI quality from only covering the happy path.

## When to use

Use for dashboards, forms, tables, modals, and data-driven screens.

## Process

1. Identify data and action states.
2. Check missing content cases.
3. Check loading and partial loading.
4. Check error recovery.
5. Check disabled and success states.
6. Use plain language in final notes.

## Output

```md
### States covered
- Default:
- Loading:
- Empty:
- Error:
- Disabled:
- Success:

### Missing states
-

### Recommendations
-
```

## User-language rule

Do not expose expert UI/UX terminology to non-expert users. Translate internal findings into plain language.
