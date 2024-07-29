from .base import *

DEBUG = False

ADMINS = (
 ('Antonio M', 'email@mydomain.com'),
)
ALLOWED_HOSTS = ['127.0.0.1:8000','educaproject.com', 'www.educaproject.com']

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'educa',
       'USER': 'educa',
       'PASSWORD': 'admin',
   }
}

# # SSL config
# SECURE_SSL_REDIRECT = True
# CSRF_COOKIE_SECURE = True