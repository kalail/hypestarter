container = $('#container')
container.imagesLoaded(
	->
		container.masonry(
			itemSelector : '.explore_artist',
			columnWidth : 240
		)
)
