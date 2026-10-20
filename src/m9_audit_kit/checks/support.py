"""Support policy check."""

from __future__ import annotations

from pathlib import Path

from . import register
from .base import Check, CheckResult

SUPPORT_NAMES = ("SUPPORT.md", ".github/SUPPORT.md", "docs/SUPPORT.md")


class SupportCheck(Check):
    """Verify that a support channel is documented."""

    slug = "support"
    description = "Checks that SUPPORT.md explains how to get help."

    def run(self, root: Path) -> CheckResult:
        """Inspect the support policy."""
        path = next((root / name for name in SUPPORT_NAMES if (root / name).is_file()), None)
        if path is None:
            return CheckResult(self.slug, "fail", "no SUPPORT policy found")

        lowered = path.read_text(encoding="utf-8", errors="ignore").lower()
        if any(word in lowered for word in ("support", "help", "issue", "discussion")):
            return CheckResult(
                check=self.slug,
                status="pass",
                message="support channel documented",
                evidence=(str(path.relative_to(root)),),
            )
        return CheckResult(
            check=self.slug,
            status="warn",
            message="support file has no actionable guidance",
            evidence=(str(path.relative_to(root)),),
        )


register(SupportCheck())
