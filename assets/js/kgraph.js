/* Self-contained force-directed knowledge graph (no external libraries). */
(function () {
  var D = JSON.parse(document.getElementById("kg-data").textContent);
  var cv = document.getElementById("kg-canvas"), ctx = cv.getContext("2d");
  var tip = document.getElementById("kg-tip"), q = document.getElementById("kg-q");
  var col = {}, title = {};
  D.cats.forEach(function (c) { col[c.slug] = c.color; title[c.slug] = c.title; });
  var byId = {}, nodes = D.nodes.map(function (n, i) {
    var a = i * 2.39996, r = 12 * Math.sqrt(i + 1);
    var o = { id: n.id, t: n.t, c: n.c, x: Math.cos(a) * r, y: Math.sin(a) * r, vx: 0, vy: 0, deg: 0, nb: {} };
    byId[n.id] = o; return o;
  });
  var links = D.links.filter(function (l) { return byId[l.s] && byId[l.t]; }).map(function (l) {
    var s = byId[l.s], t = byId[l.t]; s.deg++; t.deg++; s.nb[t.id] = 1; t.nb[s.id] = 1; return { s: s, t: t };
  });
  nodes.forEach(function (n) { n.r = 3.5 + Math.sqrt(n.deg) * 1.6; });
  // Category anchors on a ring so clusters form.
  var cats = D.cats.map(function (c) { return c.slug; }), anchor = {};
  cats.forEach(function (c, i) { var a = i / cats.length * Math.PI * 2; anchor[c] = { x: Math.cos(a) * 260, y: Math.sin(a) * 260 }; });

  var on = {}; cats.forEach(function (c) { on[c] = true; });
  var params = new URLSearchParams(location.search);
  if (params.get("cat") && anchor[params.get("cat")]) { cats.forEach(function (c) { on[c] = c === params.get("cat"); }); }
  var sel = params.get("focus") ? byId[params.get("focus")] || null : null, hover = null, query = "";
  var W = 0, H = 0, dpr = 1, view = { x: 0, y: 0, k: 1 }, alpha = 1, fitted = false;

  function visible(n) { return on[n.c] !== false; }
  function resize() {
    var r = cv.getBoundingClientRect(); dpr = Math.min(window.devicePixelRatio || 1, 2);
    W = r.width; H = r.height; cv.width = W * dpr; cv.height = H * dpr; draw();
  }
  function tick() {
    var vis = nodes.filter(visible), i, j, a, b, dx, dy, d2, f;
    for (i = 0; i < vis.length; i++) for (j = i + 1; j < vis.length; j++) {
      a = vis[i]; b = vis[j]; dx = b.x - a.x; dy = b.y - a.y; d2 = dx * dx + dy * dy + 0.01;
      if (d2 > 90000) continue;
      f = 700 / d2 * alpha; a.vx -= dx * f; a.vy -= dy * f; b.vx += dx * f; b.vy += dy * f;
    }
    links.forEach(function (l) {
      if (!visible(l.s) || !visible(l.t)) return;
      dx = l.t.x - l.s.x; dy = l.t.y - l.s.y; var d = Math.sqrt(dx * dx + dy * dy) || 1;
      f = (d - 45) / d * 0.02 * alpha; l.s.vx += dx * f; l.s.vy += dy * f; l.t.vx -= dx * f; l.t.vy -= dy * f;
    });
    vis.forEach(function (n) {
      var an = anchor[n.c] || { x: 0, y: 0 };
      n.vx += (an.x - n.x) * 0.012 * alpha; n.vy += (an.y - n.y) * 0.012 * alpha;
      if (n === drag) { n.vx = n.vy = 0; return; }
      n.vx *= 0.6; n.vy *= 0.6; n.x += n.vx; n.y += n.vy;
    });
    alpha = Math.max(alpha * 0.985, 0.02);
  }
  function fit() {
    var vis = nodes.filter(visible); if (!vis.length) return;
    // Fit to the 3rd-97th percentile so a few stragglers do not shrink the whole graph.
    var xs = vis.map(function (n) { return n.x; }).sort(function (a, b) { return a - b; });
    var ys = vis.map(function (n) { return n.y; }).sort(function (a, b) { return a - b; });
    var lo = Math.floor(vis.length * 0.03), hi = Math.ceil(vis.length * 0.97) - 1;
    var x0 = xs[lo], x1 = xs[hi], y0 = ys[lo], y1 = ys[hi];
    view.k = Math.min(W / (x1 - x0 + 80), H / (y1 - y0 + 80), 2.5);
    view.x = W / 2 - (x0 + x1) / 2 * view.k; view.y = H / 2 - (y0 + y1) / 2 * view.k;
  }
  function focusSet() {
    var f = hover || sel; if (!f) return null;
    var s = {}; s[f.id] = 1; for (var k in f.nb) s[k] = 1; return s;
  }
  function matches(n) { return query && n.t.toLowerCase().indexOf(query) >= 0; }
  function draw() {
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0); ctx.clearRect(0, 0, W, H);
    ctx.save(); ctx.translate(view.x, view.y); ctx.scale(view.k, view.k);
    var fs = focusSet(), dim = fs || query;
    links.forEach(function (l) {
      if (!visible(l.s) || !visible(l.t)) return;
      var hot = fs && fs[l.s.id] && fs[l.t.id] && (l.s === (hover || sel) || l.t === (hover || sel));
      ctx.strokeStyle = hot ? "rgba(242,181,68,.85)" : dim ? "rgba(181,172,154,.06)" : "rgba(181,172,154,.16)";
      ctx.lineWidth = (hot ? 1.6 : 0.7) / view.k;
      ctx.beginPath(); ctx.moveTo(l.s.x, l.s.y); ctx.lineTo(l.t.x, l.t.y); ctx.stroke();
    });
    nodes.forEach(function (n) {
      if (!visible(n)) return;
      var lit = fs ? fs[n.id] : query ? matches(n) : true;
      ctx.globalAlpha = lit ? 1 : 0.18;
      ctx.fillStyle = col[n.c] || "#B5AC9A";
      ctx.beginPath(); ctx.arc(n.x, n.y, n.r, 0, 6.2832); ctx.fill();
      if (n === sel || n === hover || matches(n)) { ctx.strokeStyle = "#ECE6D8"; ctx.lineWidth = 1.5 / view.k; ctx.stroke(); }
    });
    ctx.globalAlpha = 1;
    // Labels: big nodes, focused neighbourhood, search hits.
    ctx.textAlign = "center"; ctx.textBaseline = "top";
    nodes.forEach(function (n) {
      if (!visible(n)) return;
      var show = fs ? fs[n.id] : query ? matches(n) : (n.deg >= (W < 700 ? 30 : 18) || view.k > (W < 700 ? 2.2 : 1.6));
      if (!show) return;
      var size = (n === hover || n === sel ? 14 : 11) / view.k;
      ctx.font = (n === hover || n === sel ? "600 " : "300 ") + size + "px Fraunces, Georgia, serif";
      ctx.lineWidth = 3 / view.k; ctx.strokeStyle = "#14120F"; ctx.fillStyle = n === hover || n === sel ? "#F2B544" : "#ECE6D8";
      ctx.strokeText(n.t, n.x, n.y + n.r + 2 / view.k); ctx.fillText(n.t, n.x, n.y + n.r + 2 / view.k);
    });
    ctx.restore();
  }
  function loop() {
    if (alpha > 0.021 || drag) { tick(); if (!fitted && alpha < 0.3) { fit(); fitted = true; } }
    draw(); requestAnimationFrame(loop);
  }
  function toWorld(px, py) { return { x: (px - view.x) / view.k, y: (py - view.y) / view.k }; }
  function pick(px, py) {
    var p = toWorld(px, py), best = null, bd = (14 / view.k) * (14 / view.k);
    nodes.forEach(function (n) {
      if (!visible(n)) return; var dx = n.x - p.x, dy = n.y - p.y, d = dx * dx + dy * dy;
      if (d < Math.max(bd, n.r * n.r) && (!best || d < best.d)) best = { n: n, d: d };
    });
    return best && best.n;
  }
  function showTip(n, px, py) {
    if (!n) { tip.hidden = true; return; }
    tip.hidden = false;
    tip.innerHTML = "";
    var t = document.createElement("strong"); t.textContent = n.t;
    var m = document.createElement("span"); m.textContent = (title[n.c] || n.c) + " · " + n.deg + " links";
    tip.appendChild(t); tip.appendChild(m);
    tip.style.left = Math.min(px + 12, W - 220) + "px"; tip.style.top = (py + 12) + "px";
  }
  // Pointer handling: pan, drag, pinch, tap.
  var pts = {}, drag = null, panStart = null, pinch = null, moved = false, isTouch = false;
  cv.addEventListener("pointerdown", function (e) {
    cv.setPointerCapture(e.pointerId); isTouch = e.pointerType !== "mouse";
    var r = cv.getBoundingClientRect(); pts[e.pointerId] = { x: e.clientX - r.left, y: e.clientY - r.top };
    moved = false; var ids = Object.keys(pts);
    if (ids.length === 2) {
      var a = pts[ids[0]], b = pts[ids[1]]; drag = null;
      pinch = { d: Math.hypot(a.x - b.x, a.y - b.y), k: view.k, cx: (a.x + b.x) / 2, cy: (a.y + b.y) / 2, vx: view.x, vy: view.y }; return;
    }
    var p = pts[e.pointerId], n = pick(p.x, p.y);
    if (n) { drag = n; } else { panStart = { x: p.x, y: p.y, vx: view.x, vy: view.y }; }
  });
  cv.addEventListener("pointermove", function (e) {
    var r = cv.getBoundingClientRect(), px = e.clientX - r.left, py = e.clientY - r.top;
    if (pts[e.pointerId]) {
      var p0 = pts[e.pointerId]; if (Math.hypot(px - p0.x, py - p0.y) > 4) moved = true;
      pts[e.pointerId] = { x: px, y: py };
    }
    if (pinch) {
      var ids = Object.keys(pts); if (ids.length < 2) return;
      var a = pts[ids[0]], b = pts[ids[1]], k = Math.max(0.2, Math.min(6, pinch.k * Math.hypot(a.x - b.x, a.y - b.y) / pinch.d));
      view.x = pinch.cx - (pinch.cx - pinch.vx) * k / pinch.k; view.y = pinch.cy - (pinch.cy - pinch.vy) * k / pinch.k; view.k = k; return;
    }
    if (drag && moved) { var w = toWorld(px, py); drag.x = w.x; drag.y = w.y; alpha = Math.max(alpha, 0.3); return; }
    if (panStart && moved) { view.x = panStart.vx + px - panStart.x; view.y = panStart.vy + py - panStart.y; return; }
    if (!isTouch && !pts[e.pointerId]) { hover = pick(px, py); cv.style.cursor = hover ? "pointer" : "grab"; showTip(hover, px, py); }
  });
  function up(e) {
    var p = pts[e.pointerId]; delete pts[e.pointerId];
    if (pinch) { if (Object.keys(pts).length < 2) pinch = null; drag = null; panStart = null; return; }
    if (!moved && p) {
      var n = pick(p.x, p.y);
      if (n && (!isTouch || sel === n)) { location.href = n.id; }
      else { sel = n || null; showTip(sel, p.x, p.y); }
    }
    drag = null; panStart = null;
  }
  cv.addEventListener("pointerup", up); cv.addEventListener("pointercancel", up);
  cv.addEventListener("pointerleave", function () { if (!isTouch) { hover = null; tip.hidden = true; } });
  cv.addEventListener("wheel", function (e) {
    e.preventDefault(); var r = cv.getBoundingClientRect(), px = e.clientX - r.left, py = e.clientY - r.top;
    var k = Math.max(0.2, Math.min(6, view.k * Math.exp(-e.deltaY * 0.0015)));
    view.x = px - (px - view.x) * k / view.k; view.y = py - (py - view.y) * k / view.k; view.k = k;
  }, { passive: false });
  // Search + filters.
  q.addEventListener("input", function () {
    query = q.value.trim().toLowerCase(); sel = null;
    var hits = query ? nodes.filter(function (n) { return visible(n) && matches(n); }) : [];
    if (hits.length === 1) sel = hits[0];
  });
  q.addEventListener("keydown", function (e) {
    if (e.key === "Enter") { var h = nodes.filter(function (n) { return visible(n) && matches(n); }); if (h[0]) location.href = h[0].id; }
  });
  var btns = document.querySelectorAll("#kg-cats button");
  function syncBtns() { btns.forEach(function (b) { b.setAttribute("aria-pressed", on[b.dataset.cat] ? "true" : "false"); }); }
  btns.forEach(function (b) {
    b.addEventListener("click", function () {
      var c = b.dataset.cat, all = cats.every(function (x) { return on[x]; }), only = cats.every(function (x) { return on[x] === (x === c); });
      if (all) cats.forEach(function (x) { on[x] = x === c; });      // first click isolates a category
      else if (only) cats.forEach(function (x) { on[x] = true; });    // clicking the isolated one restores all
      else on[c] = !on[c];
      sel = null; alpha = Math.max(alpha, 0.5); fitted = false; syncBtns();
      var u = new URL(location.href); u.searchParams.delete("focus");
      if (cats.filter(function (x) { return on[x]; }).length === 1) u.searchParams.set("cat", c); else u.searchParams.delete("cat");
      history.replaceState(null, "", u);
    });
  });
  syncBtns();
  window.addEventListener("resize", function () { resize(); fit(); });
  resize();
  for (var i = 0; i < 220; i++) tick();  // pre-settle so the first frame is calm
  fit(); fitted = true; alpha = 0.15;
  if (sel) { view.k = 1.8; view.x = W / 2 - sel.x * view.k; view.y = H / 2 - sel.y * view.k; }
  requestAnimationFrame(loop);
})();
