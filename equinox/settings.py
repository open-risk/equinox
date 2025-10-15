# Copyright (c) 2020 - 2025 Open Risk (https://www.openriskmanagement.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Django settings for the Equinox platform.

"""

import os
from pathlib import Path

from django.utils.translation import gettext_lazy as _
from equinox.jazzmin_settings import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3i=clc#nog3a2v__q9n89wak2#p54mfs(*-x)oj7+1)igkmylf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.humanize',
    'django.contrib.staticfiles',
    'django_json_widget',
    'django_extensions',
    'django_htmx',
    'import_export',
    'rest_framework',
    'drf_yasg',
    'treebeard',
    'django.contrib.gis',
    'markdownfield',
    'leaflet',
    'django_countries',
    'start',
    'reference',
    'portfolio',
    'policy',
    'risk',
    'reporting',
    'visualization',
    'debug_toolbar',
    'behave_django'
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_htmx.middleware.HtmxMiddleware',
]

ROOT_URLCONF = 'equinox.urls'

SITE_ID = 1
# SITE_URL = "https://equinoxpoint.org"
SITE_URL = "http://127.0.0.1:8080/"

MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads/')
MEDIA_URL = '/uploads/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

WSGI_APPLICATION = 'equinox.wsgi.application'

DATABASES = {
    'default': {
        "ENGINE": "django.contrib.gis.db.backends.spatialite",
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
    # 'default': {
    #     'ENGINE': 'django.contrib.gis.db.backends.postgis',
    #     'NAME': 'equinox',
    #     'USER': 'equinoxuser',
    #     'PASSWORD': 'equinoxuser',
    #     'HOST': 'localhost',
    #     'PORT': '5433',
    # }
}
SPATIALITE_LIBRARY_PATH = 'mod_spatialite.so'

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
# LANGUAGE_CODE = 'nl'
# LANGUAGE_CODE = 'el'

LANGUAGES = [
    ('en', _('English')),
    ('nl', _('Dutch')),
    ('es', _('Spanish')),
    ('el', _('Greek')),
]

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Debug-Toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

