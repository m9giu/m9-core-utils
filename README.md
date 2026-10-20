```text
  __  __  ___    ____                  _   _ _   _ _ _
 |  \/  |/ _ \  / ___|___  _ __ ___   | | | | |_(_) |___
 | |\/| | (_) | | |  / _ \| '__/ _ \  | | | | __| | / __|
 | |  | |\__, | | |_| (_) | | |  __/  | |_| | |_| | \__ \
 |_|  |_|  /_/   \____\___/|_|  \___|   \___/ \__|_|_|___/
```

![M9 Core Utilities Banner](docs/assets/banner.png)

# M9 Core Utilities (`m9-core-utils`)

[![CI](https://github.com/M9GIU/m9-core-utils/actions/workflows/ci.yml/badge.svg)](https://github.com/M9GIU/m9-core-utils/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-3776AB?logo=python&logoColor=white)
![Ruff](https://img.shields.io/badge/code%20style-ruff-261230)
![mypy](https://img.shields.io/badge/type%20checking-mypy%20strict-2A6DB2)

## Overview

**M9 Core Utilities** is a dependency-free Python toolkit for deterministic repository
governance audits. It provides a typed check registry, immutable result contracts and
stable machine-readable reporting for CI pipelines, platform teams and engineering
governance programmes. Architecturally, it is designed to evolve into a middleware layer
for digital workers, adding concurrency, telemetry and strict schema/security primitives
(see Roadmap).

The library is intentionally conservative in its execution model: every check is a pure,
synchronous function over a working tree. There is no network I/O, no code execution from
the audited repository and no mutation of the target. Results are deterministic, ordered
and serialisable, which makes the toolkit suitable for gated pipelines, attestations and
long-lived compliance evidence.

### Design principles

- **Deterministic by construction** — identical inputs produce identical reports.
- **Immutable contracts** — results are frozen value objects, safe to cache and compare.
- **Zero runtime dependencies** — no supply-chain surface beyond the standard library.
- **Fail closed** — unexpected states surface as `fail` or `warn`, never as silent success.
- **Reviewable** — the source, tests and policy documentation remain human-auditable.

## Key Architectural Modules

### Shipped modules

| Module | Responsibility |
|---|---|
| `m9_audit_kit.checks` | Typed registry, automatic module discovery and the `Check` contract |
| `m9_audit_kit.checks.base` | Immutable `CheckResult` value object and status semantics |
| `m9_audit_kit.report` | Stable JSON (`m9.audit/1`), text rendering and summary aggregation |
| `m9_audit_kit.cli` | `m9-audit` entrypoint, check selection and exit-code contract |

### Roadmap — not shipped

The following modules describe the intended direction of the toolkit. They are **not part
of the current release** and the APIs below do not exist yet. They are listed for
architectural transparency, not as available functionality.

| Planned module | Intended scope | Status |
|---|---|---|
| `m9.core.concurrency` | Task scheduling, exponential backoff and rate limiting | Planned |
| `m9.core.telemetry` | Structured logging with zero-allocation paths and metric aggregation | Planned |
| `m9.core.schema` | Immutable data contracts and runtime type validation | Planned |
| `m9.core.security` | Cryptographic payload verification and ephemeral token handling | Planned |

> Publishing a README that presents these modules as functional would misrepresent the
> repository. They will be documented as shipped only when implemented, tested and released.

## Quality Assurance & CI/CD

Every change is validated by a protected `main` branch and a three-version test matrix:

- **Static analysis** — `ruff` with an explicit rule set (`E`, `F`, `I`, `UP`, `B`).
- **Type discipline** — `mypy --strict` across the full source tree.
- **Test matrix** — `pytest` on Python **3.10**, **3.11** and **3.12**.
- **Branch protection** — pull request required, status checks enforced, administrators included.
- **Deterministic output** — JSON schema versioned as `m9.audit/1`.

The current suite ships **10 checks** and **39 tests**. Checks are added one pull request
at a time, each with its own tests and documentation under `docs/checks/`.

## Installation & Usage Examples

### Install

```bash
python -m pip install -e ".[dev]"
```

### Command line

```bash
m9-audit . --format json | jq '.summary'
m9-audit . --checks license security_policy
```

Exit codes: `0` no failures, `1` at least one `fail`, `2` usage error. The JSON envelope is
stable (`schema: "m9.audit/1"`), with a per-status summary and an ordered result array.

### Defining a check

Checks are small, typed and side-effect free. Registering one is explicit and local:

```python
from pathlib import Path

from m9_audit_kit.checks import register
from m9_audit_kit.checks.base import Check, CheckResult


class SecurityTxtCheck(Check):
    slug = "security_txt"
    description = "Verifies RFC 9116 disclosure metadata."

    def run(self, root: Path) -> CheckResult:
        candidate = root / ".well-known" / "security.txt"
        if candidate.is_file():
            return CheckResult(
                self.slug,
                "pass",
                "security.txt present",
                (str(candidate.relative_to(root)),),
            )
        return CheckResult(self.slug, "fail", "security.txt missing")


register(SecurityTxtCheck())
```

### Typed asynchronous orchestration

The library is deliberately synchronous; concurrency is a consumer concern. The following
pattern fans checks out across a thread pool while preserving the typed contract:

```python
from __future__ import annotations

import asyncio
from pathlib import Path
from typing import Generic, Protocol, TypeVar

from m9_audit_kit.checks import all_checks
from m9_audit_kit.checks.base import CheckResult


class Runnable(Protocol):
    def run(self, root: Path) -> CheckResult: ...


T = TypeVar("T", bound=Runnable)


class AuditBatch(Generic[T]):
    def __init__(self, checks: tuple[T, ...]) -> None:
        self._checks = checks

    async def execute(self, root: Path) -> tuple[CheckResult, ...]:
        tasks = (asyncio.to_thread(check.run, root) for check in self._checks)
        return tuple(await asyncio.gather(*tasks))


async def main() -> None:
    batch = AuditBatch(all_checks())
    for result in await batch.execute(Path(".")):
        print(f"{result.status:4} {result.check}: {result.message}")


if __name__ == "__main__":
    asyncio.run(main())
```

### Machine-readable reporting

```python
from pathlib import Path

from m9_audit_kit.checks import all_checks
from m9_audit_kit.report import render_json

print(render_json(check.run(Path(".")) for check in all_checks()))
```

## License

MIT — see [`LICENSE`](LICENSE).


