# docs_index

Verifies that the documentation has a navigable entry point.

## What it checks

Finds `docs/README.md`, `docs/index.md` or `docs/INDEX.md` and requires non-empty content.

## Statuses

| Status | Meaning |
|---|---|
| `pass` | Index exists and has content |
| `warn` | Index exists but is empty |
| `fail` | No documentation index found |

## Limitations

- Does not validate links or completeness.
- Only the three conventional filenames are considered.
