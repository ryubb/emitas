from config.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

WSGI_APPLICATION = 'mysite.wsgi.develop.application'

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'circle_test',
        'USER': 'root',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}
