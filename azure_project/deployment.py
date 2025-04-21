import os 
from .settings import *
from .settings import BASE_DIR


SECRET_KEY = 'django-insecure-2#p9z0-d=39&qbu#&f1p6m=2+j!a4_n_r9q%wz192hfwva&24^'
ALLOWED_HOSTS = "https://my-django-app-69ad5c.scm.azurewebsites.net/"
CSRF_TRUSTED_ORIGINS = "https://my-django-app-69ad5c.scm.azurewebsites.net/detectors"
DEBUG = False

# WhiteNoise configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
] 

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}