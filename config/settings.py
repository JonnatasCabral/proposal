"""
Django settings for config project.
Generated by 'django-admin startproject' using Django 1.11.4.
For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
from __future__ import absolute_import
from environ import Path, Env
import os

#####################################
# LOCAL VARS
#####################################

ROOT_DIR = Path(__file__) - 2
APPS_DIR = ROOT_DIR.path('apps')
environ = Env()


#####################################
# SECURITY SETTINGS
#####################################

SECRET_KEY = environ('DJANGO_SECRET_KEY', default='CHANGEME!!!')

DEBUG = environ.bool('DJANGO_DEBUG', False)

ALLOWED_HOSTS = environ.list(
    'DJANGO_ALLOWED_HOSTS',
    default=['www.yourdomain.com'])


#####################################
# INSTALLED APPS
#####################################

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'gunicorn',
    'rest_framework',
    'rest_framework.authtoken',
]

LOCAL_APPS = []

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

#####################################
# APPLICATION SETTINGS
#####################################

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(ROOT_DIR.path('templates'))],
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

WSGI_APPLICATION = 'config.wsgi.application'


#####################################
# DATABASE SETTINGS
#####################################

DATABASES = {
    'default': environ.db(
        'DATABASE_URL',
        default='postgres:///postgres'),
}


DATABASES['default']['ATOMIC_REQUESTS'] = False


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


#####################################
# INTERNATIONALIZATION SETTINGS
#####################################

TIME_ZONE = 'America/Recife'

LANGUAGE_CODE = 'pt-BR'

USE_I18N = True

USE_L10N = True

DATE_FORMAT = 'd/m/Y'

DATETIME_FORMAT = 'd-m-Y H:i:S'

DECIMAL_SEPARATOR = ','

THOUSAND_SEPARATOR = '.'


#####################################
# STATIC AND MEDIA SETTINGS
#####################################

MEDIA_ROOT = str(ROOT_DIR('media'))

MEDIA_URL = '/media/'

STATIC_ROOT = str(ROOT_DIR('staticfiles'))

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    str(ROOT_DIR.path('static')),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

ADMIN_URL = environ('DJANGO_ADMIN_URL', default='/admin')


POSTGRES_USER = environ('POSTGRES_USER', default='')
POSTGRES_PASSWORD = environ('POSTGRES_PASSWORD', default='')
POSTGRES_HOST = environ('POSTGRES_HOST', default='')
POSTGRES_DB = environ('POSTGRES_DB', default='')
POSTGRES_PORT = environ('POSTGRES_PORT', default='')



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DATETIME_FORMAT': "%m/%d/%Y %H:%M",
}