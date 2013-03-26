import random

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from artists.models import Artist


def explore(request):
	"""Explore Page

	Show artists that you might enjoy listening to.

	"""
	# Get list of all artists and shuffle it.
	artists = list(Artist.objects.all())
	random.shuffle(artists)
	return render_to_response('explore.html',
		{
			'artists': artists,
		},
		context_instance=RequestContext(request)
	)


@login_required
def home(request):
	"""Home Page

	Show your dashboard.

	"""
	# Get data about the current user.
	return render_to_response('home.html',
		context_instance=RequestContext(request)
	)