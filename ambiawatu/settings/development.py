from .default import *

ALLOWED_HOSTS = [
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'steemit',
        'HOST': 'localhost',
        'USER': 'steemit',
        'PASSWORD': 'steemit',
    }
}
DEBUG = True

try:
    from .local_settings import *
except ImportError:
    pass