"""Security policy check."""

from __future__ import annotations

from pathlib import Path

from . import register
from .base import Check, CheckResult

SECURITY_NAMES = ("SECURITY.md", ".github/SECURITY.md", "SECURITY.rst", "SECURITY.txt")


class SecurityPolicyCheck(Check):
    """Verify that SECURITY explains how to report vulnerabilities."""

    slug = "security_policy"
    description = "Checks that SECURITY explains vulnerability reporting."

    def run(self, root: Path) -> CheckResult:
        """Inspect the security policy."""
        path = next((root / name for name in SECURITY_NAMES if (root / name).is_file()), None)
        if path is None:
            return CheckResult(self.slug, "fail", "no SECURITY policy found")

        lowered = path.read_text(encoding="utf-8", errors="ignore").lower()
        issues: list[str] = []
        if "report" not in lowered:
            issues.append("no reporting instructions")
        if "vulnerab" not in lowered and "security issue" not in lowered:
            issues.append("no vulnerability guidance")

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
            message="security policy explains private reporting",
            evidence=(path.name,),
        )


register(SecurityPolicyCheck())
