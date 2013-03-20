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
	image_alt = models.ImageField(upload_to='artist_images', blank=True)
	# Social
	twitter_handle = models.CharField(max_length=128, blank=True)
	itunes_link = models.URLField(max_length=256, blank=True)
	soundcloud_page = models.URLField(max_length=256, blank=True)
	youtube_page = models.URLField(max_length=256, blank=True)
	bandcamp_page = models.URLField(max_length=256, blank=True)
	facebook_page = models.URLField(max_length=256, blank=True)
	# Songs
	song_1 = models.TextField(blank=True)
	song_2 = models.TextField(blank=True)


	def __unicode__(self):
		return self.name