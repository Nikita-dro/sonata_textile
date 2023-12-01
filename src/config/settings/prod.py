from config.settings.base_settings import *  # NOQA

SECRET_KEY = "django-insecure-uxe#&&$9t7&x%xq*9ur)+b9a08t0pygm6*523v%+2j#ft2yq1m"

DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # NOQA
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
