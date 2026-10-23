#!/usr/bin/env python3
"""Fetch daily market data for the /markets/ section.

Writes data/markets/history/<id>.json ({date: value}) and data/markets/latest.json.
Only free, keyless sources: Yahoo Finance chart API, FRED CSV, Trading Economics page text.
Never invents numbers: on failure an instrument keeps its stored history and is flagged
"unavailable" (no data at all) or "stale" (last value older than its expected cadence).
Usage: python3 scripts/markets_update.py   (stdlib only)
"""
import csv, io, json, os, re, sys, urllib.request
from datetime import datetime, timedelta, timezone, date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT, "data", "markets")
HIST = os.path.join(DIR, "history")
UA = {"User-Agent": "Mozilla/5.0 (thevikidtruth.com markets updater)"}
DUBAI = timezone(timedelta(hours=4))
LB_PER_T = 2204.62262
ST_PER_T = 1.10231131  # short tons per metric tonne

# id, name, group, unit, kind, source, factor, decimals, cadence(days before 'stale'), note
I = [
 ("copper", "Copper (COMEX)", "Metals", "USD/t", "yahoo:HG=F", LB_PER_T, 0, 4, "COMEX front-month, converted from USD/lb"),
 ("aluminium", "Aluminium (COMEX)", "Metals", "USD/t", "yahoo:ALI=F", 1, 0, 4, "COMEX front-month; conductor and overhead-line metal"),
 ("zinc", "Zinc (CME, LME-style)", "Metals", "USD/t", "yahoo:ZNC=F", 1, 0, 4, "Galvanizing input for wire, mesh and steel structures"),
 ("copper-wire", "Copper wire & cable (US PPI)", "Metals", "index", "fred:WPU10260314", 1, 1, 70, "Monthly producer price index; no free daily copper rod feed"),
 ("steel-wire", "Steel wire drawing (US PPI)", "Steel", "index", "fred:PCU331222331222", 1, 1, 70, "Monthly producer price index; proxy for wire rod, no free daily feed"),
 ("hrc", "Steel HRC (CME US Midwest)", "Steel", "USD/t", "yahoo:HRC=F", ST_PER_T, 0, 4, "CME front-month, converted from USD/short ton"),
 ("rebar", "Steel rebar (SHFE)", "Steel", "CNY/t", "te:steel", 1, 0, 4, "Shanghai rebar futures, as quoted by Trading Economics"),
 ("cement", "Cement manufacturing (US PPI)", "Construction", "index", "fred:PCU327310327310", 1, 1, 70, "Monthly producer price index; no free daily Gulf cement feed"),
 ("brent", "Brent crude", "Energy", "USD/bbl", "yahoo:BZ=F", 1, 2, 4, "ICE front-month"),
 ("wti", "WTI crude", "Energy", "USD/bbl", "yahoo:CL=F", 1, 2, 4, "NYMEX front-month"),
 ("gold", "Gold", "Energy", "USD/oz", "yahoo:GC=F", 1, 0, 4, "COMEX front-month"),
 ("spx", "S&P 500", "Equities", "points", "yahoo:^GSPC", 1, 0, 4, ""),
 ("ndx", "Nasdaq Composite", "Equities", "points", "yahoo:^IXIC", 1, 0, 4, ""),
 ("dfm", "DFM General Index", "Equities", "points", "yahoo:DFMGI.AE", 1, 0, 4, "Dubai Financial Market"),
 ("adx", "ADX General Index", "Equities", "points", "yahoo:FADGI.FGI", 1, 0, 4, "Abu Dhabi Securities Exchange"),
 ("em", "MSCI EM (EEM ETF proxy)", "Equities", "USD", "yahoo:EEM", 1, 2, 4, "iShares MSCI Emerging Markets ETF, used as a free proxy for the index"),
 ("ust2", "US Treasury 2y", "Rates & FX", "%", "fred:DGS2", 1, 2, 5, "Daily constant-maturity yield"),
 ("ust10", "US Treasury 10y", "Rates & FX", "%", "fred:DGS10", 1, 2, 5, "Daily constant-maturity yield"),
 ("dxy", "US Dollar Index", "Rates & FX", "index", "yahoo:DX-Y.NYB", 1, 2, 4, "ICE DXY; the dirham is pegged to the dollar"),
]

def get(url, t=30):
    # FRED stalls on browser-like user agents, so it gets a plain client UA
    h = {"User-Agent": "curl/8.5.0"} if "stlouisfed" in url else UA
    with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=t) as r:
        return r.read().decode("utf-8", "replace")

def yahoo(sym):
    d = json.loads(get(f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}?range=6mo&interval=1d"))
    r = d["chart"]["result"][0]
    tz = timezone(timedelta(seconds=r["meta"].get("gmtoffset", 0)))
    out = {}
    for ts, c in zip(r["timestamp"], r["indicators"]["quote"][0]["close"]):
        if c is not None:
            out[datetime.fromtimestamp(ts, tz).date().isoformat()] = c
    m = r["meta"]  # the last daily bar is sometimes empty; use the quoted market price for that day
    if m.get("regularMarketPrice") and m.get("regularMarketTime"):
        d = datetime.fromtimestamp(m["regularMarketTime"], tz).date().isoformat()
        out.setdefault(d, m["regularMarketPrice"])
    return out, f"https://finance.yahoo.com/quote/{sym}", "Yahoo Finance"

def fred(sid):
    start = (date.today() - timedelta(days=800)).isoformat()
    for attempt in range(3):
        try:
            text = get(f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}", 30); break
        except Exception:
            if attempt == 2: raise
    rows = csv.reader(io.StringIO(text))
    next(rows)
    out = {d: float(v) for d, v in rows if v not in ("", ".") and d >= start}
    return out, f"https://fred.stlouisfed.org/series/{sid}", "FRED (St. Louis Fed)"

MONTHS = {m: i for i, m in enumerate(["January","February","March","April","May","June","July","August","September","October","November","December"], 1)}
def te(page):
    url = f"https://tradingeconomics.com/commodity/{page}"
    m = re.search(r"(?:rose|fell|increased|decreased|was unchanged at|traded (?:flat )?at)\s*(?:to\s*)?([\d,\.]+)\s*CNY/T on (\w+) (\d+), (\d{4})", get(url))
    if not m: raise ValueError("pattern not found")
    d = date(int(m.group(4)), MONTHS[m.group(2)], int(m.group(3))).isoformat()
    return {d: float(m.group(1).replace(",", ""))}, url, "Trading Economics"

def load(p, default):
    try:
        with open(p) as f: return json.load(f)
    except Exception: return default

def ago(hist, days, last):
    target = (date.fromisoformat(last) - timedelta(days=days)).isoformat()
    ks = [k for k in hist if k <= target]
    return hist[max(ks)] if ks else None

def main():
    today = datetime.now(DUBAI).date()
    latest = {"updated": datetime.now(DUBAI).isoformat(timespec="seconds"), "instruments": []}
    for (iid, name, group, unit, kind, factor, dec, cadence, note) in I:
        src, arg = kind.split(":", 1)
        hp = os.path.join(HIST, iid + ".json")
        hist = load(hp, {})
        err = None
        try:
            new, url, sname = {"yahoo": yahoo, "fred": fred, "te": te}[src](arg)
            hist.update({k: round(v * factor, 4) for k, v in new.items()})
        except Exception as e:
            err = f"{type(e).__name__}: {e}"[:160]
            url = {"yahoo": f"https://finance.yahoo.com/quote/{arg}", "fred": f"https://fred.stlouisfed.org/series/{arg}",
                   "te": f"https://tradingeconomics.com/commodity/{arg}"}[src]
            sname = {"yahoo": "Yahoo Finance", "fred": "FRED (St. Louis Fed)", "te": "Trading Economics"}[src]
            print(f"WARN {iid}: {err}", file=sys.stderr)
        hist = dict(sorted(hist.items()))
        with open(hp, "w") as f: json.dump(hist, f, indent=0)
        rec = {"id": iid, "name": name, "group": group, "unit": unit, "source": sname, "source_url": url,
               "note": note, "decimals": dec, "monthly": cadence > 30}
        if not hist:
            rec.update(status="unavailable", error=err)
        else:
            keys = list(hist); last = keys[-1]; v = hist[last]
            prev = hist[keys[-2]] if len(keys) > 1 else None
            age = (today - date.fromisoformat(last)).days
            rec.update(value=v, asof=last, status="stale" if age > cadence else ("fetch-failed" if err else "ok"), error=err)
            bp = unit == "%"
            def ch(old):
                if old is None: return None
                return round((v - old) * 100, 1) if bp else round((v / old - 1) * 100, 2)
            rec["chg_unit"] = "bp" if bp else "%"
            rec["chg_1d"] = ch(prev)          # vs previous observation (previous month for monthly series)
            rec["chg_1w"] = None if cadence > 30 else ch(ago(hist, 7, last))
            rec["chg_1m"] = ch(ago(hist, 30, last))
            rec["spark"] = [hist[k] for k in keys[-(13 if cadence > 30 else 30):]]
        latest["instruments"].append(rec)
    with open(os.path.join(DIR, "latest.json"), "w") as f: json.dump(latest, f, indent=1)
    for r in latest["instruments"]:
        print(f'{r["id"]:12} {r["status"]:12} {r.get("asof","-"):10} {r.get("value","-")} 1d={r.get("chg_1d")} 1w={r.get("chg_1w")} 1m={r.get("chg_1m")}')

if __name__ == "__main__":
    main()
