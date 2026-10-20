"""CLI tests."""

from __future__ import annotations

import json
from pathlib import Path

from m9_audit_kit.cli import main


def test_empty_root_reports_failures(tmp_path: Path, capsys: object) -> None:
    assert main([str(tmp_path)]) == 1
    captured = capsys.readouterr()  # type: ignore[attr-defined]
    assert "FAIL  license: no LICENSE file found" in captured.out
    assert "FAIL  readme: no README file found" in captured.out


def test_json_format(tmp_path: Path, capsys: object) -> None:
    assert main([str(tmp_path), "--format", "json"]) == 1
    captured = capsys.readouterr()  # type: ignore[attr-defined]
    payload = json.loads(captured.out)
    assert payload["schema"] == "m9.audit/1"
    assert payload["summary"]["fail"] >= 1
    assert "license" in {result["check"] for result in payload["results"]}


def test_missing_path_exits_two(tmp_path: Path, capsys: object) -> None:
    assert main([str(tmp_path / "missing")]) == 2
    captured = capsys.readouterr()  # type: ignore[attr-defined]
    assert "not a directory" in captured.err


def test_unknown_check_exits_two(tmp_path: Path, capsys: object) -> None:
    assert main([str(tmp_path), "--checks", "does-not-exist"]) == 2
    captured = capsys.readouterr()  # type: ignore[attr-defined]
    assert "unknown check" in captured.err


def test_list_runs(capsys: object) -> None:
    assert main(["--list"]) == 0
    captured = capsys.readouterr()  # type: ignore[attr-defined]
    assert "license: Checks that a recognised LICENSE file is present." in captured.out
