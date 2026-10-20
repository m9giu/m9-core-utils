# Roadmap

Twelve milestones, ten substantive units each (~120 pull requests). Each unit is a
mergeable change with tests and documentation; no empty or cosmetic-only pull requests.

| Milestone | Theme | Units | Example deliverables |
|---|---|---|---|
| M1 | Foundation | 10 | CLI, registry, report, docs, CI, packaging |
| M2 | Documentation checks | 10 | readme, contributing, changelog, docs index |
| M3 | Security checks | 10 | security policy, secrets scan, dependency policy |
| M4 | CI checks | 10 | workflow presence, matrix, caching, permissions |
| M5 | Community checks | 10 | code of conduct, issue/PR templates, support |
| M6 | Release checks | 10 | versioning, tags, changelog, release notes |
| M7 | Dependency checks | 10 | lockfile, Dependabot, Renovate, pinning |
| M8 | Quality checks | 10 | lint config, typing config, coverage threshold |
| M9 | Reporting | 10 | SARIF, JUnit, HTML summary, severity mapping |
| M10 | Integrations | 10 | pre-commit hook, GitHub Action, Docker image |
| M11 | Extensibility | 10 | plugin API, config file, custom checks |
| M12 | Documentation & examples | 10 | guides, fixtures, sample reports, i18n |

## Progress

- [x] M1 foundation bootstrap (this pull request)
- [ ] M1 pilot: P-01…P-04 merged; P-05…P-08 in review
- [ ] M2–M12 per milestone plans (each block requires its own approved change map)

## Rules

- A milestone starts only when the previous one is complete and CI is green.
- Each block of twenty pull requests requires a planning update before execution.
- If a unit is not genuinely useful, it is removed rather than padded.
