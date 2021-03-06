import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = os.getenv('SECRET_KEY', 'f^#!hup+c&4nq)x_z&%9bb$5#2m*ya1)k611dzve3x2p=n^@2z')
DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'oneminutelabel',
    'south'
)

MIDDLEWARE_CLASSES = (
    'sslify.middleware.SSLifyMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'oneminutelabel.urls'
WSGI_APPLICATION = 'oneminutelabel.wsgi.application'


# Database
DATABASES = {'default': {}}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/')]
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] [%(process)-6d-%(thread)-13d] [%(pathname)-70s:%(lineno)-5d] [%(levelname)-8s] --- %(message)s',
        }
    },
    'handlers': {
        'null': {
            'level': 'INFO',
            'class': 'django.utils.log.NullHandler',
            'formatter': 'verbose'
        },
        'console':{
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO'
        },
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'requests': {
            'handlers': ['console'],
            'level': 'ERROR',
        },
        'shippo': {
            'handlers': ['console'],
            'level': 'WARNING',
        },
        'stripe': {
            'handlers': ['console'],
            'level': 'WARNING',
        },
    }
}

# API Tokens
SHIPPO_TOKEN = os.getenv("SHIPPO_TOKEN")
STRIPE_TOKEN = os.getenv("STRIPE_TOKEN")
STRIPE_PUBLISHABLE_TOKEN = os.getenv("STRIPE_PUBLISHABLE_TOKEN")
STRIPE_DESCRIPTION = "One Minute Label Postage"

# Heroku
# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# Allow all host headers
ALLOWED_HOSTS = ['*']

try:
    from settings_local import *
except:
    pass