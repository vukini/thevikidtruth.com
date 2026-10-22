#!/usr/bin/env python3
"""Batch publish/unpublish wiki pages by flipping front-matter flags.

Usage:
  scripts/publish.py slug1 slug2 ...            # publish these slugs (draft: false, review removed)
  scripts/publish.py --csv decisions.csv        # CSV with columns slug,decision (keep|update|retire|merge)
  add --dry-run to preview.
Decisions: keep -> published; update|retire|merge -> draft: true, review: <decision>.
Only front matter lines 'draft:' and 'review:' are touched; content is never changed.
"""
import argparse, csv, re, sys
from pathlib import Path
CONTENT = Path(__file__).resolve().parent.parent / "content"
INDEX = {p.stem: p for p in CONTENT.rglob("*.md") if p.parent.name != "writing" and p.name != "_index.md"}

def apply(path, decision, dry):
    text = path.read_text()
    fm, body = text[4:].split("\n---\n", 1)
    lines = [l for l in fm.split("\n") if not re.match(r"^(draft|review):", l)]
    lines.append("draft: false" if decision == "keep" else "draft: true")
    if decision != "keep": lines.append(f"review: {decision}")
    new = "---\n" + "\n".join(lines) + "\n---\n" + body
    changed = new != text
    if changed and not dry: path.write_text(new)
    return changed

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("slugs", nargs="*")
    ap.add_argument("--csv"); ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    todo = [(s, "keep") for s in a.slugs]
    if a.csv:
        for r in csv.DictReader(open(a.csv, newline="", encoding="utf-8-sig")):
            r = {k.strip().lower(): (v or "").strip() for k, v in r.items()}
            slug = r.get("slug") or Path(r.get("file", "")).stem
            dec = (r.get("decision") or r.get("judgment") or "").lower()
            if slug and dec: todo.append((slug, dec))
    if not todo: ap.error("give slugs or --csv")
    stats = {"changed": 0, "unchanged": 0, "unknown": []}
    for slug, dec in todo:
        if dec not in {"keep", "update", "retire", "merge"}:
            print(f"skip {slug}: bad decision {dec!r}"); continue
        p = INDEX.get(slug)
        if not p: stats["unknown"].append(slug); continue
        if apply(p, dec, a.dry_run): stats["changed"] += 1; print(f"{dec:7} {p.relative_to(CONTENT)}")
        else: stats["unchanged"] += 1
    print(f"changed {stats['changed']}, unchanged {stats['unchanged']}, unknown {len(stats['unknown'])} {stats['unknown'][:20]}")
    if a.dry_run: print("(dry run, nothing written)")
main()
