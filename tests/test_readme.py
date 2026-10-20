"""Tests for the README check."""

from __future__ import annotations

from pathlib import Path

from m9_audit_kit.checks.readme import ReadmeCheck

GOOD = "# Project\n\n" + ("Explains the project. " * 20) + "\n\n## Usage\n\nRun it.\n"


def test_missing_readme_fails(tmp_path: Path) -> None:
    assert ReadmeCheck().run(tmp_path).status == "fail"


def test_good_readme_passes(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text(GOOD, encoding="utf-8")
    result = ReadmeCheck().run(tmp_path)
    assert result.status == "pass"
    assert result.evidence == ("README.md",)


def test_short_readme_warns(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("# Hi\n", encoding="utf-8")
    result = ReadmeCheck().run(tmp_path)
    assert result.status == "warn"
    assert "200" in result.message
