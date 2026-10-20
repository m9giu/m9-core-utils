"""Shared contract for audit checks."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal

Status = Literal["pass", "warn", "fail", "skip"]


@dataclass(frozen=True, slots=True)
class CheckResult:
    """Outcome of a single check against a repository root."""

    check: str
    status: Status
    message: str
    evidence: tuple[str, ...] = ()

    def as_dict(self) -> dict[str, object]:
        """Return a JSON-serialisable representation."""
        return {
            "check": self.check,
            "status": self.status,
            "message": self.message,
            "evidence": list(self.evidence),
        }


class Check:
    """Base class for repository checks.

    Subclasses set ``slug`` and ``description`` and implement ``run``.
    """

    slug: str = ""
    description: str = ""

    def run(self, root: Path) -> CheckResult:
        """Audit ``root`` and return a result."""
        raise NotImplementedError
