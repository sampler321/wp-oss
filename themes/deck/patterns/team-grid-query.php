<?php
/**
 * Title: Team riders (latest posts in Team)
 * Slug: deck/team-grid-query
 * Categories: team,query
 */
?>
<!-- wp:group {"align":"wide","layout":{"type":"default"}} -->
<div class="wp-block-group alignwide"><!-- wp:heading {"className":"is-style-ransom"} -->
<h2 class="wp-block-heading is-style-ransom"><mark>Meet</mark> the <strong>team</strong></h2>
<!-- /wp:heading -->

<!-- wp:query {"queryId":1,"query":{"perPage":4,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false},"align":"wide"} -->
<div class="wp-block-query alignwide"><!-- wp:post-template {"layout":{"type":"grid","columnCount":4,"minimumColumnWidth":"11rem"}} -->
<!-- wp:post-featured-image {"isLink":true,"aspectRatio":"3/4","className":"is-style-halftone"} /-->

<!-- wp:post-title {"level":3,"isLink":true,"fontSize":"large"} /-->

<!-- wp:post-excerpt {"excerptLength":14,"fontSize":"small"} /-->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p>Nothing here yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query --></div>
<!-- /wp:group -->
