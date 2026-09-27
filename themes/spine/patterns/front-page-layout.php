<?php
/**
 * Title: Home: new book, shelf, buy, events
 * Slug: spine/front-page-layout
 * Categories: featured
 * Inserter: no
 */
?>
<!-- wp:pattern {"slug":"spine/new-book-hero"} /-->

<!-- wp:pattern {"slug":"spine/shelf"} /-->

<!-- wp:columns {"className":"alignwide is-style-rule-top","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|60"},"padding":{"bottom":"var:preset|spacing|60"}}}} -->
<div class="wp-block-columns alignwide is-style-rule-top" style="padding-bottom:var(--wp--preset--spacing--60)"><!-- wp:column {"width":"55%"} -->
<div class="wp-block-column" style="flex-basis:55%"><!-- wp:pattern {"slug":"spine/buy-block"} /--></div>
<!-- /wp:column -->

<!-- wp:column {"width":"45%"} -->
<div class="wp-block-column" style="flex-basis:45%"><!-- wp:pattern {"slug":"spine/events"} /--></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:columns {"className":"alignwide","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|60"},"padding":{"bottom":"var:preset|spacing|70"}}}} -->
<div class="wp-block-columns alignwide" style="padding-bottom:var(--wp--preset--spacing--70)"><!-- wp:column {"width":"55%"} -->
<div class="wp-block-column" style="flex-basis:55%"><!-- wp:pattern {"slug":"spine/newsletter-signup"} /--></div>
<!-- /wp:column -->

<!-- wp:column {"width":"45%"} -->
<div class="wp-block-column" style="flex-basis:45%"><!-- wp:pattern {"slug":"spine/praise-single"} /--></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
