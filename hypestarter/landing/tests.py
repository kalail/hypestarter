from django.test import TestCase

class LandingIndexTestCase(TestCase):

	def test_index(self):
		resp = self.client.get('/')
		self.assertEqual(resp.status_code, 200)

	def test_index_templates(self):
		resp = self.client.get('/')
		templates = [template.name for template in resp.templates]
		self.assertTrue('landing/index.html' in templates)
		self.assertTrue('base.html' in templates)
		self.assertTrue('_nav.html' in templates)
		