"""Tests for the CODEOWNERS check."""

from __future__ import annotations

from pathlib import Path

from m9_audit_kit.checks.codeowners import CodeownersCheck


def test_missing_codeowners_fails(tmp_path: Path) -> None:
    assert CodeownersCheck().run(tmp_path).status == "fail"


def test_owner_rule_passes(tmp_path: Path) -> None:
    (tmp_path / "CODEOWNERS").write_text("* @m9giu\n", encoding="utf-8")
    result = CodeownersCheck().run(tmp_path)
    assert result.status == "pass"
    assert result.evidence == ("CODEOWNERS",)


def test_rules_without_owner_warn(tmp_path: Path) -> None:
    (tmp_path / "CODEOWNERS").write_text("# comment\n* \n", encoding="utf-8")
    assert CodeownersCheck().run(tmp_path).status == "warn"
