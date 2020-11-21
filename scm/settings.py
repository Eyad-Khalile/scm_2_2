"""
Django settings for scm project.

Generated by 'django-admin startproject' using Django 2.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

from django.conf import global_settings
import django.conf.locale
from django.conf.locale import LANG_INFO
import os
from django.utils.translation import gettext_lazy as _
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/aff

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l=2j+l)(khert5i(rrgqqst66gr5y&8t3byb&zj+16)(8bg^cd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = int(os.environ.get('DEBUG', default=1))

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'orgs',
    'crispy_forms',
    'django_countries',
    'phonenumber_filter',
    'django_filters',
    #  'django_social_share',
    'ckeditor',
    'django_template_maths',

]

# CKEDITOR_UPLOAD_PATH = 'uploads/'
# CKEDITOR_JQUERY_URL = '/static/js/jquery-2.1.1.min.js'
# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': 'Full',
#         'height': 400,
#         'width': 900,
#         'removePlugins': 'stylesheetparser',
#         'extraPlugins': 'codesnippet',
#     },
# }

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'scm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'scm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'djangodatabase',
    #     'USER': 'dbadmin',
    #     'PASSWORD': '12345',
    #     'HOST': 'localhost',
    #     'PORT': '3306',
    # }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

# if 'ku' not in LANG_INFO:
#     LANG_INFO['ku'] = {
#         'bidi': False,
#         'code': 'ku',
#         'name': 'Kurdish',
#         'name_local': 'Kurdi',
#     }


# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ar'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]


LANGUAGES = [
    ('ar', _('عربي')),
    ('en', _('English')),
    # ('km', _('Kurdish')),
    ('ku', _('Kurdî')),
]

EXTRA_LANG_INFO = {
    'ku': {
        'bidi': False,
        'code': 'ku',
        'name': 'Kurdish',
        'name_local': 'Kurdî‎',
    },
}
LANG_INFO = dict(django.conf.locale.LANG_INFO, **EXTRA_LANG_INFO)
django.conf.locale.LANG_INFO = LANG_INFO
global_settings.LANGUAGES = global_settings.LANGUAGES + [("ku", 'Kurdi')]


CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'profile'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_ROOT = (os.path.join(BASE_DIR, 'staticfiles/'))
STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'staticfiles/')
# ]

MEDIA_ROOT = (os.path.join(BASE_DIR, 'media'))
MEDIA_URL = '/media/'


# EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'khalile.eyad@gmail.com'
EMAIL_HOST_PASSWORD = 'Eyad1979@'


# KEROKU
django_heroku.settings(locals())
