"""
WSGI config for django_server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_server.settings')
django_server_profile = os.environ.get('DJANGO_SERVER_PROFILE', 'development')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_server.settings.{}'.format(django_server_profile))

application = get_wsgi_application()
