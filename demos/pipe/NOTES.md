# Pipe: notes

- Direction: a Swiss price index for a heating engineer. The owner asked for professional, toned-down elegant, clean and technical, which matches the research's Swiss neo-grotesk idea; the mono face was removed under the new rule. Demo: Brennan Heating, Sheffield.
- Fonts: Bespoke Sans only (Fontshare, the face registered for 097): 300 for large headings, 400 body, 500 labels, 700 for the phone number. No monospace.
- Palette: white, near-black, pale grey table rows; hot red only for the emergency bar and call buttons, cold blue for links and booking buttons.
- Layout: every section is a Swiss index row, a narrow left label column and a wide right column under a 1px rule. The service list is a real numbered list, and the phone number is set as large as the name. Photos are greyscale.
- Signature: "How urgent is it?", three options in the customer's words (no heating or hot water / something is wrong but working / planned work), each sending the customer to the right channel, plus what to tell us (property type, boiler model, fault code, tenant or owner).
- Nice-to-haves as patterns: guide price table with the written-price note, areas and response times (areas are posts), what to do while you wait, lead-time line, Gas Safe number with a link to the register.
- Tool note: fetch-fonts.mjs fails on Fontshare CSS because the font URLs are protocol-relative (//cdn.fontshare.com). The woff2 files and .fonts.json were fetched by hand.
