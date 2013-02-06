from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('landing.views',
	url(r'^$', 'index'),
	)