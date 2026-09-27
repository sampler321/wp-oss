<?php
/**
 * Title: News list
 * Slug: catalog/post-list
 * Categories: posts,query
 * Inserter: no
 */
?>
<!-- wp:query {"queryId":0,"query":{"perPage":12,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":true},"align":"wide"} -->
<div class="wp-block-query"><!-- wp:post-template -->
<!-- wp:group {"className":"is-style-rule-top","layout":{"type":"constrained"}} -->
<div class="wp-block-group is-style-rule-top"><!-- wp:post-date {"format":"j M Y"} /-->

<!-- wp:post-title {"isLink":true,"level":2,"fontSize":"x-large"} /-->

<!-- wp:post-excerpt {"moreText":"","excerptLength":30} /--></div>
<!-- /wp:group -->
<!-- /wp:post-template -->

<!-- wp:query-pagination -->
<!-- wp:query-pagination-previous /-->

<!-- wp:query-pagination-numbers /-->

<!-- wp:query-pagination-next /-->
<!-- /wp:query-pagination -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p class="">Nothing matches that yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query -->
