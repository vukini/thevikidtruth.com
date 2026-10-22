# Frontier AI weekly roundup: procedure

Section: `content/frontier-ai/` → https://thevikidtruth.com/frontier-ai/ (RSS: `/frontier-ai/index.xml`).
Templates: `layouts/_default/list.html` (landing, newest first), `layouts/_default/single.html` (`frontier-ai` branch, no character art on articles), homepage strip in `layouts/index.html`, `/start/` button in `layouts/_default/start.html`, colour in `data/kb_sections.yaml`, landing art in `data/art.yaml`.

## 1. File
- Name: `content/frontier-ai/YYYY-MM-DD-week.md`, date = publication day (normally Friday).
- Front matter (copy the previous roundup):
  ```yaml
  title: "Frontier AI, week of 23 October 2026"
  subtitle: "3-6 headline topics, comma-separated"
  date: 2026-10-23T00:00:00+04:00   # ALWAYS give a time + offset; a bare date is UTC midnight and Hugo skips it as "future" when built earlier in UTC
  period: "9–23 October 2026"        # window covered (~1-2 weeks since the last roundup)
  slug: "2026-10-23-week"
  description: "One sentence for SEO / RSS."
  tags: ["ai"]
  ```

## 2. Body structure
Short 1-2 sentence intro, then `##` theme groups in this order (omit empty ones):
Models and releases · Research · Agents and tools · Policy and safety · Industry and compute · Open source and open weights.
Each item:
```
### Headline (plain, factual)

2-4 sentence plain-words summary: who, what, when, key numbers as stated by the source.

**The truth:** 1-2 sentences on what actually matters vs the hype. Opinion, but no new facts.

Source: [Publisher: page title](https://primary-source-url)
```
8-15 items total. End with the "Sources were read on <date>" line.

## 3. Sourcing rules (non-negotiable)
- Every fact, number and quote must come from a page actually fetched (WebFetch/curl) during that run. No facts from memory or from search-result summaries alone.
- Prefer primary sources: lab blogs, official docs/changelogs, arXiv abstracts, government sites. Use reputable press (Reuters, AP, CBS, Axios, FT...) for reporting, and say "reported"/"citing a source" when it is unconfirmed.
- Attribute vendor claims ("Google says", "Meta calls it"). Don't repeat "best/most capable" as fact.
- Only items dated inside the period (an item a day or two before may be included if flagged, e.g. "just before our window").
- Check every link: `curl -sL -o /dev/null -w '%{http_code}' -A Mozilla/5.0 URL`. Some sites (openai.com, investing.com) return 403 to curl but load in a browser/WebFetch; that is acceptable if WebFetch read the page.
- No character art inside roundups (landing page only). Never edit Substack posts or wiki.ppk.

## 4. Build and publish
```
hugo --gc --minify && python3 scripts/check-links.py public --section frontier-ai
git add content/frontier-ai/<file>.md && git -c user.name='The VikiD Truth' -c user.email=noreply@thevikidtruth.com commit -m "Frontier AI: roundup <date>"
git fetch && git rebase origin/main && git push origin HEAD:main
```
Then confirm the Pages workflow succeeded (`gh run list -R vukini/thevikidtruth.com -L 1`) and that `/frontier-ai/`, the new roundup URL and `/frontier-ai/index.xml` return 200.
