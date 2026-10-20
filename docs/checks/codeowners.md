# codeowners

Verifies that review ownership is declared.

## What it checks

Finds `CODEOWNERS`, `.github/CODEOWNERS` or `docs/CODEOWNERS` and requires at least one
non-comment rule containing an owner (`@user` or `@org/team`).

## Statuses

| Status | Meaning |
|---|---|
| `pass` | At least one owner is referenced |
| `warn` | File exists but no owner is referenced |
| `fail` | No CODEOWNERS file found |

## Limitations

- Does not validate that the referenced users or teams exist.
- Root, `.github/` and `docs/` locations only.
