from .base import *

DEBUG = True

ALLOWED_HOSTS = ['educaproject.com', 'www.educaproject.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_ROOT = BASE_DIR / 'staticfiles'

# Uncomment if using HTTPS
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
