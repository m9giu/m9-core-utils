"""Tests for the license check."""

from __future__ import annotations

from pathlib import Path

from m9_audit_kit.checks.license import LicenseCheck


def test_missing_license_fails(tmp_path: Path) -> None:
    result = LicenseCheck().run(tmp_path)
    assert result.status == "fail"
    assert result.check == "license"


def test_mit_license_passes(tmp_path: Path) -> None:
    (tmp_path / "LICENSE").write_text(
        "MIT License\n\nPermission is hereby granted, free of charge, to any person.",
        encoding="utf-8",
    )
    result = LicenseCheck().run(tmp_path)
    assert result.status == "pass"
    assert "MIT" in result.message
    assert result.evidence == ("LICENSE",)


def test_unknown_license_warns(tmp_path: Path) -> None:
    (tmp_path / "LICENSE").write_text("All rights reserved.", encoding="utf-8")
    result = LicenseCheck().run(tmp_path)
    assert result.status == "warn"
