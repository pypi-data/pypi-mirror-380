# awsui Clarifications

## Open Questions
1. **Region override persistence**: When a user presses `r` to set a temporary region, should that value persist across sessions or only for the current invocation?
2. **Search behaviour**: Do we require fuzzy matching (e.g., `prod admin` splitting terms) or is simple case-insensitive substring search sufficient for MVP?
3. **Token TTL display**: If the AWS CLI cache lacks TTL metadata, should we hide the field, show `unknown`, or approximate using file mtime?
4. **Login progress UI**: Should the TUI block interaction during `aws sso login`, or allow cancellation and fallback to manual retry?
5. **Logging configuration**: Is JSON logging always enabled, or should we add a `--log-format` option for human-readable output in development?

## Assumptions (to verify)
- Region overrides (`--region` flag or `r` shortcut) only affect runtime environment variables and never mutate AWS config files.
- LRU and pinned profiles are optional enhancements and can be skipped for MVP unless stakeholders request them during implementation.
- Help overlay triggered by `?` can reuse static Markdown content packaged with the app.

## Dependencies & External Factors
- awsui relies on the user having AWS CLI v2 configured with SSO sessions where needed; we will not automate `aws configure sso-session` beyond documentation.
- uv availability is assumed for development workflows, but end users may invoke the packaged script via other Python runners.
