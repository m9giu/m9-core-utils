"""Tests for the release notes check."""

from __future__ import annotations

from pathlib import Path

from m9_audit_kit.checks.release_notes import ReleaseNotesCheck


def test_missing_release_notes_fails(tmp_path: Path) -> None:
    assert ReleaseNotesCheck().run(tmp_path).status == "fail"


def test_release_file_passes(tmp_path: Path) -> None:
    (tmp_path / "RELEASE_NOTES.md").write_text("# 1.0.0\n\n- initial\n", encoding="utf-8")
    result = ReleaseNotesCheck().run(tmp_path)
    assert result.status == "pass"
    assert result.evidence == ("RELEASE_NOTES.md",)


def test_releases_directory_passes(tmp_path: Path) -> None:
    directory = tmp_path / "docs" / "releases"
    directory.mkdir(parents=True)
    (directory / "1.0.0.md").write_text("# 1.0.0\n", encoding="utf-8")
    result = ReleaseNotesCheck().run(tmp_path)
    assert result.status == "pass"
    assert result.evidence == ("docs/releases/1.0.0.md",)


def test_empty_releases_directory_warns(tmp_path: Path) -> None:
    (tmp_path / "docs" / "releases").mkdir(parents=True)
    assert ReleaseNotesCheck().run(tmp_path).status == "warn"
