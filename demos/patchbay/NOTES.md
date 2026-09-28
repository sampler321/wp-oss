# patchbay: notes

- Direction: the owner asked for "something DIY, like jhspedals.info", which overrides the research's 1-bit dither look. Patchbay Pedals (Kemi Adeyemi and Rob Hartley, a railway arch in Leeds) gets JHS's flat saturated colour grounds and big product squares, crossed with the maker's bench: panel drawings with dimension lines, a signal-chain nav, boxed spec legends and versioned build docs.
- Fonts: Chubbo (Fontshare, chunky, like pedal silkscreen) for display, IBM Plex Sans for everything else. The research face, Doto, is a monospaced dot-matrix face and is out under the no-monospace rule. Two families. Chubbo is claimed in demos/patchbay/fonts-claim.txt for the registry.
- Palette: panel white #FAFAF7, ink #141414, fuzz red #C8211A for links; teal #0E9C9A, yellow #F2B90F and orange #E8622C only as flat grounds. 3px black outlines, 18px enclosure radius on panels, 6px on buttons, hard offset shadow on the spec legend only.
- Signature: the new-release block (panel drawing, "docs and power" legend, assembled vs kit prices side by side, versioned document table). Nice-to-haves built: fault table before the repair steps, retired pedals' manuals kept online, dealer directory by country, parts-substitution note, custom artwork lead time.
- Images: CC0 Commons photos of parts, a kit, an iron, a breadboard, a schematic, an amp and rigs. The commercial pedals on Commons are all other brands (Danelectro, Boss, EHX), so product images are panel and PCB drawings made for this theme by build/patchbay_draw.py (CC0), not photos of someone else's pedals.
- Core-block limits: assembled/kit/PCB are separate simple WooCommerce products (the demo builder has no variable products). The signal chain links to product category archives. The wire behind it and its mobile layout needed top-level CSS because section-style CSS drops @media blocks.

## Round 2

- Look kept ("great design"). Home h1 is now a plain statement of what is sold and where, and the intro names the current release (Moor Echo).
- Tables cut from 13 to 5 of 48 patterns: the panel legend, versioned docs, controls, warranty, retired manuals, dealers and hours are spec rows with a 2px rule, and difficulty levels are three enclosure-coloured cards. Tables remain for the kit comparison, BOM, manuals list, fault table and postage.
- Eleven new patterns from JHS, Old Blood Noise, Befaco, Aion FX and ZVEX: difficulty levels, build service, soldering evening, enclosure colours, settings to start from, limited colourway note, customer boards, out-of-warranty repair prices, FAQ, gift vouchers, and Coal Tit vs Snicket. The kits, repairs, about and contact pages use them.
- Image lightbox enabled in theme.json and on drawings and photos.
