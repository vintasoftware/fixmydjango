import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def base_dir_join(*args):
    return os.path.join(BASE_DIR, *args)


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

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
    'bootstrap_pagination',
    'django_comments',
    'django.contrib.sites',

    # Apps
    'core',
    'error_posts',
    'users',
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
        'DIRS': ['templates'],
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

# Internationalization

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Email settings
DEFAULT_FROM_EMAIL = 'contact@vinta.com.br'

# REST

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
    ),
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '3/second',
        'user': '3/second'
    }
}

# CORS
CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'^/api/.*$'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',

    'djangobower.finders.BowerFinder',
)

MEDIA_ROOT = 'media'
STATIC_ROOT = 'static'

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

# Bower

BOWER_COMPONENTS_ROOT = base_dir_join('components')

BOWER_INSTALLED_APPS = (
    'bootstrap-sass-official#3.3.4',
    'jquery#2.1.4',
    'font-awesome#4.3.0',
    'select2#4.0.0',
    'select2-bootstrap-theme#0.1.0-beta.3',
)

# Markdown settings
MARKDOWN_EXTENSIONS = ['extra', 'codehilite']

# Meta tags settings
# https://github.com/nephila/django-meta#configuration

META_USE_OG_PROPERTIES = True
META_USE_TWITTER_PROPERTIES = True
META_USE_GOOGLEPLUS_PROPERTIES = True
META_SITE_DOMAIN = 'http://www.fixmydjango.com'

# Messages
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

# Login
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

# Auth
AUTH_USER_MODEL = 'users.User'

# Default value for django.contrib.sites
SITE_ID = 1

# Comment app
COMMENTS_APP = 'error_posts'
