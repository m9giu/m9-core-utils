"""Branch protection documentation check."""

from __future__ import annotations

from pathlib import Path

from . import register
from .base import Check, CheckResult

POLICY_PATHS = (".github/branch-protection.yml", ".github/branch-protection.yaml")


class BranchProtectionCheck(Check):
    """Verify that branch protection is documented."""

    slug = "branch_protection"
    description = "Checks that branch protection is documented."

    def run(self, root: Path) -> CheckResult:
        """Inspect the documented branch-protection policy."""
        path = next((root / name for name in POLICY_PATHS if (root / name).is_file()), None)
        if path is None:
            return CheckResult(self.slug, "fail", "no .github/branch-protection.yml")

        text = path.read_text(encoding="utf-8", errors="ignore")
        if "required_status_checks" in text:
            return CheckResult(
                check=self.slug,
                status="pass",
                message="branch protection policy documents required checks",
                evidence=(str(path.relative_to(root)),),
            )
        return CheckResult(
            check=self.slug,
            status="warn",
            message="policy exists but does not document required checks",
            evidence=(str(path.relative_to(root)),),
        )


register(BranchProtectionCheck())
