"""
WSGI config for djangoRestApis project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import django
from django.core.wsgi import get_wsgi_application

django.setup()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoRestApis.settings')

application = get_wsgi_application()