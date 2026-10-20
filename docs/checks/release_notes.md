# release_notes

Verifies that release notes are published.

## What it checks

Accepts any of:

- a non-empty `RELEASE_NOTES.md`, `RELEASES.md` or `docs/RELEASE_NOTES.md`;
- at least one Markdown file in `docs/releases/`.

## Statuses

| Status | Meaning |
|---|---|
| `pass` | Release notes or a populated releases directory exist |
| `warn` | `docs/releases/` exists but is empty |
| `fail` | No release notes found |

## Limitations

- Does not validate the content or version alignment with tags.
- Only the documented filenames and directory are considered.
