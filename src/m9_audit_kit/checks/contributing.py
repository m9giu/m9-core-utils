"""Contributing guide check."""

from __future__ import annotations

from pathlib import Path

from . import register
from .base import Check, CheckResult

CONTRIBUTING_NAMES = ("CONTRIBUTING.md", "CONTRIBUTING.rst", "CONTRIBUTING.txt")


class ContributingCheck(Check):
    """Verify that CONTRIBUTING explains the pull-request workflow."""

    slug = "contributing"
    description = "Checks that CONTRIBUTING explains the pull-request workflow."

    def run(self, root: Path) -> CheckResult:
        """Inspect the contributing guide."""
        path = next(
            (root / name for name in CONTRIBUTING_NAMES if (root / name).is_file()), None
        )
        if path is None:
            return CheckResult(self.slug, "fail", "no CONTRIBUTING file found")

        lowered = path.read_text(encoding="utf-8", errors="ignore").lower()
        issues: list[str] = []
        if "pull request" not in lowered and "merge request" not in lowered:
            issues.append("no pull-request workflow")
        if "test" not in lowered:
            issues.append("no testing guidance")

        if issues:
            return CheckResult(
                check=self.slug,
                status="warn",
                message="; ".join(issues),
                evidence=(path.name,),
            )
        return CheckResult(
            check=self.slug,
            status="pass",
            message="contributing guide covers pull requests and tests",
            evidence=(path.name,),
        )


register(ContributingCheck())
