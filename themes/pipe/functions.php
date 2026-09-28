<?php
/**
 * Pipe: pattern categories only.
 *
 * @package pipe
 */

add_action(
	'init',
	function () {
		register_block_pattern_category( 'hero', array( 'label' => __( 'Pipe: openers', 'pipe' ) ) );
		register_block_pattern_category( 'services', array( 'label' => __( 'Pipe: services and prices', 'pipe' ) ) );
		register_block_pattern_category( 'quote', array( 'label' => __( 'Pipe: quotes and urgency', 'pipe' ) ) );
		register_block_pattern_category( 'areas', array( 'label' => __( 'Pipe: areas and contact', 'pipe' ) ) );
		register_block_pattern_category( 'about', array( 'label' => __( 'Pipe: people and registration', 'pipe' ) ) );
		register_block_pattern_category( 'info', array( 'label' => __( 'Pipe: help and advice', 'pipe' ) ) );
		register_block_pattern_category( 'notices', array( 'label' => __( 'Pipe: notices', 'pipe' ) ) );
		register_block_pattern_category( 'pages', array( 'label' => __( 'Pipe: page layouts', 'pipe' ) ) );
	}
);
