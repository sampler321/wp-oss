// Release one or more themes: re-test, write blueprint, export static demo, deploy, record URL in BUILD-STATUS.md.
// Usage: node tools/release.mjs <slug> [<slug> ...]   (add --skip-test to trust an existing passing report)
import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';

const ROOT = path.resolve(import.meta.dirname, '..');
const skipTest = process.argv.includes('--skip-test');
const slugs = process.argv.slice(2).filter(a => !a.startsWith('--'));
const run = (script, ...args) => {
  const r = spawnSync('node', [path.join(ROOT, 'tools', script), ...args], { cwd: ROOT, encoding: 'utf8', maxBuffer: 1 << 26, timeout: 35 * 60 * 1000, killSignal: 'SIGKILL' });
  return { ok: r.status === 0, out: (r.stdout || '') + (r.stderr || '') };
};
const setStatus = (slug, status, url = '') => {
  const p = path.join(ROOT, 'BUILD-STATUS.md');
  const lines = fs.readFileSync(p, 'utf8').split('\n').map(l => {
    const cells = l.split('|');
    if (cells.length > 6 && cells[2].trim() === slug) { cells[5] = ` ${status} `; cells[6] = ` ${url} `; return cells.join('|'); }
    return l;
  });
  fs.writeFileSync(p, lines.join('\n'));
};

for (const slug of slugs) {
  console.log(`\n== ${slug}`);
  if (!skipTest) {
    const t = run('test-theme.mjs', slug, '--quick');
    const summary = t.out.trim().split('\n').pop();
    console.log(summary);
    if (!t.ok) { const fails = t.out.split('\n').filter(l => l.startsWith('FAIL')); console.log(fails.length ? fails.join('\n') : t.out.split('\n').slice(-30).join('\n')); setStatus(slug, 'failed test'); continue; }
  }
  setStatus(slug, 'tested');
  run('make-blueprint.mjs', slug);
  const e = run('export-static.mjs', slug);
  console.log(e.out.trim().split('\n').pop());
  if (!e.ok) { setStatus(slug, 'export failed'); continue; }
  const d = run('deploy.mjs', slug);
  const url = d.out.trim().split('\n').pop();
  if (!d.ok || !url.startsWith('https://')) { console.log(d.out.slice(-800)); setStatus(slug, 'deploy failed'); continue; }
  const check = spawnSync('curl', ['-s', '-o', '/dev/null', '-w', '%{http_code}', url + '/'], { encoding: 'utf8' }).stdout;
  setStatus(slug, check === '200' ? 'deployed' : `deployed (HTTP ${check})`, url);
  console.log(`live: ${url} (${check})`);
}
