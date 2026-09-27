<?php
/**
 * Title: Zine diary (latest entries)
 * Slug: drop/diary-latest
 * Categories: diary
 */
?>
<!-- wp:group {"align":"wide","className":"is-style-scrap-flat","style":{"spacing":{"margin":{"top":"var:preset|spacing|60"}}},"layout":{"type":"default"}} -->
<div class="wp-block-group alignwide is-style-scrap-flat" style="margin-top:var(--wp--preset--spacing--60)"><!-- wp:heading -->
<h2 class="wp-block-heading">from the back bedroom</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The diary: packing days, print nights, tour notes. Same people, worse handwriting.</p>
<!-- /wp:paragraph -->

<!-- wp:query {"queryId":1,"query":{"perPage":3,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false},"align":"wide"} -->
<div class="wp-block-query alignwide"><!-- wp:post-template {"layout":{"type":"grid","columnCount":3,"minimumColumnWidth":"15rem"}} -->
<!-- wp:post-date {"metadata":{"bindings":{"datetime":{"source":"core/post-data","args":{"field":"date"}}}}} /-->

<!-- wp:post-title {"level":3,"isLink":true,"fontSize":"large"} /-->

<!-- wp:post-excerpt {"excerptLength":20,"fontSize":"small"} /-->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p>Nothing here yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query -->

<!-- wp:paragraph -->
<p><a href="/category/diary/">The whole diary</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->
