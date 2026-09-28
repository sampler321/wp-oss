<?php
/**
 * Title: Algorithm, step by step
 * Slug: seed/algorithm-steps
 * Categories: seed-writing,text
 */
?>
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">How Drift works</h3>
<!-- /wp:heading -->

<!-- wp:list {"ordered":true} -->
<ol class="wp-block-list"><!-- wp:list-item -->
<li>Make a field: at every point on the page, add four slow sine waves to get an angle.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Drop 1,400 points at random, using the seed.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Move each point a tiny step along the angle under it, and draw the step. Repeat 30 to 90 times.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Stop a line when it leaves the page. Every seventeenth line is drawn in red.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>For plotting, merge lines that nearly touch, so the pen lifts less. That cut plot time from nine hours to five.</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->
