// Build dist/_gallery: an index of every theme with its screenshot, brief, and demo links. Deploy with deploy.mjs _gallery.
// Usage: node tools/make-gallery.mjs
import fs from 'node:fs';
import path from 'node:path';

const ROOT = path.resolve(import.meta.dirname, '..');
const REPO = 'sampler321/wp-oss';
const out = path.join(ROOT, 'dist', '_gallery');
fs.rmSync(out, { recursive: true, force: true });
fs.mkdirSync(path.join(out, 'shots'), { recursive: true });
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;');

const rows = fs.readFileSync(path.join(ROOT, 'BUILD-STATUS.md'), 'utf8').split('\n')
  .map(l => l.split('|').map(c => c.trim())).filter(c => c.length > 7 && /^\d+$/.test(c[1]));
const items = rows.map(c => {
  const slug = c[2];
  const dir = path.join(ROOT, 'themes', slug);
  const css = fs.existsSync(path.join(dir, 'style.css')) ? fs.readFileSync(path.join(dir, 'style.css'), 'utf8') : '';
  const h = k => (css.match(new RegExp(`^${k}:\\s*(.+)$`, 'm')) || [])[1]?.trim() || '';
  const dep = path.join(ROOT, 'demos', slug, 'deploy.json');
  const url = fs.existsSync(dep) ? JSON.parse(fs.readFileSync(dep, 'utf8')).url : '';
  let shot = '';
  if (fs.existsSync(path.join(dir, 'screenshot.png'))) { fs.copyFileSync(path.join(dir, 'screenshot.png'), path.join(out, 'shots', `${slug}.png`)); shot = `shots/${slug}.png`; }
  return { n: c[1], slug, idea: c[3], brief: c[4], name: h('Theme Name') || slug, desc: h('Description'), url, shot };
}).filter(i => i.url);

const playground = s => `https://playground.wordpress.net/?blueprint-url=${encodeURIComponent(`https://raw.githubusercontent.com/${REPO}/main/demos/${s}/blueprint.json`)}`;
const cards = items.map(i => `
  <article>
    <a class="shot" href="${esc(i.url)}"><img src="${esc(i.shot)}" alt="Home page of the ${esc(i.name)} theme" loading="lazy" width="1200" height="900"></a>
    <p class="kind">${esc(i.idea.replace(/^\S+\s*/, ''))}</p>
    <h2><a href="${esc(i.url)}">${esc(i.name)}</a></h2>
    <p>${esc(i.desc)}</p>
    ${i.brief && i.brief !== 'as researched' ? `<p class="brief">Brief: ${esc(i.brief)}</p>` : ''}
    <p class="links"><a href="${esc(i.url)}">Demo</a> <a href="${esc(playground(i.slug))}">Try in Playground</a> <a href="https://github.com/${REPO}/tree/main/themes/${esc(i.slug)}">Source</a></p>
  </article>`).join('');

const html = `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>WP-OSS block themes</title>
<meta name="description" content="${items.length} open-source WordPress block themes for independent businesses and creatives. Core blocks only, every style in theme.json.">
<style>
:root{--bg:#f2f2ee;--ink:#111;--line:#111;--muted:#55554f;--accent:#1f3bff}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#111;--ink:#f2f2ee;--line:#f2f2ee;--muted:#a8a8a0;--accent:#8a9bff}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.5 ui-sans-serif,-apple-system,"Helvetica Neue",Arial,sans-serif}
a{color:inherit}a:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
header{padding:48px 16px 24px;border-bottom:2px solid var(--line);max-width:1400px;margin:0 auto}
h1{font-size:clamp(40px,8vw,112px);line-height:.92;letter-spacing:-.03em;margin:0 0 16px;font-weight:800}
header p{max-width:60ch;margin:0 0 8px}.meta{font-size:14px;color:var(--muted)}
main{max-width:1400px;margin:0 auto;padding:0 16px 80px;display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:0 24px}
article{border-bottom:1px solid var(--line);padding:24px 0}
.shot{display:block;border:1px solid var(--line);aspect-ratio:4/3;overflow:hidden;background:#ddd}
.shot img{width:100%;height:100%;object-fit:cover;object-position:top;display:block}
.kind{font-size:14px;color:var(--muted);margin:12px 0 4px}
h2{font-size:24px;line-height:1.1;margin:0 0 8px;letter-spacing:-.01em}h2 a{text-decoration:none}
article p{margin:0 0 8px;font-size:15px}.brief{color:var(--muted);font-style:italic}
.links{display:flex;gap:16px;flex-wrap:wrap;font-size:14px;font-weight:600}
footer{max-width:1400px;margin:0 auto;padding:24px 16px 48px;border-top:2px solid var(--line);font-size:14px}
</style></head><body>
<header>
<h1>WP-OSS<br>block themes</h1>
<p>${items.length} free, open-source WordPress block themes for small businesses, makers and creatives. Every theme uses core blocks only, and every colour, font and size lives in theme.json, so it can all be changed in the Site Editor.</p>
<p class="meta">GPL-2.0-or-later, WordPress 6.7 or newer, source on <a href="https://github.com/${REPO}">github.com/${REPO}</a></p>
</header>
<main>${cards}
</main>
<footer>Demo sites are static snapshots. "Try in Playground" boots the real theme with its demo content in your browser, editor included. Demo images are CC0 or public domain, credited in each theme's readme.</footer>
</body></html>`;
fs.writeFileSync(path.join(out, 'index.html'), html);
fs.writeFileSync(path.join(out, '404.html'), html.replace(/<main>[\s\S]*<\/main>/, '<main><p>That page isn\'t here. The themes are listed on the <a href="/">index</a>.</p></main>'));
console.log(`gallery: ${items.length} themes -> dist/_gallery`);
