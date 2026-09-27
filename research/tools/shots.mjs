// Batch-capture screenshots of every Refs deep link in the idea files.
// Usage: node shots.mjs ../parts/02r-ideas-001-042.md ../parts/05-ideas-085-110.md ...
// Output: ../screenshots/NNN-k.jpg (desktop 1440x900) + NNN-k-m.jpg (mobile 390x844), ../screenshots/manifest.json
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';

const OUT = path.resolve(import.meta.dirname, '../screenshots');
fs.mkdirSync(OUT, { recursive: true });
const manifestPath = path.join(OUT, 'manifest.json');
const manifest = fs.existsSync(manifestPath) ? JSON.parse(fs.readFileSync(manifestPath, 'utf8')) : {};

function extract(file) {
  const jobs = [];
  let idea = null, inRefs = false, k = 0;
  for (const line of fs.readFileSync(file, 'utf8').split('\n')) {
    const h = line.match(/^#### (\d{3})[ ,.:\u00b7]/);
    if (h) { idea = h[1]; inRefs = false; k = 0; continue; }
    if (/^\*\*Refs:\*\*/.test(line)) { inRefs = true; continue; }
    if (inRefs) {
      const m = line.match(/^\s*-\s*\[([^\]]+)\]\((https?:\/\/[^)\s]+)\)/);
      if (m) { k++; jobs.push({ idea, k, title: m[1], url: m[2] }); continue; }
      if (line.trim() === '') continue;
      inRefs = false;
    }
  }
  return jobs;
}

const AGE = [/^(yes|yep|yep!|i am|i'?m) ?(over )?(18|21)?\+?!?$/i, /^enter( site)?$/i, /^i am (over )?(18|21)/i, /^(yes,? )?i'?m (of legal drinking age|over (18|21))/i];
const BLOCKED = /confirm you are human|verify you are human|just a moment|attention required|access denied|captcha|are you a robot|403 forbidden/i;
const ACCEPT = [/^accept( all)?( cookies)?$/i, /^allow( all)?( cookies)?$/i, /^(i )?agree$/i, /^ok(ay)?$/i, /^got it$/i, /^alle akzeptieren$/i, /^accepteren$/i, /^tout accepter$/i];

async function dismiss(page) {
  for (const re of [...AGE, ...ACCEPT]) {
    const b = page.getByRole('button', { name: re }).first();
    if (await b.isVisible({ timeout: 300 }).catch(() => false)) { await b.click({ timeout: 1000 }).catch(() => {}); await page.waitForTimeout(400); return; }
  }
}

async function shoot(browser, job) {
  const id = `${job.idea}-${job.k}`;
  const res = { ...job, id, ok: false };
  for (const [suffix, vp, mobile] of [['', { width: 1440, height: 900 }, false], ['-m', { width: 390, height: 844 }, true]]) {
    const ctx = await browser.newContext({ viewport: vp, isMobile: mobile, deviceScaleFactor: mobile ? 2 : 1, reducedMotion: 'reduce', locale: 'en-GB',
      userAgent: mobile ? 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1' : undefined });
    const page = await ctx.newPage();
    try {
      const r = await page.goto(job.url, { waitUntil: 'domcontentloaded', timeout: 30000 });
      res.status = r?.status();
      await page.waitForLoadState('networkidle', { timeout: 8000 }).catch(() => {});
      await dismiss(page);
      await dismiss(page);
      // Trigger lazy-loaded images and sliders, then return to the top.
      await page.evaluate(async () => { for (let y = 0; y < 3000; y += 600) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 150)); } window.scrollTo(0, 0); }).catch(() => {});
      await page.waitForTimeout(1800);
      const txt = (await page.evaluate(() => document.body?.innerText?.slice(0, 2000) || '').catch(() => '')) || '';
      if (BLOCKED.test(txt) && txt.length < 1500) res.blocked = true;
      await page.screenshot({ path: path.join(OUT, `${id}${suffix}.jpg`), type: 'jpeg', quality: 72 });
      res.ok = true;
    } catch (e) { res.error = String(e.message).split('\n')[0]; }
    await ctx.close();
  }
  return res;
}

// --redo=ids.txt re-shoots the listed ids (one per line, e.g. 088-2) even if already captured.
const redoArg = process.argv.find(a => a.startsWith('--redo='));
const redo = redoArg ? new Set(fs.readFileSync(redoArg.slice(7), 'utf8').split(/\s+/).filter(Boolean)) : null;
const files = process.argv.slice(2).filter(a => !a.startsWith('--'));
const jobs = files.flatMap(extract).filter(j => redo ? redo.has(`${j.idea}-${j.k}`)
  : (!manifest[`${j.idea}-${j.k}`]?.ok || manifest[`${j.idea}-${j.k}`].url !== j.url));
console.log(`${jobs.length} URLs to capture`);
const browser = await chromium.launch();
let i = 0;
async function worker() {
  while (i < jobs.length) {
    const job = jobs[i++];
    const r = await shoot(browser, job);
    manifest[r.id] = r;
    console.log(`${r.ok ? 'ok ' : 'ERR'} ${r.id} ${r.status ?? ''} ${r.url} ${r.error ?? ''}`);
    fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2));
  }
}
await Promise.all(Array.from({ length: 6 }, worker));
await browser.close();
