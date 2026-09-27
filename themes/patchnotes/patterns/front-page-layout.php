<?php
/**
 * Title: Home: title screen, notes, commit log, boxes
 * Slug: patchnotes/front-page-layout
 * Categories: featured
 * Inserter: no
 */
?>
<!-- wp:pattern {"slug":"patchnotes/title-screen"} /-->

<!-- wp:pattern {"slug":"patchnotes/whats-in-it"} /-->

<!-- wp:pattern {"slug":"patchnotes/commit-log"} /-->

<!-- wp:pattern {"slug":"patchnotes/dither-band"} /-->

<!-- wp:columns {"align":"wide","style":{"spacing":{"padding":{"top":"var:preset|spacing|50"},"blockGap":{"left":"var:preset|spacing|40"}}}} -->
<div class="wp-block-columns alignwide" style="padding-top:var(--wp--preset--spacing--50)"><!-- wp:column {"width":"34%"} -->
<div class="wp-block-column" style="flex-basis:34%"><!-- wp:pattern {"slug":"patchnotes/bbs-menu"} /-->

<!-- wp:pattern {"slug":"patchnotes/meetups"} /--></div>
<!-- /wp:column -->

<!-- wp:column {"width":"33%"} -->
<div class="wp-block-column" style="flex-basis:33%"><!-- wp:pattern {"slug":"patchnotes/guest-lines"} /-->

<!-- wp:pattern {"slug":"patchnotes/greetz"} /--></div>
<!-- /wp:column -->

<!-- wp:column {"width":"33%"} -->
<div class="wp-block-column" style="flex-basis:33%"><!-- wp:pattern {"slug":"patchnotes/oneliners"} /-->

<!-- wp:pattern {"slug":"patchnotes/boot-log"} /--></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:group {"tagName":"section","align":"wide","style":{"spacing":{"padding":{"top":"var:preset|spacing|60","bottom":"var:preset|spacing|70"}}},"layout":{"type":"default"}} -->
<section class="wp-block-group alignwide" style="padding-top:var(--wp--preset--spacing--60);padding-bottom:var(--wp--preset--spacing--70)"><!-- wp:heading -->
<h2 class="wp-block-heading">Pay for the bandwidth</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"muted"} -->
<p class="has-muted-color has-text-color">€190 a month keeps it running. Open Collective shows every euro.</p>
<!-- /wp:paragraph -->

<!-- wp:pattern {"slug":"patchnotes/tiers-boxes"} /-->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="https://opencollective.com/">Support on Open Collective</a></div>
<!-- /wp:button -->

<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/support/">Sponsor an episode</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></section>
<!-- /wp:group -->
