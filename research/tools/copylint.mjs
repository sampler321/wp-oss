// Copy linter for AI-writing tells. See research/ANTI-AI-WRITING.md section 7.
// Usage: node copylint.mjs <files or dirs...> [--research]
//   --research: relax rules meant only for shipped copy (headings, bold lists, openers)
// Exit code 1 if any severity-5 finding.
import fs from 'node:fs';
import path from 'node:path';

const TIER_A = ['delve', 'delves', 'delving', 'tapestry', 'testament', 'realm', 'realms', 'pivotal', 'underscore', 'underscores', 'underscoring', 'showcase', 'showcases', 'showcasing', 'boasts', 'meticulous', 'meticulously', 'intricate', 'intricacies', 'interplay', 'bolster', 'bolstered', 'garner', 'garnered', 'foster', 'fostering', 'vibrant', 'nestled', 'in the heart of', 'seamless', 'seamlessly', 'elevate', 'elevates', 'unlock', 'unlocking', 'unveil', 'unveiling', 'unparalleled', 'transformative', 'groundbreaking', 'commendable', 'multifaceted', 'embark', 'harness', 'leverage', 'leverages', 'empower', 'empowers', 'elucidate', 'encapsulate', 'paving the way', 'uncharted', 'diverse array', 'enduring legacy', 'indelible mark', 'deeply rooted', 'evolving landscape', 'stands as a', 'serves as a', 'is a testament', 'plays a crucial role', 'plays a pivotal role', 'plays a vital role', 'resonate with', 'rich tapestry', 'symphony of'];
const TIER_B = ['crucial', 'enhance', 'robust', 'valuable', 'notable', 'remarkable', 'innovative', 'exceptional', 'compelling', 'comprehensive', 'curated', 'bespoke', 'passionate', 'world-class', 'cutting-edge', 'state-of-the-art', 'next-level', 'game-changer', 'effortless', 'effortlessly', 'supercharge', 'streamline', 'holistic', 'synergy', 'solutions', 'journey', 'haven', 'hidden gem'];
const TIER_C = ['collaborate', 'facilitate', 'utilise', 'utilize', 'initiate', 'liaise', 'incentivise', 'one-stop shop'];
const CHATBOT = [/hope this helps/i, /feel free to/i, /let'?s dive/i, /here'?s the thing/i, /in today'?s\b/i, /\bwhether you'?re\b/i, /look no further/i, /rest assured/i, /in conclusion/i, /in summary,/i, /take (your|it) \w+ to the next level/i];
const PARALLEL = [
  /\bnot (just|only|merely|simply)\b[^.\n]{0,60}\b(but|it'?s|they'?re|we'?re)\b/i,
  /\b(isn'?t|aren'?t|wasn'?t|doesn'?t|don'?t|won'?t) (just|simply|merely|only)\b/i,
  /\bit'?s not (about )?[^.\n]{1,40}[.,;:]\s*it'?s\b/i,
  /\bthis (isn'?t|is not) (just |another |your )/i,
  /\b(we|they)'?re not (your|just|another|like) /i,
  /(^|[.!?]\s+)not an? [a-z]+( [a-z]+)?\.\s+an? [a-z]+/i,
  /\bno \w+, no \w+(,? (just|only|and no)\b)?/i,
  /(^|[.!?]\s+)(zero|no) (compromises?|fluff|nonsense|filler|shortcuts?|gimmicks?|bs|hassle|catch|strings attached)\b/i,
  /\ball the \w+,? without the\b/i,
  /\bless \w+, more \w+/i,
  /(^|[.!?]\s+)(forget|say goodbye to) /i,
  /\?\s*(not here|never|nope)\b/i,
  /\bmore than (just )?an? [a-z]+\b(?=[.:\n]|$)/i,
];
const OPENERS = /(^|[.!?]\s+)(Additionally|Furthermore|Moreover|Ultimately|Notably|Importantly),/g;
const PLACEHOLDER = /\[(Your|Insert|Company|Name|Business)[^\]]*\](?!\()/g;
const EMOJI = /\p{Extended_Pictographic}/gu;

const research = process.argv.includes('--research');
const inputs = process.argv.slice(2).filter(a => !a.startsWith('--'));
const exts = new Set(['.md', '.php', '.html', '.txt', '.json', '.xml']);
const files = inputs.flatMap(p => fs.statSync(p).isDirectory()
  ? fs.readdirSync(p, { recursive: true }).map(f => path.join(p, f)).filter(f => exts.has(path.extname(f)) && fs.statSync(f).isFile())
  : [p]);

const wordRe = w => new RegExp(`\\b${w.replace(/[-]/g, '[- ]')}\\b`, 'gi');
let sev5 = 0;
const out = [];

for (const file of files) {
  let text = fs.readFileSync(file, 'utf8');
  // Ignore URLs, code spans and fenced code, which aren't prose.
  // Skip quoted bad examples between <!-- copylint-off --> and <!-- copylint-on -->.
  text = text.replace(/<!-- copylint-off -->[\s\S]*?<!-- copylint-on -->/g, m => m.replace(/[^\n]/g, ''));
  // Terms of art that contain a banned word.
  text = text.replace(/\bseamless (paper|backdrop|backdrops|background)\b/gi, 'paper backdrop')
    .replace(/\bfoster(ing)? (carers?|homes?|famil(y|ies)|parents?|placements?|care|dogs?|cats?|animals?|network|scheme|team|applications?)\b/gi, 'carer $2')
    .replace(/\bpage-fostering\b/g, 'page-carers');
  const prose = text.replace(/```[\s\S]*?```/g, '').replace(/`[^`]*`/g, '').replace(/https?:\/\/\S+/g, '').replace(/<!--[\s\S]*?-->/g, '').replace(/<[^>\n]+>/g, '');
  const lines = prose.split('\n');
  const find = (sev, rule, re) => lines.forEach((l, i) => { for (const m of l.matchAll(re)) out.push({ file, line: i + 1, sev, rule, hit: m[0].trim().slice(0, 60) }); });

  find(5, 'em dash', /—/g);
  find(5, 'spaced dash as em dash', /(?<=[^\s\d])\s[–-]\s(?![\d])/g);
  for (const w of TIER_A) find(5, 'tier A word', wordRe(w));
  for (const re of CHATBOT) find(5, 'chatbot phrase', new RegExp(re.source, 'gi'));
  for (const re of PARALLEL) find(research ? 3 : 5, 'emphasis by negation', new RegExp(re.source, 'gi'));
  find(5, 'placeholder bracket', PLACEHOLDER);
  find(research ? 3 : 5, 'emoji', EMOJI);
  for (const w of TIER_C) find(2, 'GOV.UK word to avoid', wordRe(w));
  if (!research) {
    find(4, 'AI sentence opener', OPENERS);
    find(4, 'hard-coded year', /©\s?20\d\d/g);
  }

  // Density rules
  const words = prose.split(/\s+/).filter(Boolean).length || 1;
  for (const w of TIER_B) {
    const n = (prose.match(wordRe(w)) || []).length;
    if (n > Math.max(1, Math.floor(words / 300))) out.push({ file, line: 0, sev: 3, rule: 'tier B word density', hit: `${w} ×${n}` });
  }
  if (!research) {
    const excl = (prose.match(/!(?=\s|$)/g) || []).length;
    if (excl > 1) out.push({ file, line: 0, sev: 3, rule: 'exclamation marks', hit: `×${excl}` });
    const sentences = prose.replace(/\n+/g, ' ').split(/(?<=[.!?])\s+/).map(s => s.split(/\s+/).length).filter(n => n > 2);
    if (sentences.length >= 5) {
      const mean = sentences.reduce((a, b) => a + b, 0) / sentences.length;
      const sd = Math.sqrt(sentences.reduce((a, b) => a + (b - mean) ** 2, 0) / sentences.length);
      if (sd / mean < 0.35) out.push({ file, line: 0, sev: 3, rule: 'uniform sentence length', hit: `CV ${(sd / mean).toFixed(2)}` });
    }
  }
}

out.sort((a, b) => b.sev - a.sev || a.file.localeCompare(b.file) || a.line - b.line);
for (const f of out) {
  if (f.sev === 5) sev5++;
  console.log(`S${f.sev}  ${path.relative(process.cwd(), f.file)}:${f.line}  ${f.rule}  "${f.hit}"`);
}
console.log(`\n${out.length} findings, ${sev5} at severity 5, ${files.length} files`);
process.exit(sev5 ? 1 : 0);
