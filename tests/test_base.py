"""Contract tests for checks."""

from __future__ import annotations

from dataclasses import FrozenInstanceError
from pathlib import Path

import pytest

from m9_audit_kit.checks import get_check
from m9_audit_kit.checks.base import Check, CheckResult


def test_check_result_serialises() -> None:
    result = CheckResult(check="license", status="pass", message="ok", evidence=("LICENSE",))
    assert result.as_dict() == {
        "check": "license",
        "status": "pass",
        "message": "ok",
        "evidence": ["LICENSE"],
    }


def test_check_result_is_immutable() -> None:
    result = CheckResult(check="license", status="pass", message="ok")
    with pytest.raises(FrozenInstanceError):
        result.status = "fail"  # type: ignore[misc]


def test_unknown_check_raises() -> None:
    with pytest.raises(KeyError, match="unknown check"):
        get_check("does-not-exist")


def test_base_check_is_abstract() -> None:
    with pytest.raises(NotImplementedError):
        Check().run(Path("."))
