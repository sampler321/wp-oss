<?php
/**
 * Scoop: pattern categories only.
 *
 * @package scoop
 */

add_action(
	'init',
	function () {
		register_block_pattern_category( 'hero', array( 'label' => __( 'Scoop: openers', 'scoop' ) ) );
		register_block_pattern_category( 'menu', array( 'label' => __( 'Scoop: menu and flavours', 'scoop' ) ) );
		register_block_pattern_category( 'tubs', array( 'label' => __( 'Scoop: tubs and vouchers', 'scoop' ) ) );
		register_block_pattern_category( 'events', array( 'label' => __( 'Scoop: events and wholesale', 'scoop' ) ) );
		register_block_pattern_category( 'about', array( 'label' => __( 'Scoop: story, method, people', 'scoop' ) ) );
		register_block_pattern_category( 'info', array( 'label' => __( 'Scoop: numbers and notes', 'scoop' ) ) );
		register_block_pattern_category( 'visit', array( 'label' => __( 'Scoop: find us', 'scoop' ) ) );
		register_block_pattern_category( 'signup', array( 'label' => __( 'Scoop: newsletter and votes', 'scoop' ) ) );
		register_block_pattern_category( 'notices', array( 'label' => __( 'Scoop: notices', 'scoop' ) ) );
		register_block_pattern_category( 'pages', array( 'label' => __( 'Scoop: page layouts', 'scoop' ) ) );
	}
);
