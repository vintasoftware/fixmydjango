"""
Django settings for fix_my_django project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
from decouple import config, Csv


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


def base_dir_join(*args):
    return os.path.join(BASE_DIR, *args)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='+jno(3dwnsd%udqda)-9g1ng#l#gbyxy1r0dwxi3hbz*wx#wa*')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=Csv())

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

LOCAL = 'IN_HEROKU' not in os.environ


# Admins and Managers

ADMINS = (
    ('Vinta', 'contact@vinta.com.br'),
)

MANAGERS = ADMINS


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    'corsheaders',
    'rest_framework',
    'djangobower',
    'compressor',
    'django_filters',
    'widget_tweaks',
    'django_markdown',
    'meta',

    # Apps
    'core',
    'error_posts',
)

MIDDLEWARE_CLASSES = (
    'log_request_id.middleware.RequestIDMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'fix_my_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'fix_my_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': base_dir_join('db.sqlite3'),
    }
}

if not LOCAL:
    DATABASES['default'] = dj_database_url.config()

# Caches
if not LOCAL:
    CACHES = {
        'default': {
            'BACKEND': 'django_bmemcached.memcached.BMemcached',
            'LOCATION': config('MEMCACHEDCLOUD_SERVERS', cast=Csv()),
            'OPTIONS': {
                'username': config('MEMCACHEDCLOUD_USERNAME'),
                'password': config('MEMCACHEDCLOUD_PASSWORD')
            }
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Email settings

DEFAULT_FROM_EMAIL = 'contact@vinta.com.br'

if LOCAL:
    INSTALLED_APPS += ('naomi',)
    EMAIL_BACKEND = 'naomi.mail.backends.naomi.NaomiBackend'
    EMAIL_FILE_PATH = base_dir_join('tmp_email')
else:
    SERVER_EMAIL = config('SERVER_EMAIL')
    EMAIL_HOST = config('EMAIL_HOST')
    EMAIL_PORT = config('EMAIL_PORT')
    EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
    EMAIL_HOST_USER = config('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

# REST

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
    ),
}

if DEBUG:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.JSONRenderer',
    )

# CORS

CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'^/api/.*$'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',

    'djangobower.finders.BowerFinder',
    'compressor.finders.CompressorFinder',
)

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', default=None)
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY', default=None)
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME', default=None)
AWS_S3_SECURE_URLS = False
AWS_QUERYSTRING_AUTH = False
AWS_S3_CUSTOM_DOMAIN = '{0}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)

STATICFILES_STORAGE = config('STATICFILES_STORAGE', 'django.contrib.staticfiles.storage.StaticFilesStorage')
DEFAULT_FILE_STORAGE = config('DEFAULT_FILE_STORAGE', 'django.core.files.storage.FileSystemStorage')
MEDIA_ROOT = base_dir_join('media')
STATIC_ROOT = base_dir_join('staticfiles')

if LOCAL:
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'
else:
    STATIC_URL = 'http://{0}/static/'.format(AWS_S3_CUSTOM_DOMAIN)
    MEDIA_URL = 'http://{0}/media/'.format(AWS_S3_CUSTOM_DOMAIN)


# collectfast

AWS_PRELOAD_METADATA = True
COLLECTFAST_CACHE = 'collectfast'
COLLECTFAST_ENABLED = not LOCAL


# Bower

BOWER_COMPONENTS_ROOT = base_dir_join('components')

BOWER_INSTALLED_APPS = (
    'bootstrap-sass-official#3.3.4',
    'jquery#2.1.4',
    'font-awesome#4.3.0',
    'select2#4.0.0',
    'select2-bootstrap-theme#0.1.0-beta.3',
)

# Compressor

COMPRESS_ENABLED = True
COMPRESS_STORAGE = STATICFILES_STORAGE
COMPRESS_URL = STATIC_URL

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'core.compressor_filters.PatchedSCSSCompiler'),
)

COMPRESS_CSS_FILTERS = (
    'core.compressor_filters.CustomCssAbsoluteFilter',
)

# Markdown settings

MARKDOWN_EXTENSIONS = ['extra', 'codehilite']
MARKDOWN_PROTECT_PREVIEW = True

# Meta tags settings
# https://github.com/nephila/django-meta#configuration

META_USE_OG_PROPERTIES = True
META_USE_TWITTER_PROPERTIES = True
META_USE_GOOGLEPLUS_PROPERTIES = True

# fix-my-django-lib settings

FIX_MY_DJANGO_ADMIN_MODE = True

# Logging
# https://docs.djangoproject.com/en/1.8/topics/logging/

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
LOG_REQUESTS = not DEBUG
