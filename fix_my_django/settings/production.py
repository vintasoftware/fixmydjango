import dj_database_url

from decouple import config, Csv

from .base import * # noqa


LOCAL = False
DEBUG = False

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

DATABASES = {
    'default': dj_database_url.config()
}

SERVER_EMAIL = config('SERVER_EMAIL')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

STATICFILES_STORAGE = config('STATICFILES_STORAGE')
DEFAULT_FILE_STORAGE = config('DEFAULT_FILE_STORAGE')

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', default=None)
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY', default=None)
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME', default=None)
AWS_S3_SECURE_URLS = False
AWS_QUERYSTRING_AUTH = False
AWS_S3_CUSTOM_DOMAIN = '{0}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)

STATIC_URL = 'http://{0}/static/'.format(AWS_S3_CUSTOM_DOMAIN)
MEDIA_URL = 'http://{0}/media/'.format(AWS_S3_CUSTOM_DOMAIN)

# Compressor
COMPRESS_STORAGE = STATICFILES_STORAGE
COMPRESS_URL = STATIC_URL

# collectfast
AWS_PRELOAD_METADATA = True
COLLECTFAST_ENABLED = True
# COLLECTFAST_CACHE = 'collectfast'

# recaptcha
RECAPTCHA_KEY = config('RECAPTCHA_KEY')
RECAPTCHA_SECRET_KEY = config('RECAPTCHA_SECRET_KEY')

# caches

# CACHES = {
#     'default': {
#         'BACKEND': 'django_bmemcached.memcached.BMemcached',
#         'LOCATION': config('MEMCACHEDCLOUD_SERVERS', cast=Csv()),
#         'OPTIONS': {
#             'username': config('MEMCACHEDCLOUD_USERNAME'),
#             'password': config('MEMCACHEDCLOUD_PASSWORD')
#         }
#     },
#     'collectfast': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'django_db_cache_collectfast',
#         'TIMEOUT': 60 * 60 * 24 * 7,  # 1 week
#         'OPTIONS': {
#             'MAX_ENTRIES': 10000
#         }
#     }
# }

# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'request_id': {
            '()': 'log_request_id.filters.RequestIDFilter'
        }
    },
    'formatters': {
        'standard': {
            'format': '%(levelname)-8s [%(asctime)s] [%(request_id)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'filters': ['request_id'],
            'formatter': 'standard',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO'
        },
        'bmemcached.protocol': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': False
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'log_request_id.middleware': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}

LOG_REQUEST_ID_HEADER = "HTTP_X_REQUEST_ID"
LOG_REQUESTS = True
