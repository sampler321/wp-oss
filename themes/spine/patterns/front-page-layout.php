<?php
/**
 * Title: Home: collage opener, patchwork, shelf, buy, events
 * Slug: spine/front-page-layout
 * Categories: featured
 * Inserter: no
 */
?>
<!-- wp:pattern {"slug":"spine/collage-hero"} /-->

<!-- wp:pattern {"slug":"spine/band-waves"} /-->

<!-- wp:pattern {"slug":"spine/series-patchwork"} /-->

<!-- wp:pattern {"slug":"spine/shelf"} /-->

<!-- wp:columns {"align":"wide","className":"is-style-rule-top","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|60"},"padding":{"bottom":"var:preset|spacing|60"}}}} -->
<div class="wp-block-columns alignwide is-style-rule-top" style="padding-bottom:var(--wp--preset--spacing--60)"><!-- wp:column {"width":"55%"} -->
<div class="wp-block-column" style="flex-basis:55%"><!-- wp:pattern {"slug":"spine/buy-block"} /--></div>
<!-- /wp:column -->

<!-- wp:column {"width":"45%"} -->
<div class="wp-block-column" style="flex-basis:45%"><!-- wp:pattern {"slug":"spine/events-rows"} /--></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:pattern {"slug":"spine/great-ideas-quote"} /-->

<!-- wp:columns {"align":"wide","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|60"},"padding":{"top":"var:preset|spacing|60","bottom":"var:preset|spacing|70"}}}} -->
<div class="wp-block-columns alignwide" style="padding-top:var(--wp--preset--spacing--60);padding-bottom:var(--wp--preset--spacing--70)"><!-- wp:column {"width":"55%"} -->
<div class="wp-block-column" style="flex-basis:55%"><!-- wp:pattern {"slug":"spine/newsletter-signup"} /--></div>
<!-- /wp:column -->

<!-- wp:column {"width":"45%"} -->
<div class="wp-block-column" style="flex-basis:45%"><!-- wp:pattern {"slug":"spine/praise-single"} /--></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
