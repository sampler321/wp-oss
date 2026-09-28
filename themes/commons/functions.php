<?php
/**
 * Commons: registers the pattern categories used by the theme's patterns.
 *
 * @package commons
 */

add_action(
	'init',
	function () {
		register_block_pattern_category( 'whats-on', array( 'label' => __( 'What\'s on', 'commons' ) ) );
		register_block_pattern_category( 'programme', array( 'label' => __( 'Programme', 'commons' ) ) );
		register_block_pattern_category( 'show', array( 'label' => __( 'Show pages', 'commons' ) ) );
		register_block_pattern_category( 'membership', array( 'label' => __( 'Membership', 'commons' ) ) );
		register_block_pattern_category( 'opportunities', array( 'label' => __( 'Opportunities', 'commons' ) ) );
		register_block_pattern_category( 'about', array( 'label' => __( 'About and committee', 'commons' ) ) );
		register_block_pattern_category( 'visit', array( 'label' => __( 'Visit and access', 'commons' ) ) );
		register_block_pattern_category( 'page', array( 'label' => __( 'Page layouts', 'commons' ) ) );
	}
);
