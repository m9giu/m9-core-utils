"""Tests for the CI workflow check."""

from __future__ import annotations

from pathlib import Path

from m9_audit_kit.checks.ci_workflow import CiWorkflowCheck

VALID = """name: ci
on:
  push:
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: echo ok
"""


def test_missing_workflows_dir_fails(tmp_path: Path) -> None:
    assert CiWorkflowCheck().run(tmp_path).status == "fail"


def test_valid_workflow_passes(tmp_path: Path) -> None:
    directory = tmp_path / ".github" / "workflows"
    directory.mkdir(parents=True)
    (directory / "ci.yml").write_text(VALID, encoding="utf-8")
    result = CiWorkflowCheck().run(tmp_path)
    assert result.status == "pass"
    assert result.evidence == (".github/workflows/ci.yml",)


def test_workflow_without_jobs_warns(tmp_path: Path) -> None:
    directory = tmp_path / ".github" / "workflows"
    directory.mkdir(parents=True)
    (directory / "ci.yml").write_text("name: ci\non: push\n", encoding="utf-8")
    assert CiWorkflowCheck().run(tmp_path).status == "warn"
