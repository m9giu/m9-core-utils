# contributing

Verifies that the repository explains how to contribute.

## What it checks

Finds `CONTRIBUTING.md`, `CONTRIBUTING.rst` or `CONTRIBUTING.txt` in the repository root
and checks that it mentions:

- a pull-request (or merge-request) workflow;
- testing.

## Statuses

| Status | Meaning |
|---|---|
| `pass` | Guide covers pull requests and tests |
| `warn` | Guide exists but misses workflow or testing guidance |
| `fail` | No contributing guide found |

## Limitations

- Keyword heuristics only; it does not validate the workflow itself.
- Root-level files only.
