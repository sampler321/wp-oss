<?php
/**
 * Title: Hero: big tray of food
 * Slug: platter/hero
 * Categories: platter,featured
 * Description: Opener: headline, one short paragraph, two buttons, a big food photo with a round price sticker.
 */
?>
<!-- wp:group {"tagName":"section","align":"full","className":"is-style-mustard","layout":{"type":"constrained"}} -->
<section class="wp-block-group alignfull is-style-mustard"><!-- wp:columns {"verticalAlignment":"center","align":"wide"} -->
<div class="wp-block-columns alignwide are-vertically-aligned-center"><!-- wp:column {"width":"46%"} -->
<div class="wp-block-column" style="flex-basis:46%"><!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">Big trays of proper food, carried in hot.</h1>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"large"} -->
<p class="has-large-font-size">Weddings, film crews, office lunches and birthday dinners for 20 to 300, cooked in our Bristol kitchen and served family-style so people pass things and talk. Femi does the cooking. Rosa makes sure it arrives.</p>
<!-- /wp:paragraph -->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/enquire/">Start your brief</a></div>
<!-- /wp:button -->

<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/menus/">See the menus</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:image {"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/paella.jpg' ) ); ?>" alt="A wide paella pan over a fire, full of rice, mussels and red peppers, with a wooden spoon going in"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph {"className":"is-style-sticker"} -->
<p class="is-style-sticker">Paella for 140 from £18 a head</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></section>
<!-- /wp:group -->
