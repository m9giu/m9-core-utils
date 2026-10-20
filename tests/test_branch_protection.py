"""Tests for the branch protection check."""

from __future__ import annotations

from pathlib import Path

from m9_audit_kit.checks.branch_protection import BranchProtectionCheck


def test_missing_policy_fails(tmp_path: Path) -> None:
    assert BranchProtectionCheck().run(tmp_path).status == "fail"


def test_documented_policy_passes(tmp_path: Path) -> None:
    directory = tmp_path / ".github"
    directory.mkdir()
    (directory / "branch-protection.yml").write_text(
        "main:\n  required_status_checks:\n    - test\n", encoding="utf-8"
    )
    result = BranchProtectionCheck().run(tmp_path)
    assert result.status == "pass"
    assert result.evidence == (".github/branch-protection.yml",)


def test_undocumented_policy_warns(tmp_path: Path) -> None:
    directory = tmp_path / ".github"
    directory.mkdir()
    (directory / "branch-protection.yml").write_text("main:\n  enabled: true\n", encoding="utf-8")
    assert BranchProtectionCheck().run(tmp_path).status == "warn"
