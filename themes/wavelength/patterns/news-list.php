<?php
/**
 * Title: Local news (latest four)
 * Slug: wavelength/news-list
 * Categories: query
 */
?>
<!-- wp:group {"align":"wide","layout":{"type":"default"}} -->
<div class="wp-block-group alignwide"><!-- wp:heading -->
<h2 class="wp-block-heading">Local news</h2>
<!-- /wp:heading -->

<!-- wp:query {"queryId":51,"query":{"perPage":4,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false}} -->
<div class="wp-block-query"><!-- wp:post-template {"layout":{"type":"grid","columnCount":2,"minimumColumnWidth":"18rem"}} -->
<!-- wp:group {"className":"is-style-rule-top","layout":{"type":"default"}} -->
<div class="wp-block-group is-style-rule-top"><!-- wp:post-date {"format":"l j F, g:ia","metadata":{"bindings":{"datetime":{"source":"core/post-data","args":{"field":"date"}}}}} /-->

<!-- wp:post-title {"level":3,"isLink":true,"fontSize":"large"} /-->

<!-- wp:post-excerpt {"moreText":"","excerptLength":30} /--></div>
<!-- /wp:group -->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p>Nothing here yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query -->

<!-- wp:paragraph -->
<p><a href="/news/">All local news</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->
