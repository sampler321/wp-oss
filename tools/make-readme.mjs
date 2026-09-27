// Generate themes/<slug>/readme.txt from style.css, .fonts.json, .images.json and an optional demos/<slug>/readme-extra.md.
// Usage: node tools/make-readme.mjs <slug>
import fs from 'node:fs';
import path from 'node:path';

const slug = process.argv[2];
const ROOT = path.resolve(import.meta.dirname, '..');
const dir = path.join(ROOT, 'themes', slug);
const css = fs.readFileSync(path.join(dir, 'style.css'), 'utf8');
const h = k => (css.match(new RegExp(`^${k}:\\s*(.+)$`, 'm')) || [])[1]?.trim() || '';
const fonts = fs.existsSync(path.join(dir, '.fonts.json')) ? JSON.parse(fs.readFileSync(path.join(dir, '.fonts.json'), 'utf8')) : { fontFamilies: [], credits: [] };
const images = fs.existsSync(path.join(dir, '.images.json')) ? JSON.parse(fs.readFileSync(path.join(dir, '.images.json'), 'utf8')) : {};
const extraPath = path.join(ROOT, 'demos', slug, 'readme-extra.md');
const extra = fs.existsSync(extraPath) ? fs.readFileSync(extraPath, 'utf8').trim() + '\n\n' : '';
const used = new Set(fs.readdirSync(path.join(dir, 'assets', 'images')).filter(f => !f.startsWith('.')).map(f => f.replace(/\.[^.]+$/, '')));

const lines = [
  `=== ${h('Theme Name')} ===`,
  `Contributors: wp-oss`,
  `Requires at least: ${h('Requires at least')}`,
  `Tested up to: ${h('Tested up to')}`,
  `Requires PHP: ${h('Requires PHP')}`,
  `Stable tag: ${h('Version')}`,
  `License: GPLv2 or later`,
  `License URI: https://www.gnu.org/licenses/gpl-2.0.html`,
  '',
  h('Description'),
  '',
  '== Description ==',
  '',
  h('Description'),
  '',
  extra + 'Every colour, font, size and spacing value lives in theme.json, so the whole look can be changed in Appearance > Editor > Styles. The theme uses only core WordPress blocks.',
  '',
  'Demo content: https://github.com/sampler321/wp-oss/tree/main/demos/' + slug,
  '',
  '== Changelog ==',
  '',
  `= ${h('Version')} =`,
  '* First release.',
  '',
  '== Copyright ==',
  '',
  `${h('Theme Name')} WordPress Theme, (C) ${new Date().getFullYear()} WP-OSS.`,
  `${h('Theme Name')} is distributed under the terms of the GNU GPL v2 or later.`,
  '',
  '== Resources ==',
  '',
  ...fonts.credits.map(c => `* Font: ${c}`),
  ...Object.entries(images).filter(([k]) => used.has(k)).map(([k, v]) => `* Image ${k}.jpg: "${v.title.replace(/\s+[-–—]\s+/g, ': ').replace(/\u2014/g, ',')}" by ${String(v.creator).replace(/\s+[-–—]\s+/g, ', ').replace(/\u2014/g, ',')}, ${v.license}, ${v.url}`),
  '',
];
fs.writeFileSync(path.join(dir, 'readme.txt'), lines.join('\n'));
const missing = [...used].filter(k => !images[k]);
if (missing.length) console.log('WARNING: images without credits:', missing.join(', '));
console.log(`wrote themes/${slug}/readme.txt`);
