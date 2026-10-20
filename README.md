# m9-audit-kit

[![ci](https://github.com/M9GIU/m9-core-utils/actions/workflows/ci.yml/badge.svg)](https://github.com/M9GIU/m9-core-utils/actions/workflows/ci.yml)

A small, dependency-free CLI that audits repository governance files: license, README,
contribution policy, code of conduct, security policy, CI, CODEOWNERS, Dependabot,
issue templates and branch-protection documentation.

> **Purpose.** This repository is an isolated engineering sandbox. It exists to build a
> genuinely useful tool and to validate GitHub mechanics without touching production,
> client or M9 core repositories. It does **not** use empty pull requests, fake accounts
> or automated bulk activity. See `docs/ACHIEVEMENTS-STRATEGY.md`.

## Install

```bash
python -m pip install -e ".[dev]"
```

## Usage

```bash
m9-audit .                 # human-readable report
m9-audit . --format json   # machine-readable report
m9-audit . --list          # list registered checks
m9-audit . --checks license readme
```

Exit codes: `0` no failures, `1` at least one `fail`, `2` usage error.

## Checks

| Check | What it verifies |
|---|---|
| `license` | A recognised LICENSE file is present |
| `readme` | README explains the project and how to use it |
| `contributing` | CONTRIBUTING explains the PR workflow |
| `code_of_conduct` | A code of conduct is adopted |
| `security_policy` | SECURITY explains how to report vulnerabilities |
| `ci_workflow` | A GitHub Actions workflow runs on push/PR |
| `codeowners` | CODEOWNERS assigns review ownership |
| `dependabot` | Dependency updates are configured |
| `issue_templates` | Issue templates guide reports |
| `branch_protection` | Branch protection is documented |

Checks are added incrementally, one pull request per check, each with tests and docs.

## Development

```bash
ruff check .
pytest
mypy src
```

## License

MIT — see `LICENSE`.
