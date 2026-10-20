"""Rendering helpers for audit results."""

from __future__ import annotations

import json
from collections import Counter
from collections.abc import Iterable

from .checks.base import CheckResult

STATUSES = ("pass", "warn", "fail", "skip")


def summarize(results: Iterable[CheckResult]) -> dict[str, int]:
    """Count results per status."""
    counts: Counter[str] = Counter(result.status for result in results)
    return {status: counts.get(status, 0) for status in STATUSES}


def render_json(results: Iterable[CheckResult]) -> str:
    """Render results as stable JSON."""
    items = list(results)
    payload = {
        "schema": "m9.audit/1",
        "summary": summarize(items),
        "results": [item.as_dict() for item in items],
    }
    return json.dumps(payload, indent=2, ensure_ascii=False)


def render_text(results: Iterable[CheckResult]) -> str:
    """Render results as human-readable text."""
    items = list(results)
    lines = [f"{item.status.upper():4}  {item.check}: {item.message}" for item in items]
    summary = summarize(items)
    lines.append(
        "checks: {pass} pass, {warn} warn, {fail} fail, {skip} skip".format(**summary)
    )
    return "\n".join(lines)
