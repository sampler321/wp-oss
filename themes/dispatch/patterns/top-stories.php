<?php
/**
 * Title: Top stories, text only
 * Slug: dispatch/top-stories
 * Categories: posts,query
 */
?>
<!-- wp:group {"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Most read this week</h3>
<!-- /wp:heading -->

<!-- wp:query {"queryId":4,"query":{"perPage":4,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false}} -->
<div class="wp-block-query"><!-- wp:post-template -->
<!-- wp:group {"className":"is-style-hairline-top","layout":{"type":"default"}} -->
<div class="wp-block-group is-style-hairline-top"><!-- wp:post-title {"level":4,"isLink":true,"fontSize":"large"} /-->

<!-- wp:post-date {"format":"j M","metadata":{"bindings":{"datetime":{"source":"core/post-data","args":{"field":"date"}}}}} /--></div>
<!-- /wp:group -->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p>Nothing here yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query --></div>
<!-- /wp:group -->
