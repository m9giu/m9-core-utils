# Security Policy

## Supported versions

`m9-audit-kit` is pre-1.0; only the latest commit on `main` receives fixes.

## Reporting a vulnerability

Please **do not** open a public issue for security problems.

Use GitHub's private vulnerability reporting:

1. Go to the repository's **Security** tab.
2. Select **Report a vulnerability**.
3. Include: affected version/commit, reproduction steps, impact and any suggested fix.

You can expect an initial acknowledgement within 7 days. Please allow time for a fix
before public disclosure; coordinated disclosure is appreciated.

## Scope

This tool reads repository files locally. It does not execute repository code, make
network calls, or handle credentials. Reports about the CI workflow or dependency supply
chain are in scope.

## Secrets

Never commit tokens or credentials. If a secret is exposed, revoke it immediately and
open a private advisory.
