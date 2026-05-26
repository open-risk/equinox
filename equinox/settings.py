# Copyright (c) 2020 - 2026 Open Risk (https://www.openriskmanagement.com)
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
import sys
from pathlib import Path
from django.db.backends.signals import connection_created
from django.utils.translation import gettext_lazy as _
from equinox.jazzmin_settings import *


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = '3i=clc#nog3a2v__q9n89wak2#p54mfs(*-x)oj7+1)igkmylf'
DEBUG = True

ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1']


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
    'import_export',
    'rest_framework',
    'drf_yasg',
    'treebeard',
    'django.contrib.gis',
    'markdownfield',
    'leaflet',
    'location_field.apps.DefaultConfig',
    'django_countries',
    'start',
    'reference',
    'portfolio',
    'policy',
    'risk',
    'reporting',
    'provenance',
    'debug_toolbar',
    'behave_django'
]

MIDDLEWARE = [
    'csp.middleware.CSPMiddleware',
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

CSP_DEFAULT_SRC = ("'self'",)
ROOT_URLCONF = 'equinox.urls'
SITE_ID = 1
# SITE_URL = "http://127.0.0.1:8080/"
SITE_URL = "http://localhost:8080/"

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

LOCATION_FIELD = {
    'map.provider': 'openstreetmap',
    'search.provider': 'nominatim',
}

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

USE_TZ = True
# TIME_ZONE = 'UTC'
TIME_ZONE = 'Europe/Amsterdam'
USE_I18N = True
USE_L10N = True

# Debug-Toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda r: False,
}


# Applying this spatialite workaround during tests
if 'test' in sys.argv or any('pytest' in arg for arg in sys.argv):
    def fix_spatialite_trigger(sender, connection, **kwargs):
        if connection.vendor == 'sqlite':
            with connection.cursor() as cursor:
                # Pre-initialize metadata to prevent Django from running the full version
                try:
                    cursor.execute("SELECT InitSpatialMetaData(1);")
                except Exception:
                    pass

    connection_created.connect(fix_spatialite_trigger)
