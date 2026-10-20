"""License check."""

from __future__ import annotations

from pathlib import Path

from . import register
from .base import Check, CheckResult

LICENSE_NAMES = ("LICENSE", "LICENSE.md", "LICENSE.txt", "COPYING", "COPYING.md")

MARKERS: dict[str, tuple[str, ...]] = {
    "MIT": ("MIT License", "Permission is hereby granted, free of charge"),
    "Apache-2.0": ("Apache License", "Version 2.0"),
    "GPL-3.0": ("GNU GENERAL PUBLIC LICENSE", "Version 3"),
    "BSD-3-Clause": ("BSD 3-Clause License", "Redistribution and use"),
}


class LicenseCheck(Check):
    """Verify that a recognised license file exists."""

    slug = "license"
    description = "Checks that a recognised LICENSE file is present."

    def run(self, root: Path) -> CheckResult:
        """Inspect the repository root for a license file."""
        for name in LICENSE_NAMES:
            path = root / name
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            for license_id, markers in MARKERS.items():
                if all(marker in text for marker in markers):
                    return CheckResult(
                        check=self.slug,
                        status="pass",
                        message=f"{license_id} license found",
                        evidence=(name,),
                    )
            return CheckResult(
                check=self.slug,
                status="warn",
                message="license file present but not recognised",
                evidence=(name,),
            )
        return CheckResult(
            check=self.slug,
            status="fail",
            message="no LICENSE file found",
        )


register(LicenseCheck())
