// Screenshot a reference site (desktop + mobile, top of page and a scrolled view) to study its style.
// Usage: node tools/peek.mjs <url> [name]   -> .cache/peek/<name>-*.jpg (view them with the Read tool)
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';
const [url, name = new URL(process.argv[2]).hostname.replace(/\W+/g, '-')] = process.argv.slice(2);
const out = path.resolve(import.meta.dirname, '..', '.cache', 'peek');
fs.mkdirSync(out, { recursive: true });
const b = await chromium.launch();
for (const [label, vp] of [['desktop', { width: 1440, height: 900 }], ['mobile', { width: 390, height: 844 }]]) {
  const p = await b.newPage({ viewport: vp });
  await p.goto(url, { waitUntil: 'networkidle', timeout: 60000 }).catch(() => {});
  for (const re of [/accept|agree|allow|ok|got it|akceptuj|zgadzam/i]) { const btn = p.getByRole('button', { name: re }).first(); if (await btn.isVisible().catch(() => false)) await btn.click().catch(() => {}); }
  await p.waitForTimeout(1500);
  await p.screenshot({ path: path.join(out, `${name}-${label}-top.jpg`), type: 'jpeg', quality: 70 });
  await p.evaluate(() => window.scrollTo(0, window.innerHeight * 1.5));
  await p.waitForTimeout(1000);
  await p.screenshot({ path: path.join(out, `${name}-${label}-scrolled.jpg`), type: 'jpeg', quality: 70 });
  const info = await p.evaluate(() => {
    const cs = e => e ? getComputedStyle(e) : null;
    const h = cs(document.querySelector('h1, h2')), bd = cs(document.body);
    return { title: document.title, headingFont: h?.fontFamily, headingSize: h?.fontSize, bodyFont: bd?.fontFamily, bg: bd?.backgroundColor, color: bd?.color };
  }).catch(() => ({}));
  if (label === 'desktop') console.log(JSON.stringify(info));
  await p.close();
}
await b.close();
console.log(`saved ${out}/${name}-{desktop,mobile}-{top,scrolled}.jpg`);
