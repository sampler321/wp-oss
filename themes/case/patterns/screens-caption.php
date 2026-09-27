<?php
/**
 * Title: Screenshot with a text description
 * Slug: case/screens-caption
 * Categories: gallery
 */
?>
<!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none","align":"wide","className":"is-style-framed"} -->
<figure class="wp-block-image alignwide size-large is-style-framed"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/selfcheckout.jpg' ) ); ?>" alt="A self-checkout screen beside a bin for scanning clothes, with the total shown in yen"/><figcaption class="wp-element-caption">Scan screen with the tag-removal step moved above the total</figcaption></figure>
<!-- /wp:image -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><strong>What changed:</strong> the security tag step used to appear after payment, so people paid, then waited for staff. It now comes first, while the bag is still open.</p>
<!-- /wp:paragraph -->
