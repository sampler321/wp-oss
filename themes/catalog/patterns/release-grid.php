<?php
/**
 * Title: Release grid: cat no above each sleeve
 * Slug: catalog/release-grid
 * Categories: featured,query
 * Keywords: releases, sleeves, catalogue
 */
?>
<!-- wp:group {"align":"wide","layout":{"type":"default"}} -->
<div class="wp-block-group alignwide"><!-- wp:group {"align":"wide","layout":{"type":"flex","flexWrap":"wrap","justifyContent":"space-between"}} -->
<div class="wp-block-group alignwide"><!-- wp:heading {"fontSize":"x-large"} -->
<h2 class="wp-block-heading has-x-large-font-size">Recent tapes</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><a href="/catalogue/">Full catalogue</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:query {"queryId":12,"query":{"perPage":8,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false},"align":"wide"} -->
<div class="wp-block-query alignwide"><!-- wp:post-template {"className":"is-style-sleeve-grid","layout":{"type":"grid","columnCount":4,"minimumColumnWidth":"13rem"}} -->
<!-- wp:post-terms {"term":"post_tag","className":"is-style-catno","fontSize":"small"} /-->

<!-- wp:post-featured-image {"isLink":true,"aspectRatio":"1"} /-->

<!-- wp:post-title {"level":3,"isLink":true,"fontSize":"large"} /-->

<!-- wp:post-excerpt {"moreText":"","excerptLength":12,"fontSize":"small"} /-->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p>Nothing here yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query --></div>
<!-- /wp:group -->
