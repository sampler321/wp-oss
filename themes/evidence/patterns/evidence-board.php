<?php
/**
 * Title: Evidence board (tagged exhibits)
 * Slug: evidence/evidence-board
 * Categories: gallery,featured
 * Description: Four greyscale exhibits, each with a manila tag. Swap the photos for your own documents.
 */
?>
<!-- wp:group {"tagName":"section","align":"full","className":"is-style-board","style":{"spacing":{"padding":{"top":"var:preset|spacing|60","bottom":"var:preset|spacing|60"},"margin":{"top":"0"}}},"layout":{"type":"constrained"}} -->
<section class="wp-block-group alignfull is-style-board" style="margin-top:0;padding-top:var(--wp--preset--spacing--60);padding-bottom:var(--wp--preset--spacing--60)"><!-- wp:group {"align":"wide","layout":{"type":"flex","flexWrap":"wrap","justifyContent":"space-between"}} -->
<div class="wp-block-group alignwide"><!-- wp:heading -->
<h2 class="wp-block-heading">On the board</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"muted","fontSize":"small"} -->
<p class="has-muted-color has-text-color has-small-font-size">Everything we show is from a public archive or given to us with permission.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"align":"wide","layout":{"type":"grid","minimumColumnWidth":"15rem"}} -->
<div class="wp-block-group alignwide"><!-- wp:group {"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:image {"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/court.jpg' ) ); ?>" alt="The old Crown Court building in Wakefield: a stone portico with columns and a clock tower"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph {"className":"is-style-exhibit-tag"} -->
<p class="is-style-exhibit-tag">Exhibit 1. The court building. The trial moved here in 1995.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:image {"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/archive.jpg' ) ); ?>" alt="Shelves of labelled grey archive boxes"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph {"className":"is-style-exhibit-tag"} -->
<p class="is-style-exhibit-tag">Exhibit 2. Box 14 of 31, where the second report was filed</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:image {"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/newspaper.jpg' ) ); ?>" alt="A printing press with newspapers coming off it and a sign reading next press run at 1.00"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph {"className":"is-style-exhibit-tag"} -->
<p class="is-style-exhibit-tag">Exhibit 3. The evening paper, 12 March 1994</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:image {"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/tape.jpg' ) ); ?>" alt="Close-up of the metal plate on an old cassette tape recorder listing its tape speed and power"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph {"className":"is-style-exhibit-tag"} -->
<p class="is-style-exhibit-tag">Exhibit 4. Janet’s tapes of her dad, recorded in 1989</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group --></section>
<!-- /wp:group -->
