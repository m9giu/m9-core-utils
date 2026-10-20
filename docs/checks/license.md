# license

Verifies that the repository declares a license.

## What it checks

Looks for `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING` or `COPYING.md` in the
repository root and matches the text against known license markers:

- MIT
- Apache-2.0
- GPL-3.0
- BSD-3-Clause

## Statuses

| Status | Meaning |
|---|---|
| `pass` | A recognised license file exists |
| `warn` | A license file exists but its text is not recognised |
| `fail` | No license file was found |

## Limitations

- Reads the root only; it does not follow `REUSE` conventions or `LICENSES/` directories.
- Marker matching is heuristic; custom or modified licenses return `warn`.
