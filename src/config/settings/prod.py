import os

from config.settings.base import *  # NOQA

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = ["localhost", "ec2-54-221-5-210.compute-1.amazonaws.com"]

DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.postgresql",
    #     "NAME": os.environ.get("POSTGRES_DB"),
    #     "USER": os.environ.get("POSTGRES_USER"),
    #     "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
    #     "HOST": os.environ.get("POSTGRES_HOST"),
    #     "PORT": os.environ.get("POSTGRES_PORT"),
    # },
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # NOQA
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"  # NOQA

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"  # NOQA
