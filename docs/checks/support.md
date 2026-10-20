# support

Verifies that users know how to get help.

## What it checks

Finds `SUPPORT.md`, `.github/SUPPORT.md` or `docs/SUPPORT.md` and requires a reference to a
support channel: issues, discussions, help or support.

## Statuses

| Status | Meaning |
|---|---|
| `pass` | Actionable support guidance is present |
| `warn` | File exists but has no actionable guidance |
| `fail` | No support policy found |

## Limitations

- Keyword heuristics only.
- Does not verify that the channel is monitored.
