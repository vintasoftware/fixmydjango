import dj_database_url

from decouple import config

from .base import * # noqa


DEBUG = True

SECRET_KEY = 'secret'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fixmydjango',
    }
}

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

MEDIA_ROOT = 'mediafiles'
MEDIA_URL = '/media/'

RECAPTCHA_KEY = ''
RECAPTCHA_SECRET_KEY = ''
