<?php
/**
 * Title: Home: title card, latest file, board, episodes
 * Slug: evidence/front-page-layout
 * Categories: featured
 * Inserter: no
 */
?>
<!-- wp:pattern {"slug":"evidence/title-card"} /-->

<!-- wp:pattern {"slug":"evidence/latest-file"} /-->

<!-- wp:pattern {"slug":"evidence/evidence-board"} /-->

<!-- wp:columns {"className":"alignwide","style":{"spacing":{"padding":{"top":"var:preset|spacing|60"},"blockGap":{"left":"var:preset|spacing|60"}}}} -->
<div class="wp-block-columns alignwide" style="padding-top:var(--wp--preset--spacing--60)"><!-- wp:column {"width":"58%"} -->
<div class="wp-block-column" style="flex-basis:58%"><!-- wp:pattern {"slug":"evidence/timeline"} /--></div>
<!-- /wp:column -->

<!-- wp:column {"width":"42%"} -->
<div class="wp-block-column" style="flex-basis:42%"><!-- wp:pattern {"slug":"evidence/in-memory"} /--></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:pattern {"slug":"evidence/episode-list"} /-->

<!-- wp:columns {"className":"alignwide","style":{"spacing":{"padding":{"bottom":"var:preset|spacing|70"},"blockGap":{"left":"var:preset|spacing|60"}}}} -->
<div class="wp-block-columns alignwide" style="padding-bottom:var(--wp--preset--spacing--70)"><!-- wp:column {"width":"58%"} -->
<div class="wp-block-column" style="flex-basis:58%"><!-- wp:pattern {"slug":"evidence/how-we-report"} /--></div>
<!-- /wp:column -->

<!-- wp:column {"width":"42%"} -->
<div class="wp-block-column" style="flex-basis:42%"><!-- wp:pattern {"slug":"evidence/tip-line"} /--></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
