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
  const api = async p => { try { return await (await fetch(site.url + p)).json(); } catch { return []; } };
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
  const r = spawnSync('wget', ['--recursive', '--level=2', '--page-requisites', '--convert-links', '--adjust-extension', '--no-host-directories',
    '--no-verbose', '-e', 'robots=off', '--reject-regex', '(wp-admin|wp-login|wp-json|xmlrpc|feed|/cart|/checkout|/my-account|add-to-cart|[?&](p|page_id|orderby|filter_[a-z_]+|_wpnonce|replytocom|s|add-to-cart|post_type)=)',
    '--content-on-error', '-P', out, '-i', seedFile], { encoding: 'utf8', maxBuffer: 1 << 26 });
  if (r.status !== 0 && r.status !== 8) console.log('wget exit', r.status, (r.stderr || '').slice(-400));

  // 404 page: wget saved it under the seed path.
  const nf = path.join(out, 'zz-static-404', 'index.html');
  if (fs.existsSync(nf)) { fs.renameSync(nf, path.join(out, '404.html')); fs.rmSync(path.dirname(nf), { recursive: true, force: true }); }

  // Rewrite remaining absolute URLs (JSON blobs, srcset) and add the demo bar.
  const origin = site.url.replace(/\/$/, '');
  const esc = origin.replace(/[.*+?^${}()|[\]\\/]/g, '\\$&');
  const playground = `https://playground.wordpress.net/?blueprint-url=${encodeURIComponent(`https://raw.githubusercontent.com/${REPO}/main/demos/${slug}/blueprint.json`)}`;
  const bar = `<div style="position:relative;z-index:99999;background:#111;color:#fff;font:14px/1.4 system-ui,sans-serif;padding:8px 16px;display:flex;gap:16px;flex-wrap:wrap;justify-content:space-between"><span>Static demo of the <strong>${slug}</strong> block theme. Forms, cart and search need the live version.</span><span><a style="color:#fff" href="${playground}">Open live in WordPress Playground</a> &middot; <a style="color:#fff" href="https://github.com/${REPO}/tree/main/themes/${slug}">Download the theme</a></span></div>`;
  let n = 0;
  const walk = d => { for (const f of fs.readdirSync(d)) { const p = path.join(d, f); if (fs.statSync(p).isDirectory()) walk(p); else if (/\.(html|css|js|json|xml)$/.test(f)) {
    let s = fs.readFileSync(p, 'utf8');
    const before = s;
    s = s.replace(new RegExp(esc.replace(/\\\//g, '\\\\?\\/'), 'g'), '').replace(new RegExp(esc, 'g'), '');
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
