// Language practice: flip cards, multiple choice and typed answers. Progress lives in localStorage only.
(function () {
  const root = document.getElementById("pr");
  if (!root) return;
  const deck = JSON.parse(document.getElementById("pr-deck").textContent);
  const KEY = "vikid-practice-" + deck.lang;
  const $ = (s) => root.querySelector(s);
  let prog = {};
  try { prog = JSON.parse(localStorage.getItem(KEY) || "{}"); } catch (e) { prog = {}; }
  const save = () => { try { localStorage.setItem(KEY, JSON.stringify(prog)); } catch (e) {} };
  const id = (c) => c.f + "\u241f" + c.b;
  const all = deck.cards.map((c, i) => Object.assign({ i }, c));
  const kindOf = (c) => c.k || "words";
  let st = { kind: "all", mode: "flip", dir: "fb", order: all.slice(), pos: 0, onlyNew: false, done: false };

  // accent-, case- and punctuation-tolerant comparison
  const norm = (s) => s.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase()
   .replace(/\([^)]*\)/g, " ").replace(/^(to|the|a|an|le|la|les|l'|el|los|las|un|une)\s+/, "")
    .replace(/[^\p{L}\p{N}\s'-]/gu, " ").replace(/\s+/g, " ").trim();
  const alts = (s) => s.split(/[,;\/·]| or /).map((x) => x.replace(/^\s*(n|mod|vi|vt|vt\.\/vi|prep|interj|conj|sep|num|pre-verb)\.?\s*[:.]?\s*/i, "")).map(norm).filter(Boolean);
  const front = (c) => (st.dir === "fb" ? c.f : c.b);
  const back = (c) => (st.dir === "fb" ? c.b : c.f);
  const answers = (c) => { const a = alts(back(c)); if (st.dir === "bf" && c.alt) a.push(...alts(c.alt)); if (st.dir === "bf") a.push(norm(c.f)); return a; };
  const lev = (a, b) => { const d = Array.from({ length: b.length + 1 }, (_, i) => i);
    for (let i = 1; i <= a.length; i++) { let p = d[0]; d[0] = i;
      for (let j = 1; j <= b.length; j++) { const t = d[j]; d[j] = Math.min(d[j] + 1, d[j - 1] + 1, p + (a[i - 1] === b[j - 1] ? 0 : 1)); p = t; } }
    return d[b.length]; };
  const check = (typed, c) => { const t = norm(typed); if (!t) return false;
    return answers(c).some((a) => a === t || (a.length > 5 && lev(a, t) <= 1)); };

  const mark = (c, ok) => { const p = prog[id(c)] || { r: 0, w: 0 }; ok ? p.r++ : p.w++; p.t = Date.now(); prog[id(c)] = p; save(); };
  const known = (c) => { const p = prog[id(c)]; return p && p.r > p.w && p.r >= 2; };
  const shuffle = (a) => { for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  const cur = () => (st.kind === "all" ? all : all.filter((c) => kindOf(c) === st.kind));
  const pool = () => (st.onlyNew ? cur().filter((c) => !known(c)) : cur());
  const esc = (s) => String(s).replace(/[&<>"]/g, (m) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[m]));

  function stats() {
    const set = cur(), k = set.filter(known).length, seen = set.filter((c) => prog[id(c)]).length;
    $("#pr-stats").textContent = `${set.length} cards · ${seen} practised · ${k} known`;
    $("#pr-bar").style.width = (100 * k / Math.max(1, set.length)).toFixed(1) + "%";
  }
  function reset(order) { st.order = order || pool().slice(); st.pos = 0; render(); }
  function next() { st.pos++; render(); }
  function details(c) {
    return (c.h ? `<p class="pr-h">${esc(c.h)}</p>` : "") + (c.x ? `<p class="pr-x">${esc(c.x)}</p>` : "") +
      (c.g ? `<p class="pr-g">${esc(c.g)}</p>` : "");
  }
  function render() {
    stats();
    const box = $("#pr-card");
    if (!st.order.length) { box.innerHTML = `<p class="pr-end">Nothing left to practise in this set. Untick "only cards I don't know yet" or reset your progress.</p>`; return; }
    if (st.pos >= st.order.length) {
      box.innerHTML = `<p class="pr-end">Round done: ${st.order.length} cards. <button type="button" class="pr-btn" id="pr-again">Go again (shuffled)</button></p>`;
      $("#pr-again").onclick = () => reset(shuffle(pool().slice())); return;
    }
    const c = st.order[st.pos];
    $("#pr-count").textContent = `${st.pos + 1} / ${st.order.length}`;
    if (st.mode === "flip") {
      box.innerHTML = `<button type="button" class="pr-flip" id="pr-flip" aria-live="polite"><span class="pr-front">${esc(front(c))}</span><span class="pr-tap">tap to flip</span></button>
        <div class="pr-row" hidden id="pr-grade"><button type="button" class="pr-btn bad" id="pr-no">Didn't know</button><button type="button" class="pr-btn good" id="pr-yes">Knew it</button></div>`;
      $("#pr-flip").onclick = () => {
        $("#pr-flip").innerHTML = `<span class="pr-q">${esc(front(c))}</span><span class="pr-front">${esc(back(c))}</span>${details(c)}`;
        $("#pr-grade").hidden = false; $("#pr-yes").focus();
      };
      $("#pr-yes") && ($("#pr-yes").onclick = () => { mark(c, true); next(); });
      $("#pr-no") && ($("#pr-no").onclick = () => { mark(c, false); next(); });
    } else if (st.mode === "mc") {
      const others = shuffle((cur().length > 3 ? cur() : all).filter((o) => back(o) !== back(c))).slice(0, 3);
      const opts = shuffle([c, ...others]);
      box.innerHTML = `<p class="pr-prompt">${esc(front(c))}</p><div class="pr-opts">${opts.map((o, k) => `<button type="button" class="pr-opt" data-k="${k}">${esc(back(o))}</button>`).join("")}</div><div id="pr-fb" aria-live="polite"></div>`;
      root.querySelectorAll(".pr-opt").forEach((b) => (b.onclick = () => {
        const ok = opts[+b.dataset.k] === c; mark(c, ok);
        root.querySelectorAll(".pr-opt").forEach((x) => { x.disabled = true; if (opts[+x.dataset.k] === c) x.classList.add("right"); });
        if (!ok) b.classList.add("wrong");
        $("#pr-fb").innerHTML = `<p class="pr-res ${ok ? "good" : "bad"}">${ok ? "Right." : "Not quite."}</p>${details(c)}<button type="button" class="pr-btn" id="pr-next">Next →</button>`;
        $("#pr-next").focus(); $("#pr-next").onclick = next;
      }));
    } else {
      box.innerHTML = `<p class="pr-prompt">${esc(front(c))}</p><form id="pr-form" class="pr-type" autocomplete="off"><label class="vh" for="pr-in">Your answer</label>
        <input id="pr-in" type="text" autocapitalize="off" autocorrect="off" spellcheck="false" placeholder="type the ${st.dir === "fb" ? "English" : deck.title}">
        <button type="submit" class="pr-btn">Check</button></form><div id="pr-fb" aria-live="polite"></div>`;
      const inp = $("#pr-in"); inp.focus({ preventScroll: true });
      $("#pr-form").onsubmit = (e) => {
        e.preventDefault();
        if ($("#pr-next")) { next(); return; }
        const ok = check(inp.value, c); mark(c, ok); inp.readOnly = true;
        $("#pr-fb").innerHTML = `<p class="pr-res ${ok ? "good" : "bad"}">${ok ? "Right." : "The answer:"} <b>${esc(back(c))}</b></p>${details(c)}
          <div class="pr-row">${ok ? "" : `<button type="button" class="pr-btn" id="pr-over">I was right</button>`}<button type="button" class="pr-btn" id="pr-next">Next →</button></div>`;
        $("#pr-next").onclick = next;
        $("#pr-over") && ($("#pr-over").onclick = () => { const p = prog[id(c)]; p.w--; p.r++; save(); next(); });
        $("#pr-next").focus();
      };
    }
  }
  root.querySelectorAll("[name=pr-mode]").forEach((r) => (r.onchange = () => { st.mode = r.value; render(); }));
  const ks = $("#pr-kind"); if (ks) { ks.querySelectorAll("option").forEach((o) => { if (o.value !== "all" && !all.some((c) => kindOf(c) === o.value)) o.remove(); }); ks.onchange = (e) => { st.kind = e.target.value; reset(); };
    const q = new URLSearchParams(location.search).get("deck"); if (q && [...ks.options].some((o) => o.value === q)) { ks.value = q; st.kind = q; } }
  $("#pr-dir").onchange = (e) => { st.dir = e.target.value; render(); };
  $("#pr-shuffle").onclick = () => reset(shuffle(pool().slice()));
  $("#pr-new").onchange = (e) => { st.onlyNew = e.target.checked; reset(); };
  $("#pr-reset").onclick = () => { if (confirm("Forget all your progress for " + deck.title + "?")) { prog = {}; save(); reset(); } };
  root.hidden = false;
  document.getElementById("pr-nojs") && document.getElementById("pr-nojs").remove();
  reset();
})();
