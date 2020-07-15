from .base import *

ALLOWED_HOSTS = ['15.164.255.161','gglabs.kr']
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = []
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gglabsdb',
        'USER': 'gglabsdb',
        'PASSWORD': 'Dthinker21B!',
        'HOST': 'pg1101.gabiadb.com',
        'PORT': '5432',
    }
}