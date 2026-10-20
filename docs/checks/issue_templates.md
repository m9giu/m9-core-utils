# issue_templates

Verifies that issue templates guide bug reports and tasks.

## What it checks

Looks for `.github/ISSUE_TEMPLATE/` and requires at least one `.md`, `.yml` or `.yaml`
template.

## Statuses

| Status | Meaning |
|---|---|
| `pass` | At least one template exists |
| `fail` | Directory missing or contains no templates |

## Limitations

- Does not validate the template schema.
- Ignores non-template files such as `config.yml`.
