from config.settings.base import *  # NOQA

SECRET_KEY = "django-secret-key"

DEBUG = True

INSTALLED_APPS += [  # NOQA
    "django_extensions",
]

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # NOQA
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = (BASE_DIR / "static",)  # NOQA

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"  # NOQA
