from django.test import TestCase

class ArtistsViewsTestCase(TestCase):

	def test_show_404(self):
		resp = self.client.get('/artists/1/show')
		self.assertEqual(resp.status_code, 404)
