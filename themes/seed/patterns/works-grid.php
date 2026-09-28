<?php
/**
 * Title: Works grid (front page)
 * Slug: seed/works-grid
 * Categories: seed-works,portfolio,query
 * Description: A tight 4-column grid of square outputs with title and year, ruled like a contact sheet.
 */
?>
<!-- wp:group {"align":"wide","layout":{"type":"flex","flexWrap":"wrap","justifyContent":"space-between"}} -->
<div class="wp-block-group alignwide"><!-- wp:heading {"fontSize":"x-large"} -->
<h2 class="wp-block-heading has-x-large-font-size">Works</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"className":"is-style-tabs"} -->
<p class="is-style-tabs"><a href="/works/">All</a> / <a href="/category/digital/">Digital</a> / <a href="/category/physical/">Physical</a> / <a href="/category/spatial/">Spatial</a> / <a href="/list/">Index</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:query {"queryId":1,"query":{"perPage":8,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false},"align":"wide"} -->
<div class="wp-block-query alignwide"><!-- wp:post-template {"className":"is-style-sheet","layout":{"type":"grid","columnCount":4}} -->
<!-- wp:post-featured-image {"isLink":true,"aspectRatio":"1"} /-->

<!-- wp:group {"style":{"spacing":{"margin":{"top":"var:preset|spacing|20"}}},"layout":{"type":"flex","flexWrap":"nowrap","justifyContent":"space-between"}} -->
<div class="wp-block-group" style="margin-top:var(--wp--preset--spacing--20)"><!-- wp:post-title {"level":3,"isLink":true,"style":{"typography":{"fontWeight":"500"}},"fontSize":"medium","fontFamily":"body"} /-->

<!-- wp:post-date {"format":"Y","metadata":{"bindings":{"datetime":{"source":"core/post-data","args":{"field":"date"}}}}} /--></div>
<!-- /wp:group -->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p>Nothing here yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query -->
