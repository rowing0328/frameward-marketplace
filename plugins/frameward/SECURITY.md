# Security Policy

Frameward hooks are designed to be conservative.

## Hook safety

- Hooks should skip non-UI tasks unless explicitly configured otherwise.
- Strict mode should be opt-in.
- Dependency installation must require explicit approval.
- MCP configuration must require explicit approval.
- Hooks should not send code, user data, or proprietary design-system information to external services by default.

## Reporting

Open an issue or contact the maintainers when a hook blocks safe work, allows unsafe work, or leaks information.
