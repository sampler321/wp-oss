// Test one theme against THEME-CONTRACT.md. Exit 0 = pass.
// Usage: node tools/test-theme.mjs <slug> [--static] [--no-shots]
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync, spawnSync } from 'node:child_process';
import Ajv from 'ajv';
import { chromium } from 'playwright';
import { startSite, ROOT } from './lib/playground.mjs';
import { openEditor, analyse, prepare, themeFiles } from './lib/editor.mjs';

const slug = process.argv[2];
const staticOnly = process.argv.includes('--static');
const noShots = process.argv.includes('--no-shots');
const quick = process.argv.includes('--quick'); // release mode: all checks, only screenshot.png
if (!slug) { console.error('usage: test-theme.mjs <slug> [--static] [--no-shots]'); process.exit(1); }
const dir = path.join(ROOT, 'themes', slug);
const demoDir = path.join(ROOT, 'demos', slug);
const results = [];
const check = (name, ok, detail = '') => { results.push({ name, ok, detail }); console.log(`${ok ? 'PASS' : 'FAIL'}  ${name}${detail ? '  ' + detail : ''}`); };
const warn = (name, detail) => { results.push({ name, ok: true, warn: true, detail }); console.log(`WARN  ${name}  ${detail}`); };
const read = f => fs.readFileSync(f, 'utf8');
const WOO_TEMPLATES = /^(archive-product|single-product|taxonomy-product_\w+|product-search-results|page-cart|page-checkout|order-confirmation|single-product-\w+)\.html$/;

// ---------------- static ----------------
const required = ['style.css', 'theme.json', 'readme.txt', 'templates/index.html', 'templates/front-page.html', 'templates/page.html', 'templates/single.html', 'templates/archive.html', 'templates/404.html', 'templates/search.html', 'parts/header.html', 'parts/footer.html'];
const missing = required.filter(f => !fs.existsSync(path.join(dir, f)));
check('required files', !missing.length, missing.join(', '));

const css = read(path.join(dir, 'style.css'));
const hdr = k => (css.match(new RegExp(`^${k}:\\s*(.+)$`, 'm')) || [])[1]?.trim();
const hdrMissing = ['Theme Name', 'Description', 'Version', 'Requires at least', 'Requires PHP', 'License', 'Text Domain'].filter(k => !hdr(k));
check('style.css header', !hdrMissing.length && hdr('Text Domain') === slug, hdrMissing.join(', ') || (hdr('Text Domain') !== slug ? `Text Domain ${hdr('Text Domain')} != ${slug}` : ''));
const cssRules = css.replace(/\/\*[\s\S]*?\*\//, '').trim();
check('style.css has no rules (styles live in theme.json)', !cssRules, cssRules.slice(0, 80));

const schemaPath = path.join(ROOT, '.cache', 'theme.schema.json');
if (!fs.existsSync(schemaPath)) execFileSync('curl', ['-sL', 'https://schemas.wp.org/trunk/theme.json', '-o', schemaPath]);
const ajv = new Ajv({ strict: false, allErrors: true });
const validate = ajv.compile(JSON.parse(read(schemaPath)));
const jsonFiles = ['theme.json', ...fs.readdirSync(path.join(dir, 'styles'), { recursive: true }).filter(f => f.endsWith('.json')).map(f => 'styles/' + f)];
const schemaErrors = [];
const jsonData = {};
for (const f of jsonFiles) {
  try {
    const d = JSON.parse(read(path.join(dir, f)));
    jsonData[f] = d;
    if (!validate(d)) schemaErrors.push(`${f}: ${validate.errors.slice(0, 2).map(e => `${e.instancePath} ${e.message}`).join('; ')}`);
  } catch (e) { schemaErrors.push(`${f}: ${e.message}`); }
}
check('theme.json + styles/*.json valid against schema', !schemaErrors.length, schemaErrors.slice(0, 4).join(' | '));

const tj = jsonData['theme.json'] || {};
const pal = Object.fromEntries((tj.settings?.color?.palette || []).map(c => [c.slug, c.color]));
const palMissing = ['base', 'contrast', 'accent', 'surface', 'line'].filter(s => !pal[s]);
check('palette has semantic slugs', !palMissing.length, palMissing.join(', '));
check('default palette/gradients/duotone off', tj.settings?.color?.defaultPalette === false && tj.settings?.color?.defaultGradients === false && tj.settings?.color?.defaultDuotone === false);
const fam = tj.settings?.typography?.fontFamilies || [];
const monoFams = Object.entries(jsonData).flatMap(([f, d]) => (d.settings?.typography?.fontFamilies || []).filter(x => /monospace|mono\b|\bcode\b|courier|typewriter/i.test(`${x.fontFamily} ${x.name} ${x.slug}`)).map(x => `${f}: ${x.name || x.slug}`));
const monoMarkup = themeFiles(dir).filter(f => /has-mono-font-family|font-family\|mono|"fontFamily":"mono"|monospace/.test(read(f))).map(f => path.relative(dir, f));
const monoCss = JSON.stringify(jsonData).match(/monospace|font-family\|mono/g);
check('no monospace fonts (AI tell)', !monoFams.length && !monoMarkup.length && !monoCss, [...monoFams, ...monoMarkup.slice(0, 4), monoCss ? 'theme.json styles reference mono' : ''].filter(Boolean).join(' | '));
check('font families display + body', ['display', 'body'].every(s => fam.some(f => f.slug === s)), fam.map(f => f.slug).join(','));
const fontSrcMissing = fam.flatMap(f => (f.fontFace || []).flatMap(ff => ff.src)).map(s => s.replace('file:./', '')).filter(s => !fs.existsSync(path.join(dir, s)));
const remoteFonts = fam.flatMap(f => (f.fontFace || []).flatMap(ff => ff.src)).filter(s => /^https?:/.test(s));
check('fonts self-hosted and present', !fontSrcMissing.length && !remoteFonts.length, [...fontSrcMissing, ...remoteFonts].join(', '));
const sizes = (tj.settings?.typography?.fontSizes || []).map(s => s.slug);
check('font size presets', ['small', 'medium', 'large', 'x-large'].every(s => sizes.includes(s)) && tj.settings?.typography?.defaultFontSizes === false, sizes.join(','));
const lb = tj.settings?.blocks?.['core/image']?.lightbox;
check('image lightbox enabled in theme.json (round 2)', lb?.enabled === true, JSON.stringify(lb || null));
check('spacing presets', (tj.settings?.spacing?.spacingSizes || []).length >= 6 && tj.settings?.spacing?.defaultSpacingSizes === false);

// Contrast across the base palette and every variation that defines a palette.
const lum = h => { const c = [1, 3, 5].map(i => parseInt(h.slice(i, i + 2), 16) / 255).map(x => x <= 0.03928 ? x / 12.92 : ((x + 0.055) / 1.055) ** 2.4); return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]; };
const ratio = (a, b) => { if (!/^#[0-9a-f]{6}$/i.test(a || '') || !/^#[0-9a-f]{6}$/i.test(b || '')) return 99; const x = lum(a), y = lum(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); };
const contrastFails = [];
for (const [f, d] of Object.entries(jsonData)) {
  if (f !== 'theme.json' && !d.settings?.color?.palette) continue;
  const p = { ...pal, ...Object.fromEntries((d.settings?.color?.palette || []).map(c => [c.slug, c.color])) };
  const pairs = [['contrast', 'base', 4.5], ['accent', 'base', 3], ['contrast', 'surface', 4.5]];
  if (p.muted) pairs.push(['muted', 'base', 4.5]);
  for (const [a, b, min] of pairs) { const r = ratio(p[a], p[b]); if (r < min) contrastFails.push(`${f}: ${a}/${b} ${r.toFixed(2)} < ${min}`); }
}
check('palette contrast (text 4.5:1, accent 3:1) in all variations', !contrastFails.length, contrastFails.slice(0, 4).join(' | '));

const variations = fs.readdirSync(path.join(dir, 'styles')).filter(f => f.endsWith('.json'));
const sections = fs.existsSync(path.join(dir, 'styles', 'sections')) ? fs.readdirSync(path.join(dir, 'styles', 'sections')).filter(f => f.endsWith('.json')) : [];
check('3+ style variations', variations.length >= 3, `${variations.length}`);
check('section styles', sections.length >= 1, `${sections.length}`);

const phpFiles = fs.readdirSync(dir, { recursive: true }).filter(f => f.endsWith('.php')).map(f => path.join(dir, f));
const phpErrors = phpFiles.map(f => ({ f, r: spawnSync('php', ['-l', f], { encoding: 'utf8' }) })).filter(x => x.r.status !== 0).map(x => path.relative(dir, x.f));
check('PHP lint', !phpErrors.length, phpErrors.join(', '));
const funcs = path.join(dir, 'functions.php');
if (fs.existsSync(funcs)) {
  const fx = read(funcs);
  check('functions.php has no enqueues or CPTs', !/wp_enqueue_style|wp_enqueue_script|register_post_type|register_taxonomy|register_block_type\(/.test(fx));
}

const files = themeFiles(dir);
const patterns = files.filter(f => f.includes('/patterns/'));
check('40+ patterns (round 2)', patterns.length >= 40, `${patterns.length}`);
const tablePatterns = patterns.filter(f => /<!-- wp:table/.test(read(f)));
check('tables in at most 20% of patterns (round 2)', tablePatterns.length <= Math.floor(patterns.length * 0.2), `${tablePatterns.length} of ${patterns.length}`);
const badHeaders = patterns.filter(f => { const h = read(f).slice(0, 600); return !/Title:/.test(h) || !new RegExp(`Slug:\\s*${slug}/`).test(h); }).map(f => path.basename(f));
check('pattern headers (Title, Slug prefix)', !badHeaders.length, badHeaders.join(', '));

const nonCore = [], tokenIssues = [];
const walkStyle = (obj, trail, f) => {
  if (!obj || typeof obj !== 'object') return;
  for (const [k, v] of Object.entries(obj)) {
    const t = `${trail}.${k}`;
    if (typeof v === 'object') { walkStyle(v, t, f); continue; }
    const val = String(v);
    if (/(^|\.)color\.|\.border\.(\w+\.)?color$/.test(t) && !/^var(:|\()/.test(val)) tokenIssues.push(`${f}: ${t}=${val}`);
    if (/\.typography\.fontSize$/.test(t)) tokenIssues.push(`${f}: custom font size ${val}`);
    if (/\.spacing\./.test(t) && !/^(var:preset\|spacing\|\w+|0(px|rem|em)?|auto)$/.test(val)) tokenIssues.push(`${f}: spacing ${t}=${val}`);
  }
};
for (const f of files) {
  const rel = path.relative(dir, f);
  const src = read(f);
  const isWoo = WOO_TEMPLATES.test(path.basename(f));
  for (const m of src.matchAll(/<!-- wp:([a-z0-9-]+\/)?([a-z0-9-]+)(\s+(\{[\s\S]*?\}))?\s*\/?-->/g)) {
    const ns = (m[1] || 'core/').slice(0, -1);
    if (ns !== 'core' && !(isWoo && ns === 'woocommerce')) nonCore.push(`${rel}: ${ns}/${m[2]}`);
    if (m[4]) { try { const a = JSON.parse(m[4]); walkStyle(a.style, 'style', rel); } catch {} }
  }
  const hex = src.replace(/<\?php[\s\S]*?\?>/g, '').match(/(?<![&\w])#[0-9a-fA-F]{6}\b|(?<![&\w])#[0-9a-fA-F]{3}\b(?![-\w])/g);
  if (hex) tokenIssues.push(`${rel}: hex ${[...new Set(hex)].join(' ')}`);
  if (/style="[^"]*font-family/i.test(src)) tokenIssues.push(`${rel}: inline font-family`);
}
check('only core blocks (woocommerce only in Woo templates)', !nonCore.length, [...new Set(nonCore)].slice(0, 6).join(' | '));
check('tokenised markup (no hex, custom font sizes or raw spacing)', !tokenIssues.length, [...new Set(tokenIssues)].slice(0, 6).join(' | '));

// Writing: em dashes anywhere in the theme; copylint on shipped copy.
const textFiles = fs.readdirSync(dir, { recursive: true }).filter(f => /\.(php|html|json|txt|css|md)$/.test(f) && !f.includes('LICENSE')).map(f => path.join(dir, f));
const dashes = textFiles.filter(f => read(f).includes('—')).map(f => path.relative(dir, f));
check('zero em dashes', !dashes.length, dashes.join(', '));
const lint = spawnSync('node', [path.join(ROOT, 'research', 'tools', 'copylint.mjs'), ...files, path.join(dir, 'readme.txt')], { encoding: 'utf8' });
const s5 = (lint.stdout || '').split('\n').filter(l => l.startsWith('S5'));
check('copylint: no S5 AI-writing tells', !s5.length, s5.slice(0, 4).map(l => l.replace(dir + '/', '').replace(/\s+/g, ' ')).join(' | '));

// Images: present, not huge, credited.
const imgDir = path.join(dir, 'assets', 'images');
const imgs = fs.existsSync(imgDir) ? fs.readdirSync(imgDir).filter(f => /\.(jpe?g|png|webp)$/i.test(f)) : [];
const big = imgs.filter(f => fs.statSync(path.join(imgDir, f)).size > 600 * 1024);
check('images under 600KB', !big.length, big.join(', '));
const readme = read(path.join(dir, 'readme.txt'));
const uncredited = imgs.filter(f => !readme.includes(f));
check('every image credited in readme.txt', !uncredited.length, uncredited.join(', '));
const refImgs = [...new Set(files.flatMap(f => [...read(f).matchAll(/assets\/images\/([\w.-]+)/g)].map(m => m[1])))];
const deadImgs = refImgs.filter(f => !imgs.includes(f));
check('referenced images exist', !deadImgs.length, deadImgs.join(', '));
check('demo content.json present', fs.existsSync(path.join(demoDir, 'content.json')));

// ---------------- dynamic ----------------
if (!staticOnly) {
  const site = await startSite(slug, { port: 9800 + Math.floor(Math.random() * 400) });
  try {
    const demo = JSON.parse(read(path.join(demoDir, 'content.json')));
    const api = async p => (await fetch(site.url + p, { signal: AbortSignal.timeout(90000) })).json();
    const pages = await api('/wp-json/wp/v2/pages?per_page=100&_fields=link,slug');
    const posts = await api('/wp-json/wp/v2/posts?per_page=100&_fields=link,slug');
    const urls = new Set(['/', ...pages.map(p => new URL(p.link).pathname).filter(x => !/^\/(cart|checkout|my-account)\//.test(x)), ...posts.slice(0, 6).map(p => new URL(p.link).pathname), ...(demo.nav || []).map(n => n.url), '/?s=the']);
    if (demo.products?.length) urls.add('/shop/');
    const cats = await api('/wp-json/wp/v2/categories?per_page=5&_fields=link,count');
    cats.filter(c => c.count).slice(0, 2).forEach(c => urls.add(new URL(c.link).pathname));
    const bad = [];
    for (const u of urls) {
      let r, h; try { r = await fetch(site.url + u, { redirect: 'manual', signal: AbortSignal.timeout(90000) }); h = await r.text(); } catch (e) { bad.push(`${u} timeout`); continue; }
      if (r.status >= 300 && r.status < 400 && !u.startsWith('/?') && !/^\/(cart|checkout|my-account)\//.test(u)) { bad.push(`${u} redirects to ${r.headers.get('location')}`); continue; }
      const notice = (h.match(/<b>(Warning|Notice|Fatal error|Deprecated|Parse error)<\/b>:[^<]{0,200}/g) || []).filter(n => !/\/plugins\//.test(n));
      if (r.status !== 200) bad.push(`${u} ${r.status}`);
      if (notice.length) bad.push(`${u} ${notice[0].replace(/<[^>]+>/g, '').slice(0, 140)}`);
      if (/core\/missing|Your site doesn’t include support for/.test(h)) bad.push(`${u} missing block`);
    }
    // Round 2: home page composition and content depth.
    const homeHtml = await (await fetch(site.url + '/', { signal: AbortSignal.timeout(90000) })).text();
    const homeMain = homeHtml.replace(/[\s\S]*?<main/, '<main');
    check('home page shows no table (round 2)', !/<table[\s>]/.test(homeMain));
    const h1 = ((homeMain.match(/<h1[^>]*>([\s\S]*?)<\/h1>/) || [])[1] || '').replace(/<[^>]+>/g, '').replace(/&[a-z#0-9]+;/g, ' ').trim();
    check('home h1 is not a motto ending in a full stop (round 2)', !(h1.length > 20 && /\.$/.test(h1)), h1.slice(0, 80));
    check('demo has 6+ posts (round 2)', posts.length >= 6, `${posts.length}`);
    // Dead internal links across the pages we fetched.
    const linkSet = new Set();
    for (const u of [...urls].filter(x => !x.startsWith('/?')).slice(0, 25)) {
      try {
        const h = await (await fetch(site.url + u, { signal: AbortSignal.timeout(90000) })).text();
        for (const m of h.matchAll(/href="([^"#?]+)"/g)) {
          let l = m[1];
          if (l.startsWith(site.url)) l = l.slice(site.url.length) || '/';
          if (!l.startsWith('/') || l.startsWith('//')) continue;
          if (/^\/(wp-|feed|comments|xmlrpc|cart|checkout|my-account)|\.(css|js|png|jpe?g|webp|svg|woff2?|xml|ico|pdf|zip)$|\/feed\/$|\/(page\/\d+)\/$/.test(l)) continue;
          linkSet.add(l);
        }
      } catch {}
    }
    const dead = [];
    for (const l of linkSet) {
      try { const r = await fetch(site.url + l, { redirect: 'manual', signal: AbortSignal.timeout(60000) }); if (r.status === 404) dead.push(l); } catch {}
    }
    check(`no dead internal links (${linkSet.size} checked, round 2)`, !dead.length, dead.slice(0, 6).join(' '));
    const r404 = await fetch(site.url + '/zz-no-such-page-' + Date.now() + '/', { redirect: 'manual', signal: AbortSignal.timeout(90000) });
    if (![404, 301, 302].includes(r404.status)) bad.push(`404 page returned ${r404.status}`);
    check(`front end: ${urls.size} pages 200, no PHP notices`, !bad.length, bad.slice(0, 5).join(' | '));

    let editor;
    try { editor = await openEditor(site.url); }
    catch (e) { check('editor loads', false, String(e.message).split('\n')[0]); }
    if (editor) {
    const { browser, page } = editor;
    const prepared = files.map(prepare);
    const res = await analyse(page, prepared.map(p => p.body));
    const probs = res.flatMap((r, i) => r.problems.map(p => `${path.relative(dir, files[i])}: ${p.kind} ${p.block} ${p.issue || ''}`));
    check('editor: zero invalid/unknown blocks in templates, parts, patterns', !probs.length, probs.slice(0, 5).join(' | '));
    // Page content saved in the demo (from patterns) must be valid too.
    const bodies = await page.evaluate(() => wp.apiFetch({ path: '/wp/v2/pages?per_page=100&context=edit&_fields=slug,content' }));
    let pageProbs = [];
    check('editor: demo pages readable', Array.isArray(bodies) && bodies.length > 0, `${bodies?.length}`);
    if (Array.isArray(bodies) && bodies[0]?.content?.raw !== undefined) {
      const pr = await analyse(page, bodies.map(b => b.content.raw));
      pageProbs = pr.flatMap((r, i) => r.problems.map(p => `${bodies[i].slug}: ${p.kind} ${p.block}`));
      check('editor: demo page content valid', !pageProbs.length, pageProbs.slice(0, 5).join(' | '));
      const allContent = bodies.map(b => b.content.raw).join('\n');
      const unshown = patterns.map(f => (read(f).match(/Slug:\s*(\S+)/) || [])[1]).filter(sl => sl && !allContent.includes(`"slug":"${sl}"`) && !allContent.includes(`"slug":"${sl.replace('/', '\\/')}"`));
      check('every pattern appears in the demo (round 2)', !unshown.length, `${unshown.length} missing: ${unshown.slice(0, 5).join(', ')}`);
    }
    await browser.close();
    }

    // Layout + screenshots.
    const b2 = await chromium.launch();
    const shotDir = path.join(demoDir, 'screens');
    if (!noShots) fs.mkdirSync(shotDir, { recursive: true });
    const overflow = [];
    const shotUrls = ['/', ...(demo.nav || []).map(n => n.url)].slice(0, 8);
    for (const [label, vp] of [['desktop', { width: 1440, height: 900 }], ['mobile', { width: 390, height: 844 }]]) {
      const ctx = await b2.newContext({ viewport: vp, deviceScaleFactor: 1, reducedMotion: 'reduce' });
      const pg = await ctx.newPage();
      for (const u of shotUrls) {
        await pg.goto(site.url + u, { waitUntil: quick ? 'load' : 'networkidle', timeout: 90000 }).catch(() => {});
        if (label === 'mobile') {
          const w = await pg.evaluate(() => document.documentElement.scrollWidth);
          if (w > vp.width + 2) overflow.push(`${u} ${w}px`);
        }
        if (!noShots && !quick) {
          const name = (u === '/' ? 'home' : u.replace(/[^a-z0-9]+/gi, '-').replace(/^-|-$/g, '')) + `-${label}.jpg`;
          await pg.screenshot({ path: path.join(shotDir, name), type: 'jpeg', quality: 75, fullPage: true });
        }
      }
      if (label === 'desktop' && !noShots) {
        await pg.setViewportSize({ width: 1200, height: 900 });
        await pg.goto(site.url + '/', { waitUntil: 'networkidle' }).catch(() => {});
        await pg.screenshot({ path: path.join(dir, 'screenshot.png') });
      }
      await ctx.close();
    }
    await b2.close();
    check('mobile 390px: no horizontal overflow', !overflow.length, overflow.join(', '));
  } finally {
    await site.stop();
  }
  check('screenshot.png 1200x900', fs.existsSync(path.join(dir, 'screenshot.png')));
}

const failed = results.filter(r => !r.ok);
fs.mkdirSync(demoDir, { recursive: true });
fs.writeFileSync(path.join(demoDir, 'test-report.json'), JSON.stringify({ slug, date: new Date().toISOString(), passed: !failed.length, results }, null, 2));
console.log(`\n${slug}: ${failed.length ? `FAILED ${failed.length} of ${results.length}` : `PASSED all ${results.length}`}`);
process.exit(failed.length ? 1 : 0);
