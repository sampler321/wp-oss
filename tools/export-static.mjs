// Export a theme's demo site as static HTML for Cloudflare Pages.
// Usage: node tools/export-static.mjs <slug>   ->  dist/<slug>/
import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { startSite, ROOT } from './lib/playground.mjs';

const slug = process.argv[2];
const REPO = process.env.WPOSS_REPO || 'sampler321/wp-oss';
if (!slug) { console.error('usage: export-static.mjs <slug>'); process.exit(1); }
const out = path.join(ROOT, 'dist', slug);
fs.rmSync(out, { recursive: true, force: true });
fs.mkdirSync(out, { recursive: true });

const site = await startSite(slug, { port: 10000 + Math.floor(Math.random() * 500) });
try {
  const demo = JSON.parse(fs.readFileSync(path.join(ROOT, 'demos', slug, 'content.json'), 'utf8'));
  const api = async p => { try { return await (await fetch(site.url + p, { signal: AbortSignal.timeout(90000) })).json(); } catch { return []; } };
  const seeds = new Set(['/', ...(demo.nav || []).map(n => n.url)]);
  for (const t of ['pages', 'posts', 'categories', 'tags']) for (const x of await api(`/wp-json/wp/v2/${t}?per_page=100&_fields=link`)) if (x.link) seeds.add(new URL(x.link).pathname);
  if (demo.products?.length) {
    seeds.add('/shop/');
    for (const x of await api('/wp-json/wc/store/v1/products?per_page=100')) if (x.permalink) seeds.add(new URL(x.permalink).pathname);
  }
  for (const s of [...seeds]) if (/^\/(cart|checkout|my-account)\//.test(s)) seeds.delete(s);
  seeds.add('/zz-static-404/');
  const seedFile = path.join(ROOT, '.cache', `seeds-${slug}.txt`);
  fs.writeFileSync(seedFile, [...seeds].map(s => site.url + s).join('\n'));
  const r = spawnSync('wget', ['--timeout=60', '--tries=2', '--recursive', '--level=2', '--page-requisites', '--convert-links', '--adjust-extension', '--no-host-directories',
    '--no-verbose', '-e', 'robots=off', '--reject-regex', '(wp-admin|wp-login|wp-json|xmlrpc|feed|/cart|/checkout|/my-account|add-to-cart|[?&](p|page_id|orderby|filter_[a-z_]+|_wpnonce|replytocom|s|add-to-cart|post_type)=)',
    '--content-on-error', '-P', out, '-i', seedFile], { encoding: 'utf8', maxBuffer: 1 << 26, timeout: 10 * 60 * 1000, killSignal: 'SIGKILL' });
  if (r.error) console.log('wget hit the 10 min cap; continuing with what was fetched');
  if (r.status !== 0 && r.status !== 8) console.log('wget exit', r.status, (r.stderr || '').slice(-400));

  // 404 page: wget saved it under the seed path.
  const nf = path.join(out, 'zz-static-404', 'index.html');
  if (fs.existsSync(nf)) { fs.renameSync(nf, path.join(out, '404.html')); fs.rmSync(path.dirname(nf), { recursive: true, force: true }); }

  // Fix versioned asset names: wget saves `style.min.css?ver=7.1.2` as `style.min.css?ver=7.1.2.css`,
  // but static hosts ignore the query string and look for `style.min.css`.
  const walkFiles = (d, acc = []) => { for (const f of fs.readdirSync(d)) { const p = path.join(d, f); fs.statSync(p).isDirectory() ? walkFiles(p, acc) : acc.push(p); } return acc; };
  for (const f of walkFiles(out)) {
    const base = path.basename(f);
    if (!base.includes('?')) continue;
    const clean = path.join(path.dirname(f), base.split('?')[0]);
    if (!fs.existsSync(clean)) fs.renameSync(f, clean); else fs.unlinkSync(f);
  }
  // Fetch assets that wget can't discover: script modules in import maps, their imports, lazy CSS and fonts.
  const assetRe = /(?:["'(=]|\\\/)(\/(?:wp-includes|wp-content)\/[^"'()\s?#\\]+\.(?:js|mjs|css|woff2?|ttf|svg|png|jpe?g|webp|gif))/g;
  for (let pass = 0; pass < 4; pass++) {
    const missing = new Set();
    for (const f of walkFiles(out)) {
      if (!/\.(html|js|mjs|css|json)$/.test(f)) continue;
      const txt = fs.readFileSync(f, 'utf8').replace(/\\\//g, '/').split(site.url.replace(/\/$/, '')).join('');
      for (const m of txt.matchAll(assetRe)) { const rel = m[1]; if (!fs.existsSync(path.join(out, rel))) missing.add(rel); }
      // Relative module imports inside JS files: import ... from "./x.js" / "../y.min.js"
      if (/\.m?js$/.test(f)) for (const m of txt.matchAll(/(?:from|import)\s*\(?\s*["'](\.{1,2}\/[^"']+\.m?js)["']/g)) {
        const rel = '/' + path.relative(out, path.resolve(path.dirname(f), m[1])).split(path.sep).join('/');
        if (!fs.existsSync(path.join(out, rel))) missing.add(rel);
      }
    }
    if (!missing.size) break;
    let got = 0;
    for (const rel of missing) {
      try {
        const r = await fetch(site.url + rel, { signal: AbortSignal.timeout(30000) });
        if (!r.ok) continue;
        const dest = path.join(out, rel);
        fs.mkdirSync(path.dirname(dest), { recursive: true });
        fs.writeFileSync(dest, Buffer.from(await r.arrayBuffer()));
        got++;
      } catch {}
    }
    console.log(`asset pass ${pass + 1}: ${got} of ${missing.size} missing assets fetched`);
    if (!got) break;
  }

  // Rewrite remaining absolute URLs (JSON blobs, srcset) and add the demo bar.
  const origin = site.url.replace(/\/$/, '');
  const esc = origin.replace(/[.*+?^${}()|[\]\\/]/g, '\\$&');
  const playground = `https://playground.wordpress.net/?blueprint-url=${encodeURIComponent(`https://raw.githubusercontent.com/${REPO}/main/demos/${slug}/blueprint.json`)}`;
  const bar = `<div style="position:relative;z-index:99999;background:#111;color:#fff;font:14px/1.4 system-ui,sans-serif;padding:8px 16px;display:flex;gap:16px;flex-wrap:wrap;justify-content:space-between"><span>Static demo of the <strong>${slug}</strong> block theme. Forms, cart and search need the live version.</span><span style="display:flex;gap:16px;flex-wrap:wrap"><a style="color:#fff" href="${playground}">Open live in WordPress Playground</a><a style="color:#fff" href="https://github.com/${REPO}/tree/main/themes/${slug}">Download the theme</a></span></div>`;
  let n = 0;
  const walk = d => { for (const f of fs.readdirSync(d)) { const p = path.join(d, f); if (fs.statSync(p).isDirectory()) walk(p); else if (/\.(html|css|js|json|xml)$/.test(f)) {
    let s = fs.readFileSync(p, 'utf8');
    const before = s;
    s = s.replace(new RegExp(esc.replace(/\\\//g, '\\\\?\\/'), 'g'), '').replace(new RegExp(esc, 'g'), '');
    s = s.replace(/(\.(?:css|js|mjs))%3F[^"'\s)<>]*/g, '$1');
    // wget's link conversion turns duotone filter refs url(#wp-duotone-x) into url(index.html); restore them.
    s = s.replace(/(--wp--preset--duotone--([\w-]+):\s*)url\([^)]*\)/g, '$1url(#wp-duotone-$2)');
    if (f.endsWith('.html')) s = s.replace(/<body([^>]*)>/, `<body$1>${bar}`);
    if (s !== before) { fs.writeFileSync(p, s); n++; }
  } } };
  walk(out);
  fs.writeFileSync(path.join(out, '_headers'), '/*\n  X-Robots-Tag: noindex\n  Cache-Control: public, max-age=3600\n');
  const count = spawnSync('find', [out, '-name', '*.html'], { encoding: 'utf8' }).stdout.trim().split('\n').length;
  console.log(`exported ${slug}: ${count} html pages, ${n} files rewritten -> dist/${slug}`);
} finally {
  await site.stop();
}
