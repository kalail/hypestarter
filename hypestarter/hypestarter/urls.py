from django.conf.urls import patterns, include, url 
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Social Auth
    url(r'', include('social_auth.urls')),
    # Admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # Artists
    url(r'^artists/', include('artists.urls')),
    # Other
    url(r'^explore/$', 'hypestarter.views.explore', name='explore'),
    url(r'^home/$', 'hypestarter.views.home', name='home'),
    # Landing
    url(r'', include('landing.urls')),

# Serve media files in development.
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)