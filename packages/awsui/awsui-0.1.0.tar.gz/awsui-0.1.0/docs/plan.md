# awsui Implementation Plan

## Tech Stack
- **Language & Runtime**: Python 3.13 managed via uv.
- **Frameworks**: Textual (TUI), Rich (rendering helpers).
- **Tooling**: uv for dependency management, pytest for testing, ruff/black optional for lint/format.
- **External CLI**: AWS CLI v2 for STS and SSO operations.

## Milestones
1. **Foundations**: project scaffolding, configuration loading, logging utilities.
2. **Authentication Flow**: AWS CLI wrapper, credential validation, SSO retry logic.
3. **TUI Experience**: Searchable profile list, detail pane, status bar, WhoAmI.
4. **AI & Enhancements**: Amazon Q integration, autocomplete, cheatsheet.
5. **Hardening**: Error handling, observability, documentation, and cross-platform polish.

## Detailed Steps
### 1. Foundations
- Initialise `awsui` package with `app.py`, `models.py`, `aws_cli.py`, `config.py`, `logging.py`, `q_assistant.py` placeholders and `pyproject.toml` metadata (entry point `awsui.app:main`).
- Implement configuration discovery honoring `AWS_CONFIG_FILE` and `AWS_SHARED_CREDENTIALS_FILE`; create parsers that build `Profile` objects.
- Add pytest scaffolding with fixtures for synthetic AWS config files.

### 2. Authentication Flow
- Implement `aws_cli.list_profiles()` bridging to parsed models as needed.
- Create an AWS CLI runner that executes `aws sts get-caller-identity` and interprets success/failure codes.
- Add `ensure_login(profile)` that triggers `aws sso login --profile` once, surfaces progress events, and propagates errors with actionable messages.
- Cache token metadata (expiry if available) to support WhoAmI displays.

### 3. TUI Experience
- Build Textual layout: search input, ListView of profiles, detail panel (account, role, region, session, token TTL), bottom status bar.
- Wire search to filter profiles (initially substring; upgrade to multi-term if clarified).
- Bind shortcuts (`/`, `Enter`, `l`, `w`, `r`, `?`, `q`), add inline help overlay, and empty-state message guiding `aws configure sso-session`.
- Integrate login flow feedback (progress spinner, success/failure banners).

### 4. AI & Enhancements
- Integrate Amazon Q Developer CLI with contextual prompts.
- Polish command autocomplete and cheatsheet metadata.
- Provide region overrides via CLI flag or runtime shortcut without persisting to disk.

### 5. Hardening & Delivery
- Add structured JSON logging via `awsui.logging` with configurable log levels.
- Expand tests: parsing edge cases, login retry logic, CLI mode selection, TUI events (where feasible with Textual testing helpers).
- Document setup (uv-based), usage examples, troubleshooting (error codes), and security considerations in README.
- Prepare CI configuration (GitHub Actions or similar) covering Linux/macOS/Windows with Python 3.13 and coverage reporting.

## Risks & Mitigations
- **SSO inconsistencies**: rely on AWS CLI behaviour; add configurable timeouts and clear error messaging.
- **Cross-platform shell handling**: abstract shell launch logic and unit-test with platform-specific guards; confirm behaviour manually on Windows.
- **Performance regressions**: profile startup path, lazy-load heavy modules, and memoize profile parsing when possible.

## Exit Criteria
- All MVP functional requirements in `docs/specify.md` implemented and covered by automated tests.
- Structured logging enabled by default; CLI flags documented and exercised in tests.
- Verified profile switch flow (including SSO login) works on at least one POSIX shell and PowerShell.
