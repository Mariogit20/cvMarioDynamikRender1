"""
WSGI config for portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

# Add your project directory to the sys.path
# Replace '/path/to/your/project' with your actual path
sys.path.insert(0, os.path.dirname(__file__))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

