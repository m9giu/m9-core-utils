"""CLI tests."""

from __future__ import annotations

import json
from pathlib import Path

from m9_audit_kit.cli import main


def test_empty_root_exits_zero(tmp_path: Path, capsys: object) -> None:
    assert main([str(tmp_path)]) == 0
    captured = capsys.readouterr()  # type: ignore[attr-defined]
    assert "checks: 0 pass, 0 warn, 0 fail, 0 skip" in captured.out


def test_json_format(tmp_path: Path, capsys: object) -> None:
    assert main([str(tmp_path), "--format", "json"]) == 0
    captured = capsys.readouterr()  # type: ignore[attr-defined]
    payload = json.loads(captured.out)
    assert payload["schema"] == "m9.audit/1"
    assert payload["results"] == []


def test_missing_path_exits_two(tmp_path: Path, capsys: object) -> None:
    assert main([str(tmp_path / "missing")]) == 2
    captured = capsys.readouterr()  # type: ignore[attr-defined]
    assert "not a directory" in captured.err


def test_unknown_check_exits_two(tmp_path: Path, capsys: object) -> None:
    assert main([str(tmp_path), "--checks", "does-not-exist"]) == 2
    captured = capsys.readouterr()  # type: ignore[attr-defined]
    assert "unknown check" in captured.err


def test_list_runs(tmp_path: Path, capsys: object) -> None:
    assert main(["--list"]) == 0
    captured = capsys.readouterr()  # type: ignore[attr-defined]
    assert "no checks registered" in captured.out
