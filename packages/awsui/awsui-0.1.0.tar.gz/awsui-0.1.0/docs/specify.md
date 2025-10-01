# awsui Specification

## Product Overview
awsui is a Textual-based terminal UI that lets engineers search, inspect, and activate AWS IAM Identity Center (SSO) and legacy profiles. It validates credentials via `aws sts get-caller-identity`, triggers `aws sso login` when needed, and keeps users within a single interactive TUI session.

## Target Users
- Cloud engineers who juggle dozens of AWS accounts and roles across environments.
- On-call SREs who need reliable reauthentication flows without leaving the terminal.
- Data engineers who require immediate visibility into their active AWS identity to avoid production mistakes.

## User Stories
- As a cloud engineer, I can fuzzy-search profiles by name, account, role, or region, pick one, and immediately see who I am authenticated as.
- As an SRE, when credentials expire the tool automatically performs `aws sso login` and retries my request so I stay productive under pressure.
- As a data engineer, I can verify the active `AWS_PROFILE`, account, and region from a WhoAmI panel before running sensitive operations.

## Functional Requirements
1. Read and parse `~/.aws/config` and `~/.aws/credentials`, including SSO sessions, delegated profiles (`source_profile`/`role_arn`), and static credentials, while honouring `AWS_CONFIG_FILE` and `AWS_SHARED_CREDENTIALS_FILE`.
2. Provide a Textual UI composed of a search box, selectable profile list, detail sidebar, and status bar.
3. Execute `aws sts get-caller-identity` to validate credentials; on failure, run `aws sso login --profile <name>` once and retry with progress and error messaging.
4. Surface a WhoAmI panel showing account, ARN/user, and cached token TTL when available.
5. Offer CLI arguments: `--profile`, `--region`, `--lang zh-TW|en`, `--log-level INFO|DEBUG`.
7. Expose shortcuts: `/` search focus, `Enter` apply profile, `l` force login, `w` WhoAmI, `r` region override, `?` help, `q` quit.

## Non-Functional Requirements
- Platforms: Linux, macOS, Windows (PowerShell tested).
- Performance: startup ≤ 300 ms, search ≤ 50 ms, switch (with one login) ≤ 5 s.
- Reliability: SSO login success ≥ 98%; crash rate < 0.1%.
- Observability: structured JSON logs on STDERR containing `ts, level, action, duration_ms, profile, result`.
- Compatibility: Python `>=3.13,<3.14`; Textual stable release; AWS CLI v2 present.

## Out of Scope (MVP)
- Modifying AWS configuration files or storing long-lived credentials.
- Replacing aws-vault or providing browser-based console access.
- Automatically launching the AWS Console.

## Success Metrics
- Time to first usable profile switch (including SSO login) under five seconds.
- Positive feedback from target personas on discoverability of shortcuts and status indicators.
- Automated test coverage ≥ 80% on parsing, CLI, and TUI logic.
- Zero incidents of leaking full account numbers or ARNs in logs.
