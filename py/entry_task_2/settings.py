"""
Django settings for helloword project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ROOT_PATH = os.path.realpath(os.path.dirname(__file__))
LOG_DIR = os.path.join(ROOT_PATH, 'log')

# country id
COUNTRY = os.getenv('cid', "id").upper()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@^9om2m^-z$i)1+b1emn(_ijy4@32ew(m4$t3v+dyf8vfm3-ca'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'djcelery',
	'task',
	'model',
	'view',
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'middleware.params_parse.ParamsParse',
	'middleware.authentication.Authentication',
	# 'middleware.response_wrapper.ResponseWrapper',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'startup.wsgi.application'

LOGGER_CONFIG = {
	'log_dir': LOG_DIR,
}
LOG_REGION = 'SG'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'entry_task_db',
		'USER': 'root',
		'PASSWORD': 'Asdf123!@#',
		'HOST': 'localhost',
		'PORT': '3306',
	}
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
	os.path.join(ROOT_PATH, 'static')
]

import djcelery

djcelery.setup_loader()
BROKER_URL = 'redis://localhost:6379/1'
CELERY_CONCURRENCY = 2
CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'
