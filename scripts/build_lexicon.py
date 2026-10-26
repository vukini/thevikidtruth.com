#!/usr/bin/env python3
"""Merge scripts/lexicon/<lang>.txt into the language pages.

Each file has '# words', '# phrases', '# sentences' parts, '## Theme' headings and lines
'term | English | note' (Japanese: 'japanese | romaji | English | note').
- words go into a marked 'Core vocabulary by theme' block at the end of the language's vocabulary page,
  skipping any term the page (or the other vocabulary pages for that language) already has;
- phrases and sentences become content/languages/<lang>-phrases.md and <lang>-sentences.md.
Re-run after editing a lexicon file, then run scripts/build_practice.py.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_practice as bp

LEX = os.path.join(bp.ROOT, "scripts", "lexicon")
VOCAB = {"spanish": "spanishvocab1", "french": "frenchvocabulary", "esperanto": "esperantovortoj",
         "swahili": "swvocab001", "tokipona": "tokiponavocab", "japanese": "japanese-vocabulary"}
START, END = "<!-- core-vocab:start -->", "<!-- core-vocab:end -->"
DATE = "2026-10-26T06:30:00+04:00"

def parse(lang):
    parts, part, theme = {"words": [], "phrases": [], "sentences": []}, None, ""
    for l in open(os.path.join(LEX, lang + ".txt"), encoding="utf-8"):
        l = l.rstrip("\n")
        if not l.strip(): continue
        if l.startswith("## "): theme = l[3:].strip(); continue
        if l.startswith("# "): part = l[2:].strip(); theme = ""; continue
        f = [x.strip() for x in l.split(" | ")]
        parts[part].append((theme, f))
    return parts

def key(s):
    return re.sub(r"^(el|la|los|las|le|la|les|l'|un|une)\s+", "", bp.clean(s).lower()).strip(" .!?¿¡")

def table(rows, jp, title):
    hdr = "| Japanese | Romaji | English | Note |\n|---|---|---|---|" if jp else f"| {title} | English | Note |\n|---|---|---|"
    out, theme = [], None
    for th, f in rows:
        if th != theme:
            if theme is not None: out.append("")
            if th: out.append(f"### {th}\n")
            out.append(hdr); theme = th
        n = 4 if jp else 3
        f = (f + [""] * n)[:n]
        out.append("| " + " | ".join(x.replace("|", "/") for x in f) + " |")
    return "\n".join(out) + "\n"

def page(path, title, desc, lang, step, intro, body):
    fm = f"---\ntitle: '{title}'\ndescription: \"{desc}\"\ndate: '{DATE}'\nlastmod: '{DATE}'\ntags:\n- languages\ncategories:\n- languages\ntopics:\n- {lang}\npath_step: {step}\ndraft: false\n---\n\n"
    open(path, "w", encoding="utf-8").write(fm + f"# {title}\n\n{intro}\n\n" + body)

def main():
    for lang, slug in VOCAB.items():
        if not os.path.exists(os.path.join(LEX, lang + ".txt")): continue
        title = bp.DECKS[lang][0]; jp = lang == "japanese"
        p = parse(lang)
        vp = os.path.join(bp.LANG, slug + ".md")
        if not os.path.exists(vp):
            page(vp, f"{title}: Vocabulary", f"Core {title} vocabulary by theme, with kana, kanji and romaji.", lang, 3,
                 "High-frequency words by theme. Kanji where it's normally used, kana, and romaji. Practise them on the [practice page](/languages/japanese-practice/).", "")
        txt = open(vp, encoding="utf-8").read()
        txt = re.sub(re.escape(START) + r".*?" + re.escape(END) + r"\n?", "", txt, flags=re.S).rstrip() + "\n"
        open(vp, "w", encoding="utf-8").write(txt)
        have = set()
        for s in bp.DECKS[lang][2]:
            if s.endswith(("-phrases", "-sentences")) or not os.path.exists(os.path.join(bp.LANG, s + ".md")): continue
            have |= {key(c["f"]) for c in bp.cards_from(s)}
        words, seen, skipped = [], set(), []
        for th, f in p["words"]:
            k = key(f[0])
            if k in have: skipped.append(f[0]); continue
            if k in seen: continue
            seen.add(k); words.append((th, f))
        block = (f"\n{START}\n\n## Core vocabulary by theme\n\nHigh-frequency words, added October 2026"
                 + (": all the official pu words plus the ku suli words" if lang == "tokipona" else "")
                 + ". Words already in my notes above aren't repeated."
                 + f" Practise them on the [{title} practice page](/languages/{lang}-practice/).\n\n"
                 + table(words, jp, title) + f"\n{END}\n")
        open(vp, "w", encoding="utf-8").write(txt + block)
        n_ph, n_se = len(p["phrases"]), len(p["sentences"])
        page(os.path.join(bp.LANG, f"{lang}-phrases.md"), f"{title}: Everyday Phrases",
             f"{n_ph} everyday {title} phrases by situation, with English translations.", lang, 20,
             f"Everyday phrases by situation. Practise them on the [{title} practice page](/languages/{lang}-practice/?deck=phrases) (Phrases deck).",
             table(p["phrases"], jp, title))
        page(os.path.join(bp.LANG, f"{lang}-sentences.md"), f"{title}: Example Sentences",
             f"{n_se} {title} example sentences from simple to intermediate, with translations and grammar notes.", lang, 21,
             f"Example sentences, roughly from simple to intermediate, each with a translation and, where useful, a one-line grammar note. Practise them on the [{title} practice page](/languages/{lang}-practice/?deck=sentences) (Sentences deck).",
             table([("", f) for _, f in p["sentences"]], jp, title))
        print(f"{lang:10} words added {len(words):4} (skipped {len(skipped)} already in notes) phrases {n_ph} sentences {n_se}")

if __name__ == "__main__":
    main()
