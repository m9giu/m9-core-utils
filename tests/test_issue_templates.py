"""Tests for the issue templates check."""

from __future__ import annotations

from pathlib import Path

from m9_audit_kit.checks.issue_templates import IssueTemplatesCheck


def test_missing_templates_dir_fails(tmp_path: Path) -> None:
    assert IssueTemplatesCheck().run(tmp_path).status == "fail"


def test_template_passes(tmp_path: Path) -> None:
    directory = tmp_path / ".github" / "ISSUE_TEMPLATE"
    directory.mkdir(parents=True)
    (directory / "task.yml").write_text("name: Task\n", encoding="utf-8")
    result = IssueTemplatesCheck().run(tmp_path)
    assert result.status == "pass"
    assert result.evidence == (".github/ISSUE_TEMPLATE/task.yml",)


def test_empty_templates_dir_fails(tmp_path: Path) -> None:
    directory = tmp_path / ".github" / "ISSUE_TEMPLATE"
    directory.mkdir(parents=True)
    (directory / "notes.txt").write_text("ignore me", encoding="utf-8")
    assert IssueTemplatesCheck().run(tmp_path).status == "fail"
