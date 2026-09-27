<?php
/**
 * Title: Home: lead, wire, goals, investigations, membership
 * Slug: dispatch/front-page-layout
 * Categories: featured
 * Inserter: no
 */
?>
<!-- wp:pattern {"slug":"dispatch/breaking-bar"} /-->

<!-- wp:pattern {"slug":"dispatch/lead-and-wire"} /-->

<!-- wp:pattern {"slug":"dispatch/goals"} /-->

<!-- wp:pattern {"slug":"dispatch/investigations-grid"} /-->

<!-- wp:columns {"align":"wide","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|50"},"padding":{"bottom":"var:preset|spacing|60"}}}} -->
<div class="wp-block-columns alignwide" style="padding-bottom:var(--wp--preset--spacing--60)"><!-- wp:column {"width":"40%"} -->
<div class="wp-block-column" style="flex-basis:40%"><!-- wp:pattern {"slug":"dispatch/top-stories"} /--></div>
<!-- /wp:column -->

<!-- wp:column {"width":"30%"} -->
<div class="wp-block-column" style="flex-basis:30%"><!-- wp:pattern {"slug":"dispatch/behind-the-story"} /--></div>
<!-- /wp:column -->

<!-- wp:column {"width":"30%"} -->
<div class="wp-block-column" style="flex-basis:30%"><!-- wp:pattern {"slug":"dispatch/podcast-episode"} /--></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:group {"tagName":"section","align":"wide","className":"is-style-rule-top","style":{"spacing":{"padding":{"bottom":"var:preset|spacing|60"}}},"layout":{"type":"default"}} -->
<section class="wp-block-group alignwide is-style-rule-top" style="padding-bottom:var(--wp--preset--spacing--60)"><!-- wp:heading -->
<h2 class="wp-block-heading">Membership</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"large"} -->
<p class="has-large-font-size">Readout has no advertising and no investors. About 2,400 people pay for Readout, and that is the whole budget.</p>
<!-- /wp:paragraph -->

<!-- wp:pattern {"slug":"dispatch/tier-columns"} /--></section>
<!-- /wp:group -->

<!-- wp:columns {"align":"wide","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|60"},"padding":{"bottom":"var:preset|spacing|70"}}}} -->
<div class="wp-block-columns alignwide" style="padding-bottom:var(--wp--preset--spacing--70)"><!-- wp:column {"width":"50%"} -->
<div class="wp-block-column" style="flex-basis:50%"><!-- wp:pattern {"slug":"dispatch/signup-box"} /--></div>
<!-- /wp:column -->

<!-- wp:column {"width":"50%"} -->
<div class="wp-block-column" style="flex-basis:50%"><!-- wp:pattern {"slug":"dispatch/tips"} /--></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
