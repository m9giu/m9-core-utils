# Contributing

Thanks for helping improve `m9-audit-kit`.

## Ground rules

- One pull request = one substantive unit of work (a check, a fix, a refactor or a doc
  improvement). Empty or cosmetic-only pull requests are not accepted.
- Every pull request must link an issue and pass CI (`ruff`, `mypy`, `pytest`).
- No secrets, tokens or personal data in code, tests, logs or screenshots.
- Be respectful; see `CODE_OF_CONDUCT.md`.

## Pull request workflow

1. Open or pick an issue with a verifiable acceptance criterion.
2. Create a branch: `feat/<issue>-<slug>`.
3. Implement the change and add tests.
4. Run locally:

   ```bash
   ruff check .
   mypy src
   pytest
   ```

5. Open the pull request using the template. Describe **what**, **why**, and **how it was
   tested**.
6. A maintainer reviews and squash-merges. Branches are deleted after merge.

## Co-authorship

Co-authorship credits real collaboration. If you pair with someone on a commit:

```text
Co-authored-by: Real Name <verified-email@users.noreply.github.com>
```

- The co-author must be a real person who contributed to the change and consented.
- The email must be verified on their GitHub account.
- Secondary or fake accounts are forbidden and will be reported.

## Documentation

Every new check requires `docs/checks/<slug>.md` describing what it verifies, its
statuses and its limitations. Update `README.md` and `docs/ROADMAP.md` when the public
surface changes.
