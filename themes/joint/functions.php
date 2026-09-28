<?php
/**
 * Joint: registers the pattern categories used by the theme's patterns.
 *
 * @package joint
 */

add_action(
	'init',
	function () {
		register_block_pattern_category( 'object', array( 'label' => __( 'Object pages', 'joint' ) ) );
		register_block_pattern_category( 'pieces', array( 'label' => __( 'Pieces and shop', 'joint' ) ) );
		register_block_pattern_category( 'hero', array( 'label' => __( 'Heroes', 'joint' ) ) );
		register_block_pattern_category( 'making', array( 'label' => __( 'Materials and making', 'joint' ) ) );
		register_block_pattern_category( 'services', array( 'label' => __( 'Commissions and trade', 'joint' ) ) );
		register_block_pattern_category( 'about', array( 'label' => __( 'Workshop and makers', 'joint' ) ) );
		register_block_pattern_category( 'projects', array( 'label' => __( 'Projects', 'joint' ) ) );
		register_block_pattern_category( 'contact', array( 'label' => __( 'Visit and contact', 'joint' ) ) );
		register_block_pattern_category( 'page', array( 'label' => __( 'Page layouts', 'joint' ) ) );
	}
);
