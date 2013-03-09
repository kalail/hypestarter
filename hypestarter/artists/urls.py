from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('artists.views',
	url(r'^(?P<artist_id>\d+)/show/$', 'show', name='show_artist'),
)