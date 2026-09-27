// Field-study extractor: loads each site at 1440x900, screenshots the first viewport,
// then measures computed styles, markup fingerprints, section order and copy.
// Usage: node analyze.mjs sites.json out-dir
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';

const [listFile, outDir] = process.argv.slice(2);
const sites = JSON.parse(fs.readFileSync(listFile, 'utf8'));
fs.mkdirSync(path.join(outDir, 'shots'), { recursive: true });
fs.mkdirSync(path.join(outDir, 'text'), { recursive: true });
fs.mkdirSync(path.join(outDir, 'data'), { recursive: true });
const only = process.env.ONLY ? process.env.ONLY.split(',') : null;

async function resolveIframe(browser, src) {
  const p = await browser.newPage();
  try {
    await p.goto(src, { waitUntil: 'domcontentloaded', timeout: 45000 });
    await p.waitForSelector('iframe', { timeout: 20000 });
    await p.waitForTimeout(2000);
    const srcs = await p.$$eval('iframe', fs => fs.map(f => f.src).filter(Boolean));
    return srcs.find(s => /vusercontent|vercel\.app/.test(s)) || srcs[0];
  } finally { await p.close(); }
}

// Runs in the page.
function measure() {
  const vis = el => { const r = el.getBoundingClientRect(); const cs = getComputedStyle(el); return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.display !== 'none'; };
  const cv = document.createElement('canvas'); cv.width = cv.height = 1; const cx = cv.getContext('2d', { willReadFrequently: true }); const cache = new Map();
  const toHex = c => { if (!c || c === 'transparent') return null; const m = c.match(/rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)/); if (m) { if (m[4] !== undefined && +m[4] < 0.05) return null; return '#' + [m[1], m[2], m[3]].map(x => (+x | 0).toString(16).padStart(2, '0')).join('').toUpperCase(); }
    if (cache.has(c)) return cache.get(c); const a = c.match(/\/\s*([\d.]+)(%?)\s*\)$/); if (a && (a[2] ? +a[1] / 100 : +a[1]) < 0.05) { cache.set(c, null); return null; }
    cx.clearRect(0, 0, 1, 1); cx.fillStyle = '#000'; cx.fillStyle = c.replace(/\/\s*[\d.]+%?\s*\)$/, ')'); cx.fillRect(0, 0, 1, 1); const d = cx.getImageData(0, 0, 1, 1).data; const h = '#' + [d[0], d[1], d[2]].map(x => x.toString(16).padStart(2, '0')).join('').toUpperCase(); cache.set(c, h); return h; };
  const all = [...document.querySelectorAll('body *')].filter(el => !['SCRIPT', 'STYLE', 'NOSCRIPT', 'TEMPLATE', 'svg', 'path'].includes(el.tagName));
  const tally = () => new Map();
  const inc = (m, k, n = 1) => { if (k == null || k === '') return; m.set(k, (m.get(k) || 0) + n); };
  const top = (m, n = 12) => [...m.entries()].sort((a, b) => b[1] - a[1]).slice(0, n);
  const first = f => (f || '').split(',')[0].replace(/["']/g, '').trim();

  const html = document.documentElement.outerHTML;
  const root = getComputedStyle(document.documentElement);
  const vars = {};
  for (const v of ['--radius', '--primary', '--background', '--foreground', '--muted-foreground', '--accent', '--ring', '--border', '--font-sans', '--font-serif', '--font-heading', '--font-display']) vars[v] = root.getPropertyValue(v).trim();

  const fp = {
    next: !!document.getElementById('__next') || /\/_next\//.test(html),
    vite: /\/assets\/index-[A-Za-z0-9_-]+\.(js|css)/.test(html),
    lovableBadge: /lovable-badge|Edit with Lovable|lovable\.dev/i.test(html),
    boltBadge: /bolt\.new|Made in Bolt|bolt-badge/i.test(html),
    v0: /v0\.(dev|app)|vusercontent/i.test(html),
    wordpress: /wp-content|wp-includes/.test(html),
    elementor: /elementor/.test(html),
    tenweb: /10web|twbb/i.test(html),
    durable: /durable\.(co|com)|durablecdn/i.test(html),
    generator: [...document.querySelectorAll('meta[name=generator]')].map(m => m.content).join(' | '),
    tailwindClasses: 0, shadcnClasses: 0,
    lucide: document.querySelectorAll('svg.lucide, svg[class*="lucide-"]').length,
    lucideNames: [...new Set([...document.querySelectorAll('svg[class*="lucide-"]')].map(s => [...s.classList].find(c => c.startsWith('lucide-'))))].slice(0, 60),
    svgs: document.querySelectorAll('svg').length,
    fontAwesome: document.querySelectorAll('[class*="fa-"], i.fa, i.fas, i.far, i.fab').length,
    framerMotionInline: document.querySelectorAll('[style*="opacity: 0"], [style*="opacity:0"]').length,
  };
  const twRe = /^(?:[a-z]+:)*(?:-?(?:m|p)[trblxy]?-\d|flex$|grid$|gap-|text-(?:xs|sm|base|lg|[2-9]?xl)|rounded(?:-|$)|shadow(?:-|$)|bg-(?:white|black|gray|slate|zinc|neutral|stone|red|orange|amber|yellow|lime|green|emerald|teal|cyan|sky|blue|indigo|violet|purple|fuchsia|pink|rose)-|max-w-|min-h-|items-center|justify-between|tracking-|leading-|font-(?:bold|semibold|medium))/;
  const shRe = /^(?:[a-z]+:)*(?:text-muted-foreground|bg-background|bg-primary|text-primary-foreground|bg-muted|border-border|bg-card|text-card-foreground|bg-secondary|ring-ring|bg-accent|text-foreground)$/;
  const twHits = tally();
  for (const el of document.querySelectorAll('[class]')) {
    const cls = typeof el.className === 'string' ? el.className.split(/\s+/) : [...el.classList];
    for (const c of cls) { if (twRe.test(c)) { fp.tailwindClasses++; inc(twHits, c.replace(/^(?:[a-z]+:)+/, '')); } if (shRe.test(c)) fp.shadcnClasses++; }
  }
  const classMap = {};
  for (const el of document.querySelectorAll('[class]')) { const cls = typeof el.className === 'string' ? el.className.split(/\s+/) : [...el.classList]; for (const c of cls) if (c) classMap[c] = (classMap[c] || 0) + 1; }
  const hoverLift = document.querySelectorAll('[class*="hover:-translate-y"], [class*="hover:scale-"]').length;
  const groupHover = document.querySelectorAll('[class*="group-hover:"]').length;
  const bgClipTextCls = document.querySelectorAll('[class*="bg-clip-text"]').length;
  const gradCls = document.querySelectorAll('[class*="bg-gradient-to-"], [class*="bg-linear-to-"]').length;
  const blurCls = document.querySelectorAll('[class*="blur-"]').length;
  const backdropCls = document.querySelectorAll('[class*="backdrop-blur"]').length;

  // Fonts
  const body = getComputedStyle(document.body);
  const h1 = [...document.querySelectorAll('h1')].find(vis);
  const h2 = [...document.querySelectorAll('h2')].find(vis);
  const btn = [...document.querySelectorAll('button, a[class*="btn"], a[class*="button"], .wp-block-button__link, .elementor-button')].find(vis);
  const h1cs = h1 && getComputedStyle(h1);
  const pEls = [...document.querySelectorAll('p')].filter(vis).filter(p => p.innerText.trim().length > 60);
  const pcs = pEls[0] && getComputedStyle(pEls[0]);
  const fonts = {
    body: first(body.fontFamily), bodyStack: body.fontFamily,
    h1: h1cs ? first(h1cs.fontFamily) : null, h2: h2 ? first(getComputedStyle(h2).fontFamily) : null,
    button: btn ? first(getComputedStyle(btn).fontFamily) : null,
    loaded: [...new Set([...document.fonts].filter(f => f.status === 'loaded').map(f => f.family.replace(/["']/g, '')))],
    googleLinks: [...document.querySelectorAll('link[href*="fonts.googleapis"], link[href*="fonts.bunny"]')].map(l => l.href).slice(0, 4),
  };
  const faceTally = tally();
  for (const el of all) { if (!el.childNodes.length) continue; const hasText = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim().length > 1); if (hasText && vis(el)) inc(faceTally, first(getComputedStyle(el).fontFamily), (el.innerText || "").length); }

  const type = h1cs ? {
    h1Text: h1.innerText.trim().slice(0, 160), h1Size: parseFloat(h1cs.fontSize), h1Weight: h1cs.fontWeight, h1Tracking: h1cs.letterSpacing, h1LineHeight: h1cs.lineHeight, h1Align: h1cs.textAlign,
    h1Italic: h1cs.fontStyle, h1Count: document.querySelectorAll('h1').length,
    h1MixedFaces: [...h1.querySelectorAll('*')].some(c => first(getComputedStyle(c).fontFamily) !== first(h1cs.fontFamily) || getComputedStyle(c).fontStyle === 'italic' && h1cs.fontStyle !== 'italic'),
    h1ColouredSpan: [...h1.querySelectorAll('span, em, i, strong')].some(c => { const cs = getComputedStyle(c); return cs.color !== h1cs.color || cs.backgroundImage !== 'none'; }),
    h1Gradient: h1cs.backgroundImage.includes('gradient') || [...h1.querySelectorAll('*')].some(c => getComputedStyle(c).backgroundImage.includes('gradient') && getComputedStyle(c).webkitBackgroundClip === 'text'),
  } : { h1Count: 0 };
  type.bodySize = pcs ? parseFloat(pcs.fontSize) : parseFloat(body.fontSize);
  type.bodyLineHeight = pcs ? pcs.lineHeight : body.lineHeight;
  type.bodyColor = pcs ? toHex(pcs.color) : toHex(body.color);
  type.bodyMeasurePx = pEls[0] ? Math.round(pEls[0].getBoundingClientRect().width) : null;

  // Colours
  const textCol = tally(), bgCol = tally(), borderCol = tally(), btnBg = tally(), linkCol = tally(), iconCol = tally();
  const radius = { button: tally(), card: tally(), input: tally(), image: tally(), badge: tally(), all: tally() };
  const shadows = tally(); let gradients = 0, gradientText = 0, backdrop = 0, blurDeco = 0, radialGlow = 0; const gradList = tally();
  let eyebrows = 0; const eyebrowTexts = []; let emojiCount = 0; let opacityZero = 0; let pills = 0;
  const trackingTally = tally(); const maxW = tally(); const secPad = tally(); const transitions = tally();
  for (const el of all) {
    if (!vis(el)) continue;
    const cs = getComputedStyle(el); const r = el.getBoundingClientRect(); const tag = el.tagName;
    const hasText = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim().length > 1);
    if (hasText) inc(textCol, toHex(cs.color), Math.min((el.innerText || "").length, 400));
    const bg = toHex(cs.backgroundColor); if (bg) inc(bgCol, bg, Math.round(r.width * r.height / 1000));
    if (parseFloat(cs.borderTopWidth) > 0 && cs.borderTopStyle !== 'none') inc(borderCol, toHex(cs.borderTopColor));
    const rad = cs.borderTopLeftRadius; const isRounded = rad && rad !== '0px';
    const isBtn = tag === 'BUTTON' || (tag === 'A' && (bg || parseFloat(cs.borderTopWidth) > 0) && parseFloat(cs.paddingLeft) >= 10 && r.height >= 28 && r.height <= 72);
    const isInput = tag === 'INPUT' && !['checkbox', 'radio', 'hidden'].includes(el.type) || tag === 'TEXTAREA' || tag === 'SELECT';
    const isImg = tag === 'IMG' && r.width > 120;
    const isCard = !isBtn && !isInput && ['DIV', 'ARTICLE', 'LI', 'A'].includes(tag) && r.width >= 180 && r.width <= 700 && r.height >= 120 && (bg || cs.boxShadow !== 'none' || parseFloat(cs.borderTopWidth) > 0);
    const isBadge = !isBtn && hasText && r.height <= 34 && r.width < 320 && (bg || parseFloat(cs.borderTopWidth) > 0) && (el.innerText || "").trim().length < 40;
    if (isBtn) { inc(radius.button, rad); if (bg) inc(btnBg, bg); }
    if (isInput) inc(radius.input, rad);
    if (isImg) inc(radius.image, rad);
    if (isCard) inc(radius.card, rad);
    if (isBadge) { inc(radius.badge, rad); if (parseFloat(rad) >= r.height / 2 - 1) pills++; }
    if (isRounded) inc(radius.all, rad);
    if (tag === 'A' && hasText && !isBtn) inc(linkCol, toHex(cs.color));
    if (cs.boxShadow && cs.boxShadow !== 'none') inc(shadows, cs.boxShadow.replace(/(?:rgba?|oklch|oklab|lab|lch|color)\([^)]*\)/g, c => toHex(c) ? `${toHex(c)}@${(c.match(/[,/]\s*([\d.]+%?)\s*\)$/) || [0, 1])[1]}` : 'transparent'));
    const bi = cs.backgroundImage;
    if (bi && bi.includes('gradient')) { gradients++; inc(gradList, bi.replace(/(?:rgba?|oklch|oklab|lab|lch|color)\([^)]*\)/g, c => toHex(c) || 'transparent').slice(0, 140)); if (bi.includes('radial')) radialGlow++; if (cs.webkitBackgroundClip === 'text' || cs.backgroundClip === 'text') gradientText++; }
    if (cs.backdropFilter && cs.backdropFilter !== 'none') backdrop++;
    if (cs.filter && /blur\((?:[3-9]|\d\d+)/.test(cs.filter)) blurDeco++;
    if (hasText && cs.textTransform === 'uppercase' && parseFloat(cs.letterSpacing) > 0.5 && parseFloat(cs.fontSize) <= 15 && (el.innerText || "").trim().length < 40) { eyebrows++; if (eyebrowTexts.length < 8) eyebrowTexts.push((el.innerText || "").trim()); }
    if (cs.opacity === '0' && hasText) opacityZero++;
    if (/^H[1-3]$/.test(tag)) inc(trackingTally, `${tag}:${cs.letterSpacing}`);
    if (cs.maxWidth !== 'none' && r.width > 900) inc(maxW, cs.maxWidth);
    if ((tag === 'SECTION' || el.parentElement === document.querySelector('main')) && r.height > 200) inc(secPad, `${cs.paddingTop}/${cs.paddingBottom}`);
    if (cs.transitionProperty && cs.transitionDuration !== '0s') inc(transitions, `${cs.transitionProperty.split(',')[0]} ${cs.transitionDuration.split(',')[0]} ${cs.transitionTimingFunction.split(',')[0].slice(0, 40)}`);
  }
  const text = document.body.innerText;
  emojiCount = (text.match(/\p{Emoji_Presentation}|[\u2600-\u27BF]\uFE0F/gu) || []).length; var emojiList = [...new Set(text.match(/\p{Emoji_Presentation}|[\u2600-\u27BF]\uFE0F/gu) || [])].slice(0, 20);

  // Icon tiles: small square boxes with a background and a single svg/i child.
  let iconTiles = 0;
  for (const el of all) {
    const r = el.getBoundingClientRect(); if (r.width < 32 || r.width > 72 || Math.abs(r.width - r.height) > 4) continue;
    const cs = getComputedStyle(el); if (!toHex(cs.backgroundColor) && !cs.backgroundImage.includes('gradient')) continue;
    if (el.children.length === 1 && ['svg', 'I', 'IMG', 'SPAN'].includes(el.children[0].tagName) && !(el.innerText || "").trim()) iconTiles++;
  }
  // Star ratings
  const stars = (text.match(/★/g) || []).length + document.querySelectorAll('svg.lucide-star, [class*="fa-star"], [class*="star-rating"], .elementor-star-rating').length;

  // Sections and order
  const secRoot = document.querySelector('main') || document.body;
  let secs = [...secRoot.querySelectorAll(':scope > section, :scope > div > section, :scope > footer, :scope > header, :scope > div > footer, section, footer')].filter(s => vis(s) && s.getBoundingClientRect().height > 120);
  secs = secs.filter(s => !secs.some(o => o !== s && o.contains(s)));
  secs.sort((a, b) => a.getBoundingClientRect().top - b.getBoundingClientRect().top);
  const cardGrid = s => { // >=3 siblings of equal width, each with a heading and text
    for (const par of [s, ...s.querySelectorAll('div, ul')]) {
      const kids = [...par.children].filter(vis); if (kids.length < 3) continue;
      const w = kids.map(k => Math.round(k.getBoundingClientRect().width)); const same = w.filter(x => Math.abs(x - w[0]) <= 3).length;
      if (same >= 3 && w[0] > 150 && w[0] < 700 && kids.filter(k => k.querySelector('h3,h4,h5,strong,[class*="font-semibold"],[class*="font-bold"]') && k.innerText.length > 30).length >= 3) return { n: kids.length, tiles: kids.filter(k => [...k.querySelectorAll('div,span')].some(t => { const r = t.getBoundingClientRect(); const c = getComputedStyle(t); return r.width >= 32 && r.width <= 72 && Math.abs(r.width - r.height) <= 4 && (toHex(c.backgroundColor) || c.backgroundImage.includes('gradient')) && t.querySelector('svg,i,img'); })).length };
    }
    return null;
  };
  const classify = (s, i) => {
    const t = s.innerText.toLowerCase(); const hd = [...s.querySelectorAll('h1,h2,h3')].slice(0, 2).map(h => h.innerText.toLowerCase().replace(/\s+/g, ' ')).join(' | ');
    const words = t.split(/\s+/).length;
    if (s.tagName === 'FOOTER' || s.closest('footer')) return 'footer';
    if (s.querySelector('h1') || i === 0) return 'hero';
    if (/faq|frequently asked|common questions|questions\b|good to know/.test(hd) || s.querySelectorAll('details, [aria-expanded], [class*="accordion"]').length >= 3) return 'faq';
    if (/pric|plans?\b|packages?\b|rates\b|membership/.test(hd) || /\/\s?(mo|month|year)\b|per month|most popular/.test(t)) return 'pricing';
    if (/testimonial|what (our )?(clients|customers|people|students|members|guests|parents|patients|couples)|reviews?|loved by|kind words|say about|happy (clients|customers)/.test(hd) || (t.match(/[“"]/g) || []).length >= 4 || s.querySelectorAll('blockquote').length >= 2) return 'testimonials';
    if (/trusted by|as seen|partners|backed by|logos|companies|brands|featured in/.test(hd) || (words < 40 && !s.querySelector('form') && s.querySelectorAll('img, svg').length >= 4)) return 'logos';
    if (/how it works|process|steps|how we work|getting started|simple steps/.test(hd)) return 'how-it-works';
    if (/team|meet (the|our)|our (people|experts|coaches|attorneys|doctors|staff|instructors)/.test(hd)) return 'team';
    if (/gallery|portfolio|our work|works\b|projects|recent work|lookbook|instagram/.test(hd)) return 'gallery';
    if (/blog|news|articles|journal|insights|latest|stories/.test(hd)) return 'blog';
    const nums = (s.innerText.match(/\b\d[\d,.]*\s?(\+|%|k\+?|m\+?|x|\/7|★)(?=\s|$)/gi) || []).length;
    if (nums >= 3 && words < 150) return 'stats';
    if (/contact|get in touch|visit us|reach us|location|find us|hours/.test(hd) || s.querySelector('form') && s.querySelectorAll('input,textarea').length >= 3) return 'contact';
    if (words < 120 && s.querySelector('a,button') && /ready|get started|start|join|let'?s|book|today|now|sign up|subscribe|newsletter|discuss|call/.test(hd)) return 'cta';
    if (/about|our story|who we are|mission|why we|since \d{4}|years of|experience|philosophy|approach/.test(hd)) return 'about';
    const cg = cardGrid(s);
    if (cg || /services|features|why choose|what we (do|offer)|benefits|everything you|offer|menu|specialt|solutions|expertise/.test(hd)) return 'features';
    return 'other';
  };
  let cardGrids = 0, cardGridsWithTiles = 0; for (const s of secs) { const cg = cardGrid(s); if (cg) { cardGrids++; if (cg.tiles >= 3) cardGridsWithTiles++; } }
  const order = secs.map(classify);
  const sections = secs.map((s, i) => ({ kind: order[i], heading: (s.querySelector('h1,h2,h3')?.innerText || '').trim().slice(0, 80), bg: toHex(getComputedStyle(s).backgroundColor), h: Math.round(s.getBoundingClientRect().height) }));

  // CTAs and headings
  const ctas = [...new Set([...document.querySelectorAll('button, a')].filter(vis).filter(a => { const cs = getComputedStyle(a); return toHex(cs.backgroundColor) && a.innerText.trim().length > 1 && a.innerText.trim().length < 40; }).map(a => a.innerText.trim().replace(/\s+/g, ' ')))].slice(0, 20);
  const headings = [...document.querySelectorAll('h1,h2,h3')].filter(vis).map(h => h.innerText.trim().replace(/\s+/g, ' ')).filter(Boolean).slice(0, 40);
  const nav = [...document.querySelectorAll('header a, nav a')].filter(vis).map(a => a.innerText.trim()).filter(t => t && t.length < 25).slice(0, 12);
  const footerText = (document.querySelector('footer')?.innerText || '').slice(0, 600);

  return {
    title: document.title, vars, fp, twTop: top(twHits, 25), fonts, faceTally: top(faceTally, 5), type,
    colours: { text: top(textCol, 8), bg: top(bgCol, 8), border: top(borderCol, 5), buttonBg: top(btnBg, 6), link: top(linkCol, 5) },
    bodyBg: toHex(body.backgroundColor) || toHex(root.backgroundColor),
    radius: Object.fromEntries(Object.entries(radius).map(([k, v]) => [k, top(v, 6)])),
    shadows: top(shadows, 8), gradients, gradientText, gradList: top(gradList, 5), backdrop, blurDeco, radialGlow,
    classSignals: { hoverLift, groupHover, bgClipTextCls, gradCls, blurCls, backdropCls },
    eyebrows, eyebrowTexts, pills, emojiCount, emojiList, classMap, opacityZero, iconTiles, stars,
    tracking: top(trackingTally, 6), maxW: top(maxW, 5), secPad: top(secPad, 5), transitions: top(transitions, 5),
    order, sections, cardGrids, cardGridsWithTiles, ctas, headings, nav, footerText,
    words: text.split(/\s+/).filter(Boolean).length, emDash: (text.match(/—/g) || []).length, enDashSpaced: (text.match(/\s–\s/g) || []).length,
    text,
  };
}

let browser = await chromium.launch();
const results = [];
const queue = sites.filter(s => !only || only.includes(s.id));
async function one(s) {
  if (!browser.isConnected()) browser = await chromium.launch();
  const res = { ...s };
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, locale: 'en-GB', userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0 Safari/537.36' });
  const page = await ctx.newPage();
  try {
    let url = s.iframe ? s.src : s.url;
    const r = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
    res.status = r?.status(); res.finalUrl = page.url();
    await page.waitForLoadState('networkidle', { timeout: 12000 }).catch(() => {});
    let T = page;
    if (s.iframe) {
      await page.waitForSelector('iframe', { timeout: 20000 });
      await page.$eval('iframe', f => { f.style.cssText = 'position:fixed!important;left:0;top:0;width:1440px!important;height:900px!important;max-width:none!important;z-index:2147483647;border:0;background:#fff;transform:none!important'; document.body.style.overflow = 'hidden'; });
      await page.waitForTimeout(5000);
      T = page.frames().find(f => /vusercontent|vercel\.app/.test(f.url()));
      if (!T) throw new Error('no preview frame');
      res.resolved = T.url().split('?')[0];
    }
    for (const re of [/^accept( all)?( cookies)?$/i, /^allow( all)?( cookies)?$/i, /^(i )?agree$/i, /^got it$/i, /^ok$/i]) {
      const b = page.getByRole('button', { name: re }).first();
      if (await b.isVisible({ timeout: 300 }).catch(() => false)) { await b.click({ timeout: 1000 }).catch(() => {}); break; }
    }
    await page.waitForTimeout(4000);
    const hiddenAtLoad = await T.evaluate(() => [...document.querySelectorAll('body *')].filter(el => { const cs = getComputedStyle(el); const r = el.getBoundingClientRect(); return cs.opacity === '0' && r.top > window.innerHeight && el.innerText && (el.innerText || "").trim().length > 20; }).length);
    await page.screenshot({ path: path.join(outDir, 'shots', `${s.id}.jpg`), type: 'jpeg', quality: 80 });
    // scroll through the page so scroll-triggered content appears
    const H = await T.evaluate(() => document.body.scrollHeight);
    for (let y = 0; y < Math.min(H, 30000); y += 700) { await T.evaluate(y => window.scrollTo(0, y), y); await page.waitForTimeout(180); }
    await T.evaluate(() => window.scrollTo(0, 0)); await page.waitForTimeout(1200);
    const m = await T.evaluate(measure);
    res.hiddenBelowFoldAtLoad = hiddenAtLoad; res.pageHeight = H;
    fs.writeFileSync(path.join(outDir, 'text', `${s.id}.txt`), m.text);
    delete m.text;
    Object.assign(res, m); res.ok = true;
  } catch (e) { res.ok = false; res.error = String(e.message).split('\n')[0]; }
  fs.writeFileSync(path.join(outDir, 'data', `${s.id}.json`), JSON.stringify(res, null, 1));
  console.log(`${res.ok ? 'ok ' : 'ERR'} ${s.id} ${res.status ?? ''} ${res.error ?? ''} words=${res.words ?? ''} order=${(res.order || []).join('>')}`);
  results.push(res);
  await ctx.close().catch(() => {});
}
async function worker() { while (queue.length) { const s = queue.shift(); await Promise.race([one(s), new Promise(r => setTimeout(r, 180000))]).catch(e => console.log('ERR', s.id, e.message)); } }
await Promise.all([worker(), worker(), worker()]);
await browser.close().catch(() => {});
