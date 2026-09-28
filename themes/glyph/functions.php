<?php
/**
 * Glyph: registers the pattern categories used by the theme's patterns.
 *
 * @package glyph
 */

add_action(
	'init',
	function () {
		register_block_pattern_category( 'specimen', array( 'label' => __( 'Specimen', 'glyph' ) ) );
		register_block_pattern_category( 'typefaces', array( 'label' => __( 'Typefaces', 'glyph' ) ) );
		register_block_pattern_category( 'licensing', array( 'label' => __( 'Licensing and shop', 'glyph' ) ) );
		register_block_pattern_category( 'trials', array( 'label' => __( 'Trials and free fonts', 'glyph' ) ) );
		register_block_pattern_category( 'in-use', array( 'label' => __( 'In use', 'glyph' ) ) );
		register_block_pattern_category( 'about', array( 'label' => __( 'Foundry', 'glyph' ) ) );
		register_block_pattern_category( 'page', array( 'label' => __( 'Page layouts', 'glyph' ) ) );
	}
);
