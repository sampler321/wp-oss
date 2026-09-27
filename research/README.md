# wp-oss research

Research for a library of open-source, native WordPress block themes for small independent businesses, creatives and organisations.

## Read first
- **`THEME-IDEAS.md`**: the main document. It covers what stock WordPress can do, the plugin toolkit, a list of site types across 30 sectors, and **310 theme ideas**. Each idea has real-world basis sites, a signature feature seen on a live site, nice-to-haves, a full style brief, deep-link refs and desktop and mobile screenshots. It ends with the shared companion blocks, the library structure, the release checks and a suggested first wave of 20 themes.
- **`ANTI-VIBE.md`**: 263 visual traits that make a site look AI-built or vibe-coded, with what to do instead, and a 53-question release check.
- **`ANTI-VIBE-FIELD-STUDY.md`**: measurements from 65 live AI-built sites against 12 hand-built ones, plus 40 lint rules.
- **`ANTI-AI-WRITING.md`**: writing tells: the em dash ban, AI vocabulary, emphasis by negation, voice briefs with before and after samples, demo-content rules and a 30-question checklist.
- **`FONT-REGISTRY.md`**: one unique display font per theme (310 of 310). New themes claim a font here first.

## Folders
- `parts/`: source files that `tools/assemble.py` combines into `THEME-IDEAS.md`. `parts/SPEC.md` is the entry format and the rules. `parts/archive/` holds the superseded first drafts of ideas 01–84.
- `screenshots/`: `NNN-k.jpg` (desktop 1440×900) and `NNN-k-m.jpg` (mobile), plus `manifest.json` with status and blocked flags. `screenshots/anti-vibe/` holds the field-study captures.
- `tools/`:
  - `shots.mjs`: batch screenshots of every Refs link (`--redo=ids.txt` to re-shoot).
  - `copylint.mjs`: the AI-writing linter (`--research` relaxes rules meant for shipped copy).
  - `assemble.py`: rebuilds `THEME-IDEAS.md`.
  - `antivibe/`: field-study scripts.

## Rebuild
```
cd research
node tools/shots.mjs parts/*-ideas-*.md     # capture any new or changed refs
python3 tools/assemble.py                   # rebuild THEME-IDEAS.md
node tools/copylint.mjs --research THEME-IDEAS.md
```
