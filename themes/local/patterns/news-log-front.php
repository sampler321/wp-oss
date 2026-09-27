<?php
/**
 * Title: News log (latest, after the lead)
 * Slug: local/news-log-front
 * Categories: posts,query
 */
?>
<!-- wp:group {"align":"wide","className":"is-style-rule-thick","style":{"spacing":{"padding":{"bottom":"var:preset|spacing|60"}}}} -->
<div class="wp-block-group alignwide is-style-rule-thick" style="padding-bottom:var(--wp--preset--spacing--60)"><!-- wp:group {"layout":{"type":"flex","flexWrap":"wrap","justifyContent":"space-between"}} -->
<div class="wp-block-group"><!-- wp:heading -->
<h2 class="wp-block-heading">News log</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"x-small","fontFamily":"body"} -->
<p class="has-body-font-family has-x-small-font-size"><a href="/news/">All reports</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:query {"queryId":3,"query":{"perPage":6,"pages":0,"offset":1,"postType":"post","order":"desc","orderBy":"date","inherit":false}} -->
<div class="wp-block-query"><!-- wp:post-template {"className":"is-style-log"} -->
<!-- wp:columns {"style":{"spacing":{"blockGap":{"left":"var:preset|spacing|40"}}}} -->
<div class="wp-block-columns"><!-- wp:column {"width":"9rem"} -->
<div class="wp-block-column" style="flex-basis:9rem"><!-- wp:post-date {"format":"j M Y","metadata":{"bindings":{"datetime":{"source":"core/post-data","args":{"field":"date"}}}}} /-->

<!-- wp:post-terms {"term":"category"} /--></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:post-title {"level":3,"isLink":true,"fontSize":"large"} /-->

<!-- wp:post-excerpt {"moreText":"","excerptLength":28} /--></div>
<!-- /wp:column -->

<!-- wp:column {"width":"220px"} -->
<div class="wp-block-column" style="flex-basis:220px"><!-- wp:post-featured-image {"isLink":true,"aspectRatio":"3/2","sizeSlug":"medium"} /--></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p>No reports filed yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query --></div>
<!-- /wp:group -->
