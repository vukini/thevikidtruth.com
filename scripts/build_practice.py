#!/usr/bin/env python3
"""Build flashcard decks for /languages/*-practice/ from the vocabulary tables in content/languages/.

Reads markdown tables (and Toki Pona '### word' + bullet lists), writes data/practice/<lang>.json:
{"lang": ..., "title": ..., "sources": [...], "cards": [{"f": term, "b": meaning, "h": hint, "x": example, "s": source page, "g": section heading}]}
Re-run after editing a vocabulary page:  python3 scripts/build_practice.py
"""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANG = os.path.join(ROOT, "content", "languages")
OUT = os.path.join(ROOT, "data", "practice")
DECKS = {
    "esperanto": ("Esperanto", "eo", ["esperantovortoj", "vortaro"]),
    "french": ("French", "fr", ["frenchvocabulary"]),
    "spanish": ("Spanish", "es", ["spanishvocab1"]),
    "swahili": ("Swahili", "sw", ["swvocab001", "swphrases101"]),
    "tokipona": ("Toki Pona", "tok", ["tokiponavocab"]),
    "japanese": ("Japanese", "ja", ["jpcolors"]),
}
MEANING = re.compile(r"^(english|meaning)$", re.I)

def clean(s):
    s = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", s)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"[*_`]", "", s)
    return re.sub(r"\s+", " ", s).strip()

def body(slug):
    t = open(os.path.join(LANG, slug + ".md"), encoding="utf-8").read()
    parts = t.split("---", 2)
    return parts[2] if t.startswith("---") else t

def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]

def tables(slug):
    """yield (heading, header or None, rows)"""
    head, cur, hdr = "", [], None
    lines = body(slug).splitlines() + [""]
    i = 0
    while i < len(lines):
        l = lines[i]
        if l.startswith("#"):
            head = clean(l.lstrip("#"))
        if l.startswith("|"):
            block = []
            while i < len(lines) and lines[i].startswith("|"):
                block.append(cells(lines[i])); i += 1
            hdr = None
            if len(block) > 1 and all(re.fullmatch(r":?-+:?", c) for c in block[1] if c):
                hdr, block = block[0], block[2:]
            yield head, hdr, block
            continue
        i += 1

def cards_from(slug):
    out = []
    for head, hdr, rows in tables(slug):
        h = [clean(c) for c in hdr] if hdr else []
        n = len(h) if h else max((len(r) for r in rows), default=0)
        # paired tables: Swahili | English | Swahili | English
        if h and n == 4 and h[0] == h[2] and h[1] == h[3]:
            rows = [r[:2] for r in rows] + [r[2:4] for r in rows if len(r) >= 4]
            h = h[:2]
        mi = next((k for k, c in enumerate(h) if MEANING.match(c)), 1)
        if h and h[0].lower() in ("english",) and len(h) > 1:  # e.g. "toki pona | English" written reversed
            mi = 0
        ti = 0 if mi != 0 else 1
        for r in rows:
            if len(r) <= max(mi, ti): continue
            f, b = clean(r[ti]), clean(r[mi])
            if not f or not b or f.lower() == b.lower(): continue
            extra = {clean(h[k]).lower() if k < len(h) else str(k): clean(c) for k, c in enumerate(r) if k not in (mi, ti) and clean(c)}
            c = {"f": f, "b": b, "s": slug, "g": head}
            ex = extra.pop("example", None)
            if ex: c["x"] = ex
            if "romaji" in extra: c["alt"] = extra["romaji"]
            if extra: c["h"] = " · ".join(f"{k}: {v}" if not k.isdigit() else v for k, v in extra.items())
            out.append(c)
    if slug == "vortaro":  # only the short "Words I Am Learning" list before the big dictionary dump
        skip = {"disigebla", "trudataj"}  # glosses on the page look wrong (separable / imposed), so not drilled
        for l in body(slug).split("#### Vortaro Granda")[0].split("# Esperanto: Words I Am Learning")[-1].splitlines():
            m = re.match(r"^\s*(\S+)\s+(?:-{3,}\s*)?(.+?)\s*\|?\s*$", l)
            if m and not l.startswith(("#", "*")) and m.group(1) not in skip:
                out.append({"f": m.group(1), "b": clean(m.group(2).lstrip("-")), "s": slug, "g": "Words I am learning"})
    if slug == "tokiponavocab":  # '### word' followed by '- n. meaning' bullets
        head, word = "", None
        for l in body(slug).splitlines():
            if l.startswith("## "): head = clean(l[3:])
            elif l.startswith("### "): word = clean(l[4:]); defs = []
            elif word and l.startswith("- "):
                d = clean(l[2:])
                if not any(x["f"] == word for x in out):
                    out.append({"f": word, "b": re.sub(r"^(n|mod|vi|vt|sep|prep|interj|conj|pre-verb|num)\.\s*", "", d).split(";")[0].split(",")[0].strip(),
                                "h": d, "s": slug, "g": head})
    return out

def main():
    for key, (title, code, slugs) in DECKS.items():
        cards, seen = [], set()
        for s in slugs:
            for c in cards_from(s):
                k = (c["f"].lower(), c["b"].lower())
                if k in seen: continue
                seen.add(k); cards.append(c)
        with open(os.path.join(OUT, key + ".json"), "w", encoding="utf-8") as fh:
            json.dump({"lang": key, "title": title, "code": code, "sources": slugs, "cards": cards}, fh, ensure_ascii=False, indent=0)
        print(f"{key:10} {len(cards):4} cards from {', '.join(slugs)}")

if __name__ == "__main__":
    main()
