from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-=ew%38r8vx%k(f0@m92m59xaz%7m1)b=*&6f$shm%)@y(5j3c)'

DEBUG = True  # Cambiar a False cuando subas a producción

ALLOWED_HOSTS = ["*"]  # Render/Railway lo necesitan para funcionar


# =============================
#       APPS INSTALADAS
# =============================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'appReinas',
]


# =============================
#       MIDDLEWARE
# =============================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',   # <-- IMPORTANTE
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'Reinasdelcaribe.urls'


# =============================
#       TEMPLATES
# =============================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / "templates" ],  # opcional si usas carpeta global
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Reinasdelcaribe.wsgi.application'


# =============================
#       BASE DE DATOS
# =============================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Si usas Render con PostgreSQL, aquí lo cambiamos
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =============================
#       PASSWORDS
# =============================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# =============================
#       IDIOMA Y HORA
# =============================
LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'America/Santo_Domingo'

USE_I18N = True
USE_TZ = True


# =============================
#       ARCHIVOS ESTÁTICOS
# =============================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"   # <-- NECESARIO PARA RENDER
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# =============================
#       MEDIA (Fotos de jugadoras, tienda, etc.)
# =============================
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# =============================
#       PRIMARY KEY
# =============================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
