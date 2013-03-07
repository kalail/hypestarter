from django.db import models

class Genre(models.Model):
	"""Genre

	A particular type of music.
	
	"""
	name = models.CharField(max_length=64)

	def __unicode__(self):
		return self.name

class Artist(models.Model):
	"""Artist

	A band or individual who makes music.

	"""
	name = models.CharField(max_length=256)
	description = models.TextField(blank=True)
	bio = models.TextField(blank=True)
	genre = models.ForeignKey(Genre)
	image = models.ImageField(upload_to='artist_images')

	def __unicode__(self):
		return self.name