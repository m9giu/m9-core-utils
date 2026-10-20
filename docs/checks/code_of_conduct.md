# code_of_conduct

Verifies that the repository adopts a code of conduct.

## What it checks

Finds `CODE_OF_CONDUCT.md`, `CODE_OF_CONDUCT.rst`, `CODE_OF_CONDUCT.txt` or
`CODE_OF_CONDUCT` in the repository root and checks that it references the
Contributor Covenant or a code of conduct.

## Statuses

| Status | Meaning |
|---|---|
| `pass` | A code of conduct is adopted |
| `warn` | File exists but does not reference a code of conduct |
| `fail` | No code of conduct found |

## Limitations

- Keyword heuristics; it does not validate enforcement procedures.
- Root-level files only.
