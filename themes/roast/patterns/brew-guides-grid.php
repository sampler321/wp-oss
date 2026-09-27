<?php
/**
 * Title: Brew guides (grid)
 * Slug: roast/brew-guides-grid
 * Categories: brew,query
 */
?>
<!-- wp:group {"align":"wide","className":"is-style-rule-top","style":{"spacing":{"padding":{"bottom":"var:preset|spacing|60"}}},"layout":{"type":"default"}} -->
<div class="wp-block-group alignwide is-style-rule-top" style="padding-bottom:var(--wp--preset--spacing--60)"><!-- wp:group {"layout":{"type":"flex","flexWrap":"wrap","justifyContent":"space-between"}} -->
<div class="wp-block-group"><!-- wp:heading -->
<h2 class="wp-block-heading">Brew guides</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><a href="/brew-guides/">All guides</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:query {"queryId":2,"query":{"perPage":6,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false}} -->
<div class="wp-block-query"><!-- wp:post-template {"className":"is-style-guide-list","layout":{"type":"grid","columnCount":3,"minimumColumnWidth":"14rem"}} -->
<!-- wp:post-title {"level":3,"isLink":true,"fontSize":"large"} /-->

<!-- wp:post-excerpt {"moreText":"Open the guide","excerptLength":20,"fontSize":"small"} /-->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p>No guides yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query --></div>
<!-- /wp:group -->
