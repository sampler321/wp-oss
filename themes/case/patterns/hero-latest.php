<?php
/**
 * Title: Hero: name, one fact and the latest case study
 * Slug: case/hero-latest
 * Categories: hero
 * Description: Opens with the work: the newest case study, beside a name and one line.
 */
?>
<!-- wp:columns {"align":"wide","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|60"},"padding":{"top":"var:preset|spacing|50"}}}} -->
<div class="wp-block-columns alignwide" style="padding-top:var(--wp--preset--spacing--50)"><!-- wp:column {"width":"38%"} -->
<div class="wp-block-column" style="flex-basis:38%"><!-- wp:heading {"level":1,"fontSize":"xx-large"} -->
<h1 class="wp-block-heading has-xx-large-font-size">Nadia Branković</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Product designer in Glasgow. I work on ticket machines, parking, self-checkout and the apps next to them, and I start on the platform, not in Figma.</p>
<!-- /wp:paragraph -->

<!-- wp:pattern {"slug":"case/capacity-note"} /-->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/work/">All case studies</a></div>
<!-- /wp:button -->

<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/working-together/">Working together</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:query {"queryId":44,"query":{"perPage":1,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false}} -->
<div class="wp-block-query"><!-- wp:post-template -->
<!-- wp:post-featured-image {"isLink":true,"aspectRatio":"16/10","className":"is-style-framed"} /-->

<!-- wp:group {"layout":{"type":"flex","flexWrap":"wrap","justifyContent":"space-between"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size">Latest case study</p>
<!-- /wp:paragraph -->

<!-- wp:post-terms {"term":"category","className":"is-style-tag"} /--></div>
<!-- /wp:group -->

<!-- wp:post-title {"isLink":true,"fontSize":"x-large"} /-->

<!-- wp:post-excerpt /-->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p>Nothing here yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
