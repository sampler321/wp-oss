"""Add missing inline padding/margin styles to group/columns blocks whose attributes declare them.

Usage: python3 tools/repair-inline-spacing.py [slug ...]   (default: all themes)
"""
import glob, json, os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib'))
from blocks import _style

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
slugs = sys.argv[1:] or sorted(os.listdir(os.path.join(ROOT, 'themes')))
RE = re.compile(r'<!-- wp:(group|columns) (\{.*?\}) -->\n<(\w+)((?: [\w-]+="[^"]*")*)>')
fixed = 0
for slug in slugs:
    for f in glob.glob(os.path.join(ROOT, 'themes', slug, '*', '*.html')) + glob.glob(os.path.join(ROOT, 'themes', slug, 'patterns', '*.php')):
        src = open(f, encoding='utf-8').read()
        def fix(m):
            global fixed
            try:
                attrs = json.loads(m.group(2))
            except Exception:
                return m.group(0)
            want = _style(attrs)
            if not want or ' style="' in m.group(4):
                return m.group(0)
            fixed += 1
            return m.group(0)[:-1] + want + '>'
        out = RE.sub(fix, src)
        if out != src:
            open(f, 'w', encoding='utf-8').write(out)
            print('fixed', os.path.relpath(f, ROOT))
print('blocks fixed:', fixed)
