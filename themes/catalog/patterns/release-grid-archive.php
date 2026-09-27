<?php
/**
 * Title: Release grid (inherits the page query)
 * Slug: catalog/release-grid-archive
 * Categories: query
 * Inserter: no
 */
?>
<!-- wp:query {"queryId":0,"query":{"perPage":12,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":true},"align":"wide"} -->
<div class="wp-block-query alignwide"><!-- wp:post-template {"className":"is-style-sleeve-grid","layout":{"type":"grid","columnCount":4,"minimumColumnWidth":"13rem"}} -->
<!-- wp:post-terms {"term":"post_tag","className":"is-style-catno","fontSize":"small"} /-->

<!-- wp:post-featured-image {"isLink":true,"aspectRatio":"1"} /-->

<!-- wp:post-title {"level":3,"isLink":true,"fontSize":"large"} /-->

<!-- wp:post-excerpt {"moreText":"","excerptLength":12,"fontSize":"small"} /-->
<!-- /wp:post-template -->

<!-- wp:query-pagination -->
<!-- wp:query-pagination-previous /-->

<!-- wp:query-pagination-numbers /-->

<!-- wp:query-pagination-next /-->
<!-- /wp:query-pagination -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p>Nothing matches that yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query -->
