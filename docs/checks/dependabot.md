# dependabot

Verifies that dependency updates are automated.

## What it checks

Finds `.github/dependabot.yml` or `.github/dependabot.yaml` and requires at least one
`package-ecosystem` entry.

## Statuses

| Status | Meaning |
|---|---|
| `pass` | Dependabot declares a package ecosystem |
| `warn` | File exists but declares no ecosystem |
| `fail` | No Dependabot configuration |

## Limitations

- Text heuristics, not YAML parsing.
- Does not verify that Dependabot has run or opened pull requests.
