"""Documentation index check."""

from __future__ import annotations

from pathlib import Path

from . import register
from .base import Check, CheckResult

INDEX_NAMES = ("docs/README.md", "docs/index.md", "docs/INDEX.md")


class DocsIndexCheck(Check):
    """Verify that the documentation has an entry point."""

    slug = "docs_index"
    description = "Checks that docs/README.md or docs/index.md exists."

    def run(self, root: Path) -> CheckResult:
        """Inspect the documentation index."""
        path = next((root / name for name in INDEX_NAMES if (root / name).is_file()), None)
        if path is None:
            return CheckResult(self.slug, "fail", "no documentation index found")

        if not path.read_text(encoding="utf-8", errors="ignore").strip():
            return CheckResult(
                check=self.slug,
                status="warn",
                message="documentation index is empty",
                evidence=(str(path.relative_to(root)),),
            )
        return CheckResult(
            check=self.slug,
            status="pass",
            message="documentation index present",
            evidence=(str(path.relative_to(root)),),
        )


register(DocsIndexCheck())
