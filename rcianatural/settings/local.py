from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$4-5#3mt(57ic8-q$=d3x42wud&!lrg7k=#u1jkn556cqjp(sp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# PARA QUE FUNCIONE EN RENDER
ALLOWED_HOSTS = [
    'resistencianatural.onrender.com', 
    'localhost', 
    '127.0.0.1'
]

CSRF_TRUSTED_ORIGINS = [
    "https://resistencianatural.onrender.com",
]

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
