<?php
/**
 * Title: Case study: screens gallery (lightbox)
 * Slug: case/cs-screens-gallery
 * Categories: case-study
 */
?>
<!-- wp:heading {"level":3,"anchor":"screens"} -->
<h3 id="screens" class="wp-block-heading">Screens</h3>
<!-- /wp:heading -->

<!-- wp:gallery {"columns":3,"linkTo":"none","align":"wide"} -->
<figure class="wp-block-gallery alignwide has-nested-images columns-3 is-cropped"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/ui-kiosk-after.jpg' ) ); ?>" alt="New ticket machine screen: a search box, then a list of nearby stations with journey times, Partick highlighted"/><figcaption class="wp-element-caption">Destination</figcaption></figure>
<!-- /wp:image -->

<!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/ui-kiosk-price.jpg' ) ); ?>" alt="Price screen: three ticket types, each with the railcard price highlighted beside the full price"/><figcaption class="wp-element-caption">Price with railcard</figcaption></figure>
<!-- /wp:image -->

<!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/ui-kit.jpg' ) ); ?>" alt="Design system sheet: five colour swatches, two type sizes, three button styles and the search field"/><figcaption class="wp-element-caption">UI kit</figcaption></figure>
<!-- /wp:image --></figure>
<!-- /wp:gallery -->
