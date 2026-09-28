<?php
/**
 * Room: registers the pattern categories used by the theme's patterns.
 *
 * @package room
 */

add_action(
	'init',
	function () {
		register_block_pattern_category( 'project', array( 'label' => __( 'Project stories', 'room' ) ) );
		register_block_pattern_category( 'shop', array( 'label' => __( 'Shop', 'room' ) ) );
		register_block_pattern_category( 'fabric', array( 'label' => __( 'Fabric and wallpaper', 'room' ) ) );
		register_block_pattern_category( 'services', array( 'label' => __( 'Services and fees', 'room' ) ) );
		register_block_pattern_category( 'about', array( 'label' => __( 'About', 'room' ) ) );
		register_block_pattern_category( 'contact', array( 'label' => __( 'Contact', 'room' ) ) );
		register_block_pattern_category( 'hero', array( 'label' => __( 'Heroes', 'room' ) ) );
		register_block_pattern_category( 'page', array( 'label' => __( 'Page layouts', 'room' ) ) );
	}
);
