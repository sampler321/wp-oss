// Download self-hosted fonts into a theme and print theme.json fontFamilies entries.
// Usage:
//   node tools/fetch-fonts.mjs <slug> "display=Bricolage Grotesque:opsz,wght@12..96,200..800" "mono=Sometype Mono:wght@400;500"
//   node tools/fetch-fonts.mjs <slug> "display=fontshare:gambarino@400"
// Each arg is <fontSlug>=<Google css2 family spec> or <fontSlug>=fontshare:<slug>@<weights comma-separated>.
// Writes themes/<slug>/assets/fonts/*.woff2 + licence files, and themes/<slug>/.fonts.json (fontFamilies array).
import fs from 'node:fs';
import path from 'node:path';

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36';
const [slug, ...specs] = process.argv.slice(2);
if (!slug || !specs.length) { console.error('usage: fetch-fonts.mjs <theme-slug> "<fontSlug>=<spec>" ...'); process.exit(1); }
const themeDir = path.resolve(import.meta.dirname, '..', 'themes', slug);
const fontDir = path.join(themeDir, 'assets', 'fonts');
fs.mkdirSync(fontDir, { recursive: true });

const get = async (url, bin = false) => {
  const r = await fetch(url, { headers: { 'User-Agent': UA } });
  if (!r.ok) throw new Error(`${r.status} ${url}`);
  return bin ? Buffer.from(await r.arrayBuffer()) : r.text();
};
const kebab = s => s.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');

// Parse @font-face blocks, keeping only the latin subset (Google marks subsets with a /* latin */ comment).
function parseFaces(css, latinOnly) {
  const faces = [];
  const re = /(\/\*\s*([\w-]+)\s*\*\/\s*)?@font-face\s*{([^}]+)}/g;
  let m;
  while ((m = re.exec(css))) {
    const subset = m[2];
    if (latinOnly && subset && !['latin', 'latin-ext'].includes(subset)) continue;
    const body = m[3];
    const prop = k => (body.match(new RegExp(`${k}:\\s*([^;]+);`)) || [])[1]?.trim();
    const src = (body.match(/url\(['"]?([^)'"]+)['"]?\)\s*format\(['"]?(woff2|woff)['"]?\)/) || [])[1];
    if (!src) continue;
    faces.push({ family: prop('font-family').replace(/['"]/g, ''), style: prop('font-style') || 'normal', weight: prop('font-weight') || '400', src: src.replace(/['"]/g, ''), stretch: prop('font-stretch'), unicodeRange: prop('unicode-range'), subset: subset || '' });
  }
  return faces;
}

const families = [];
const credits = [];
for (const spec of specs) {
  const [fontSlug, rest] = spec.split(/=(.*)/s);
  let css, source, licenceUrl, familyName;
  if (rest.startsWith('fontshare:')) {
    const [fs_slug, weights] = rest.slice(10).split('@');
    const q = `f[]=${fs_slug}@${weights || '400'}`;
    css = await get(`https://api.fontshare.com/v2/css?${q}&display=swap`);
    source = 'Fontshare'; licenceUrl = `https://www.fontshare.com/licenses/itf-ffl`;
    css = css.replace(/url\((['"]?)\/\//g, 'url($1https://');
  } else {
    familyName = rest.split(':')[0];
    css = await get(`https://fonts.googleapis.com/css2?family=${encodeURIComponent(rest).replace(/%20/g, '+').replace(/%3A/g, ':').replace(/%40/g, '@').replace(/%2C/g, ',').replace(/%3B/g, ';')}&display=swap`);
    source = 'Google Fonts';
  }
  const faces = parseFaces(css, source === 'Google Fonts');
  if (!faces.length) throw new Error(`no faces for ${spec}`);
  familyName = faces[0].family;
  // Merge faces that point at the same file (variable fonts served once per weight).
  const bySrc = new Map();
  for (const f of faces) {
    const k = f.src + f.style + (f.unicodeRange || '');
    if (!bySrc.has(k)) bySrc.set(k, { ...f, weights: [] });
    bySrc.get(k).weights.push(...f.weight.split(/\s+/).map(Number));
  }
  for (const f of bySrc.values()) { const lo = Math.min(...f.weights), hi = Math.max(...f.weights); f.weight = lo === hi ? String(lo) : `${lo} ${hi}`; }
  const fontFace = [];
  const seen = new Set();
  for (const f of bySrc.values()) {
    const file = `${kebab(familyName)}-${f.style}-${f.weight.replace(/\s+/g, '_')}${f.subset && f.subset !== 'latin' ? '-' + f.subset : ''}.woff2`;
    if (seen.has(file)) continue; seen.add(file);
    fs.writeFileSync(path.join(fontDir, file), await get(f.src, true));
    const face = { fontFamily: familyName, fontStyle: f.style, fontWeight: f.weight, src: [`file:./assets/fonts/${file}`] };
    if (f.stretch && f.stretch !== 'normal') face.fontStretch = f.stretch;
    if (f.unicodeRange && f.subset) face.unicodeRange = f.unicodeRange;
    fontFace.push(face);
  }
  // Licence file
  if (source === 'Google Fonts') {
    const dirName = familyName.toLowerCase().replace(/[^a-z0-9]/g, '');
    for (const lic of ['ofl', 'apache', 'ufl']) {
      try { const t = await get(`https://raw.githubusercontent.com/google/fonts/main/${lic}/${dirName}/${lic === 'ofl' ? 'OFL.txt' : 'LICENSE.txt'}`); fs.writeFileSync(path.join(fontDir, `${kebab(familyName)}-LICENSE.txt`), t); licenceUrl = `https://github.com/google/fonts/tree/main/${lic}/${dirName}`; break; } catch {}
    }
  } else {
    fs.writeFileSync(path.join(fontDir, `${kebab(familyName)}-LICENSE.txt`), `${familyName} is distributed by Indian Type Foundry via Fontshare under the ITF Free Font License.\n${licenceUrl}\n`);
  }
  const generic = /mono/i.test(familyName) || fontSlug === 'mono' ? 'monospace' : /serif|slab|caslon|garamond|bodoni|didone/i.test(familyName) && !/sans/i.test(familyName) ? 'serif' : 'sans-serif';
  families.push({ fontFamily: `"${familyName}", ${generic}`, name: familyName, slug: fontSlug, fontFace });
  credits.push(`${familyName} (${source}), ${licenceUrl || 'see licence file'}`);
  console.log(`ok ${fontSlug}: ${familyName} (${fontFace.length} faces)`);
}
fs.writeFileSync(path.join(themeDir, '.fonts.json'), JSON.stringify({ fontFamilies: families, credits }, null, 2));
console.log(`wrote themes/${slug}/.fonts.json`);
