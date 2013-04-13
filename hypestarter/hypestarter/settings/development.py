import os

# Debug
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Database
import dj_database_url
DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

# Amazon S3 setting
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = 'hypestarter_dev'

DEFAULT_FILE_STORAGE = 'helpers.storages.MediaS3Storage'
STATICFILES_STORAGE = 'helpers.storages.StaticS3Storage'

# URL prefix for files.
STATIC_URL = 'https://s3.amazonaws.com/' + AWS_STORAGE_BUCKET_NAME + '/static/'
MEDIA_URL = 'https://s3.amazonaws.com/' + AWS_STORAGE_BUCKET_NAME + '/media/'

# RabbitMQ
BROKER_URL = os.environ.get('CLOUDAMQP_URL')
BROKER_POOL_LIMIT = 1

# Memcachier
os.environ['MEMCACHE_SERVERS'] = os.environ.get('MEMCACHIER_SERVERS', '')
os.environ['MEMCACHE_USERNAME'] = os.environ.get('MEMCACHIER_USERNAME', '')
os.environ['MEMCACHE_PASSWORD'] = os.environ.get('MEMCACHIER_PASSWORD', '')

# Cache settings
CACHES = {
 	'default': {
		'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
		'LOCATION': os.environ.get('MEMCACHIER_SERVERS', ''),
		'TIMEOUT': 500,
		'BINARY': True,
	}
}

INSTALLED_APPS = (
	# Contrib
	'suit',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.admin',
	'django.contrib.admindocs',
	
	# Third party
	'south',
	'djcelery',
	'storages',
	'gunicorn',
	'django_extensions',
	'social_auth',
	'crispy_forms',
	'raven.contrib.django.raven_compat',
	'sorl.thumbnail',

	# Project
	'landing',
	'artists',
)

SECRET_KEY = os.environ.get('SECRET_KEY')

TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware',
)

THUMBNAIL_DEBUG = True