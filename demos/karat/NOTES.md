# Karat: notes

- Direction: "bench specimen" for a one-person goldsmith in Norwich (Edie Achterberg). Every piece sits on a flat wax-grey mount like a museum specimen, with a small-caps label for metal, size and price. Steel-grey page (#EEF0F0), loupe black text, 18ct gold (#7A5A22) only for prices and the main button.
- Fonts: Italiana (display, one weight) and Petrona (body, true italics). Petrona replaced the research's Newsreader because two later themes claimed Newsreader as their display face.
- Layout: centred wordmark header, then asymmetric 42/58 splits (text left, larger specimen right). Square corners, 1px hairlines.
- Signature: the Bespoke page as a vertical ledger of seven stages (consultation to collection), each a ruled row with week numbers, text and one bench photo, followed by the deposit and payment split, try-on-the-wax, hallmarking at the Birmingham Assay Office and a workshop-visit note.
- Also: specimen tray and one-of-one grid with a sold state, ring size table (stacks on phones), free ring sizer request, metal options with a stated limit (no rose or white gold), care, delivery and FAQ.
- WooCommerce: 8 simple products. The shop, cart and checkout use Woo's default templates and inherit theme.json; prices take the gold accent and the sort select is restyled in root CSS. The header uses a "Basket" nav link instead of Woo's hooked mini-cart.
- Core-block limits: variable products (metal x size) aren't possible with the demo builder, so sizes are described in the product text. Stage photos can't be scrubbed left and right without JS; they are a plain vertical sequence.

## Round 2

- Image lightbox on globally.
- 49 patterns (was 32). New commission-story kit (what came in, before and after, three stages in pictures, metal and stone and size, what it cost, client quote) and three full stories built from it as journal posts: the garnet seal ring, a signet with the Norfolk coast engraved, and two wedding bands from one grandmother's ring. Nine journal posts in total.
- New services from real jewellers' sites: repairs and resizing price list, insurance valuations, engraving, gift vouchers, appointment card, a which-gold guide and a single new-in piece on the home page. A Repairs page is in the nav.
- Tables down to 3 (ring sizes, repairs prices, metals). Deposit terms, delivery and story specs are ledger rows.
- Several reference sites (Glen & Effie, Michael Platt) now only render footers or 404 for the headless browser; their footers' service lists were used.
