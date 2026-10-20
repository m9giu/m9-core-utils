# readme

Verifies that the repository explains itself.

## What it checks

Finds `README.md`, `README.rst` or `README.txt` in the repository root and checks:

- length of at least 200 characters;
- a markdown title (`#`) at the start;
- an installation or usage section.

## Statuses

| Status | Meaning |
|---|---|
| `pass` | All checks pass |
| `warn` | README exists but is short or lacks structure |
| `fail` | No README found |

## Limitations

- Only the repository root is inspected.
- Plain-text and reStructuredText files are length-checked but not structure-checked.
