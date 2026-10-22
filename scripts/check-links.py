#!/usr/bin/env python3
"""Check internal links in the built site (public/).

Usage: python3 scripts/check-links.py [public_dir] [--section languages]
Reports hrefs/srcs that point at files missing from the build, and wiki links
that rendered as span.missing-link. Exit code 1 if anything is broken.
"""
import sys, re, pathlib, urllib.parse
from html.parser import HTMLParser
args=[a for a in sys.argv[1:] if not a.startswith("--")]
pub=pathlib.Path(args[0] if args else "public").resolve()
sec=sys.argv[sys.argv.index("--section")+1] if "--section" in sys.argv else None
if sec in args: args.remove(sec)
class P(HTMLParser):
    def __init__(s): super().__init__(); s.links=[]; s.missing=0
    def handle_starttag(s,tag,a):
        a=dict(a)
        for k in ("href","src"):
            if a.get(k): s.links.append(a[k])
        if tag=="span" and "missing-link" in (a.get("class") or ""): s.missing+=1
def exists(path):
    p=pub/path.lstrip("/")
    return p.is_file() or (p/"index.html").is_file() or p.with_suffix(".html").is_file()
bad=[]; miss=[]; n=0
for f in pub.rglob("*.html"):
    rel="/"+str(f.relative_to(pub))
    if sec and not rel.startswith("/%s/"%sec): continue
    p=P(); p.feed(f.read_text(errors="ignore"))
    if p.missing: miss.append((rel,p.missing))
    base=rel.rsplit("/",1)[0]+"/"
    for l in p.links:
        if re.match(r"^(https?:|mailto:|tel:|data:|javascript:|#|//)",l):
            if l.startswith("https://thevikidtruth.com/"): l=l[len("https://thevikidtruth.com"):]
            else: continue
        u=urllib.parse.urlparse(l).path
        if not u: continue
        u=urllib.parse.unquote(u if u.startswith("/") else urllib.parse.urljoin(base,u))
        n+=1
        if not exists(u): bad.append((rel,l))
for r,l in sorted(set(bad)): print("BROKEN  %s -> %s"%(r,l))
for r,c in sorted(miss): print("MISSING %s (%d unresolved wiki links)"%(r,c))
print("checked %d internal links: %d broken, %d pages with missing-link spans"%(n,len(set(bad)),len(miss)))
sys.exit(1 if bad or miss else 0)
