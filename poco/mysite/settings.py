"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@21e!kx-)0-c(dago2o99euah8yppxs(a-ci=m(*yor!@5wn$5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ["poco.pythonanywhere.com",'localhost', '127.0.0.1']
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'main.apps.MainConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites'
    #'social.apps.django_app.default',
    #'oauth2_provider',
    #'corsheaders',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                #'social.apps.django_app.context_processors.backends',
                #'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

LOGIN_REDIRECT_URL = 'main/login.html'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
SITE_ID=1

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTHENTICATION_BACKENDS = (
    'main.backends.GoogleAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
)

CLIENT_ID = ''

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

# The manual mentions that this should be set to True for the server to
# take the TIME_ZONE into consideration.
# However, when that is done, the database timestamps were set according to UTS
# For some reason of the other, setting this to False works fine.
# May be the server time is equal to the TIME_ZONE specified and that is why
# this is working.
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

#STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

CODEMIRROR_PATH = "/static/codemirror"

# STATIC_ROOT = '/home/poco/waggle-classroom/main/static/'
# STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "main", "static")
STATIC_URL = '/static/'


# MEDIA_ROOT='/home/poco/waggle-classroom/main/media/'
# MEDIA_URL='/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "main", "media")
MEDIA_URL = '/media/'


#Email
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'abc@gmail.com'
EMAIL_HOST_PASSWORD = 'abcd'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
