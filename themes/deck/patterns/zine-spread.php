<?php
/**
 * Title: Zine spread (photo, text, pull quote)
 * Slug: deck/zine-spread
 * Categories: zine
 * Description: An inside spread from the zine.
 */
?>
<!-- wp:columns {"align":"wide","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|50"}}}} -->
<div class="wp-block-columns alignwide"><!-- wp:column {"width":"55%"} -->
<div class="wp-block-column" style="flex-basis:55%"><!-- wp:image {"lightbox":{"enabled":true},"aspectRatio":"4/3","scale":"cover","sizeSlug":"large","linkDestination":"none","className":"is-style-halftone"} -->
<figure class="wp-block-image size-large is-style-halftone"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/sunset-park.jpg' ) ); ?>" alt="A skater on the coping of a concrete park at sunset, silhouetted" style="aspect-ratio:4/3;object-fit:cover"/></figure>
<!-- /wp:image --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"className":"is-style-ransom"} -->
<h2 class="wp-block-heading is-style-ransom"><mark>Ten</mark> years <strong>of</strong> <em>the</em> Lagoon <mark>bowl</mark></h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The bowl went in with council money and a lot of letters from parents. Jonny was there the day they poured it and still has the concrete splash on his trainers to prove it.</p>
<!-- /wp:paragraph -->

<!-- wp:pullquote -->
<figure class="wp-block-pullquote"><blockquote><p>Nobody asked for it to be this rough. It is perfect.</p><cite>Jonny Kerr</cite></blockquote></figure>
<!-- /wp:pullquote --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
