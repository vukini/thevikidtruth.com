# Truth Checks: how to add one

One page per claim in `content/truth-checks/<slug>.md`. The landing page, homepage strip, RSS (`/truth-checks/index.xml`),
/start/ button and /map/ colour (`data/kb_sections.yaml`, #E8505B) all update automatically.

1. **Pick a claim** people really repeat: AI hype, market myths, tech or Linux folklore, science misconceptions.
   Prefer topics that link to the site's sections (Frontier AI, Markets, Computing, Science).
2. **Research before writing.** Find the primary source: the paper, the official data, the company's own disclosure. Read it,
   and quote or paraphrase only what it actually says. Never invent a number, a quote or a study. If you can't source a point,
   cut it. Label company-reported figures as such.
3. **Front matter** (date in Dubai time, no later than now, or Hugo won't publish it):
   ```yaml
   title: "Question-style title?"
   date: 2026-10-25T04:00:00+04:00
   claim: "The claim, in the words people actually use."
   verdict: "True" | "False" | "Misleading" | "Half-true"   # exactly one of these; it drives the badge colour
   topic: "Frontier AI"      # short label shown on the card
   truth: "One or two sentences, shown in the verdict box under 'The truth:'."
   description: "Truth Check: ... (for search and social cards)"
   tags: ["ai"]
   ```
4. **Body**, in VikiD's voice (the superhero who looks closer; first person, plain words, short sentences, no hype):
   `## Where the claim comes from` → `## What's actually true` (bullets, each with the evidence) →
   `## The truth` with a paragraph starting `**The truth:**` → `## Sources` (a list of links).
   Don't edit Substack bodies in `content/writing/`. Link to them instead.
5. **Build and check:** `hugo --gc --minify`, then open `public/truth-checks/<slug>/index.html` and check the badge, box and links.
6. **Publish:** `git fetch && git rebase origin/main`, then
   `git -c user.name='The VikiD Truth' -c user.email=noreply@thevikidtruth.com commit -m "truth-checks: <slug>"`, push,
   and watch the Pages workflow with `gh run watch`.
