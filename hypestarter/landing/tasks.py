from artists.models import Artist
from .models import Featured


def update_featured_artists():
	# Get all artists
	all_artists = Artist.objects.all()
	# Create new fetured model
	featured = Featured()
	featured.save()
	# Add all artists to featured model
	for artist in all_artists:
		featured.artists.add(artist)
		featured.save()

