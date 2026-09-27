<?php
/**
 * Title: Lead report with meetings rail
 * Slug: local/lead-with-meetings
 * Categories: featured
 */
?>
<!-- wp:columns {"align":"wide","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|60"},"padding":{"bottom":"var:preset|spacing|60"}}}} -->
<div class="wp-block-columns alignwide" style="padding-bottom:var(--wp--preset--spacing--60)"><!-- wp:column {"width":"66%"} -->
<div class="wp-block-column" style="flex-basis:66%"><!-- wp:query {"queryId":2,"query":{"perPage":1,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false}} -->
<div class="wp-block-query"><!-- wp:post-template -->
<!-- wp:post-featured-image {"isLink":true,"aspectRatio":"3/2"} /-->

<!-- wp:post-terms {"term":"category","separator":", ","textColor":"accent"} /-->

<!-- wp:post-title {"isLink":true,"level":1,"fontSize":"display"} /-->

<!-- wp:group {"className":"is-style-abstract","layout":{"type":"constrained"}} -->
<div class="wp-block-group is-style-abstract"><!-- wp:heading {"level":6} -->
<h6 class="wp-block-heading">Abstract</h6>
<!-- /wp:heading -->

<!-- wp:post-excerpt {"excerptLength":60,"moreText":"Read the full report","fontSize":"medium"} /--></div>
<!-- /wp:group -->

<!-- wp:post-date {"format":"j F Y"} /-->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p class="">No reports filed yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:pattern {"slug":"local/meetings-rail"} /-->

<!-- wp:pattern {"slug":"local/correction-latest"} /--></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
