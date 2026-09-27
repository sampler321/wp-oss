<?php
/**
 * Title: Recent jobs on the ticket rail
 * Slug: platter/ticket-rail
 * Categories: platter,query
 * Description: The signature: case studies as kitchen tickets with venue, guest count and what was served.
 */
?>
<!-- wp:group {"tagName":"section","align":"full","className":"is-style-tomato","layout":{"type":"constrained"}} -->
<section class="wp-block-group alignfull is-style-tomato"><!-- wp:group {"align":"wide","layout":{"type":"flex","flexWrap":"wrap","justifyContent":"space-between"}} -->
<div class="wp-block-group alignwide"><!-- wp:heading -->
<h2 class="wp-block-heading">On the rail</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><a href="/recent-jobs/">All the recent jobs</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:query {"queryId":1,"query":{"perPage":3,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false},"align":"wide"} -->
<div class="wp-block-query alignwide"><!-- wp:post-template {"className":"is-style-ticket-rail","layout":{"type":"grid","columnCount":3,"minimumColumnWidth":"17rem"}} -->
<!-- wp:post-terms {"term":"category"} /-->

<!-- wp:post-title {"level":3,"isLink":true,"fontSize":"large"} /-->

<!-- wp:post-excerpt {"excerptLength":30} /-->

<!-- wp:post-featured-image {"isLink":true,"aspectRatio":"4/3"} /-->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p>Nothing here yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query --></section>
<!-- /wp:group -->
