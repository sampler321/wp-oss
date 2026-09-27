<?php
/**
 * Title: Staff picks (shelf-talker cards)
 * Slug: shelf/staff-picks
 * Categories: featured,posts
 * Description: The signature: staff picks as tilted yellow shelf-talkers with the bookseller's note.
 */
?>
<!-- wp:group {"align":"wide","className":"is-style-newsprint","layout":{"type":"default"}} -->
<div class="wp-block-group alignwide is-style-newsprint"><!-- wp:group {"layout":{"type":"flex","flexWrap":"wrap","justifyContent":"space-between"}} -->
<div class="wp-block-group"><!-- wp:heading {"fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-xx-large-font-size">This month's yellow cards</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p class=""><a href="/picks/">Every pick, every month</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:query {"queryId":2,"query":{"perPage":6,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false}} -->
<div class="wp-block-query"><!-- wp:post-template {"className":"is-style-talker-list","layout":{"type":"grid","columnCount":3,"minimumColumnWidth":"16rem"}} -->
<!-- wp:post-featured-image {"isLink":true,"aspectRatio":"4/3"} /-->

<!-- wp:post-title {"isLink":true,"level":3,"fontSize":"large"} /-->

<!-- wp:post-excerpt {"excerptLength":30,"moreText":"Read the whole note"} /-->

<!-- wp:post-terms {"term":"post_tag","separator":", "} /-->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p class="">No picks on the shelf yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query --></div>
<!-- /wp:group -->
