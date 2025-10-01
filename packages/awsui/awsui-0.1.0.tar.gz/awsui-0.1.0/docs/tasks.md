# awsui Task List

## Ready
- Scaffold project structure (`pyproject.toml`, package modules, entrypoint wiring).
- Implement AWS config/credentials parsers with unit tests covering SSO and assume-role scenarios.
- Build AWS CLI wrapper for `sts get-caller-identity` with retry via `aws sso login`.
- Create Textual layout (search box, profile list, detail pane, status bar) with placeholder data.
- Design structured logging helper and integrate with CLI argument parsing.

## In Progress
- Clarify outstanding questions in `docs/clarify.md` with stakeholders (region override persistence, search semantics, TTL display, login UX, log formatting).

## Next
- Connect TUI selection to authentication flow and status updates.
- Add WhoAmI panel rendering TTL and identity info from cached credentials.
- Build integration tests simulating expired credentials and SSO recovery.
- Document installation (uv) and troubleshooting steps in README.
- Configure CI matrix (Linux/macOS/Windows) with coverage reporting ≥ 80%.
