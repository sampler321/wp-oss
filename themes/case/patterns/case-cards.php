<?php
/**
 * Title: Case studies (big cards)
 * Slug: case/case-cards
 * Categories: featured,query
 * Keywords: case studies, work
 */
?>
<!-- wp:group {"align":"wide","layout":{"type":"default"}} -->
<div class="wp-block-group alignwide"><!-- wp:group {"align":"wide","layout":{"type":"flex","flexWrap":"wrap","justifyContent":"space-between"}} -->
<div class="wp-block-group alignwide"><!-- wp:heading -->
<h2 class="wp-block-heading">Case studies</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><a href="/work/">All work, including NDA projects</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:query {"queryId":42,"query":{"perPage":3,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false},"align":"wide"} -->
<div class="wp-block-query alignwide"><!-- wp:post-template {"layout":{"type":"default"}} -->
<!-- wp:columns {"verticalAlignment":"center","className":"is-style-case-card","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|50"}}}} -->
<div class="wp-block-columns are-vertically-aligned-center is-style-case-card"><!-- wp:column {"width":"58%"} -->
<div class="wp-block-column" style="flex-basis:58%"><!-- wp:post-featured-image {"isLink":true,"aspectRatio":"16/10","className":"is-style-framed"} /--></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:post-terms {"term":"category","className":"is-style-tag"} /-->

<!-- wp:post-title {"isLink":true,"fontSize":"x-large"} /-->

<!-- wp:post-excerpt /-->

<!-- wp:read-more {"content":"Read the case study"} /--></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p>Nothing here yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query --></div>
<!-- /wp:group -->
