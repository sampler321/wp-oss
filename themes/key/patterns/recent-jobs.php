<?php
/**
 * Title: Recent jobs (latest posts)
 * Slug: key/recent-jobs
 * Categories: posts,query
 */
?>
<!-- wp:heading -->
<h2 class="wp-block-heading">Recent jobs</h2>
<!-- /wp:heading -->

<!-- wp:query {"queryId":1,"query":{"perPage":3,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false}} -->
<div class="wp-block-query"><!-- wp:post-template -->
<!-- wp:post-title {"level":3,"isLink":true,"fontSize":"medium"} /-->

<!-- wp:post-excerpt {"moreText":""} /-->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p>Nothing here yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><a href="/category/jobs/">All job reports</a></p>
<!-- /wp:paragraph -->
