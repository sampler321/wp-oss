<?php
/**
 * Title: In-store events (latest posts)
 * Slug: crate/events-list
 * Categories: posts,query
 */
?>
<!-- wp:group {"align":"wide","style":{"spacing":{"padding":{"top":"var:preset|spacing|60","bottom":"var:preset|spacing|60"}}},"layout":{"type":"default"}} -->
<div class="wp-block-group alignwide" style="padding-top:var(--wp--preset--spacing--60);padding-bottom:var(--wp--preset--spacing--60)"><!-- wp:group {"align":"wide","layout":{"type":"flex","flexWrap":"wrap","justifyContent":"space-between"}} -->
<div class="wp-block-group alignwide"><!-- wp:heading -->
<h2 class="wp-block-heading">In the shop</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"className":"is-style-label"} -->
<p class="is-style-label"><a href="/events/">All events</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:query {"queryId":1,"query":{"perPage":4,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false},"align":"wide"} -->
<div class="wp-block-query"><!-- wp:post-template {"layout":{"type":"grid","columnCount":4,"minimumColumnWidth":"10rem"}} -->
<!-- wp:post-featured-image {"isLink":true,"aspectRatio":"4/5","scale":"cover"} /-->

<!-- wp:post-date {"format":"j M"} /-->

<!-- wp:post-title {"isLink":true,"level":3} /-->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p class="">Nothing here yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query --></div>
<!-- /wp:group -->
