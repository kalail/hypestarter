from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('artists.views',
	url(r'^(?P<artist_id>\d+)/$', 'show', name='show_artist'),
	url(r'^hot/$', 'hot', name='hot_artists')
)