import os
from .base import *

DEBUG = False
SECRET_KEY = 'q@v$$%!_4$@gn42(ifo17kdgxvusgz0s42i3!c)^j!0(+4_=52'
ALLOWED_HOSTS = ['localhost', 'noba.wheteit.is.goingtolive', '134.122.78.176']
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
        "NAME": 'nobadb',
        "USER": 'noba_usr_db',
        "PASSWORD": '8py1lEQxY+vU^7',
        "HOST": 'localhost',
        "PORT": '',
    }
}

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://2584eb980d764b3ba6121438ab12a7ce@o1144710.ingest.sentry.io/6208959",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

try:
    from .local import *
except ImportError:
    pass
