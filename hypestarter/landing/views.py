from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib import auth, messages


from .models import Featured

def index(request):
	"""Landing

	Landing page for the website.

	"""
	# Collect data for index page
	try:
		featured = Featured.objects.latest()
	except Featured.DoesNotExist:
		featured = None
	return render_to_response(
		'landing/index.html',
		{
			'featured': featured,
		},
		context_instance=RequestContext(request)
	)

def about(request):
	"""About Page

	Displays information about the project and the team behind it.

	"""
	return render_to_response(
		'landing/about.html',
		context_instance=RequestContext(request)
	)

def logout(request):
	"""Logout View

	Log out the current user.

	"""
	auth.logout(request)
	messages.success(request, 'Logged out!')
	return HttpResponseRedirect(reverse('index'))