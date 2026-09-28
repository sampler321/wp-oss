// Capture card screenshots for the open-wp-themes library from the live demos (1200x900, below the demo bar).
// Usage: node tools/capture-cards.mjs
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';
const ROOT = path.resolve(import.meta.dirname, '..');
const data = JSON.parse(fs.readFileSync(path.join(ROOT, 'site/open-wp-themes/src/data/themes.json'), 'utf8'));
const out = path.join(ROOT, 'site/open-wp-themes/public/shots');
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1200, height: 960 } });
for (const t of data) {
  await p.goto(t.demo, { waitUntil: 'networkidle', timeout: 90000 }).catch(() => {});
  await p.waitForTimeout(1500);
  const bar = await p.evaluate(() => document.body.firstElementChild?.getBoundingClientRect().height || 0);
  await p.screenshot({ path: path.join(out, `${t.slug}.png`), clip: { x: 0, y: Math.round(bar), width: 1200, height: 900 } });
  console.log('shot', t.slug);
}
await b.close();
