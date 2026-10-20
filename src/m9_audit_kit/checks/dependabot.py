"""Dependabot configuration check."""

from __future__ import annotations

from pathlib import Path

from . import register
from .base import Check, CheckResult

DEPENDABOT_PATHS = (".github/dependabot.yml", ".github/dependabot.yaml")


class DependabotCheck(Check):
    """Verify that Dependabot is configured."""

    slug = "dependabot"
    description = "Checks that Dependabot is configured."

    def run(self, root: Path) -> CheckResult:
        """Inspect the Dependabot configuration."""
        path = next((root / name for name in DEPENDABOT_PATHS if (root / name).is_file()), None)
        if path is None:
            return CheckResult(self.slug, "fail", "no .github/dependabot.yml")

        text = path.read_text(encoding="utf-8", errors="ignore")
        if "package-ecosystem" in text:
            return CheckResult(
                check=self.slug,
                status="pass",
                message="Dependabot declares a package ecosystem",
                evidence=(str(path.relative_to(root)),),
            )
        return CheckResult(
            check=self.slug,
            status="warn",
            message="Dependabot file has no package-ecosystem entry",
            evidence=(str(path.relative_to(root)),),
        )


register(DependabotCheck())
