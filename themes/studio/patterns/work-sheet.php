<?php
/**
 * Title: Work sheet: latest seven projects in 8/4 spans
 * Slug: studio/work-sheet
 * Categories: portfolio,query
 * Keywords: work, grid, index
 */
?>
<!-- wp:group {"align":"wide","layout":{"type":"default"}} -->
<div class="wp-block-group alignwide"><!-- wp:pattern {"slug":"studio/filter-bar"} /-->

<!-- wp:query {"queryId":1,"query":{"perPage":7,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false},"align":"wide"} -->
<div class="wp-block-query alignwide"><!-- wp:post-template {"className":"is-style-work-sheet"} -->
<!-- wp:post-featured-image {"isLink":true,"sizeSlug":"large"} /-->

<!-- wp:post-title {"level":3,"isLink":true,"fontSize":"large"} /-->

<!-- wp:post-excerpt {"moreText":"","excerptLength":22} /-->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p>No projects yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query --></div>
<!-- /wp:group -->
