from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
	"""Index Page

	Index page.

	"""
	# Collect data for index page

	return render_to_response(
		'index.html',
		context_instance=RequestContext(request)
	)