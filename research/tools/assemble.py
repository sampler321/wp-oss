"""Assemble research/THEME-IDEAS.md from the part files and insert screenshots under each Refs list.

Usage: python3 tools/assemble.py   (run from anywhere)
"""
import json, os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PARTS = os.path.join(ROOT, 'parts')
SHOTS = os.path.join(ROOT, 'screenshots')
ORDER = ['01-foundations.md', '01b-part4-intro.md', '02r-ideas-001-042.md', '03r-ideas-043-084.md', '05-ideas-085-110.md',
         '06-ideas-111-134.md', '07-ideas-135-160.md', '08-ideas-161-188.md', '09-ideas-189-218.md',
         '10-ideas-219-248.md', '11-ideas-249-280.md', '12-ideas-281-310.md', '13-shared-and-roadmap.md']

manifest = json.load(open(os.path.join(SHOTS, 'manifest.json')))


def shots_block(idea, refs):
    cells = []
    for k, title in refs:
        rid = f'{idea}-{k}'
        m = manifest.get(rid, {})
        d, mob = f'{rid}.jpg', f'{rid}-m.jpg'
        if not m.get('ok') or m.get('blocked') or not os.path.exists(os.path.join(SHOTS, d)):
            continue
        img = f'<a href="screenshots/{d}"><img src="screenshots/{d}" width="300" alt="Screenshot: {title}"></a>'
        if os.path.exists(os.path.join(SHOTS, mob)):
            img += f' <a href="screenshots/{mob}"><img src="screenshots/{mob}" width="90" alt="Mobile screenshot: {title}"></a>'
        cells.append(img)
    if not cells:
        return []
    return ['', '**Screens** (desktop + mobile, click to enlarge):', '', '<p>' + '<br>\n'.join(cells) + '</p>', '']


out, toc = [], []
for name in ORDER:
    lines = open(os.path.join(PARTS, name), encoding='utf-8').read().split('\n')
    idea, refs, in_refs = None, [], False
    for i, line in enumerate(lines):
        h = re.match(r'^#### (\d{3}) · (.*)', line)
        if h:
            idea = h.group(1)
            toc.append(f'- [{idea} · {h.group(2)}](#{idea})')
            out.append(f'<a id="{idea}"></a>')
        s = re.match(r'^### ([IVXL]+\. .*)', line)
        if s:
            toc.append(f'\n**{s.group(1)}**\n')
        if line.startswith('**Refs:**'):
            in_refs, refs = True, []
            out.append(line)
            continue
        if in_refs:
            r = re.match(r'^\s*-\s*\[([^\]]+)\]\((https?://[^)\s]+)\)', line)
            if r:
                refs.append((len(refs) + 1, r.group(1).replace('"', "'")))
                out.append(line)
                continue
            if line.strip() == '' and i + 1 < len(lines) and re.match(r'^\s*-\s*\[', lines[i + 1]):
                out.append(line)
                continue
            out.extend(shots_block(idea, refs))
            in_refs = False
        out.append(line)
    if in_refs:
        out.extend(shots_block(idea, refs))

doc = '\n'.join(out)
# Insert the idea index after the ground rules (before Part 1).
marker = '## Part 1:'
idx = doc.index(marker)
index = '## Index of the 310 ideas\n' + '\n'.join(toc) + '\n\n---\n\n'
doc = doc[:idx] + index + doc[idx:]
doc = doc.replace('\n\n\n\n', '\n\n')
open(os.path.join(ROOT, 'THEME-IDEAS.md'), 'w', encoding='utf-8').write(doc)
n_imgs = doc.count('<img src="screenshots/')
print(f'THEME-IDEAS.md: {len(doc.splitlines())} lines, {doc.count(chr(10) + "#### ")} ideas, {n_imgs} images, em dashes: {doc.count(chr(0x2014))}')
