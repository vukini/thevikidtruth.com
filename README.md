# thevikidtruth.com

Hugo site (no theme). `hugo server -D` to preview incl. drafts; `hugo --gc --minify && pagefind --site public` to build with search.

- `content/writing/` – Substack essays (verbatim). Images in `static/assets/<slug>/`.
- `content/{computing,mathematics,science,languages,music,essays,resources,about}/` – wiki pages. Front matter `wikislug`, `draft`, `review: update|retire`.
- Wiki links `slug.md` resolve via `layouts/_default/_markup/render-link.html`; unpublished/nonexistent targets render as plain text (`span.missing-link`).
- Design: all CSS in `assets/css/main.css`; templates in `layouts/` (baseof, header/footer partials, list, single, index, search). Replace freely.

## Batch publishing
    python3 scripts/publish.py slug1 slug2           # publish
    python3 scripts/publish.py --csv decisions.csv   # columns slug,decision (keep|update|retire|merge)
    python3 scripts/publish.py --csv decisions.csv --dry-run
Commit and push; the GitHub Action rebuilds and deploys.

## Deploy
Repo Settings → Pages → Source: GitHub Actions. Custom domain from `static/CNAME` (thevikidtruth.com); point DNS A/AAAA records to GitHub Pages (or ALIAS), then enable HTTPS.
`scripts/import_sources.py` re-imports from /workspace exports (overwrites content/).
