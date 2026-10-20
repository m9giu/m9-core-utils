"""Tests for the changelog check."""

from __future__ import annotations

from pathlib import Path

from m9_audit_kit.checks.changelog import ChangelogCheck


def test_missing_changelog_fails(tmp_path: Path) -> None:
    assert ChangelogCheck().run(tmp_path).status == "fail"


def test_version_heading_passes(tmp_path: Path) -> None:
    (tmp_path / "CHANGELOG.md").write_text("# 1.2.0\n\n- initial\n", encoding="utf-8")
    result = ChangelogCheck().run(tmp_path)
    assert result.status == "pass"
    assert result.evidence == ("CHANGELOG.md",)


def test_changelog_without_version_warns(tmp_path: Path) -> None:
    (tmp_path / "CHANGELOG.md").write_text("# Changelog\n\nNotes.\n", encoding="utf-8")
    assert ChangelogCheck().run(tmp_path).status == "warn"
