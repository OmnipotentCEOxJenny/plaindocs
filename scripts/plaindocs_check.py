#!/usr/bin/env python3
"""PlainDocs automatic first pass for a Markdown or text document (standard library only).
Usage: python3 scripts/plaindocs_check.py FILE [--json]
Checks (rough heuristics, based on Technical Writing Essentials and Professional
Writing in the Digital Age): has a heading; long sentences (>25 words); long
paragraphs (>10 lines or >120 words); wordy phrases; possible passive voice;
average sentence length. Exit 0 = no issues found, 1 = issues found, 2 = usage error.
It cannot judge accuracy, tone or whether readers understand."""
import json, re, sys

WORDY = {"in order to": "to", "due to the fact that": "because", "at this point in time": "now",
         "in the event that": "if", "a large number of": "many", "for the purpose of": "to / for",
         "has the ability to": "can", "make a decision": "decide", "prior to": "before",
         "in spite of the fact that": "although", "with regard to": "about", "utilize": "use"}
PASSIVE = re.compile(r"\b(is|are|was|were|be|been|being)\s+(\w+ed|done|made|given|taken|shown|written|known|seen)\b", re.I)


def check(text):
    issues = []
    lines = text.splitlines()
    if not any(l.lstrip().startswith("#") for l in lines):
        issues.append({"check": "headings", "detail": "no Markdown heading found"})
    body = re.sub(r"```.*?```", "", text, flags=re.S)
    paras = [p for p in re.split(r"\n\s*\n", body) if p.strip() and not p.lstrip().startswith("#")]
    sentences = []
    for p in paras:
        plines = p.strip().splitlines()
        words = len(p.split())
        if not plines[0].lstrip().startswith(("-", "*", "1", "|")) and (len(plines) > 10 or words > 120):
            issues.append({"check": "paragraph-length", "detail": f"{words} words: {p.strip()[:60]}..."})
        for item in plines:
            item = re.sub(r"^\s*([-*]|\d+[.)])\s+", "", item)
            sentences += [s.strip() for s in re.split(r"(?<=[.!?])\s+", item) if s.strip()]
    for s in sentences:
        n = len(s.split())
        if n > 25:
            issues.append({"check": "long-sentence", "detail": f"{n} words: {s[:80]}"})
        for m in PASSIVE.finditer(s):
            issues.append({"check": "possible-passive", "detail": f"'{m.group(0)}' in: {s[:80]}"})
    low = body.lower()
    for k, v in WORDY.items():
        if re.search(r"\b" + re.escape(k) + r"\b", low):
            issues.append({"check": "wordy-phrase", "detail": f"'{k}' -> '{v}'"})
    avg = round(sum(len(s.split()) for s in sentences) / len(sentences), 1) if sentences else 0
    return {"sentences": len(sentences), "average_words_per_sentence": avg, "issues": issues}


def main(argv):
    if len(argv) < 2:
        print(__doc__); return 2
    r = check(open(argv[1], encoding="utf-8").read())
    if "--json" in argv:
        print(json.dumps(r, indent=2))
    else:
        print(f"sentences: {r['sentences']}, average words per sentence: {r['average_words_per_sentence']}")
        for i in r["issues"]:
            print(f"- {i['check']}: {i['detail']}")
        print("no issues found (heuristic only; a human read is still needed)" if not r["issues"] else f"{len(r['issues'])} issue(s) found (heuristic only)")
    return 1 if r["issues"] else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
