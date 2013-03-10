from django.test import TestCase
from .models import Artist, Genre

class ArtistsViewsNotAuthenticatedTestCase(TestCase):

	def setUp(self):
		super(ArtistsViewsNotAuthenticatedTestCase, self).setUp()
		g = Genre.objects.create(name='default')
		Artist.objects.create(
			name = 'Justin Bieber',
			genre = g,
			image = 'artist_images/macklemore.jpg'
		)

	def test_show(self):
		resp = self.client.get('/artists/1/show')
		# Test response
		self.assertEqual(resp.status_code, 301)


class ArtistsViewsAuthenticatedTestCase(TestCase):

	def setUp(self):
		super(ArtistsViewsAuthenticatedTestCase, self).setUp()
		g = Genre.objects.create(name='default')
		Artist.objects.create(
			name = 'Justin Bieber',
			genre = g,
			image = 'artist_images/macklemore.jpg'
		)


	def test_show(self):
		resp = self.client.get('/artists/1/show')
		# Test 200
		self.assertEqual(resp.status_code, 200)
		# Test template
		self.assertTrue('artists/show.html' in resp.templates)
		# Test object
		self.assertTrue('artist' in resp.context)