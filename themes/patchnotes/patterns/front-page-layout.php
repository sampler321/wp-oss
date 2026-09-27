<?php
/**
 * Title: Home: latest release, notes, log, guests
 * Slug: patchnotes/front-page-layout
 * Categories: featured
 * Inserter: no
 */
?>
<!-- wp:pattern {"slug":"patchnotes/latest-release"} /-->

<!-- wp:pattern {"slug":"patchnotes/whats-in-it"} /-->

<!-- wp:pattern {"slug":"patchnotes/release-log"} /-->

<!-- wp:columns {"align":"wide","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|60"}}}} -->
<div class="wp-block-columns alignwide"><!-- wp:column {"width":"26%"} -->
<div class="wp-block-column" style="flex-basis:26%"><!-- wp:heading {"fontSize":"large"} -->
<h2 class="wp-block-heading has-large-font-size">On the show</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"muted","fontSize":"small"} -->
<p class="has-muted-color has-text-color has-small-font-size">People who maintain things, fix things or get paged about them.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column {"width":"74%"} -->
<div class="wp-block-column" style="flex-basis:74%"><!-- wp:table -->
<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr><th>Guest</th><th>Works on</th><th>Episode</th></tr></thead><tbody><tr><td>Sanne Vermeulen</td><td>On-call and incident reviews at a payments company, Antwerp</td><td><a href="/the-pager-went-off-at-3am/">88</a></td></tr><tr><td>Tomás Ferreira</td><td>Maintains an image-decoding library used by most of your phone apps</td><td><a href="/who-maintains-the-pdf-library/">87</a></td></tr><tr><td>Hana Novák</td><td>Accessibility auditor, Brno. Has filed around 3,000 bugs</td><td><a href="/accessibility-audits-that-get-fixed/">86</a></td></tr><tr><td>Jonas Peeters</td><td>Runs infrastructure for a Ghent newspaper, now mostly on its own servers</td><td><a href="/leaving-the-cloud-a-bit/">85</a></td></tr><tr><td>Ines Duarte</td><td>Hardware engineer, teaches soldering at a hackerspace in Lisbon</td><td><a href="/soldering-for-software-people/">82</a></td></tr></tbody></table></figure>
<!-- /wp:table -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><a href="/guests/">All guests</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:columns {"className":"alignwide","style":{"spacing":{"padding":{"top":"var:preset|spacing|60","bottom":"var:preset|spacing|70"},"blockGap":{"left":"var:preset|spacing|60"}}}} -->
<div class="wp-block-columns alignwide" style="padding-top:var(--wp--preset--spacing--60);padding-bottom:var(--wp--preset--spacing--70)"><!-- wp:column {"width":"26%"} -->
<div class="wp-block-column" style="flex-basis:26%"><!-- wp:heading {"fontSize":"large"} -->
<h2 class="wp-block-heading has-large-font-size">Pay for it</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"muted","fontSize":"small"} -->
<p class="has-muted-color has-text-color has-small-font-size">€190 a month keeps it running.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column {"width":"74%"} -->
<div class="wp-block-column" style="flex-basis:74%"><!-- wp:table -->
<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr><th>Tier</th><th>Price</th><th>You get</th></tr></thead><tbody><tr><td>Patch</td><td>€3 / month</td><td>Ad-free feed</td></tr><tr><td>Minor</td><td>€6 / month</td><td>Ad-free feed and the monthly “what we cut” episode</td></tr><tr><td>Major</td><td>€15 / month</td><td>All of that, the planning Discord and your name in the notes</td></tr></tbody></table></figure>
<!-- /wp:table -->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="https://opencollective.com/">Support on Open Collective</a></div>
<!-- /wp:button -->

<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/support/">Sponsor an episode</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
