from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'keyword-django',
        'USER': 'postgres',
        'PASSWORD': 'medi180615',
        'HOST': 'keyword-django.cwxq9xvnodtq.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    },
    'read1': {
        'NAME': 'hospital_keyword',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'admin',
        'PASSWORD': 'medi180615',
        'HOST': 'eszett-hospital-info-readonly1.cwxq9xvnodtq.ap-northeast-2.rds.amazonaws.com',
        'PORT': '3306',
    },
    'read2': {
        'NAME': 'hospital_keyword',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'admin',
        'PASSWORD': 'medi180615',
        'HOST': 'eszett-hospital-info-readonly2.cwxq9xvnodtq.ap-northeast-2.rds.amazonaws.com',
        'PORT': '3306',
    }
}

DATABASES_ROUTERS = ['config.master_slave_router.MasterSlaveRouter']


ALLOWED_HOSTS = []
