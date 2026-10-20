"""CI workflow check."""

from __future__ import annotations

from pathlib import Path

from . import register
from .base import Check, CheckResult

WORKFLOW_DIR = Path(".github/workflows")


class CiWorkflowCheck(Check):
    """Verify that a GitHub Actions workflow runs on push and pull request."""

    slug = "ci_workflow"
    description = "Checks that a CI workflow declares triggers and jobs."

    def run(self, root: Path) -> CheckResult:
        """Inspect GitHub Actions workflows."""
        directory = root / WORKFLOW_DIR
        if not directory.is_dir():
            return CheckResult(self.slug, "fail", "no .github/workflows directory")

        files = sorted([*directory.glob("*.yml"), *directory.glob("*.yaml")])
        if not files:
            return CheckResult(self.slug, "fail", "no workflow files found")

        for path in files:
            text = path.read_text(encoding="utf-8", errors="ignore")
            if "on:" in text and "jobs:" in text:
                return CheckResult(
                    check=self.slug,
                    status="pass",
                    message=f"{path.name} declares triggers and jobs",
                    evidence=(str(path.relative_to(root)),),
                )
        return CheckResult(
            check=self.slug,
            status="warn",
            message="workflow files found but none declares triggers and jobs",
            evidence=tuple(str(path.relative_to(root)) for path in files),
        )


register(CiWorkflowCheck())
