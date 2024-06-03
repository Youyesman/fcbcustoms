"""
WSGI config for fcbcustoms project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os,sys

sys.path.append('/home/fcbcustoms')
sys.path.append('/home/fcbcustoms/venv/lib/python3.10/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fcbcustoms.settings')

application = get_wsgi_application()
