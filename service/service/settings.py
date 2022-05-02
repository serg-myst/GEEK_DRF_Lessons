"""
Django settings for service project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'blh!qzf_k6+luy9o+g#gvgk1yyj*hyjmh3_pvezs7y20%%%d%c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # На django 4.0 Будет ошибка при старте сервере
    # Лекарство: https://stackoverflow.com/questions/70382084/import-error-force-text-from-django-utils-encoding
    # 'graphene_django',  # Lesson_10 Требуется установить pip install graphene-django

    'rest_framework',  # Lesson_1 подключаем установленное приложение Django-REST
    'authapp',  # Lesson_1 подключаем новое приложение (django-admin startapp authapp)

    'corsheaders',  # Lesson_2 Обязательно, иначе бэк и фронт работать не будут

    'todonotes',  # Lesson_3 Новое приложение

    'django_filters',  # Lesson_4 Обязательно для использования библиотеки pip install django-filter

    'rest_framework.authtoken',
    # Lesson_6 Авторизация по токену. После подключения выполнить миграции. python manage.py migrate
    # Теперь у нас будет модель для хранения токена и таблица с соответствием пользователя (User) и его
    # токена (Token).
    # Таблица authtoken_token. Поля key, created, user_id

    'rest_framework_simplejwt',  # Lesson_6

    'drf_yasg',  # Lesson_9

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Lesson_2 Обязательно, иначе бэк и фронт работать не будут
    'django.middleware.common.CommonMiddleware',  # Lesson_2 Обязательно, иначе бэк и фронт работать не будут
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'service.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'service.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': BASE_DIR / 'db.sqlite3',
    # }

    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'service',
        'USER': 'serg',
        'PASSWORD': 'serg123456',
        'HOST': 'db',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

AUTH_USER_MODEL = 'authapp.TodoUser'

# Lesson_2 Обязательно, иначе бэк и фронт работать не будут
# CORS_ALLOWED_ORIGINS = [
#    'http://localhost:3000',
#    'http://127.0.0.1:3000',
# ]

# Lesson_12 Переводим на реальный сервер
# CORS_ALLOWED_ALL_ORIGINS = True
# CORS_ALLOWED_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    'http://5.63.159.42:8000',
    'http://5.63.159.42:8080',
    'http://5.63.159.42:80',
]

# Lesson_3
# Для CamelCase https://github.com/vbabiy/djangorestframework-camel-case

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',  # Выводим на страницу чистый JSON (ну в понятиях python словарь)
        'rest_framework.renderers.BrowsableAPIRenderer',  # Lesson_3 Это интерфейс API. Перекрывает верхнюю строку
        # 'rest_framework.renderers.StaticHTMLIRenderer',  # Lesson_3 Это какая-то дичь. Надо разбираться
        # 'rest_framework.renderers.AdminRenderer',  # Lesson_3 Это админский интерфейс

        # Lesson_3
        # 'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        # 'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer',
    ],

    # Lesson_4 Подключаем пагинацию и фильтры
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,

    # Lesson_6
    # IsAuthenticated - только для авторизованных пользователей.
    # Иначе ошибка: {"detail":"Authentication credentials were not provided."}
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        # 'rest_framework.permissions.IsAuthenticated',
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',

        # 'rest_framework_simplejwt.authentication.JWTAuthentication',  # Lesson_6 JWT аутентификация

    ],

    # ,
    # 'DEFAULT_PARSER_CLASSES': [
    #    # If you use MultiPartFormParser or FormParser, we also have a camel case version
    #    'djangorestframework_camel_case.parser.CamelCaseFormParser',
    #    'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
    #    'djangorestframework_camel_case.parser.CamelCaseJSONParser',
    #    # Any other parsers
    #

    # Lesson_9
    # 'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',  # Указание версии в части URL-адреса
    # 'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',  # NamespaceVersioning

    # Указание версии в параметре URL-адреса
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.QueryParameterVersioning',

    # Указание версии в заголовках. Этот способ считается оптимальным
    # 'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.AcceptHeaderVersioning',
}

# Lesson_10 путь до объекта с описанием схемы. В нашем случае мы создадим файл schema.py в папке с настройками проекта
# GRAPHENE = {
#    'SCHEMA': 'service.schema.schema'
# }
