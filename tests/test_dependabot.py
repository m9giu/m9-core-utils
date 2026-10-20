"""Tests for the Dependabot check."""

from __future__ import annotations

from pathlib import Path

from m9_audit_kit.checks.dependabot import DependabotCheck


def test_missing_dependabot_fails(tmp_path: Path) -> None:
    assert DependabotCheck().run(tmp_path).status == "fail"


def test_configured_dependabot_passes(tmp_path: Path) -> None:
    directory = tmp_path / ".github"
    directory.mkdir()
    (directory / "dependabot.yml").write_text(
        "version: 2\nupdates:\n  - package-ecosystem: pip\n", encoding="utf-8"
    )
    result = DependabotCheck().run(tmp_path)
    assert result.status == "pass"
    assert result.evidence == (".github/dependabot.yml",)


def test_empty_dependabot_warns(tmp_path: Path) -> None:
    directory = tmp_path / ".github"
    directory.mkdir()
    (directory / "dependabot.yml").write_text("version: 2\n", encoding="utf-8")
    assert DependabotCheck().run(tmp_path).status == "warn"
