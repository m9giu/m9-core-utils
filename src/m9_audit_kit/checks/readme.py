"""README check."""

from __future__ import annotations

from pathlib import Path

from . import register
from .base import Check, CheckResult

README_NAMES = ("README.md", "README.rst", "README.txt")


class ReadmeCheck(Check):
    """Verify that the README explains the project."""

    slug = "readme"
    description = "Checks that README explains the project and how to use it."

    def run(self, root: Path) -> CheckResult:
        """Inspect the repository README."""
        path = next((root / name for name in README_NAMES if (root / name).is_file()), None)
        if path is None:
            return CheckResult(self.slug, "fail", "no README file found")

        text = path.read_text(encoding="utf-8", errors="ignore")
        issues: list[str] = []
        if len(text.strip()) < 200:
            issues.append("shorter than 200 characters")
        if not text.lstrip().startswith("#"):
            issues.append("no markdown title")
        lowered = text.lower()
        if "install" not in lowered and "usage" not in lowered:
            issues.append("no installation or usage section")

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
            message="README explains the project",
            evidence=(path.name,),
        )


register(ReadmeCheck())
