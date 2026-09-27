<?php
/**
 * Drop: pattern categories only.
 *
 * @package drop
 */

add_action(
	'init',
	function () {
		register_block_pattern_category( 'hero', array( 'label' => __( 'Drop: openers', 'drop' ) ) );
		register_block_pattern_category( 'merch', array( 'label' => __( 'Drop: merch', 'drop' ) ) );
		register_block_pattern_category( 'drops', array( 'label' => __( 'Drop: drops and archive', 'drop' ) ) );
		register_block_pattern_category( 'lookbook', array( 'label' => __( 'Drop: lookbook', 'drop' ) ) );
		register_block_pattern_category( 'tour', array( 'label' => __( 'Drop: tour', 'drop' ) ) );
		register_block_pattern_category( 'diary', array( 'label' => __( 'Drop: zine and diary', 'drop' ) ) );
		register_block_pattern_category( 'collabs', array( 'label' => __( 'Drop: collabs and stockists', 'drop' ) ) );
		register_block_pattern_category( 'info', array( 'label' => __( 'Drop: sizing and shipping', 'drop' ) ) );
		register_block_pattern_category( 'signup', array( 'label' => __( 'Drop: sign-ups', 'drop' ) ) );
		register_block_pattern_category( 'notices', array( 'label' => __( 'Drop: notices', 'drop' ) ) );
		register_block_pattern_category( 'about', array( 'label' => __( 'Drop: the band', 'drop' ) ) );
		register_block_pattern_category( 'contact', array( 'label' => __( 'Drop: contact', 'drop' ) ) );
		register_block_pattern_category( 'pages', array( 'label' => __( 'Drop: page layouts', 'drop' ) ) );
	}
);
