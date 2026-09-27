// Fetch CC0 / public-domain demo images from Wikimedia Commons into a theme.
// Usage: node tools/fetch-images.mjs <slug> "<name>=<search query>[|pick=2][|minWidth=1000][|orient=landscape|portrait|square]" ...
//   name:  output file (assets/images/<name>.jpg)
//   pick:  take the Nth acceptable result (1-based), to avoid near-duplicates or a bad first hit
//   query: plain words; the tool restricts to bitmaps licensed CC0 or public domain
// Output: themes/<slug>/assets/images/<name>.jpg (max 1600px, JPEG q78); credits in themes/<slug>/.images.json
// ALWAYS look at every downloaded image (Read tool) and re-fetch with pick=N or a new query if it doesn't fit.
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const UA = 'wp-oss-theme-builder/1.0 (https://github.com/sampler321/wp-oss)';
const [slug, ...specs] = process.argv.slice(2);
if (!slug || !specs.length) { console.error('usage: fetch-images.mjs <slug> "<name>=<query>" ...'); process.exit(1); }
const themeDir = path.resolve(import.meta.dirname, '..', 'themes', slug);
const imgDir = path.join(themeDir, 'assets', 'images');
fs.mkdirSync(imgDir, { recursive: true });
const creditsPath = path.join(themeDir, '.images.json');
const credits = fs.existsSync(creditsPath) ? JSON.parse(fs.readFileSync(creditsPath, 'utf8')) : {};
const sleep = ms => new Promise(r => setTimeout(r, ms));
const strip = s => (s || '').replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim();
const FREE = /^(cc0|public domain|pd|pdm|no restrictions)/i;

async function search(q, extra) {
  const params = new URLSearchParams({ action: 'query', format: 'json', generator: 'search', gsrnamespace: '6', gsrlimit: '50',
    gsrsearch: `${q} filetype:bitmap ${extra}`.trim(), prop: 'imageinfo', iiprop: 'url|size|extmetadata|mime', iiurlwidth: '1600' });
  for (let tries = 0; tries < 4; tries++) {
    const r = await fetch(`https://commons.wikimedia.org/w/api.php?${params}`, { headers: { 'User-Agent': UA } });
    if (r.status === 429 || r.status >= 500) { await sleep(3000 * (tries + 1)); continue; }
    const d = await r.json();
    const pages = Object.values(d.query?.pages || {}).sort((a, b) => a.index - b.index);
    return pages.map(p => ({ title: p.title, ...p.imageinfo?.[0] })).filter(x => x.extmetadata);
  }
  return [];
}

for (const spec of specs) {
  const [name, rest] = spec.split(/=(.*)/s);
  const [query, ...opts] = rest.split('|');
  const o = Object.fromEntries(opts.map(x => x.split('=')));
  const minW = +(o.minWidth || 1000), pick = +(o.pick || 1), orient = o.orient;
  const ok = x => {
    const lic = x.extmetadata.LicenseShortName?.value || '';
    if (!FREE.test(lic) || !/jpeg|png|webp/.test(x.mime || '')) return false;
    if ((x.width || 0) < minW) return false;
    const r = x.width / x.height;
    if (orient === 'landscape' && r < 1.15) return false;
    if (orient === 'portrait' && r > 0.9) return false;
    if (orient === 'square' && (r < 0.8 || r > 1.25)) return false;
    return true;
  };
  let results = (await search(query, 'incategory:CC-zero')).filter(ok);
  if (results.length < pick) results.push(...(await search(query, '')).filter(ok).filter(x => !results.some(y => y.title === x.title)));
  const hit = results[pick - 1];
  if (!hit) { console.log(`MISS ${name}: "${query}"`); continue; }
  const tmp = path.join(imgDir, `.${name}.src`);
  try {
    const img = await fetch(hit.thumburl || hit.url, { headers: { 'User-Agent': UA } });
    if (!img.ok) throw new Error(`HTTP ${img.status}`);
    fs.writeFileSync(tmp, Buffer.from(await img.arrayBuffer()));
    const out = path.join(imgDir, `${name}.jpg`);
    // Resize to 1600px and compress progressively until under ~560KB.
    execFileSync('python3', ['-c', `
import os,sys
from PIL import Image
src,out=sys.argv[1],sys.argv[2]
im=Image.open(src).convert('RGB'); im.thumbnail((1600,1600))
for q in (74,68,62,56,50):
    im.save(out,'JPEG',quality=q,optimize=True,progressive=True)
    if os.path.getsize(out)<560*1024: break
`, tmp, out], { stdio: 'ignore' });
    fs.unlinkSync(tmp);
    const m = hit.extmetadata;
    credits[name] = { title: hit.title.replace(/^File:/, ''), creator: strip(m.Artist?.value) || 'unknown', license: m.LicenseShortName?.value, source: 'Wikimedia Commons', url: hit.descriptionurl, query };
    console.log(`ok   ${name}: ${hit.title.slice(5, 70)} [${m.LicenseShortName?.value}] ${hit.width}x${hit.height}`);
  } catch (e) {
    if (fs.existsSync(tmp)) fs.unlinkSync(tmp);
    console.log(`ERR  ${name}: ${e.message}`);
  }
  await sleep(400);
}
fs.writeFileSync(creditsPath, JSON.stringify(credits, null, 2));
