"""Check registry."""

from __future__ import annotations

from .base import Check, CheckResult, Status

_REGISTRY: dict[str, Check] = {}


def register(check: Check) -> Check:
    """Register a check instance under its slug."""
    if not check.slug:
        raise ValueError("check.slug must not be empty")
    if check.slug in _REGISTRY:
        raise ValueError(f"duplicate check slug: {check.slug}")
    _REGISTRY[check.slug] = check
    return check


def get_check(slug: str) -> Check:
    """Return a registered check by slug."""
    try:
        return _REGISTRY[slug]
    except KeyError as exc:
        raise KeyError(f"unknown check: {slug}") from exc


def all_checks() -> tuple[Check, ...]:
    """Return every registered check in deterministic order."""
    return tuple(_REGISTRY[slug] for slug in sorted(_REGISTRY))


__all__ = ["Check", "CheckResult", "Status", "all_checks", "get_check", "register"]
