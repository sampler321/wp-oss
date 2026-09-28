<?php
/**
 * Oil: pattern categories only.
 *
 * @package oil
 */

add_action(
	'init',
	function () {
		foreach ( array(
			'oil-catalogue' => 'Painter: catalogue and works',
			'oil-work-page' => 'Painter: work page details',
			'oil-exhibitions' => 'Painter: exhibitions and gallery',
			'oil-cv' => 'Painter: CV and press',
			'oil-journal' => 'Painter: journal',
			'oil-contact' => 'Painter: visits, buying and contact',
			'oil-pages' => 'Painter: page layouts',
		) as $slug => $label ) {
			register_block_pattern_category( $slug, array( 'label' => $label ) );
		}
	}
);
