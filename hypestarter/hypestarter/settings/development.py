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

# Set up simple master logger
LOGGING = {
	'version': 1,
	'disable_existing_loggers': True,
	'formatters': {
		'verbose': {
			'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
		},
		'simple': {
			'format': '%(levelname)s %(message)s'
		},
	},
	'handlers': {
		'console':{
			'level': 'INFO',
			'class': 'logging.StreamHandler',
			'formatter': 'simple'
		},
	},
	'loggers': {
		'': {
			'handlers': ['console'],
			'level': 'INFO',
			'propagate': True,
		},
	}
}