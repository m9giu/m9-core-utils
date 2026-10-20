"""Command-line entry point for m9-audit-kit."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

from . import __version__
from .checks import all_checks, get_check
from .report import render_json, render_text


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser."""
    parser = argparse.ArgumentParser(
        prog="m9-audit",
        description="Audit repository governance files.",
    )
    parser.add_argument("path", nargs="?", default=".", help="repository root (default: .)")
    parser.add_argument("--format", choices=("text", "json"), default="text", help="output format")
    parser.add_argument("--checks", nargs="*", metavar="SLUG", help="run only these checks")
    parser.add_argument("--list", action="store_true", help="list available checks and exit")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the CLI and return a process exit code."""
    args = build_parser().parse_args(argv)

    if args.list:
        checks = all_checks()
        if not checks:
            print("no checks registered")
        for check in checks:
            print(f"{check.slug}: {check.description}")
        return 0

    root = Path(args.path)
    if not root.is_dir():
        print(f"error: not a directory: {root}", file=sys.stderr)
        return 2

    try:
        if args.checks:
            selected = tuple(get_check(slug) for slug in args.checks)
        else:
            selected = all_checks()
    except KeyError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    results = [check.run(root) for check in selected]
    print(render_json(results) if args.format == "json" else render_text(results))
    return 1 if any(result.status == "fail" for result in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
