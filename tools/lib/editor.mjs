// Load the block editor in a real browser against a Playground site and run WordPress's own
// parser/serializer over theme files.
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';

const PHP_RE = /<\?php[\s\S]*?\?>/g;

// Split a pattern file into its PHP header and block body; replace inline PHP with tokens.
export function prepare(file) {
  const raw = fs.readFileSync(file, 'utf8');
  let header = '', body = raw;
  if (file.endsWith('.php')) {
    const m = raw.match(/^<\?php[\s\S]*?\?>\s*/);
    if (m) { header = m[0]; body = raw.slice(m[0].length); }
  }
  const php = [];
  // Identical PHP snippets share one token, so an image URL used in both a block attribute and its HTML still matches.
  body = body.replace(PHP_RE, s => { let i = php.indexOf(s); if (i < 0) { php.push(s); i = php.length - 1; } return `WPOSSPHP${i}X`; });
  return { header, body, php };
}

export function restore({ header, php }, body) {
  return header + body.replace(/WPOSSPHP(\d+)X/g, (_, i) => php[+i]).trim() + '\n';
}

export function themeFiles(themeDir) {
  const list = [];
  for (const d of ['templates', 'parts', 'patterns']) {
    const dir = path.join(themeDir, d);
    if (!fs.existsSync(dir)) continue;
    for (const f of fs.readdirSync(dir).sort()) if (/\.(html|php)$/.test(f)) list.push(path.join(dir, f));
  }
  return list;
}

export async function openEditor(siteUrl) {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1400, height: 900 } });
  await page.goto(`${siteUrl}/wp-login.php`, { waitUntil: 'domcontentloaded', timeout: 120000 });
  await page.fill('#user_login', 'admin');
  await page.fill('#user_pass', 'password');
  await Promise.all([page.waitForNavigation({ timeout: 120000 }).catch(() => {}), page.click('#wp-submit')]);
  // Plugins (WooCommerce) may redirect the first admin visit; retry until the post editor is up.
  for (let attempt = 0; attempt < 4; attempt++) {
    await page.goto(`${siteUrl}/wp-admin/post-new.php`, { waitUntil: 'domcontentloaded', timeout: 120000 });
    if (!page.url().includes('post-new.php')) continue;
    try { await page.waitForFunction(() => window.wp?.blocks?.getBlockTypes?.().length > 60, null, { timeout: 180000 }); break; }
    catch (e) { if (attempt === 3) throw e; }
  }
  // Close the welcome guide if present, so it doesn't matter for screenshots.
  await page.evaluate(() => { try { wp.data.dispatch('core/preferences').set('core/edit-post', 'welcomeGuide', false); } catch {} });
  return { browser, page };
}

// Analyse and canonicalise many block documents in one round trip.
export async function analyse(page, docs) {
  return page.evaluate((docs) => {
    const { parse, serialize, createBlock, getBlockType } = wp.blocks;
    const out = [];
    for (const src of docs) {
      const problems = [];
      const names = new Set();
      const walk = (blocks, trail) => {
        for (const b of blocks) {
          names.add(b.name);
          const where = trail ? `${trail} > ${b.name}` : b.name;
          if (b.name === 'core/missing') problems.push({ kind: 'unknown', block: b.attributes?.originalName, where });
          else if (!getBlockType(b.name)) problems.push({ kind: 'unregistered', block: b.name, where });
          if (b.isValid === false) {
            const issue = (b.validationIssues || []).map(i => (i.args || []).filter(x => typeof x === 'string').slice(-2).join(' | ')).join(' ; ').slice(0, 300);
            problems.push({ kind: 'invalid', block: b.name, where, issue });
          }
          walk(b.innerBlocks || [], where);
        }
      };
      const blocks = parse(src);
      walk(blocks, '');
      // Freeform/classic content between blocks is a sign of stray HTML.
      const freeform = blocks.filter(b => b.name === 'core/freeform' && (b.attributes.content || '').trim());
      for (const f of freeform) problems.push({ kind: 'stray-html', block: 'core/freeform', where: (f.attributes.content || '').trim().slice(0, 80) });
      const rebuild = b => (b.name === 'core/missing' || b.name === 'core/freeform') ? b : createBlock(b.name, { ...b.attributes }, (b.innerBlocks || []).map(rebuild));
      let canonical = null;
      try { canonical = serialize(blocks.map(rebuild)); } catch (e) { problems.push({ kind: 'serialize-error', block: '', where: String(e) }); }
      out.push({ problems, names: [...names], canonical });
    }
    return out;
  }, docs);
}
