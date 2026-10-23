# Changelog

## 1.0.3 (2026-10-23)
- Translations: each language section in TRANSLATIONS.md now starts with a one-line notice in that language saying it is a machine translation, not reviewed by a native speaker, and that the English version is authoritative. README Languages section notes this. No behavior changes.
- Local tests re-run and passed. Not tested in-app. Not submitted to the marketplace.

## 1.0.2 (2026-10-23)
- `keywords.md` and the README keyword line now show the universals as PlainDocs, JennyEcho and OmnipotentCeo, matching the manifest (they still showed the old lowercase forms). No behavior changes.
- Local tests re-run and passed. Not tested in-app. Not submitted to the marketplace.

## 1.0.1 (2026-10-22)
- Fix: a compiled Python cache file (`scripts/__pycache__/*.pyc`) was committed by mistake and changed every time the tests ran. Removed it from the repo and added a `.gitignore` for `__pycache__/` and `*.pyc`.
- No behavior changes.

## 1.0.0 (2026-10-22)
- First version: skills `plaindocs-write` and `plaindocs-check`, rule `pillars-and-scope.mdc`, optional standard-library checker `scripts/plaindocs_check.py`, before-and-after worked example, plain-language README, 40 search keywords (lowercase, no hyphens, PlainDocs-specific, per Rob's keyword rules) in the manifest plus `keywords.md`, 23 machine-translated summaries.
- Checklist drawn from *Technical Writing Essentials* (Last) and *Professional Writing in the Digital Age* (Schechter and Hall).
- Tests: `tests/check_frontmatter.py` and `tests/test_checker.py`. Local only; not tested in-app. Not submitted to the marketplace.
