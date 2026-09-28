<?php
/**
 * Seed: pattern categories only.
 *
 * @package seed
 */

add_action(
	'init',
	function () {
		foreach ( array(
			'seed-hero' => 'Code art: openers',
			'seed-works' => 'Code art: works and outputs',
			'seed-writing' => 'Code art: process writing',
			'seed-prints' => 'Code art: prints and editions',
			'seed-about' => 'Code art: about, shows and workshops',
			'seed-contact' => 'Code art: contact and notices',
			'seed-pages' => 'Code art: page layouts',
		) as $slug => $label ) {
			register_block_pattern_category( $slug, array( 'label' => $label ) );
		}
	}
);
