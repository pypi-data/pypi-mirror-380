# awsui Constitution

## Mission
- Deliver a fast, reliable, cross-platform terminal UI for discovering and switching AWS profiles with seamless SSO re-authentication.
- Empower engineers to see their active AWS identity at a glance and avoid costly environment mistakes.

## Product & UX Principles
- Prioritise speed: startup under 300 ms, search results within 50 ms, end-to-end profile switch under 5 s.
- Keep interactions discoverable: clear keyboard shortcuts, contextual help, and meaningful empty states.
- Respect the terminal: no unnecessary noise on STDOUT; user-facing text should default to Traditional Chinese with an English fallback.

## Engineering Principles
- Target Python 3.13 with Textual ≥ 0.60 and Rich ≥ 13.7; depend on uv for reproducible tooling.
- Treat AWS configuration files as read-only sources; never persist long-lived credentials locally.
- Structure the codebase into focused modules (`app`, `models`, `aws_cli`, `config`, `logging`, `q_assistant`) to keep responsibilities isolated and testable.

## Development Workflow
- Capture requirements and user stories in `docs/specify.md`; keep clarifications in `docs/clarify.md` and update them before planning.
- Use `docs/plan.md` for iteration-level implementation plans and `docs/tasks.md` for day-to-day execution tracking.
- Prefer incremental, reviewable changes with automated tests and logging instrumentation accompanying new features.

## Quality & Observability
- Enforce automated linting and unit tests locally (or in CI) before merge; maintain ≥ 80% coverage on core modules.
- Mock AWS CLI subprocesses in tests to ensure deterministic CI runs; add integration smoke tests with uv when feasible.
- Emit structured JSON logs on STDERR (`ts, level, action, duration_ms, profile, result`) and keep log verbosity tuneable via CLI.

## Security & Privacy
- Trust but verify AWS CLI output; handle errors defensively and avoid leaking sensitive identifiers in logs.
- Support `AWS_CONFIG_FILE` and `AWS_SHARED_CREDENTIALS_FILE` overrides to respect user environments.
- Document recovery steps for authentication failures and make retries safe and idempotent.
