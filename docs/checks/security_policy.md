# security_policy

Verifies that the repository explains how to report vulnerabilities.

## What it checks

Finds `SECURITY.md`, `.github/SECURITY.md`, `SECURITY.rst` or `SECURITY.txt` and checks
that it mentions reporting and vulnerabilities (or security issues).

## Statuses

| Status | Meaning |
|---|---|
| `pass` | Private reporting and vulnerability guidance are present |
| `warn` | Policy exists but lacks reporting or vulnerability guidance |
| `fail` | No security policy found |

## Limitations

- Keyword heuristics; it does not verify that the reporting channel works.
- Root and `.github/` locations only.
