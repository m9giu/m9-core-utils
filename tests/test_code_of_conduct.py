"""Tests for the code of conduct check."""

from __future__ import annotations

from pathlib import Path

from m9_audit_kit.checks.code_of_conduct import CodeOfConductCheck


def test_missing_conduct_fails(tmp_path: Path) -> None:
    assert CodeOfConductCheck().run(tmp_path).status == "fail"


def test_contributor_covenant_passes(tmp_path: Path) -> None:
    (tmp_path / "CODE_OF_CONDUCT.md").write_text(
        "This project adopts the Contributor Covenant, version 2.1.", encoding="utf-8"
    )
    result = CodeOfConductCheck().run(tmp_path)
    assert result.status == "pass"
    assert result.evidence == ("CODE_OF_CONDUCT.md",)


def test_unrelated_file_warns(tmp_path: Path) -> None:
    (tmp_path / "CODE_OF_CONDUCT.md").write_text("Be nice.", encoding="utf-8")
    assert CodeOfConductCheck().run(tmp_path).status == "warn"
