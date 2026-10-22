"""Strip Substack export boilerplate (markup only; prose and real images untouched)."""
import re
PATTERNS = {
    "empty_cdn_link": r"\[\]\(https://substackcdn\.com/[^)\s]*\)",
    "data_uri_icon":  r"!?\[[^\]]*\]\(data:image/[^)\s]*\)",
    "subscribe_btn":  r"\[Subscribe(?: now)?\]\(https://[^)\s]*substack\.com/[^)\s]*\)",
    "share_btn":      r"\[Share(?: The Vikid Truth)?\]\(https://[^)\s]*substack\.com/[^)\s]*\)",
    "comment_btn":    r"\[Leave a comment\]\(https://[^)\s]*substack\.com/[^)\s]*\)",
}
def clean(text, counts=None):
    for k, p in PATTERNS.items():
        # only lines consisting solely of boilerplate links
        rx = re.compile(r"^[ \t]*(?:" + p + r"[ \t]*)+$\n?", re.M)
        n = len(re.findall(p, "\n".join(m.group(0) for m in rx.finditer(text))))
        text = rx.sub("", text)
        if counts is not None: counts[k] = counts.get(k, 0) + n
    # empty CDN links inside other lines (e.g. list items) carry no text: drop inline
    text, n = re.subn(r"[ \t]*" + PATTERNS["empty_cdn_link"], "", text)
    if counts is not None: counts["empty_cdn_link"] += n
    return re.sub(r"\n{3,}", "\n\n", text)
