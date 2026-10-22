#!/usr/bin/env python3
"""Functional test: the checker must flag examples/before.md and pass examples/after.md."""
import pathlib, sys
root = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root / "scripts"))
from plaindocs_check import check
bad = check((root / "examples/before.md").read_text(encoding="utf-8"))
good = check((root / "examples/after.md").read_text(encoding="utf-8"))
kinds = {i["check"] for i in bad["issues"]}
need = {"headings", "long-sentence", "wordy-phrase", "possible-passive"}
ok = need <= kinds and not good["issues"]
print("before.md issues:", sorted(kinds), len(bad["issues"]))
print("after.md issues:", good["issues"], "avg words/sentence:", good["average_words_per_sentence"])
print("PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
