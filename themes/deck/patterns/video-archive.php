<?php
/**
 * Title: Video archive (latest posts)
 * Slug: deck/video-archive
 * Categories: posts,query,featured
 */
?>
<!-- wp:group {"align":"full","className":"is-style-red deck-torn","layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull is-style-red deck-torn"><!-- wp:group {"align":"wide","layout":{"type":"flex","flexWrap":"wrap","justifyContent":"space-between"}} -->
<div class="wp-block-group alignwide"><!-- wp:heading {"className":"is-style-ransom"} -->
<h2 class="wp-block-heading is-style-ransom"><mark>Shop</mark> videos</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"large"} -->
<p class="has-large-font-size"><a href="/videos/">Every video</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:query {"queryId":1,"query":{"perPage":3,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false},"align":"wide"} -->
<div class="wp-block-query"><!-- wp:post-template {"layout":{"type":"grid","columnCount":3,"minimumColumnWidth":"15rem"}} -->
<!-- wp:post-featured-image {"isLink":true,"aspectRatio":"16/9","scale":"cover","className":"is-style-halftone"} /-->

<!-- wp:post-date /-->

<!-- wp:post-title {"isLink":true,"level":3,"fontSize":"large"} /-->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p class="">Nothing here yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query --></div>
<!-- /wp:group -->
