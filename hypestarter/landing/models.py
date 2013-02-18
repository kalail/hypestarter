from django.db import models
from artists.models import Artist
from django.utils import timezone


class FeaturedArtists(models.Model):
	"""Featured Artist

	Artists tht are displayed on the homepage.

	"""
	artists = models.ManyToManyField(Artist)
	date = models.DateField(default=timezone.now)