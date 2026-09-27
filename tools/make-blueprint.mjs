// Write demos/<slug>/blueprint.json: boots the theme from GitHub in WordPress Playground with its demo content.
// Usage: node tools/make-blueprint.mjs <slug>
import fs from 'node:fs';
import path from 'node:path';
import { blueprintFor, ROOT } from './lib/playground.mjs';
const slug = process.argv[2];
const bp = blueprintFor(slug, { local: false, repo: process.env.WPOSS_REPO || 'sampler321/wp-oss', ref: 'main' });
bp.login = true;
fs.writeFileSync(path.join(ROOT, 'demos', slug, 'blueprint.json'), JSON.stringify(bp, null, 2) + '\n');
console.log(`wrote demos/${slug}/blueprint.json`);
