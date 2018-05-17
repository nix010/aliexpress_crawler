
from project.settings.base import *

DEBUG = False


DATABASES = {
    'default': {
        'ENGINE'    : 'django.db.backends.postgresql',
        'NAME'      : 'aliexpress',
        'USER'      : 'postgres',
        'PASSWORD'  : '123456',
        'HOST'      : 'localhost',
        'PORT'      : '5432',
    }
}

