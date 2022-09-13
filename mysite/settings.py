"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import mysql.connector
import json 
import pymysql
from datetime import date, datetime

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# 数据库部分
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

def get_information(sql):
    mydb = mysql.connector.connect(
     host="xue.kaikeba.com",       # 数据库主机地址
     user="lys",    # 数据库用户名
     passwd="wLQ2uFbMiZEeh7qS",   # 数据库密码
     database="suanke"
    )
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    fields = mycursor.description
    result = mycursor.fetchall()
    column_list=[]
    for i in fields:
        column_list.append(i[0])
    for row in result:
        data = {}
        for i in range(len(column_list)):
            data[column_list[i]] = row[i]
        jsondata = json.dumps(data, cls=ComplexEncoder, ensure_ascii=False)
    return jsondata

def get_event():
    sql = "select * from suanke_choice_questions where id < 10"
    return get_information(sql)

def get_event_type():
    sql = "select * from suanke_choice_question_user_answer_data"
    return get_information(sql)


#print(get_event())
#print(get_event_type())


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y^wjje+euq=4beor2dhb%x1$(76(k6oey)b0u&ox5nd0e@k3iu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['121.40.138.226']


# Application definition

INSTALLED_APPS = [
    'simpleui', # 注意这里
    'polls.apps.PollsConfig',
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
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': BASE_DIR / 'db.sqlite3',
    #}
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'database',
    'USER': 'root',
    'PASSWORD': 'root',
    'HOST': '121.40.138.226',
    'PORT': '3306',
    },
    'database1': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'database2',
    'USER': 'root',
    'PASSWORD': 'root',
    'HOST': '121.40.138.226',
    'PORT': '3306',
    },
    'database2': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'suanke',
    'USER': 'lys',
    'PASSWORD': 'wLQ2uFbMiZEeh7qS',
    'HOST': 'xue.kaikeba.com',
    'PORT': '3306',
    }

}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#隐藏广告连接
SIMPLEUI_HOME_INFO = False 
SIMPLEUI_ANALYSIS = False 

#SIMPLEUI_LOGO = ''

# 设置默认主题，指向主题css文件名。Admin Lte风格
# SIMPLEUI_DEFAULT_THEME = 'admin.lte.css'
 
# 设置默认主题，指向主题css文件名。Element-ui风格
# SIMPLEUI_DEFAULT_THEME = 'element.css'
 
# 设置默认主题，指向主题css文件名。layui风格
#SIMPLEUI_DEFAULT_THEME = 'layui.css'
 
# 设置默认主题，指向主题css文件名。紫色风格
#SIMPLEUI_DEFAULT_THEME = 'purple.css'
#SIMPLEUI_LOGO = 'http://p.qpic.cn/qqcourse/QFzQYCgCrxlaicQ0RApYfR2zYdlvicqaO4wq1YA4Y7eib7wib9zTK6B2bTEKr15RxEPr/'
SIMPLEUI_LOGO = 'https://img.kaikeba.com/a/90841172501202nbao.png'

#SIMPLEUI_HOME_PAGE = 'polls/dashboard/'
SIMPLEUI_HOME_TITLE = '控制面板!' 
#SIMPLEUI_HOME_ICON = 'fa fa-eye'


DATABASE_ROUTERS = ['mysite.DatabaseAppsRouter.DatabaseAppsRouter'] 
 
DATABASE_APPS_MAPPING = {
# example:
# 'app_name':'database_name',
    'admin': 'default',
    'polls': 'database1',
    #'polls': 'database2',
}