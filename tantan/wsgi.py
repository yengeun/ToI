<<<<<<< HEAD:tantan/wsgi.py
"""
WSGI config for tantan project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tantan.settings")

application = get_wsgi_application()
=======
"""
WSGI config for tantan project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tantan.settings")

application = get_wsgi_application()
>>>>>>> 6a10e3d4e4d66cc32dbd8dfe7a2d2be912220cca:tantan/tantan/wsgi.py
