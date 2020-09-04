"""
Django settings for pur_beurre project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE_DIR :: {}".format(BASE_DIR))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^+%82556f9ka=e3q!z67#fxr1br1y*ds80)@+7=&u^*nr*hb@('
if 'SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ['SECRET_KEY']
print('secret key :{}'.format(len(SECRET_KEY)))

ALLOWED_HOSTS = []
# SECURITY WARNING: don't run with debug turned on in production!
if 'DEPLOY_ENVIRON' in os.environ and os.environ['DEPLOY_ENVIRON'] == 'PRODUCTION':
    if 'FORCE_DEBUG' in os.environ and os.environ['FORCE_DEBUG'] == 'YES':
        DEBUG = True
    else:
        DEBUG = False
    ALLOWED_HOSTS = ['yapb.herokuapp.com']
else:
    if 'FORCE_DEBUG' in os.environ and os.environ['FORCE_DEBUG'] == 'NO':
        DEBUG = False
        ALLOWED_HOSTS = ['127.0.0.1']
    else:
        DEBUG = True
        ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'product.apps.ProductConfig',
    'user.apps.UserConfig',
    'substitute.apps.SubstituteConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'pur_beurre.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'pur_beurre.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pur_beurre',
        'USER': 'pur_beurre',
        'PASSWORD':  'pur_beurre',
        'HOST': '127.0.0.1',
        'PORT': 5432,
    }


}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True

INTERNAL_IPS =['127.0.0.1']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

if 'DEPLOY_ENVIRON' in os.environ and os.environ['DEPLOY_ENVIRON'] == 'PRODUCTION':
    STATIC_ROOT = os.path.join(BASE_DIR, 'dumps')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(db_from_env)
    
# awesome_website/settings.py
LOGIN_REDIRECT_URL = "dashboard"
# LOGIN_REDIRECT_URL = "dashboard_section"
