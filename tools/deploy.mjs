// Deploy dist/<slug> to Cloudflare (Workers static assets) with wrangler. Prints the live URL.
// Usage: node tools/deploy.mjs <slug>
import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';

const slug = process.argv[2];
const ROOT = path.resolve(import.meta.dirname, '..');
const dist = path.join(ROOT, 'dist', slug);
if (!fs.existsSync(path.join(dist, 'index.html'))) { console.error(`no dist/${slug}; run export-static first`); process.exit(1); }
const name = `wposs-${slug}`.toLowerCase().replace(/[^a-z0-9-]/g, '-');
const cfgDir = path.join(ROOT, '.cache', 'deploy', slug);
fs.mkdirSync(cfgDir, { recursive: true });
fs.writeFileSync(path.join(cfgDir, 'wrangler.jsonc'), JSON.stringify({
  name, compatibility_date: '2026-09-01',
  assets: { directory: dist, not_found_handling: '404-page', html_handling: 'auto-trailing-slash' },
  workers_dev: true, preview_urls: false,
}, null, 2));
const r = spawnSync('npx', ['--yes', 'wrangler@latest', 'deploy', '--config', path.join(cfgDir, 'wrangler.jsonc')], { cwd: cfgDir, encoding: 'utf8', maxBuffer: 1 << 26 });
const out = (r.stdout || '') + (r.stderr || '');
const url = (out.match(/https:\/\/[a-z0-9.-]+\.workers\.dev/) || [])[0];
if (r.status !== 0 || !url) { console.error(out.slice(-2000)); process.exit(1); }
const statusPath = path.join(ROOT, 'demos', slug, 'deploy.json');
fs.writeFileSync(statusPath, JSON.stringify({ slug, url, worker: name, date: new Date().toISOString() }, null, 2) + '\n');
console.log(url);
