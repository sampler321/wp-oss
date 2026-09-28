<?php
/**
 * Good Dog: pattern categories only.
 *
 * @package good-dog
 */

add_action(
	'init',
	function () {
		register_block_pattern_category( 'hero', array( 'label' => __( 'Good Dog: openers', 'good-dog' ) ) );
		register_block_pattern_category( 'products', array( 'label' => __( 'Good Dog: shop', 'good-dog' ) ) );
		register_block_pattern_category( 'guides', array( 'label' => __( 'Good Dog: size and care guides', 'good-dog' ) ) );
		register_block_pattern_category( 'dog-wall', array( 'label' => __( 'Good Dog: dog wall', 'good-dog' ) ) );
		register_block_pattern_category( 'reviews', array( 'label' => __( 'Good Dog: reviews', 'good-dog' ) ) );
		register_block_pattern_category( 'about', array( 'label' => __( 'Good Dog: about', 'good-dog' ) ) );
		register_block_pattern_category( 'info', array( 'label' => __( 'Good Dog: delivery and repairs', 'good-dog' ) ) );
		register_block_pattern_category( 'signup', array( 'label' => __( 'Good Dog: sign-ups', 'good-dog' ) ) );
		register_block_pattern_category( 'notices', array( 'label' => __( 'Good Dog: notices', 'good-dog' ) ) );
		register_block_pattern_category( 'pages', array( 'label' => __( 'Good Dog: page layouts', 'good-dog' ) ) );
	}
);
