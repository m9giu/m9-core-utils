"""Tests for the security policy check."""

from __future__ import annotations

from pathlib import Path

from m9_audit_kit.checks.security_policy import SecurityPolicyCheck


def test_missing_policy_fails(tmp_path: Path) -> None:
    assert SecurityPolicyCheck().run(tmp_path).status == "fail"


def test_complete_policy_passes(tmp_path: Path) -> None:
    (tmp_path / "SECURITY.md").write_text(
        "Please report vulnerabilities privately through GitHub advisories.", encoding="utf-8"
    )
    result = SecurityPolicyCheck().run(tmp_path)
    assert result.status == "pass"
    assert result.evidence == ("SECURITY.md",)


def test_incomplete_policy_warns(tmp_path: Path) -> None:
    (tmp_path / "SECURITY.md").write_text("We care about security.", encoding="utf-8")
    result = SecurityPolicyCheck().run(tmp_path)
    assert result.status == "warn"
    assert "reporting instructions" in result.message
