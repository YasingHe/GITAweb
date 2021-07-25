"""
Django settings for gita project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lr7tctk(xe@j^ipzy3-hq&9s!guscemi$&7l&cq_1w7c%8vf$j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # 我的app
    'main',

    # 第三方app
    'simpleui',
    'ckeditor',
    'ckeditor_uploader',

    # 自带app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gita.urls'

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

WSGI_APPLICATION = 'gita.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.join(BASE_DIR, '/static/'))

STATICFILES_DIRS = (
    os.path.join(os.path.join(BASE_DIR, 'static')),
)

MEDIA_URL = '/media/'
# 放在django项目根目录，同时也需要创建media文件夹
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CKEDITOR_UPLOAD_PATH = 'upload/'
# ckeditor
CKEDITOR_CONFIGS = {
    # 配置名是default时，django-ckeditor默认使用这个配置
    'default': {
        # 使用简体中文
        'language': 'zh-cn',
        # 编辑器的宽高请根据你的页面自行设置
        # 'width': '730px',
        'height': '350px',
        'image_previewText': ' ',
        # 'tabSpaces': 4,
        # 'toolbar': 'full',  # 完整工具条
        'toolbar': 'full',  # 常用工具条
        # 添加按钮在这里
        # 'toolbar_Custom': [
        #     ['Bold', 'Italic', 'Underline', 'Format', 'RemoveFormat'],
        #     ['NumberedList', 'BulletedList'],
        #     ['Blockquote', 'CodeSnippet'],
        #     ['Image', 'Link', 'Unlink'],
        #     ['Maximize']
        # ],
        # 插件
        'extraPlugins': ','.join(['codesnippet', 'uploadimage', 'widget', 'lineutils', ]),
    }
}


SIMPLEUI_LOGO = '/static/img/i.png'
SIMPLEUI_HOME_INFO = True