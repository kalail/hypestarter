from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('landing.views',
	url(r'^$', 'index', name='index'),
	url(r'^about/$', 'about', name='about'),
	url(r'^logout/$', 'logout', name='logout'),
)