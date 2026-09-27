<?php
/**
 * Registers this theme's block pattern categories. Nothing else.
 */
add_action( 'init', function () {
	register_block_pattern_category( 'hero', array( 'label' => __( 'Hero', 'lingua' ) ) );
	register_block_pattern_category( 'prices', array( 'label' => __( 'Prices', 'lingua' ) ) );
} );
