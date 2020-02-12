"""
WSGI config for blog_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os, sys, site

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
WORK_DIRECTORY = os.path.join(CURRENT_DIRECTORY, '..')

# Add the site-packages
site.addsitedir('/var/www/html/venv/lib/python3.6/site-packages')

# Add the project to the python path
sys.path.append(WORK_DIRECTORY)

# Add the parent directory to the python path
sys.path.append(os.path.join(WORK_DIRECTORY, '..'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
