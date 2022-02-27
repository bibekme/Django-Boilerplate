import mimetypes
from .common import *

# Django debug toolbar settings
mimetypes.add_type("application/javascript", ".js", True)

DEBUG = True

SECRET_KEY = "django-insecure-hs6j037urx6iav+7#10%-vu4l4f5@@-1_zo)oft4g7$vf2$jmp"


CELERY_BROKER_URL = "redis://redis:6379/0"
REDIS_URL = "redis://redis:6379/1"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "projectname",
        "USER": "postgres",
        "PASSWORD": "password",
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": "5432",
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "TIMEOUT": 10 * 60,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

EMAIL_HOST = "mailhog"
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_PORT = 1025

DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda request: True}

INTERNAL_IPS = [
    "127.0.0.1",
]
