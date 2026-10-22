#!/usr/bin/env python3
"""Categorise Substack posts (content/writing) and relate them to knowledge-base pages.
Never edits post files. Writes:
  data/writing_topics.yaml   post slug -> [topic slugs]   (topics defined in data/topics/writing.yaml)
  data/writing_related.yaml  post slug -> [wikislug, ...] (KB pages ranked by shared keywords, TF-IDF)
Re-run after new posts are imported:  python3 scripts/relate_writing.py
"""
import re, math, glob, os, yaml, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def load(f):
    t = open(f, encoding='utf-8').read()
    m = re.match(r'^---\n(.*?)\n---\n?(.*)$', t, re.S)
    if not m: return {}, t
    try: fm = yaml.safe_load(m.group(1)) or {}
    except Exception: fm = {}
    return fm, m.group(2)
STOP = set("""a about above after again against all am an and any are as at be because been before being below between both but by can could did do does doing down during each few for from further had has have having he her here hers herself him himself his how i if in into is it its itself just me more most my myself no nor not now of off on once only or other our ours ourselves out over own same she should so some such than that the their theirs them themselves then there these they this those through to too under until up very was we were what when where which while who whom why will with would you your yours yourself yourselves also one two get got like even much many way thing things really know see make made say said going go well back still us let new time first us dont im youre thats its isnt cant wont didnt doesnt ive id ill shall may might must every never always something nothing anything everything someone people man men life world day years year good great little long right part need want think take come came look use used ever around another though yet without within upon whether rather quite actually simply perhaps however less least https http www com html png jpg substack page pages missing""".split())
def toks(s):
    s = re.sub(r'!\[[^\]]*\]\([^)]*\)|https?://\S+|<[^>]+>', ' ', s.lower())
    return [w for w in re.findall(r"[a-z][a-z\-]{2,}", s) if w not in STOP]
def stem(w):
    for suf in ('ings','ing','ies','es','s','ly','ed'):
        if w.endswith(suf) and len(w) - len(suf) >= 4: return w[:-len(suf)]
    return w

TOPICS = {  # writing topic slug -> keywords (title/subtitle weighted x4)
 'health':   "fast fasting fasted water hydration dry weight bulking cutting diet food eat eating breakfast health body bowels hunger coconut adipose fitness gym exercise cancer",
 'spirit':   "god spiritual spirituality meditation non-dual nondual advaita awareness consciousness enlightenment yoga mystic mysticism mystical divine soul jesus buddha tao sermon prayer brahman ramakrishna ribhu third eye guru maharishi heaven grail occult",
 'mind':     "logic paradox science scientific physics math mathematics numbers infinity entropy quantum wave neuroscience intelligence stupidity philosophy philosopher ontology metaphysics zeno string",
 'society':  "politics political election lockdown virus pandemic covid war government economy economic money inflation tyranny equality left right maga trump media propaganda climate net zero cancel culture history empire britannia colonized society social elite wef schwab",
 'culture':  "movie film review avatar superman nolan pulp fiction book novel story character hero heroes expanse dune beatles comedy cinema interview podcast brand",
 'music':    "music musical guitar fretboard song songs chord chords scale scales sound frequencies jazz musician instrument palmisano",
 'tech':     "computer computers computing ai artificial digital identity lisp code programming machine robot internet technology brain unit",
}
OVERRIDE = {'the-vikid-truth-day-14-of-20': ['health','spirit']}

def main():
    wfiles = [f for f in sorted(glob.glob(f'{ROOT}/content/writing/*.md')) if not f.endswith('_index.md')]
    secs = [s['slug'] for s in yaml.safe_load(open(f'{ROOT}/data/kb_sections.yaml')) if s['slug'] != 'writing']
    kb = []
    for s in secs:
        for f in glob.glob(f'{ROOT}/content/{s}/*.md'):
            if f.endswith('_index.md'): continue
            fm, body = load(f)
            if fm.get('draft') or not fm.get('wikislug'): continue
            body = re.sub(r'(?m)^[ \t]*(?:\[[^\]\n]*\]\([^)]*\)[ \t]*\|?[ \t]*){2,}$', '', body)
            if len(body) < 300: continue
            kb.append((str(fm['wikislug']), str(fm.get('title','')), body))
    posts = []
    for f in wfiles:
        fm, body = load(f)
        posts.append((os.path.basename(f)[:-3], f"{fm.get('title','')} {fm.get('subtitle','')}", body))
    docs = [[stem(w) for w in toks(t*1) + toks(t)*3 + toks(b)] for _, t, b in kb] + \
           [[stem(w) for w in toks(t)*3 + toks(b)] for _, t, b in posts]
    df = collections.Counter(w for d in docs for w in set(d)); N = len(docs)
    def vec(d):
        c = collections.Counter(d); v = {w: (1+math.log(n)) * math.log(N/df[w]) for w, n in c.items() if df[w] >= 2 and df[w] < N*0.12}
        norm = math.sqrt(sum(x*x for x in v.values())) or 1
        return {w: x/norm for w, x in v.items()}
    kv = [vec(d) for d in docs[:len(kb)]]; pv = [vec(d) for d in docs[len(kb):]]
    kt = [set(stem(w) for w in toks(t)) for _, t, _ in kb]
    topics, related = {}, {}
    tk = {k: set(stem(w) for w in v.split()) for k, v in TOPICS.items()}
    for (slug, title, body), v in zip(posts, pv):
        tw = [stem(w) for w in toks(title)]; bw = [stem(w) for w in toks(body)]
        sc = {k: 4*sum(w in ks for w in tw) + sum(w in ks for w in bw) / max(1, len(bw)/400) for k, ks in tk.items()}
        if slug.startswith('the-vikid-fast') or 'fast' in slug: sc['health'] += 50
        ranked = sorted(sc, key=sc.get, reverse=True)
        t = [ranked[0]] if sc[ranked[0]] > 2.5 else ['life']
        if t != ['life'] and sc[ranked[1]] >= 0.6*sc[ranked[0]] and sc[ranked[1]] > 2: t.append(ranked[1])
        topics[slug] = OVERRIDE.get(slug, t)
        pset = set(bw) | set(tw)
        scores = []
        for i, (ws, kt_title, _) in enumerate(kb):
            s = sum(x * kv[i].get(w, 0) for w, x in v.items())
            if kt[i] and kt[i] <= pset and len(kt_title) > 3: s += 0.05
            if ws in set(tw) or (kt[i] and kt[i] <= set(tw)): s += 0.3
            scores.append((s, ws))
        scores.sort(reverse=True)
        related[slug] = [ws for s, ws in scores[:5] if s > 0.08]
    hdr = "# Generated by scripts/relate_writing.py. Do not edit by hand; re-run the script.\n"
    open(f'{ROOT}/data/writing_topics.yaml','w').write(hdr + yaml.safe_dump(topics, sort_keys=True, default_flow_style=None, width=200))
    open(f'{ROOT}/data/writing_related.yaml','w').write(hdr + yaml.safe_dump(related, sort_keys=True, default_flow_style=None, width=200))
    print(collections.Counter(t for v in topics.values() for t in v), sum(1 for v in related.values() if v), len(posts), len(kb))
main()

def write_cascade():
    topics = yaml.safe_load(open(f'{ROOT}/data/writing_topics.yaml'))
    os.makedirs(f'{ROOT}/config/_default', exist_ok=True)
    out = ["# Generated by scripts/relate_writing.py from data/writing_topics.yaml: gives each Substack post its `topics`",
           "# without touching the post files. Do not edit by hand.", "cascade:"]
    for slug, t in sorted(topics.items()):
        out.append(f"  - target: {{path: /writing/{slug}}}\n    params: {{topics: [{', '.join(t)}]}}")
    open(f'{ROOT}/config/_default/cascade.yaml', 'w').write('\n'.join(out) + '\n')
write_cascade()
