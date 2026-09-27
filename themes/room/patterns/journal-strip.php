<?php
/**
 * Title: From the notebook (latest projects list)
 * Slug: room/journal-strip
 * Categories: posts,query
 */
?>
<!-- wp:group {"className":"is-style-rule-top","layout":{"type":"constrained"}} -->
<div class="wp-block-group is-style-rule-top"><!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">Recently finished</h4>
<!-- /wp:heading -->

<!-- wp:query {"queryId":22,"query":{"perPage":5,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false}} -->
<div class="wp-block-query"><!-- wp:post-template -->
<!-- wp:group {"layout":{"type":"flex","flexWrap":"wrap","justifyContent":"space-between"}} -->
<div class="wp-block-group"><!-- wp:post-title {"level":5,"isLink":true} /-->

<!-- wp:post-date {"format":"F Y","metadata":{"bindings":{"datetime":{"source":"core/post-data","args":{"field":"date"}}}}} /--></div>
<!-- /wp:group -->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p>Nothing here yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query --></div>
<!-- /wp:group -->
