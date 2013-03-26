# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from .models import Artist


def show(request, artist_id):
	"""Show Page

	Displays the artist Show page.

	"""
	# Get artist object
	artist = get_object_or_404(Artist, id=artist_id)

	return render_to_response('artists/show.html',
		{
			'artist': artist,
		},
		context_instance=RequestContext(request)
	)


def hot(request):
	"""Hot Page

	Displays the artists that are hot right now.

	"""
	artists = Artist.objects.all()[:5]
	return render_to_response('artists/hot.html',
		{
			'artists': artists
		},
		context_instance=RequestContext(request)
	)