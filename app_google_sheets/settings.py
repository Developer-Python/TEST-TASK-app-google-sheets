# Модули для работы с [Системой и временем]
import os, sys, time

# Каталог \app_google_sheets\
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Каталог \app_google_sheets\token.json
CREDENTIALS_FILE = os.path.join(BASE_DIR, 'token.json')

# Изменнёная директория для пойска приложений
PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))

# Использовать режим отладки ?
DEBUG = True

# Защита подписанных данных
SECRET_KEY = '12345test'

# Разрешённые хосты для которых может работать текущий сайт
ALLOWED_HOSTS = ['*']

# Список установленных приложений
INSTALLED_APPS = [

    # Стандартные приложения
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Мой приложения
    'main.apps.MainConfig',

]

# Промежуточный слой
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Главная конфигурация ссылок
ROOT_URLCONF = 'app_google_sheets.urls'

# Шаблоны
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # Использование шаблонов из папки [templates]
        'DIRS': [os.path.join(PROJECT_ROOT, 'templates')],

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

# Выступает в роли простого сервера [WSGI]
WSGI_APPLICATION = 'app_google_sheets.wsgi.application'

# База данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Используем движок "PostgreSql"
        'NAME': 'sheets',                                    # Используем БД под названием "sheets"
        'USER': 'admin',                                     # Используем пользователя с доступом к БД "admin"
        'PASSWORD': 'admin',                                 # Пароль от пользователя "admin"
        'HOST': 'localhost',                                 # HOST подключения
        'PORT': '',                                          # PORT подключения
    }
}

# Управления пользовательскими паролями.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Язык
LANGUAGE_CODE = 'ru'

# Часовой пояс
TIME_ZONE = 'UTC'

# Использовать механизм перевода [Django] ?
USE_I18N = True

# Использовать локализованный формат даты ?
USE_L10N = False

# Использовать часовой пояс ?
USE_TZ = True

# Настройка статических файлов
STATIC_URL = '/static/'
STATIC_DIR = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# Настройка динамичных файлов
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
