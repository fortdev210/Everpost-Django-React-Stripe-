import os
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
from config.environment import SETTINGS_MODULE

os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS_MODULE)
application = get_wsgi_application()
application = DjangoWhiteNoise(application)