# ci_workflow

Verifies that the repository runs continuous integration.

## What it checks

Looks for `.github/workflows/*.yml` or `*.yaml` and requires at least one workflow with:

- an `on:` trigger block;
- a `jobs:` block.

## Statuses

| Status | Meaning |
|---|---|
| `pass` | A workflow declares triggers and jobs |
| `warn` | Workflows exist but none declares both |
| `fail` | No workflows directory or no workflow files |

## Limitations

- Text heuristics, not YAML parsing.
- Does not verify that the workflow has ever run or passed.
