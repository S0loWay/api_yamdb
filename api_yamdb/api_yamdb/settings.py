from pathlib import Path

from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'p&l%385148kslhtyn^##a1)ilz@4zqj=rq&agdol^##zgl9(vs'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'djoser',
    'api.apps.ApiConfig',
    'reviews.apps.ReviewsConfig',
]

AUTH_USER_MODEL = 'reviews.CustomUser'

DJOSER = {
    'SERIALIZERS': {
        'user_create': 'api.serializers.CustomUserCreateSerializer',  # Кастомный сериализатор для обычного пользователя
        'user_create_admin': 'api.serializers.CustomUserCreateAdminSerializer',  # Кастомный сериализатор для администратора
    }
}

SITE_NAME = 'YaMDB'
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = BASE_DIR / 'sent_emails'

EMAIL_HOST = 'smtp.gmail.com'  # SMTP сервер
EMAIL_PORT = 587  # Порт SMTP сервера
EMAIL_USE_TLS = True  # Использовать TLS для защиты соединения
EMAIL_HOST_USER = 'test-YaMDB@yandex.ru'  # Логин для SMTP сервера
EMAIL_HOST_PASSWORD = 'qweqweqwe123321123'  # Пароль для SMTP сервера

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.UserRateThrottle',
        'rest_framework.throttling.AnonRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'user': '10000/day',
        'anon': '1000/day',
        'user_minute': '60/min',
        'anon_minute': '10/min',
    },
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=100),
    'AUTH_HEADER_TYPES': ('Bearer',),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api_yamdb.urls'

TEMPLATES_DIR = BASE_DIR / 'templates'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'api_yamdb.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = False

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = ((BASE_DIR / 'static/'),)
