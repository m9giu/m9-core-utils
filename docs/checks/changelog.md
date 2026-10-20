# changelog

Verifies that released versions are recorded.

## What it checks

Finds `CHANGELOG.md`, `CHANGELOG.rst` or `CHANGELOG.txt` and requires a version heading
such as `## 1.2.0`, `## [1.2.0]` or `### v1.2.0`.

## Statuses

| Status | Meaning |
|---|---|
| `pass` | A version heading is present |
| `warn` | Changelog exists but has no version heading |
| `fail` | No changelog found |

## Limitations

- Heading heuristics only; it does not validate semantic versioning or entry quality.
- Root-level files only.
