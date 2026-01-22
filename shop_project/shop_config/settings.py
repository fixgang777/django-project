import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ВАЖНО: На Render ключ будет браться из переменных окружения, которые мы заполняли
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-j5yvc)a7q5)0#$^up25jjwnpuu#_h1k&_s#b#bmcbi5!m7sr0h')

# На сервере DEBUG должен быть False, но для теста оставим True.
# Если сайт заработает, поменяй на False.
DEBUG = True

# Добавляем адрес твоего сайта на Render
ALLOWED_HOSTS = ['my-shop-project.onrender.com', '127.0.0.1', 'localhost']

ENABLE_REVIEWS = True
ENABLE_PROMOTIONS = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'core',
]

if ENABLE_REVIEWS:
    INSTALLED_APPS.append('reviews')
if ENABLE_PROMOTIONS:
    INSTALLED_APPS.append('promotions')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Добавили для работы CSS/картинок
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shop_config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'shop_config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Настройки статики
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # Папка, куда соберутся файлы для Render
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'