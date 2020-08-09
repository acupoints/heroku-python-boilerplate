# from .base import * #NOQA
from ..settings_original import *

# Modify settings in production mode
# SECURE_SSL_REDIRECT = True

# import django_heroku
# django_heroku.settings(locals())

django_heroku.settings(locals())
