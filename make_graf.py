#!/usr/bin/env python3
"""Vygeneruje graf.html z price_log.csv — vývoj najnižšej ceny na osobu v čase.

Tri sledované metriky: Let 1 -> FLL, Let 1 -> MIA, Let 2 (MIA->LAS).
Spúšťa sa po každom skene: python3 make_graf.py
"""
import csv
import json
import os
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(BASE, "price_log.csv")
OUT = os.path.join(BASE, "graf.html")

SERIES = [
    ("Let 1 → FLL", "let1", "FLL", 100),   # (label, let, cieľové letisko, nákupný prah)
    ("Let 1 → MIA", "let1", "MIA", 150),
    ("Let 2 MIA → LAS", "let2", "LAS", 175),
]


def load_points():
    by_ts = {}
    with open(LOG, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            try:
                price = float(row["cena_usd_1os"])
            except (ValueError, KeyError):
                continue
            ts = row["timestamp"].strip()
            dest = row["trasa"].strip().split("-")[-1]
            key = None
            for label, let, target, _ in SERIES:
                if row["let"].strip() == let and dest == target:
                    key = label
                    break
            if key is None:
                continue
            cur = by_ts.setdefault(ts, {})
            detail = f'{row.get("aerolinka", "?")} {row.get("odlet", "")} {row.get("trasa", "")} ({row.get("prestupy", "")})'
            if key not in cur or price < cur[key][0]:
                cur[key] = (price, detail)
    return by_ts


def main():
    by_ts = load_points()
    timestamps = sorted(by_ts)
    data = {
        "timestamps": timestamps,
        "series": [
            {
                "label": label,
                "threshold": thr,
                "points": [
                    {"y": by_ts[ts][label][0], "d": by_ts[ts][label][1]} if label in by_ts[ts] else None
                    for ts in timestamps
                ],
            }
            for label, _, _, thr in SERIES
        ],
        "generated": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    html = TEMPLATE.replace("__DATA__", json.dumps(data, ensure_ascii=False))
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"graf.html: {len(timestamps)} skenov, {sum(1 for s in data['series'] for p in s['points'] if p)} bodov")


TEMPLATE = r"""<!doctype html>
<html lang="sk">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Letenky — vývoj cien</title>
<style>
  :root {
    --surface-1: #fcfcfb; --page: #f9f9f7;
    --ink-1: #0b0b0b; --ink-2: #52514e; --muted: #898781;
    --grid: #e1e0d9; --baseline: #c3c2b7; --border: rgba(11,11,11,0.10);
    --s1: #2a78d6; --s2: #1baf7a; --s3: #eda100;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --surface-1: #1a1a19; --page: #0d0d0d;
      --ink-1: #ffffff; --ink-2: #c3c2b7; --muted: #898781;
      --grid: #2c2c2a; --baseline: #383835; --border: rgba(255,255,255,0.10);
      --s1: #3987e5; --s2: #199e70; --s3: #c98500;
    }
  }
  * { box-sizing: border-box; }
  body { margin: 0; padding: 24px; background: var(--page); color: var(--ink-1);
         font-family: system-ui, -apple-system, "Segoe UI", sans-serif; }
  .card { max-width: 860px; margin: 0 auto; background: var(--surface-1);
          border: 1px solid var(--border); border-radius: 12px; padding: 20px 24px; }
  h1 { font-size: 17px; margin: 0 0 2px; }
  .sub { color: var(--ink-2); font-size: 13px; margin: 0 0 16px; }
  .legend { display: flex; gap: 18px; flex-wrap: wrap; font-size: 13px; color: var(--ink-2); margin-bottom: 8px; }
  .legend span { display: inline-flex; align-items: center; gap: 6px; }
  .swatch { width: 10px; height: 10px; border-radius: 3px; display: inline-block; }
  .chartwrap { position: relative; }
  svg { width: 100%; height: auto; display: block; }
  .tip { position: absolute; pointer-events: none; background: var(--surface-1);
         border: 1px solid var(--border); border-radius: 8px; padding: 8px 10px;
         font-size: 12px; color: var(--ink-1); box-shadow: 0 2px 10px rgba(0,0,0,.12);
         display: none; min-width: 180px; z-index: 2; }
  .tip .t { color: var(--muted); margin-bottom: 4px; }
  .tip .row { display: flex; justify-content: space-between; gap: 12px; }
  .tip .d { color: var(--ink-2); font-size: 11px; }
  details { margin-top: 14px; font-size: 13px; }
  summary { cursor: pointer; color: var(--ink-2); }
  table { border-collapse: collapse; width: 100%; margin-top: 8px; font-variant-numeric: tabular-nums; }
  th, td { text-align: left; padding: 5px 8px; border-bottom: 1px solid var(--grid); font-size: 12px; }
  th { color: var(--muted); font-weight: 600; }
  .empty { color: var(--muted); text-align: center; padding: 40px 0; font-size: 14px; }
</style>
</head>
<body>
<div class="card">
  <h1>Letenky — vývoj najnižšej ceny na osobu</h1>
  <p class="sub">NYC → Miami 30. 8. 2026 (po 19:00) &nbsp;·&nbsp; MIA → Las Vegas 5. 9. 2026 (po 13:00) &nbsp;·&nbsp; aktualizované: <span id="gen"></span></p>
  <div class="legend" id="legend"></div>
  <div class="chartwrap" id="wrap"><svg id="chart" viewBox="0 0 820 380" role="img" aria-label="Vývoj cien leteniek"></svg><div class="tip" id="tip"></div></div>
  <details><summary>Tabuľka hodnôt</summary><div id="tablewrap" style="overflow-x:auto"></div></details>
</div>
<script>
const DATA = __DATA__;
const COLORS = ['var(--s1)', 'var(--s2)', 'var(--s3)'];
document.getElementById('gen').textContent = DATA.generated;

const legend = document.getElementById('legend');
DATA.series.forEach((s, i) => {
  const el = document.createElement('span');
  el.innerHTML = `<span class="swatch" style="background:${COLORS[i]}"></span>${s.label}`;
  legend.appendChild(el);
});

const svg = document.getElementById('chart');
const NS = 'http://www.w3.org/2000/svg';
const W = 820, H = 380, M = {t: 16, r: 120, b: 42, l: 46};
const iw = W - M.l - M.r, ih = H - M.t - M.b;
const n = DATA.timestamps.length;

function el(tag, attrs, parent) {
  const e = document.createElementNS(NS, tag);
  for (const k in attrs) e.setAttribute(k, attrs[k]);
  (parent || svg).appendChild(e);
  return e;
}

if (n === 0) {
  document.getElementById('wrap').innerHTML = '<div class="empty">Zatiaľ žiadne dáta — graf sa naplní po prvých skenoch.</div>';
} else {
  const allY = DATA.series.flatMap(s => s.points.filter(Boolean).map(p => p.y))
    .concat(DATA.series.map(s => s.threshold));
  let yMin = Math.min(...allY), yMax = Math.max(...allY);
  const pad = Math.max(10, (yMax - yMin) * 0.12);
  yMin = Math.max(0, Math.floor((yMin - pad) / 10) * 10);
  yMax = Math.ceil((yMax + pad) / 10) * 10;

  const x = i => n === 1 ? M.l + iw / 2 : M.l + i * iw / (n - 1);
  const y = v => M.t + ih - (v - yMin) / (yMax - yMin) * ih;

  const step = Math.max(10, Math.ceil((yMax - yMin) / 5 / 10) * 10);
  for (let v = yMin; v <= yMax; v += step) {
    el('line', {x1: M.l, x2: W - M.r, y1: y(v), y2: y(v), stroke: 'var(--grid)', 'stroke-width': 1});
    el('text', {x: M.l - 8, y: y(v) + 4, 'text-anchor': 'end', 'font-size': 11, fill: 'var(--muted)'}).textContent = '$' + v;
  }
  el('line', {x1: M.l, x2: W - M.r, y1: y(yMin), y2: y(yMin), stroke: 'var(--baseline)', 'stroke-width': 1});

  const fmt = ts => { const d = new Date(ts); return (d.getDate()) + '.' + (d.getMonth() + 1) + '. ' + String(d.getHours()).padStart(2, '0') + ':' + String(d.getMinutes()).padStart(2, '0'); };
  const maxTicks = 7, tickEvery = Math.max(1, Math.ceil(n / maxTicks));
  DATA.timestamps.forEach((ts, i) => {
    if (i % tickEvery !== 0 && i !== n - 1) return;
    el('text', {x: x(i), y: H - M.b + 18, 'text-anchor': 'middle', 'font-size': 11, fill: 'var(--muted)'}).textContent = fmt(ts);
  });

  DATA.series.forEach((s, si) => {
    let d = '', started = false;
    s.points.forEach((p, i) => {
      if (!p) { started = false; return; }
      d += (started ? ' L' : ' M') + x(i).toFixed(1) + ' ' + y(p.y).toFixed(1);
      started = true;
    });
    if (d) el('path', {d, fill: 'none', stroke: COLORS[si], 'stroke-width': 2, 'stroke-linejoin': 'round', 'stroke-linecap': 'round'});
    s.points.forEach((p, i) => {
      if (p) el('circle', {cx: x(i), cy: y(p.y), r: 3.5, fill: COLORS[si], stroke: 'var(--surface-1)', 'stroke-width': 2});
    });
    let last = null;
    for (let i = n - 1; i >= 0; i--) if (s.points[i]) { last = i; break; }
    if (last !== null) {
      el('text', {x: x(last) + 10, y: y(s.points[last].y) + 4, 'font-size': 12, 'font-weight': 600, fill: 'var(--ink-1)'})
        .textContent = '$' + s.points[last].y + ' ' + s.label;
    }
  });

  const hover = el('line', {y1: M.t, y2: H - M.b, stroke: 'var(--baseline)', 'stroke-width': 1, 'stroke-dasharray': '3 3', visibility: 'hidden'});
  const tip = document.getElementById('tip');
  const wrap = document.getElementById('wrap');
  svg.addEventListener('mousemove', ev => {
    const r = svg.getBoundingClientRect();
    const px = (ev.clientX - r.left) * W / r.width;
    let best = 0, bd = 1e9;
    for (let i = 0; i < n; i++) { const dd = Math.abs(x(i) - px); if (dd < bd) { bd = dd; best = i; } }
    hover.setAttribute('x1', x(best)); hover.setAttribute('x2', x(best));
    hover.setAttribute('visibility', 'visible');
    let rows = '';
    DATA.series.forEach((s, si) => {
      const p = s.points[best];
      if (!p) return;
      rows += `<div class="row"><span><span class="swatch" style="background:${COLORS[si]}"></span> ${s.label}</span><b>$${p.y}</b></div><div class="d">${p.d}</div>`;
    });
    tip.innerHTML = `<div class="t">${fmt(DATA.timestamps[best])}</div>` + (rows || '<div class="d">bez dát</div>');
    tip.style.display = 'block';
    const wr = wrap.getBoundingClientRect();
    const lx = (x(best) / W) * wr.width;
    tip.style.left = Math.min(wr.width - 200, Math.max(0, lx + 12)) + 'px';
    tip.style.top = '20px';
  });
  svg.addEventListener('mouseleave', () => { tip.style.display = 'none'; hover.setAttribute('visibility', 'hidden'); });
}

let t = '<table><tr><th>Čas skenu</th>' + DATA.series.map(s => '<th>' + s.label + '</th>').join('') + '</tr>';
DATA.timestamps.forEach((ts, i) => {
  t += '<tr><td>' + ts.replace('T', ' ') + '</td>' + DATA.series.map(s => '<td>' + (s.points[i] ? '$' + s.points[i].y : '—') + '</td>').join('') + '</tr>';
});
t += '</table>';
document.getElementById('tablewrap').innerHTML = t;
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
