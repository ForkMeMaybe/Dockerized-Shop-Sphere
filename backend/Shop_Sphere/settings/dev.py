from .common import *
import os

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]


CELERY_BROKER_URL = "redis://redis:6379/1"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

DEBUG = True

DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda request: True}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "shop_sphere",
        "USER": "odd",
        "PASSWORD": "MyPassword",
        "HOST": "postgres",
    }
}


DEFAULT_FROM_EMAIL = "YOUR_EMAIL"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "YOUR_EMAIL_HOST_USER"
EMAIL_HOST_PASSWORD = "YOUR_EMAIL_HOST_PASSWORD"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

RAZOR_KEY_ID = "YOUR_RAZOR_KEY_ID"
RAZOR_KEY_SECRET = "YOUR_RAZOR_KEY_SECRET"

if DEBUG:
    INTERNAL_IPS = ["127.0.0.1"]

SECRET_KEY = "django-insecure-#cfv0anz362tub&z7&cs3by87pa1l@7d%@3@bylt23!-+89wfn"
