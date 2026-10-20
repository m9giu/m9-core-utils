"""Changelog check."""

from __future__ import annotations

import re
from pathlib import Path

from . import register
from .base import Check, CheckResult

CHANGELOG_NAMES = ("CHANGELOG.md", "CHANGELOG.rst", "CHANGELOG.txt")
VERSION_HEADING = re.compile(r"^#{1,6}\s*\[?v?\d+\.\d+", re.MULTILINE)


class ChangelogCheck(Check):
    """Verify that a changelog records released versions."""

    slug = "changelog"
    description = "Checks that CHANGELOG records released versions."

    def run(self, root: Path) -> CheckResult:
        """Inspect the changelog."""
        path = next((root / name for name in CHANGELOG_NAMES if (root / name).is_file()), None)
        if path is None:
            return CheckResult(self.slug, "fail", "no CHANGELOG file found")

        text = path.read_text(encoding="utf-8", errors="ignore")
        if VERSION_HEADING.search(text):
            return CheckResult(
                check=self.slug,
                status="pass",
                message="changelog includes a version heading",
                evidence=(path.name,),
            )
        return CheckResult(
            check=self.slug,
            status="warn",
            message="changelog has no version heading",
            evidence=(path.name,),
        )


register(ChangelogCheck())
