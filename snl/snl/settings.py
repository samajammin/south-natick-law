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
# SECRET_KEY = os.environ['SECRET_KEY']
SECRET_KEY = 'hf(ft0wh$xjqz%la)$l&4mtkw^ff&vj(#rm81(oio$gyyqp6@p'

# SECURITY WARNING: don't run with debug turned on in production!

# Production
# DEBUG = False
# Dev
DEBUG = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']


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

# todo email confirmation from @southnaticklaw.com email
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'SouthNatickLaw@gmail.com'
EMAIL_HOST_PASSWORD = '@BGrowing'
DEFAULT_FROM_MAIL = 'SouthNatickLaw@gmail.com'
DEFAULT_FROM_EMAIL = 'SouthNatickLaw@gmail.com'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

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
# SITE_ID = 2

#Test
SITE_ID = 1

MARKDOWN_EDITOR_SKIN = 'simple'

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

MEDIA_URL = "/media/"
# MEDIA_ROOT = os.path.join(PROJECT_ROOT, "static", *MEDIA_URL.strip("/").split("/"))
MEDIA_ROOT = os.path.join(BASE_DIR, "..", "www", "media")

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'website/templates/'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

# STATIC_ROOT = os.path.join(BASE_DIR, "..", "snl", "website", "static")
STATIC_ROOT = os.path.join(BASE_DIR, "..", "www", "static")
STATIC_URL = '/static/'


STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'website', 'static'),
)



try:
    from local_settings import *
except ImportError:
    pass
