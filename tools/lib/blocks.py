"""Helpers that emit core block markup for templates, parts and patterns.

The output is close to what WordPress saves. `tools/normalize-blocks.mjs` then re-serialises every file
through WordPress's own block parser, so wrapper classes and inline styles end up canonical. What must be
right here is the *sourced* content: text, image src/alt, captions, link hrefs, table cells, list items.

Usage in a build script:
    import sys; sys.path.insert(0, 'tools/lib'); from blocks import *
    set_theme('ink')
    pattern('hero', 'Hero', 'featured', J(heading('Hello', 1), para('Text')))
"""
import json, os

THEME = {'slug': None, 'dir': None}


def set_theme(slug, root=None):
    THEME['slug'] = slug
    THEME['dir'] = root or os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'themes', slug)


def J(*parts):
    """Join blocks with blank lines. Accepts strings or lists."""
    out = []
    for p in parts:
        if isinstance(p, (list, tuple)):
            out.extend(p)
        elif p:
            out.append(p)
    return '\n\n'.join(out)


def _a(attrs):
    return (' ' + json.dumps(attrs, separators=(',', ':'), ensure_ascii=False)) if attrs else ''


def _cls(base, attrs):
    c = [base]
    if attrs.get('align'):
        c.append('align' + attrs['align'])
    if attrs.get('className'):
        c.append(attrs['className'])
    if attrs.get('textColor'):
        c += ['has-%s-color' % attrs['textColor'], 'has-text-color']
    if attrs.get('backgroundColor'):
        c += ['has-%s-background-color' % attrs['backgroundColor'], 'has-background']
    if attrs.get('fontSize'):
        c.append('has-%s-font-size' % attrs['fontSize'])
    if attrs.get('fontFamily'):
        c.append('has-%s-font-family' % attrs['fontFamily'])
    return ' '.join(x for x in c if x)



def _css_val(v):
    if isinstance(v, str) and v.startswith('var:preset|'):
        _, kind, slug = v.split('|')
        return 'var(--wp--preset--%s--%s)' % (kind, slug)
    return v


def _style(attrs):
    """Inline style WordPress saves for spacing padding/margin and min-height (in attribute order)."""
    st = attrs.get('style') or {}
    out = []
    sp = st.get('spacing') or {}
    for prop in ('padding', 'margin'):
        v = sp.get(prop)
        if isinstance(v, dict):
            for side in v:
                out.append('%s-%s:%s' % (prop, side, _css_val(v[side])))
        elif isinstance(v, str):
            out.append('%s:%s' % (prop, _css_val(v)))
    mh = (st.get('dimensions') or {}).get('minHeight')
    if mh:
        out.append('min-height:%s' % _css_val(mh))
    return (' style="%s"' % ';'.join(out)) if out else ''


def img_url(filename):
    """PHP expression for a theme image (patterns only)."""
    return "<?php echo esc_url( get_theme_file_uri( 'assets/images/%s' ) ); ?>" % filename


# ---- text ----
def para(text, **attrs):
    return '<!-- wp:paragraph%s -->\n<p class="%s">%s</p>\n<!-- /wp:paragraph -->' % (_a(attrs), _cls('', attrs).strip(), text)


def heading(text, level=2, **attrs):
    if level != 2:
        attrs = {'level': level, **attrs}
    return '<!-- wp:heading%s -->\n<h%d class="%s">%s</h%d>\n<!-- /wp:heading -->' % (_a(attrs), level, _cls('wp-block-heading', attrs), text, level)


def lst(items, ordered=False, **attrs):
    if ordered:
        attrs = {'ordered': True, **attrs}
    tag = 'ol' if ordered else 'ul'
    inner = ''.join('<!-- wp:list-item -->\n<li>%s</li>\n<!-- /wp:list-item -->' % i for i in items)
    return '<!-- wp:list%s -->\n<%s class="%s">%s</%s>\n<!-- /wp:list -->' % (_a(attrs), tag, _cls('wp-block-list', attrs), inner, tag)


def quote(text, cite='', **attrs):
    c = ('<cite>%s</cite>' % cite) if cite else ''
    return '<!-- wp:quote%s -->\n<blockquote class="%s">%s%s</blockquote>\n<!-- /wp:quote -->' % (_a(attrs), _cls('wp-block-quote', attrs), para(text), c)


def pullquote(text, cite='', **attrs):
    c = ('<cite>%s</cite>' % cite) if cite else ''
    return '<!-- wp:pullquote%s -->\n<figure class="%s"><blockquote><p>%s</p>%s</blockquote></figure>\n<!-- /wp:pullquote -->' % (_a(attrs), _cls('wp-block-pullquote', attrs), text, c)


def details(summary, body_blocks, **attrs):
    return '<!-- wp:details%s -->\n<details class="%s"><summary>%s</summary>%s</details>\n<!-- /wp:details -->' % (_a(attrs), _cls('wp-block-details', attrs), summary, body_blocks)


def table(rows, head=None, caption='', **attrs):
    th = ('<thead><tr>' + ''.join('<th>%s</th>' % c for c in head) + '</tr></thead>') if head else ''
    tb = '<tbody>' + ''.join('<tr>' + ''.join('<td>%s</td>' % c for c in r) + '</tr>' for r in rows) + '</tbody>'
    cap = ('<figcaption class="wp-element-caption">%s</figcaption>' % caption) if caption else ''
    return '<!-- wp:table%s -->\n<figure class="%s"><table class="has-fixed-layout">%s%s</table>%s</figure>\n<!-- /wp:table -->' % (_a(attrs), _cls('wp-block-table', attrs), th, tb, cap)


def code(text, **attrs):
    return '<!-- wp:code%s -->\n<pre class="%s"><code>%s</code></pre>\n<!-- /wp:code -->' % (_a(attrs), _cls('wp-block-code', attrs), text)


def preformatted(text, **attrs):
    return '<!-- wp:preformatted%s -->\n<pre class="%s">%s</pre>\n<!-- /wp:preformatted -->' % (_a(attrs), _cls('wp-block-preformatted', attrs), text)


def verse(text, **attrs):
    return '<!-- wp:verse%s -->\n<pre class="%s">%s</pre>\n<!-- /wp:verse -->' % (_a(attrs), _cls('wp-block-verse', attrs), text)


def separator(**attrs):
    return '<!-- wp:separator%s -->\n<hr class="%s"/>\n<!-- /wp:separator -->' % (_a(attrs), _cls('wp-block-separator has-alpha-channel-opacity', attrs))


def spacer(height='var:preset|spacing|50'):
    css = height
    if height.startswith('var:preset|spacing|'):
        css = 'var(--wp--preset--spacing--%s)' % height.split('|')[-1]
    return '<!-- wp:spacer {"height":"%s"} -->\n<div style="height:%s" aria-hidden="true" class="wp-block-spacer"></div>\n<!-- /wp:spacer -->' % (height, css)


# ---- media ----
def image(filename, alt, caption='', lightbox=True, href=None, **attrs):
    a = {'sizeSlug': 'large', 'linkDestination': 'custom' if href else 'none', **attrs}
    if lightbox and not href:
        a['lightbox'] = {'enabled': True}
    cap = ('<figcaption class="wp-element-caption">%s</figcaption>' % caption) if caption else ''
    src = img_url(filename) if not filename.startswith(('http', '<?php', '/')) else filename
    im = '<img src="%s" alt="%s"/>' % (src, alt)
    if href:
        im = '<a href="%s">%s</a>' % (href, im)
    return '<!-- wp:image%s -->\n<figure class="%s">%s%s</figure>\n<!-- /wp:image -->' % (_a(a), _cls('wp-block-image size-large', a), im, cap)


def cover(filename, inner, dim=40, min_height=None, overlay='contrast', **attrs):
    src = img_url(filename)
    a = {'url': src, 'dimRatio': dim, 'overlayColor': overlay, 'isUserOverlayColor': True, **attrs}
    if min_height:
        a['minHeight'] = min_height
        a['minHeightUnit'] = 'vh'
    return ('<!-- wp:cover%s -->\n<div class="%s"><span aria-hidden="true" class="wp-block-cover__background has-%s-background-color has-background-dim-%d has-background-dim"></span>'
            '<img class="wp-block-cover__image-background" alt="" src="%s" data-object-fit="cover"/><div class="wp-block-cover__inner-container">%s</div></div>\n<!-- /wp:cover -->') % (
        _a(a), _cls('wp-block-cover', a), overlay, dim, src, inner)


def gallery(images, columns=3, **attrs):
    """images: list of (filename, alt, caption)."""
    a = {'columns': columns, 'linkTo': 'none', **attrs}
    inner = '\n\n'.join(image(f, alt, cap) for f, alt, cap in images)
    return '<!-- wp:gallery%s -->\n<figure class="%s">%s</figure>\n<!-- /wp:gallery -->' % (_a(a), _cls('wp-block-gallery has-nested-images columns-%d is-cropped' % columns, a), inner)


def media_text(filename, alt, inner, right=False, width=50, **attrs):
    a = {'mediaType': 'image', 'mediaWidth': width, **attrs}
    if right:
        a['mediaPosition'] = 'right'
    return ('<!-- wp:media-text%s -->\n<div class="%s"><figure class="wp-block-media-text__media"><img src="%s" alt="%s" class="size-full"/></figure>'
            '<div class="wp-block-media-text__content">%s</div></div>\n<!-- /wp:media-text -->') % (
        _a(a), _cls('wp-block-media-text is-stacked-on-mobile' + (' has-media-on-the-right' if right else ''), a), img_url(filename), alt, inner)


def embed(url, provider='youtube', type_='video', **attrs):
    a = {'url': url, 'type': type_, 'providerNameSlug': provider, 'responsive': True, **attrs}
    return ('<!-- wp:embed%s -->\n<figure class="wp-block-embed is-type-%s is-provider-%s wp-block-embed-%s"><div class="wp-block-embed__wrapper">\n%s\n</div></figure>\n<!-- /wp:embed -->') % (
        _a(a), type_, provider, provider, url)


def audio(src, caption='', **attrs):
    cap = ('<figcaption class="wp-element-caption">%s</figcaption>' % caption) if caption else ''
    return '<!-- wp:audio%s -->\n<figure class="wp-block-audio"><audio controls src="%s"></audio>%s</figure>\n<!-- /wp:audio -->' % (_a(attrs), src, cap)


# ---- design ----
def group(inner, tag='div', layout='constrained', **attrs):
    a = dict(attrs)
    if tag != 'div':
        a = {'tagName': tag, **a}
    if layout:
        a['layout'] = layout if isinstance(layout, dict) else {'type': layout}
    anchor = (' id="%s"' % a['anchor']) if a.get('anchor') else ''
    return '<!-- wp:group%s -->\n<%s%s class="%s"%s>%s</%s>\n<!-- /wp:group -->' % (_a(a), tag, anchor, _cls('wp-block-group', a), _style(a), inner, tag)


def row(inner, justify=None, wrap=True, **attrs):
    lay = {'type': 'flex', 'flexWrap': 'wrap' if wrap else 'nowrap'}
    if justify:
        lay['justifyContent'] = justify
    return group(inner, layout=lay, **attrs)


def stack(inner, **attrs):
    return group(inner, layout={'type': 'flex', 'orientation': 'vertical'}, **attrs)


def grid(inner, min_width='16rem', **attrs):
    return group(inner, layout={'type': 'grid', 'minimumColumnWidth': min_width}, **attrs)


def columns(*cols, **attrs):
    """cols: (width or None, inner) tuples."""
    out = []
    for w, c in cols:
        if w:
            out.append('<!-- wp:column {"width":"%s"} -->\n<div class="wp-block-column" style="flex-basis:%s">%s</div>\n<!-- /wp:column -->' % (w, w, c))
        else:
            out.append('<!-- wp:column -->\n<div class="wp-block-column">%s</div>\n<!-- /wp:column -->' % c)
    return '<!-- wp:columns%s -->\n<div class="%s"%s>%s</div>\n<!-- /wp:columns -->' % (_a(attrs), _cls('wp-block-columns', attrs), _style(attrs), '\n\n'.join(out))


def buttons(*btns, **attrs):
    """btns: (label, url) or (label, url, {button attrs})."""
    inner = []
    for b in btns:
        label, url = b[0], b[1]
        ba = b[2] if len(b) > 2 else {}
        inner.append('<!-- wp:button%s -->\n<div class="%s"><a class="wp-block-button__link wp-element-button" href="%s">%s</a></div>\n<!-- /wp:button -->' % (_a(ba), _cls('wp-block-button', ba), url, label))
    return '<!-- wp:buttons%s -->\n<div class="%s">%s</div>\n<!-- /wp:buttons -->' % (_a(attrs), _cls('wp-block-buttons', attrs), '\n\n'.join(inner))


def social(links, **attrs):
    """links: list of (service, url)."""
    inner = ''.join('<!-- wp:social-link {"url":"%s","service":"%s"} /-->' % (u, s) for s, u in links)
    return '<!-- wp:social-links%s -->\n<ul class="%s">%s</ul>\n<!-- /wp:social-links -->' % (_a(attrs), _cls('wp-block-social-links', attrs), inner)


# ---- dynamic (no saved HTML) ----
def dyn(name, **attrs):
    return '<!-- wp:%s%s /-->' % (name, _a(attrs))


def pattern_ref(slug):
    return '<!-- wp:pattern {"slug":"%s/%s"} /-->' % (THEME['slug'], slug)


def template_part(slug, tag=None):
    a = {'slug': slug}
    if tag:
        a['tagName'] = tag
    return dyn('template-part', **a)


def query(inner_template, per_page=6, category=None, query_id=1, columns_=None, layout=None, pagination=False, no_results='Nothing here yet.', template_class=None, **attrs):
    """inner_template: blocks inside post-template. category: term id placeholder not known at build time, so use className+'taxQuery' only when known."""
    q = {'perPage': per_page, 'pages': 0, 'offset': 0, 'postType': 'post', 'order': 'desc', 'orderBy': 'date', 'inherit': False}
    if category is not None:
        q['taxQuery'] = {'category': [category]} if isinstance(category, int) else None
    a = {'queryId': query_id, 'query': q, **attrs}
    pt_attrs = {}
    if template_class:
        pt_attrs['className'] = template_class
    if layout:
        pt_attrs['layout'] = layout
    pt = '<!-- wp:post-template%s -->\n%s\n<!-- /wp:post-template -->' % (_a(pt_attrs), inner_template)
    pag = ''
    if pagination:
        pag = '\n\n<!-- wp:query-pagination -->\n<!-- wp:query-pagination-previous /-->\n\n<!-- wp:query-pagination-numbers /-->\n\n<!-- wp:query-pagination-next /-->\n<!-- /wp:query-pagination -->'
    nr = '\n\n<!-- wp:query-no-results -->\n%s\n<!-- /wp:query-no-results -->' % para(no_results)
    return '<!-- wp:query%s -->\n<div class="wp-block-query">%s%s%s</div>\n<!-- /wp:query -->' % (_a(a), pt, pag, nr)


def inherit_query(inner_template, layout=None, template_class=None, **attrs):
    a = {'queryId': 0, 'query': {'perPage': 12, 'pages': 0, 'offset': 0, 'postType': 'post', 'order': 'desc', 'orderBy': 'date', 'inherit': True}, **attrs}
    pt_attrs = {}
    if template_class:
        pt_attrs['className'] = template_class
    if layout:
        pt_attrs['layout'] = layout
    return ('<!-- wp:query%s -->\n<div class="wp-block-query"><!-- wp:post-template%s -->\n%s\n<!-- /wp:post-template -->\n\n'
            '<!-- wp:query-pagination -->\n<!-- wp:query-pagination-previous /-->\n\n<!-- wp:query-pagination-numbers /-->\n\n<!-- wp:query-pagination-next /-->\n<!-- /wp:query-pagination -->\n\n'
            '<!-- wp:query-no-results -->\n%s\n<!-- /wp:query-no-results --></div>\n<!-- /wp:query -->') % (_a(a), _a(pt_attrs), inner_template, para('Nothing matches that yet.'))


# ---- file writers ----
def pattern(slug, title, categories, body, block_types=None, inserter=True, description='', post_types=None, template_types=None, keywords=None):
    h = ['<?php', '/**', ' * Title: %s' % title, ' * Slug: %s/%s' % (THEME['slug'], slug), ' * Categories: %s' % categories]
    if description:
        h.append(' * Description: %s' % description)
    if keywords:
        h.append(' * Keywords: %s' % keywords)
    if block_types:
        h.append(' * Block Types: %s' % block_types)
    if post_types:
        h.append(' * Post Types: %s' % post_types)
    if template_types:
        h.append(' * Template Types: %s' % template_types)
    if not inserter:
        h.append(' * Inserter: no')
    h += [' */', '?>']
    path = os.path.join(THEME['dir'], 'patterns', slug + '.php')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(h) + '\n' + body.strip() + '\n')


def write(relpath, content):
    path = os.path.join(THEME['dir'], relpath)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')


def page_template(main_inner, header='header', footer='footer', **main_attrs):
    main = group(main_inner, tag='main', **main_attrs)
    return J(template_part(header, 'header'), main, template_part(footer, 'footer'))
