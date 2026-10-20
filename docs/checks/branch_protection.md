# branch_protection

Verifies that branch protection is documented in the repository.

## What it checks

Finds `.github/branch-protection.yml` or `.github/branch-protection.yaml` and requires a
`required_status_checks` entry.

## Statuses

| Status | Meaning |
|---|---|
| `pass` | Policy documents required status checks |
| `warn` | Policy exists but does not document required checks |
| `fail` | No documented policy |

## Limitations

- Documentation only: it does not call the GitHub API.
- The authoritative configuration is the repository setting enforced by GitHub.
