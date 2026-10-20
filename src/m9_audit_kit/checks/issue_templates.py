"""Issue templates check."""

from __future__ import annotations

from pathlib import Path

from . import register
from .base import Check, CheckResult

TEMPLATE_DIR = Path(".github/ISSUE_TEMPLATE")
SUFFIXES = {".md", ".yml", ".yaml"}


class IssueTemplatesCheck(Check):
    """Verify that issue templates exist."""

    slug = "issue_templates"
    description = "Checks that issue templates guide reports."

    def run(self, root: Path) -> CheckResult:
        """Inspect the issue template directory."""
        directory = root / TEMPLATE_DIR
        if not directory.is_dir():
            return CheckResult(self.slug, "fail", "no .github/ISSUE_TEMPLATE directory")

        templates = sorted(
            path
            for path in directory.iterdir()
            if path.is_file() and path.suffix.lower() in SUFFIXES
        )
        if not templates:
            return CheckResult(self.slug, "fail", "no issue templates found")

        return CheckResult(
            check=self.slug,
            status="pass",
            message=f"{len(templates)} issue template(s) found",
            evidence=tuple(str(path.relative_to(root)) for path in templates),
        )


register(IssueTemplatesCheck())
