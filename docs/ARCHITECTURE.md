# Architecture

## Goals

- Zero runtime dependencies.
- Deterministic, offline checks over a repository working tree.
- Stable JSON output for automation; readable text output for humans.
- One check per module, registered by slug.

## Modules

| Module | Responsibility |
|---|---|
| `m9_audit_kit.cli` | Argument parsing, check selection, exit codes |
| `m9_audit_kit.checks` | Registry (`register`, `get_check`, `all_checks`) |
| `m9_audit_kit.checks.base` | `Check` contract and `CheckResult` value object |
| `m9_audit_kit.report` | Text and JSON rendering, summary counts |
| `m9_audit_kit.checks.<slug>` | One check implementation per file |

## Check contract

```python
class Check:
    slug: str
    description: str

    def run(self, root: Path) -> CheckResult: ...
```

`CheckResult` is immutable and carries:

- `check`: slug
- `status`: `pass` | `warn` | `fail` | `skip`
- `message`: one-line human explanation
- `evidence`: tuple of relevant paths or findings

## Exit codes

| Code | Meaning |
|---|---|
| 0 | No `fail` results |
| 1 | At least one `fail` |
| 2 | Usage error (bad path or unknown check) |

## Extending

1. Create `src/m9_audit_kit/checks/<slug>.py`.
2. Subclass `Check`, set `slug` and `description`, implement `run`.
3. Register an instance in `checks/__init__.py`.
4. Add `tests/test_<slug>.py` and `docs/checks/<slug>.md`.
5. Update `README.md` and `docs/ROADMAP.md`.

## Non-goals

- Network calls or GitHub API access in checks.
- Executing repository code.
- Mutating the audited repository.
