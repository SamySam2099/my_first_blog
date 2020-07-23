"""
WSGI config for my_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
