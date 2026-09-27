// Boot a WordPress Playground server for one theme, with its demo content built.
// import { startSite } from './lib/playground.mjs'; const site = await startSite('ink', { port: 9500 }); ... await site.stop();
import { spawn } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import net from 'node:net';

export const ROOT = path.resolve(import.meta.dirname, '..', '..');

async function freePort(start) {
  for (let p = start; p < start + 200; p++) {
    const tryHost = host => new Promise(res => { const s = net.createServer().once('error', () => res(false)).once('listening', () => s.close(() => res(true))).listen(p, host); });
    if ((await tryHost('127.0.0.1')) && (await tryHost('::'))) return p;
  }
  throw new Error('no free port');
}

export function blueprintFor(slug, { local = true, repo = 'sampler321/wp-oss', ref = 'main' } = {}) {
  const demoPath = path.join(ROOT, 'demos', slug, 'content.json');
  const demo = fs.existsSync(demoPath) ? JSON.parse(fs.readFileSync(demoPath, 'utf8')) : {};
  const steps = [];
  if (demo.products?.length) {
    steps.push({ step: 'installPlugin', pluginData: { resource: 'wordpress.org/plugins', slug: 'woocommerce' }, options: { activate: true } });
  }
  if (local) {
    steps.push({ step: 'activateTheme', themeFolderName: slug });
  } else {
    steps.push({ step: 'installTheme', themeData: { resource: 'git:directory', url: `https://github.com/${repo}`, ref, path: `themes/${slug}` }, options: { activate: true, targetFolderName: slug } });
    steps.push({ step: 'writeFile', path: '/wordpress/wp-content/demo-data/content.json', data: { resource: 'url', url: `https://raw.githubusercontent.com/${repo}/${ref}/demos/${slug}/content.json` } });
    steps.push({ step: 'writeFile', path: '/wordpress/wp-content/demo-lib/demo-builder.php', data: { resource: 'url', url: `https://raw.githubusercontent.com/${repo}/${ref}/tools/lib/demo-builder.php` } });
  }
  steps.push({ step: 'runPHP', code: "<?php require '/wordpress/wp-load.php'; require '/wordpress/wp-content/demo-lib/demo-builder.php'; wposs_build_demo('/wordpress/wp-content/demo-data/content.json');" });
  return { $schema: 'https://playground.wordpress.net/blueprint-schema.json', landingPage: '/', preferredVersions: { php: '8.3', wp: 'latest' }, features: { networking: true }, steps };
}

export async function startSite(slug, { port = 9500, verbose = false, extraMounts = [] } = {}) {
  port = await freePort(port);
  const cache = path.join(ROOT, '.cache', 'playground');
  fs.mkdirSync(cache, { recursive: true });
  const bpPath = path.join(cache, `blueprint-${slug}.json`);
  fs.writeFileSync(bpPath, JSON.stringify(blueprintFor(slug, { local: true }), null, 2));
  const args = ['@wp-playground/cli', 'server', `--port=${port}`, '--workers=2', '--wp=latest', '--php=8.3',
    `--mount=${path.join(ROOT, 'themes', slug)}:/wordpress/wp-content/themes/${slug}`,
    `--mount=${path.join(ROOT, 'demos', slug)}:/wordpress/wp-content/demo-data`,
    `--mount=${path.join(ROOT, 'tools', 'lib')}:/wordpress/wp-content/demo-lib`,
    ...extraMounts.map(m => `--mount=${m}`),
    `--blueprint=${bpPath}`, '--define-bool', 'WP_DEBUG', 'true', '--define-bool', 'WP_DEBUG_DISPLAY', 'true'];
  const child = spawn('npx', args, { cwd: path.join(ROOT, 'tools'), stdio: ['ignore', 'pipe', 'pipe'], detached: true });
  const killTree = sig => { try { process.kill(-child.pid, sig); } catch {} };
  process.once('exit', () => killTree('SIGKILL'));
  let log = '';
  const url = `http://127.0.0.1:${port}`;
  await new Promise((resolve, reject) => {
    const timer = setTimeout(() => reject(new Error(`Playground did not start in 6 min for ${slug}\n${log.slice(-3000)}`)), 360000);
    const onData = d => {
      log += d.toString();
      if (verbose) process.stdout.write(d);
      if (/Ready!|listening|WordPress is running/i.test(log)) { clearTimeout(timer); resolve(); }
    };
    child.stdout.on('data', onData);
    child.stderr.on('data', onData);
    child.on('exit', code => { clearTimeout(timer); reject(new Error(`Playground exited (${code}) for ${slug}\n${log.slice(-3000)}`)); });
  });
  return {
    url, port, log: () => log,
    stop: () => new Promise(res => { child.removeAllListeners('exit'); child.once('exit', res); killTree('SIGTERM'); setTimeout(() => { killTree('SIGKILL'); res(); }, 5000); }),
  };
}
