from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
	"""Index Page

	Landing page for the website.

	"""
	# Collect data for index page
	return render_to_response('base.html', context_instance=RequestContext(request))