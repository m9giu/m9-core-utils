"""CODEOWNERS check."""

from __future__ import annotations

from pathlib import Path

from . import register
from .base import Check, CheckResult

CODEOWNERS_PATHS = ("CODEOWNERS", ".github/CODEOWNERS", "docs/CODEOWNERS")


class CodeownersCheck(Check):
    """Verify that CODEOWNERS assigns review ownership."""

    slug = "codeowners"
    description = "Checks that CODEOWNERS assigns ownership."

    def run(self, root: Path) -> CheckResult:
        """Inspect the CODEOWNERS file."""
        path = next((root / name for name in CODEOWNERS_PATHS if (root / name).is_file()), None)
        if path is None:
            return CheckResult(self.slug, "fail", "no CODEOWNERS file found")

        rules = [
            line.strip()
            for line in path.read_text(encoding="utf-8", errors="ignore").splitlines()
            if line.strip() and not line.strip().startswith("#")
        ]
        if any("@" in rule for rule in rules):
            return CheckResult(
                check=self.slug,
                status="pass",
                message="CODEOWNERS assigns at least one owner",
                evidence=(str(path.relative_to(root)),),
            )
        return CheckResult(
            check=self.slug,
            status="warn",
            message="CODEOWNERS has no owner references",
            evidence=(str(path.relative_to(root)),),
        )


register(CodeownersCheck())
