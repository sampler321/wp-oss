<?php
/**
 * Title: Essay: merging lines
 * Slug: seed/essay-merging
 * Categories: seed-writing,text
 */
?>
<!-- wp:paragraph {"textColor":"muted","fontSize":"small"} -->
<p class="has-muted-color has-text-color has-small-font-size">Published 12 January 2026</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Cutting plot time in half by merging lines</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"large"} -->
<p class="has-large-font-size">A Drift sheet has 1,400 lines. Plotted in the order the code draws them, the pen lifts and travels 1,400 times, mostly across the whole sheet. That took nine hours.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Two changes fixed it. First, sort the lines so each one starts near where the last ended. Second, join lines whose ends are closer than 0.5mm into one path, so the pen stays down.</p>
<!-- /wp:paragraph -->

<!-- wp:pattern {"slug":"seed/code-snippet"} /-->

<!-- wp:columns -->
<div class="wp-block-columns"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/drift-412.jpg' ) ); ?>" alt="Drift seed 412"/><figcaption class="wp-element-caption">Seed 412: nine hours before sorting</figcaption></figure>
<!-- /wp:image --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/drift-301.jpg' ) ); ?>" alt="Drift seed 301"/><figcaption class="wp-element-caption">Seed 301: five hours after</figcaption></figure>
<!-- /wp:image --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:paragraph -->
<p>The drawings look the same. The pens last longer too, because they spend less time in the air drying out.</p>
<!-- /wp:paragraph -->
