"""
Django settings for netflix_site project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = (
    "django-insecure-4nbwghw!)m-#27t(p875*2imt0$^dlx4vhitab_$%^g37)n*i7"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]  # * allows the application to be hosted on any domain.


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core",
    "gunicorn",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "netflix_site.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # Tells Django where to find templates
        "DIRS": [os.path.join(BASE_DIR, "/netflix_site/core/templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "netflix_site.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

# Postgresql Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "Netflix",
        "USER": "postgres",
        "PASSWORD": "Imelaezemoh7!",
        "HOST": "localhost",
        "PORT": "5432",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# URL to use when referring to static files located in STATICFILES_DIRS.
STATIC_URL = "static/"

# Additional locations the staticfiles app will traverse.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Shows where the movies will be uploaded to
MEDIA_URL = "media/"

# MEDIA_ROOT is the directory where uploaded media files are stored.
# Media files include user-uploaded content like profile pictures, document uploads, etc.
# The path is set to a 'media' directory within the project's base directory.
# Example: If BASE_DIR is "/home/user/myproject", MEDIA_ROOT will be "/home/user/myproject/media".
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# STATIC_ROOT is the directory where static files are collected to when running the 'collectstatic' management command.
# Static files include JavaScript, CSS, images, and other files used to render the website.
# The path is set to a 'staticfiles' directory within the project's base directory.
# Example: If BASE_DIR is "/home/user/myproject", STATIC_ROOT will be "/home/user/myproject/staticfiles".
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CSRF_TRUSTED_ORIGINS is a list of trusted origins (domains) that are allowed to make
# Cross-Site Request Forgery (CSRF) protected requests to this Django application.
# This setting is particularly useful when you have your Django app hosted on multiple
# domains or when making cross-origin requests from trusted domains.
# Example: ['https://example.com', 'https://api.example.com']
CSRF_TRUSTED_ORIGINS = []

# CSRF_COOKIE_SECURE ensures that the CSRF cookie is only sent over HTTPS connections.
# This setting should be enabled (set to True) in production environments to enhance security.
# It helps prevent the CSRF token from being transmitted over unencrypted connections, reducing the risk of interception.
CSRF_COOKIE_SECURE = True

# SESSION_COOKIE_SECURE ensures that the session cookie is only sent over HTTPS connections.
# This setting should be enabled (set to True) in production environments to enhance security.
# It helps prevent session cookies from being transmitted over unencrypted connections, reducing the risk of session hijacking.
SESSION_COOKIE_SECURE = True

# SECURE_PROXY_SSL_HEADER is used when the Django application is behind a proxy (like a load balancer) that handles SSL termination.
# This setting indicates which header the proxy uses to indicate that the request was originally made over HTTPS.
# In this case, the proxy sets the "X-Forwarded-Proto" header to "https" when the request is secure.
# This allows Django to properly detect secure requests and apply appropriate security measures.
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
