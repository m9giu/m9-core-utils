"""Code of conduct check."""

from __future__ import annotations

from pathlib import Path

from . import register
from .base import Check, CheckResult

CONDUCT_NAMES = (
    "CODE_OF_CONDUCT.md",
    "CODE_OF_CONDUCT.rst",
    "CODE_OF_CONDUCT.txt",
    "CODE_OF_CONDUCT",
)


class CodeOfConductCheck(Check):
    """Verify that a code of conduct is adopted."""

    slug = "code_of_conduct"
    description = "Checks that a code of conduct is adopted."

    def run(self, root: Path) -> CheckResult:
        """Inspect the code of conduct."""
        path = next((root / name for name in CONDUCT_NAMES if (root / name).is_file()), None)
        if path is None:
            return CheckResult(self.slug, "fail", "no CODE_OF_CONDUCT file found")

        lowered = path.read_text(encoding="utf-8", errors="ignore").lower()
        if "contributor covenant" in lowered or "code of conduct" in lowered:
            return CheckResult(
                check=self.slug,
                status="pass",
                message="code of conduct adopted",
                evidence=(path.name,),
            )
        return CheckResult(
            check=self.slug,
            status="warn",
            message="file present but does not reference a code of conduct",
            evidence=(path.name,),
        )


register(CodeOfConductCheck())
