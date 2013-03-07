from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from artists.models import Artist


@login_required
def index(request):
	"""Index Page

	Index page.

	"""
	# Collect data for index page
	artists = Artist.objects.all()
	return render_to_response('index.html',
		{
			'artists': artists,
		},
		context_instance=RequestContext(request)
	)