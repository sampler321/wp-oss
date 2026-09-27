// Re-serialise a theme's templates, parts and patterns through WordPress's own block serializer,
// so block wrappers, classes and inline styles are exactly what the editor expects.
// Usage: node tools/normalize-blocks.mjs <slug> [--dry]
import path from 'node:path';
import fs from 'node:fs';
import { startSite, ROOT } from './lib/playground.mjs';
import { openEditor, analyse, prepare, restore, themeFiles } from './lib/editor.mjs';

const slug = process.argv[2];
const dry = process.argv.includes('--dry');
if (!slug) { console.error('usage: normalize-blocks.mjs <slug> [--dry]'); process.exit(1); }
const themeDir = path.join(ROOT, 'themes', slug);
const files = themeFiles(themeDir);
const prepared = files.map(prepare);

const site = await startSite(slug, { port: 9600 + Math.floor(Math.random() * 300) });
let changed = 0;
try {
  const { browser, page } = await openEditor(site.url);
  // Two passes: the first rebuild can change attributes that the second pass settles.
  let bodies = prepared.map(p => p.body);
  for (let pass = 0; pass < 2; pass++) {
    const res = await analyse(page, bodies);
    bodies = res.map((r, i) => r.canonical ?? bodies[i]);
    if (pass === 1) {
      res.forEach((r, i) => {
        const rel = path.relative(themeDir, files[i]);
        const serious = r.problems.filter(p => p.kind !== 'invalid');
        if (serious.length) console.log(`!! ${rel}: ${serious.map(p => `${p.kind} ${p.block} @ ${p.where}`).join('; ')}`);
      });
    }
  }
  bodies.forEach((b, i) => {
    const next = restore(prepared[i], b);
    const prev = fs.readFileSync(files[i], 'utf8');
    if (next !== prev) {
      changed++;
      if (!dry) fs.writeFileSync(files[i], next);
    }
  });
  await browser.close();
} finally {
  await site.stop();
}
console.log(`${dry ? 'would change' : 'normalised'} ${changed} of ${files.length} files in ${slug}`);
