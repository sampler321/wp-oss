<?php
/**
 * Platter: pattern categories only.
 *
 * @package platter
 */

add_action(
	'init',
	function () {
		register_block_pattern_category( 'hero', array( 'label' => __( 'Platter: openers', 'platter' ) ) );
		register_block_pattern_category( 'case-study', array( 'label' => __( 'Platter: case studies', 'platter' ) ) );
		register_block_pattern_category( 'menu', array( 'label' => __( 'Platter: menus', 'platter' ) ) );
		register_block_pattern_category( 'services', array( 'label' => __( 'Platter: event types', 'platter' ) ) );
		register_block_pattern_category( 'enquire', array( 'label' => __( 'Platter: enquiries and pricing', 'platter' ) ) );
		register_block_pattern_category( 'about', array( 'label' => __( 'Platter: team, suppliers, venues', 'platter' ) ) );
		register_block_pattern_category( 'info', array( 'label' => __( 'Platter: questions and practical', 'platter' ) ) );
		register_block_pattern_category( 'notices', array( 'label' => __( 'Platter: notices', 'platter' ) ) );
		register_block_pattern_category( 'pages', array( 'label' => __( 'Platter: page layouts', 'platter' ) ) );
	}
);
