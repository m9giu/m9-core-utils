"""Release notes check."""

from __future__ import annotations

from pathlib import Path

from . import register
from .base import Check, CheckResult

RELEASE_FILES = ("RELEASE_NOTES.md", "RELEASES.md", "docs/RELEASE_NOTES.md")
RELEASE_DIR = Path("docs/releases")


class ReleaseNotesCheck(Check):
    """Verify that release notes are published."""

    slug = "release_notes"
    description = "Checks that release notes or a releases directory exist."

    def run(self, root: Path) -> CheckResult:
        """Inspect release notes."""
        for name in RELEASE_FILES:
            path = root / name
            if path.is_file() and path.read_text(encoding="utf-8", errors="ignore").strip():
                return CheckResult(
                    check=self.slug,
                    status="pass",
                    message="release notes present",
                    evidence=(name,),
                )

        directory = root / RELEASE_DIR
        if directory.is_dir():
            notes = sorted(directory.glob("*.md"))
            if notes:
                return CheckResult(
                    check=self.slug,
                    status="pass",
                    message=f"{len(notes)} release note file(s) found",
                    evidence=tuple(str(path.relative_to(root)) for path in notes),
                )
            return CheckResult(
                check=self.slug,
                status="warn",
                message="docs/releases exists but is empty",
                evidence=(str(RELEASE_DIR),),
            )

        return CheckResult(self.slug, "fail", "no release notes found")


register(ReleaseNotesCheck())
