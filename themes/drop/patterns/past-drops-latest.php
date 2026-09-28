<?php
/**
 * Title: Past drops (latest four)
 * Slug: drop/past-drops-latest
 * Categories: drops
 */
?>
<!-- wp:group {"align":"wide","style":{"spacing":{"padding":{"top":"var:preset|spacing|60","bottom":"var:preset|spacing|60"}}},"layout":{"type":"default"}} -->
<div class="wp-block-group alignwide" style="padding-top:var(--wp--preset--spacing--60);padding-bottom:var(--wp--preset--spacing--60)"><!-- wp:heading -->
<h2 class="wp-block-heading">the past drops pile</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p class="">Sold out stays up. It is the closest thing we have to a discography of t-shirts. <a href="/past-drops/">See every drop</a></p>
<!-- /wp:paragraph -->

<!-- wp:query {"queryId":1,"query":{"perPage":4,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false},"align":"wide"} -->
<div class="wp-block-query"><!-- wp:post-template {"className":"is-style-xerox-grid","layout":{"type":"grid","columnCount":4,"minimumColumnWidth":"13rem"}} -->
<!-- wp:post-featured-image {"isLink":true,"aspectRatio":"4/5","scale":"cover"} /-->

<!-- wp:post-title {"isLink":true,"level":3,"fontSize":"large"} /-->

<!-- wp:post-date /-->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p class="">Nothing here yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query --></div>
<!-- /wp:group -->
