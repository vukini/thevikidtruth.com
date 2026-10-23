# Markets: daily update procedure

The `/markets/` section is a daily board (`content/markets/_index.md` + `layouts/markets/list.html` +
`layouts/partials/markets-table.html`) fed by `data/markets/`, plus one dated note per day in `content/markets/`.

## Data

- `scripts/markets_update.py` (Python 3, standard library only, no API keys) fetches every instrument and writes:
  - `data/markets/history/<id>.json`: `{ "YYYY-MM-DD": value }`. This is merged, never truncated, so history builds up
    (DFM, ADX and SHFE rebar have no free back history, so their weekly and monthly changes appear as days accumulate).
  - `data/markets/latest.json`: per instrument value, unit, as-of date, day/week/month change, a 30-point sparkline,
    source name and URL, and a status of `ok`, `stale` (older than expected), `fetch-failed` (shows the last stored value) or
    `unavailable` (no data at all).
- Sources:
  | id | instrument | source | notes |
  |---|---|---|---|
  | copper | COMEX copper HG=F | Yahoo Finance | USD/lb × 2204.62 → USD/t |
  | aluminium | COMEX aluminium ALI=F | Yahoo Finance | USD/t |
  | zinc | CME zinc ZNC=F | Yahoo Finance | USD/t (galvanising input) |
  | copper-wire | US PPI copper wire & cable WPU10260314 | FRED | monthly index; there's no free daily copper rod feed |
  | steel-wire | US PPI steel wire drawing PCU331222331222 | FRED | monthly index; proxy for wire rod |
  | hrc | CME US Midwest HRC HRC=F | Yahoo Finance | USD/short ton × 1.10231 → USD/t |
  | rebar | SHFE rebar | Trading Economics page text (`/commodity/steel`) | CNY/t; parsed from the page summary |
  | cement | US PPI cement manufacturing PCU327310327310 | FRED | monthly index; there's no free daily Gulf cement feed |
  | brent / wti | BZ=F / CL=F | Yahoo Finance | USD/bbl |
  | gold | GC=F | Yahoo Finance | USD/oz |
  | spx / ndx | ^GSPC / ^IXIC | Yahoo Finance | |
  | dfm / adx | DFMGI.AE / FADGI.FGI | Yahoo Finance | Yahoo serves only the latest value |
  | em | EEM ETF | Yahoo Finance | free proxy for MSCI EM |
  | ust2 / ust10 | DGS2 / DGS10 | FRED | changes are in basis points |
  | dxy | DX-Y.NYB | Yahoo Finance | |
- Futures values are the latest quote at fetch time, not official settlements. Never type a number into the data
  files by hand, and never invent one. If a source fails, leave the status the script sets.

## Daily run (Dubai morning, around 06:00 UTC+4)

1. `cd /workspace/site && git fetch && git rebase origin/main`
   (another worker commits here. The `Markets data (daily)` Actions cron, 05:30 Dubai, may already have committed
   fresh data. Re-running the script is harmless.)
2. `python3 scripts/markets_update.py` and read the printed table (status, as-of, 1d/1w/1m).
3. Write `content/markets/YYYY-MM-DD.md` (today's Dubai date) using the front matter of the last note as a template:
   `date: YYYY-MM-DDT05:00:00+04:00` (not later than the current time: Hugo skips future-dated pages), `slug`, `title: "Markets, D Month YYYY"`, a one-line `subtitle`,
   `data_asof`, `description`, `tags: ["markets"]`. Body:
   - `## What moved`: 4–6 bullets in plain words, using only the numbers in `data/markets/latest.json` (rounded,
     with units and as-of dates where they differ). Say plainly when something is stale, unavailable or has no history yet.
   - A paragraph starting `**The truth:**`, a single paragraph on what it means for UAE cable, electrical and construction suppliers: conductor
     metals (copper, aluminium), steel and zinc for wire, mesh, fencing, towers and rebar, cement for civils, oil for
     Gulf budgets, freight and energy, and rates and the dollar for financing (the AED is pegged). Use the Frontier AI voice:
     first person, short sentences, no hype, no predictions dressed up as facts, not investment advice.
   - Never name specific companies. Talk about UAE suppliers in general terms.
4. `hugo --gc --minify` must build cleanly. Check `public/markets/index.html` shows the new note and the board.
5. Commit and push:
   `git add data/markets content/markets && git -c user.name='The VikiD Truth' -c user.email=noreply@thevikidtruth.com commit -m "markets: daily note YYYY-MM-DD"`
   then `git fetch && git rebase origin/main && git push`.
6. Check the "Deploy Hugo site to GitHub Pages" run with `gh run list -L 3` and `gh run watch`, then
   `curl -s https://thevikidtruth.com/markets/ | grep "Markets, D Month"`.
