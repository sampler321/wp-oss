// Capture the 20 representative first-viewport screenshots at 1440x900.
import { chromium } from 'playwright';
import fs from 'node:fs';
const OUT = '/Users/borys/Desktop/wp-oss/research/screenshots/anti-vibe';
fs.mkdirSync(OUT, { recursive: true });
const sites = JSON.parse(fs.readFileSync(new URL('./sites.json', import.meta.url)));
const pick = ['lov-aquafix','lov-trimsync','lov-vitalpath','lov-buildright','lov-apex','bolt-lumiere','bolt-maison','bolt-kern','bolt-nonprofit','bolt-saas','bolt-meridian','v0-optimus','v0-hously','v0-liquid','10w-electric','10w-smiledent','10w-joanne','10w-vowvenue','10w-harvest','dur-pours'];
const b = await chromium.launch();
let n = 0;
for (const id of pick) {
  n++; const s = sites.find(x => x.id === id);
  const file = `${OUT}/${String(n).padStart(2, '0')}-${id}.jpg`;
  const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, locale: 'en-GB' });
  const p = await ctx.newPage();
  try {
    await p.goto(s.iframe ? s.src : s.url, { waitUntil: 'domcontentloaded', timeout: 45000 });
    await p.waitForLoadState('networkidle', { timeout: 12000 }).catch(() => {});
    if (s.iframe) {
      await p.waitForSelector('iframe');
      await p.evaluate(() => { const f = document.querySelector('iframe'); for (const el of document.querySelectorAll('body *')) if (!el.contains(f) && el !== f) el.style.visibility = 'hidden'; f.style.cssText = 'position:fixed!important;left:0;top:0;width:1440px!important;height:900px!important;max-width:none!important;z-index:2147483647;border:0;visibility:visible'; });
      await p.waitForTimeout(6000);
    }
    for (const re of [/^accept( all)?( cookies)?$/i, /^allow( all)?( cookies)?$/i, /^got it$/i]) { const x = p.getByRole('button', { name: re }).first(); if (await x.isVisible({ timeout: 300 }).catch(() => false)) { await x.click().catch(() => {}); break; } }
    await p.waitForTimeout(4500);
    await p.screenshot({ path: file, type: 'jpeg', quality: 80 });
    console.log('ok', file);
  } catch (e) { console.log('ERR', id, e.message.split('\n')[0]); }
  await ctx.close();
}
await b.close();
