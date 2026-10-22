# Changelog

## 1.0.1 (2026-10-22)
- Fix: a compiled Python cache file (`scripts/__pycache__/*.pyc`) was committed by mistake and changed every time the tests ran. Removed it from the repo and added a `.gitignore` for `__pycache__/` and `*.pyc`.
- No behavior changes.

## 1.0.0 (2026-10-22)
- First version: skills `plaindocs-write` and `plaindocs-check`, rule `pillars-and-scope.mdc`, optional standard-library checker `scripts/plaindocs_check.py`, before-and-after worked example, plain-language README, 40 search keywords (lowercase, no hyphens, PlainDocs-specific, per Rob's keyword rules) in the manifest plus `keywords.md`, 23 machine-translated summaries.
- Checklist drawn from *Technical Writing Essentials* (Last) and *Professional Writing in the Digital Age* (Schechter and Hall).
- Tests: `tests/check_frontmatter.py` and `tests/test_checker.py`. Local only; not tested in-app. Not submitted to the marketplace.
