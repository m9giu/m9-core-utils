"""Tests for the support check."""

from __future__ import annotations

from pathlib import Path

from m9_audit_kit.checks.support import SupportCheck


def test_missing_support_fails(tmp_path: Path) -> None:
    assert SupportCheck().run(tmp_path).status == "fail"


def test_support_documented_passes(tmp_path: Path) -> None:
    (tmp_path / "SUPPORT.md").write_text(
        "Open an issue or start a discussion for help.", encoding="utf-8"
    )
    result = SupportCheck().run(tmp_path)
    assert result.status == "pass"
    assert result.evidence == ("SUPPORT.md",)


def test_empty_support_warns(tmp_path: Path) -> None:
    (tmp_path / "SUPPORT.md").write_text("TODO", encoding="utf-8")
    assert SupportCheck().run(tmp_path).status == "warn"
