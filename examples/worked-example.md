# Worked example: rewriting a confusing setup note (real run, 2026-10-22)

**Before** (`examples/before.md`): one 58-word sentence, no heading, passive voice, four wordy phrases.

`python3 scripts/plaindocs_check.py examples/before.md`:
```
sentences: 2, average words per sentence: 31.5
- headings: no Markdown heading found
- long-sentence: 58 words: In order to get the backup tool working it is necessary that the configuration f
- possible-passive: 'is edited' in: In order to get the backup tool working it is necessary that the configuration f
- possible-passive: 'be saved' in: In order to get the backup tool working it is necessary that the configuration f
- wordy-phrase: 'in order to' -> 'to'
- wordy-phrase: 'due to the fact that' -> 'because'
- wordy-phrase: 'a large number of' -> 'many'
- wordy-phrase: 'prior to' -> 'before'
8 issue(s) found (heuristic only)
```

**After** (`examples/after.md`): a title, the purpose and time at the top, a Note placed before the step it concerns, four numbered one-action steps, and a "what to do if" section.

`python3 scripts/plaindocs_check.py examples/after.md`:
```
sentences: 2, average words per sentence: 10.0
no issues found (heuristic only; a human read is still needed)
```

The script is only a first pass. A person still checked that the rewrite is accurate and complete.
