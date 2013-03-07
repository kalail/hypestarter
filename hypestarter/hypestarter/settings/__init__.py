import os

# Relative path settings
from unipath import Path
PROJECT_ROOT = Path(__file__).ancestor(3)

# Set various variables.
TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = PROJECT_ROOT.child('media')

# Absolute path to the directory static files should be collected to using collectstatic.
STATIC_ROOT = ''

# Additional locations of static files - absolute paths
STATICFILES_DIRS = (
	PROJECT_ROOT.child('static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader'
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'hypestarter.urls'

# WSGI server for debug server.
WSGI_APPLICATION = 'hypestarter.wsgi.application'

# Templates location - absolute path
TEMPLATE_DIRS = (
	PROJECT_ROOT.child('templates'),
)

# Set up Sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# Celery settings
import djcelery
djcelery.setup_loader()


LOGIN_URL = '/login/twitter/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL = '/login-error/'

AUTHENTICATION_BACKENDS = (
	'social_auth.backends.twitter.TwitterBackend',
	'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
	'social_auth.backends.pipeline.social.social_auth_user',
	'social_auth.backends.pipeline.user.get_username',
	'social_auth.backends.pipeline.user.create_user',
	'social_auth.backends.pipeline.social.associate_user',
	'social_auth.backends.pipeline.social.load_extra_data',
	'social_auth.backends.pipeline.user.update_user_details'
)

# Import corresponding environment settings.
try:
	app_env = os.environ["HYPESTARTER_ENV"]
	if app_env == "production":
		# Import production settings
		from .production import *
	elif app_env == "development":
		# Import development settings
		from .development import *
except KeyError, e:
	# import local settings
	from .local import *