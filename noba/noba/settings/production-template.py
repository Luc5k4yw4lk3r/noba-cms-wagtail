import os
from .base import *

DEBUG = False
SECRET_KEY = 'q@vsdasdasd~@#@#SDSDASD'
ALLOWED_HOSTS = ['localhost', '*']
cwd = os.getcwd()
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": f"{cwd}/.cache"
    }
}

DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.postgresql_psycopg2',
        "NAME": 'db',
        "USER": 'usr_db',
        "PASSWORD": '1232143423',
        "HOST": 'localhost',
        "PORT": '',
    }
}
