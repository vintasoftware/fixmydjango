from .base import * # noqa


DEBUG = True

SECRET_KEY = 'secrete'

DATABASES = {
    'default': config('DATABASE_URL',
                      default='postgresql://localhost:5432/fixmydjango',
                      cast=dj_database_url.parse),
}

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

MEDIA_ROOT = 'mediafiles'
MEDIA_URL = '/media/'

RECAPTCHA_KEY = ''
RECAPTCHA_SECRET_KEY = ''
