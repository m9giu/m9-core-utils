#!/usr/bin/env bash
# Read-only counters for the sandbox. Never writes to GitHub.
set -euo pipefail

REPO="${REPO:-M9GIU/m9-core-utils}"
TARGET="${TARGET:-128}"

command -v gh >/dev/null 2>&1 || { echo "error: gh is not installed" >&2; exit 2; }
gh auth status >/dev/null 2>&1 || { echo "error: gh is not authenticated" >&2; exit 2; }

merged="$(gh api -X GET search/issues -f q="repo:${REPO} is:pr is:merged" --jq '.total_count')"
open_prs="$(gh api -X GET search/issues -f q="repo:${REPO} is:pr is:open" --jq '.total_count')"
remaining=$(( merged < TARGET ? TARGET - merged : 0 ))

echo "repo:              ${REPO}"
echo "merged_prs:        ${merged}"
echo "open_prs:          ${open_prs}"
echo "pull_shark_target: ${TARGET}"
echo "remaining:         ${remaining}"

echo
echo "public badges (best effort, HTML is dynamic):"
curl -sL https://github.com/users/M9GIU/achievements \
  | grep -o 'Pair Extraordinaire\|Pull Shark\|Quickdraw\|Galaxy Brain\|YOLO' \
  | sort | uniq -c || true
