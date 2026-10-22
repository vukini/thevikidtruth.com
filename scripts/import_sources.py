#!/usr/bin/env python3
"""One-off importer: Substack + wiki exports -> Hugo content/. Re-runnable (overwrites content)."""
from pathlib import Path
import re, csv, shutil, sys, yaml
sys.path.insert(0, str(Path(__file__).resolve().parent))
from substack_clean import clean as substack_clean
SITE = Path(__file__).resolve().parent.parent
SUB = Path("/workspace/substack/out"); WIKI = Path("/workspace/wiki/out")
SECTION = {"computing":"computing","math":"mathematics","science":"science","languages":"languages",
           "music":"music","articles":"essays","misc":"essays","quicklinks":"resources",
           "readinglist":"resources","help":"about","site":"about","orphan":"about"}
OVERRIDE = {"morevikid":"about","caveatemptor":"about"}
c = SITE/"content"; st = SITE/"static/assets"
for d in ["writing",*set(SECTION.values())]:
    shutil.rmtree(c/d, ignore_errors=True); (c/d).mkdir(parents=True)
st.mkdir(parents=True, exist_ok=True)
# Substack: prose verbatim, export boilerplate stripped (see substack_clean.py); images reference /assets/<slug>/...
for f in sorted((SUB/"articles").glob("*.md")):
    (c/"writing"/f.name).write_text(substack_clean(f.read_text()))
shutil.copytree(SUB/"assets", st, dirs_exist_ok=True)
shutil.copytree(WIKI/"assets", st, dirs_exist_ok=True)
inv = {r["slug"]: r for r in csv.DictReader(open(WIKI/"inventory.csv"))}
counts = {}
for f in sorted((WIKI/"articles").glob("*.md")):
    slug = f.stem; r = inv.get(slug, {})
    sec = OVERRIDE.get(slug) or SECTION.get(r.get("category",""), "about")
    judg = r.get("judgment", "update")
    text = f.read_text()
    assert text.startswith("---\n")
    fm_txt, body = text[4:].split("\n---\n", 1)
    # goldmark needs block attributes on their own line: "![x](y){.right}" -> "![x](y)\n{.right}" (markup only, wording untouched)
    body = re.sub(r"(!\[[^\]\n]*\]\([^)\n]*\))[ \t]*(\{\.(?:left|right|center)\})[ \t]*$", r"\1\n\2", body, flags=re.M)
    fm = yaml.safe_load(fm_txt) or {}
    fm["wikislug"] = slug
    fm["draft"] = judg != "keep"
    if judg != "keep": fm["review"] = judg
    fm.pop("review", None) if judg == "keep" else None
    out = "---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True) + "---\n" + body
    (c/sec/f.name).write_text(out)
    counts.setdefault(sec, [0,0]); counts[sec][0 if judg=="keep" else 1] += 1
TITLES={"writing":("Writing","Essays first published on Substack"),"computing":("Computing","PicoLisp, programming languages, Linux, networking & security"),"mathematics":("Mathematics","Sets, algebra, logic, category theory"),"science":("Science","Physics, chemistry, biology"),"languages":("Languages","Kiswahili, Arabic, Esperanto and more"),"music":("Music","Theory, practice, listening"),"essays":("Essays & Ideas","Philosophy, politics, economics, film"),"resources":("Resources","Quicklinks and reading lists"),"about":("About","Who is The VikiD Truth?")}
for w,(k,(v,d)) in enumerate(TITLES.items()): (c/k/"_index.md").write_text(f'---\ntitle: "{v}"\ndescription: "{d}"\nweight: {w}\n---\n')
print("section: published, draft", counts)
