<?php
/**
 * Title: Home: latest episode, overheard, episodes, guests, hosts
 * Slug: confidante/front-page-layout
 * Categories: featured
 * Inserter: no
 */
?>
<!-- wp:pattern {"slug":"confidante/latest-hero"} /-->

<!-- wp:pattern {"slug":"confidante/overheard-photo"} /-->

<!-- wp:pattern {"slug":"confidante/episode-cards"} /-->

<!-- wp:pattern {"slug":"confidante/guest-strip"} /-->

<!-- wp:pattern {"slug":"confidante/dear-say-more"} /-->

<!-- wp:columns {"align":"wide","style":{"spacing":{"padding":{"top":"var:preset|spacing|70","bottom":"var:preset|spacing|60"},"blockGap":{"left":"var:preset|spacing|60"}}}} -->
<div class="wp-block-columns alignwide" style="padding-top:var(--wp--preset--spacing--70);padding-bottom:var(--wp--preset--spacing--60)"><!-- wp:column {"width":"30%"} -->
<div class="wp-block-column" style="flex-basis:30%"><!-- wp:heading {"fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-xx-large-font-size">Who’s talking</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Two friends at a kitchen table in Levenshulme. One keeps spreadsheets, one sends voice notes. We record on Sunday afternoons and it goes out on Tuesday at 6am.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><a href="/hosts/">How the show started</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column {"width":"70%"} -->
<div class="wp-block-column" style="flex-basis:70%"><!-- wp:pattern {"slug":"confidante/hosts"} /--></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:pattern {"slug":"confidante/topics"} /-->
