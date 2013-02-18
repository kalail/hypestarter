from django.db import models
from artists.models import Artist
from django.utils import timezone


class Featured(models.Model):
	"""Featured

	A collection of Artists that are displayed on the homepage.

	"""
	artists = models.ManyToManyField(Artist)
	date = models.DateField(default=timezone.now)

	class Meta:
		get_latest_by = 'date'

	def __unicode__(self):
		return 'Featured on %s' % self.date