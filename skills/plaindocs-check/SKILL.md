---
name: plaindocs-check
description: Check a guide, README or help page against a plain-language writing checklist and report what passes, what fails and how to fix it. Use when a user asks to review, proofread, simplify or check documentation.
---

# Check a document

Follow `rules/pillars-and-scope.mdc`. Answer in the user's language.

Do several passes, one aspect per pass (Technical Writing Essentials, revision checklist):

1. **Document:** clear title and headings; the purpose is stated at the top; logical order; everything the reader needs is there (Complete); reader-centred tone.
2. **Paragraphs:** each starts with a topic sentence; no paragraph longer than about 5 to 10 lines; no off-topic material.
3. **Sentences:** flag sentences over 25 words; prefer active voice with a clear actor; keep subject and verb close and early.
4. **Words:** plain, not pompous ("express, not impress"); replace wordy phrases ("in order to" → "to"); define or remove jargon; no clichés, slang or ad-speak.
5. **Instructions (if any):** numbered steps for a fixed order; one action per step; commands in the imperative; warnings placed before the step; an equipment or requirements list if needed.
6. **Seven Cs summary:** Clear, Coherent, Concise, Concrete, Correct, Complete, Courteous. When they conflict, clear wins.

If the user can run Python, also run `python3 scripts/plaindocs_check.py FILE` for an automatic first pass (sentence length, paragraph length, wordy phrases, possible passive voice, headings, step numbering). It is a rough heuristic: it cannot judge accuracy, tone or whether the reader will understand. A person's read-through is still needed.

Report: a pass/fail line per checklist item, the exact sentences to fix with a suggested rewrite, and anything you could not check (mark UNVERIFIED).
