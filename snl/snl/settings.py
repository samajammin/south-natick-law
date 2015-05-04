"""
Django settings for snl project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

if 'SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!

# Production
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

ADMINS = (('Sam', 'sbrichards@gmail.com'), ('Sam', 'srichards@southnaticklaw.com'))

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.redirects',
    'website',
    'django_extensions',
    'django_markdown',
    'bootstrapform',
    'storages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
)

ROOT_URLCONF = 'snl.urls'

WSGI_APPLICATION = 'snl.wsgi.application'

if 'EMAIL_HOST' in os.environ:
    EMAIL_USE_TLS = True
    EMAIL_HOST = os.environ['EMAIL_HOST']
    EMAIL_PORT = os.environ['EMAIL_PORT']
    EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
    EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
    DEFAULT_FROM_MAIL = os.environ['DEFAULT_FROM_MAIL']
    DEFAULT_FROM_EMAIL = os.environ['DEFAULT_FROM_EMAIL']

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#Production
SITE_ID = 1

MARKDOWN_EDITOR_SKIN = 'simple'

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))


if 'AWS_STORAGE_BUCKET_NAME' in os.environ:
    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_KEY']
    # Tell django-storages that when coming up with the URL for an item in S3 storage, keep
    # it simple - just use this domain plus the path. (If this isn't set, things get complicated).
    # This controls how the `static` template tag from `staticfiles` gets expanded, if you're using it.
    # We also use it in the next setting.
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    # This is used by the `static` template tag from `static`, if you're using that. Or if anything else
    # refers directly to STATIC_URL. So it's safest to always set it.
    # STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
    # Tell the staticfiles app to use S3Boto storage when writing the collected static files (when
    # you run `collectstatic`).
    # STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    STATICFILES_LOCATION = 'static'
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
    MEDIAFILES_LOCATION = 'media'
    MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'




try:
    from local_settings import *
except ImportError:
    pass
