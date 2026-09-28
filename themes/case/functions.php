<?php
/**
 * Case: registers the pattern categories used by the theme's patterns.
 *
 * @package case
 */

add_action(
	'init',
	function () {
		register_block_pattern_category( 'case-study', array( 'label' => __( 'Case study blocks', 'case' ) ) );
		register_block_pattern_category( 'case-page', array( 'label' => __( 'Case study pages', 'case' ) ) );
		register_block_pattern_category( 'hero', array( 'label' => __( 'Heroes', 'case' ) ) );
		register_block_pattern_category( 'work', array( 'label' => __( 'Work lists', 'case' ) ) );
		register_block_pattern_category( 'services', array( 'label' => __( 'Working together', 'case' ) ) );
		register_block_pattern_category( 'about', array( 'label' => __( 'About', 'case' ) ) );
		register_block_pattern_category( 'contact', array( 'label' => __( 'Contact', 'case' ) ) );
		register_block_pattern_category( 'writing', array( 'label' => __( 'Writing', 'case' ) ) );
	}
);
