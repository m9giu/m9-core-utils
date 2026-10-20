"""Tests for the documentation index check."""

from __future__ import annotations

from pathlib import Path

from m9_audit_kit.checks.docs_index import DocsIndexCheck


def test_missing_index_fails(tmp_path: Path) -> None:
    assert DocsIndexCheck().run(tmp_path).status == "fail"


def test_index_passes(tmp_path: Path) -> None:
    directory = tmp_path / "docs"
    directory.mkdir()
    (directory / "README.md").write_text("# Docs\n\n- architecture\n", encoding="utf-8")
    result = DocsIndexCheck().run(tmp_path)
    assert result.status == "pass"
    assert result.evidence == ("docs/README.md",)


def test_empty_index_warns(tmp_path: Path) -> None:
    directory = tmp_path / "docs"
    directory.mkdir()
    (directory / "index.md").write_text("   \n", encoding="utf-8")
    assert DocsIndexCheck().run(tmp_path).status == "warn"
