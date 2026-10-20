"""Tests for the contributing check."""

from __future__ import annotations

from pathlib import Path

from m9_audit_kit.checks.contributing import ContributingCheck


def test_missing_contributing_fails(tmp_path: Path) -> None:
    assert ContributingCheck().run(tmp_path).status == "fail"


def test_complete_guide_passes(tmp_path: Path) -> None:
    (tmp_path / "CONTRIBUTING.md").write_text(
        "Open a pull request and run the tests before requesting review.", encoding="utf-8"
    )
    result = ContributingCheck().run(tmp_path)
    assert result.status == "pass"
    assert result.evidence == ("CONTRIBUTING.md",)


def test_incomplete_guide_warns(tmp_path: Path) -> None:
    (tmp_path / "CONTRIBUTING.md").write_text("Be nice to each other.", encoding="utf-8")
    result = ContributingCheck().run(tmp_path)
    assert result.status == "warn"
    assert "pull-request workflow" in result.message
    assert "testing guidance" in result.message
