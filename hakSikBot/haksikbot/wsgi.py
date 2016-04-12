#!/root/.pyenv/versions/py3.4.1/bin/python3.4

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "haksikbot.settings")

application = get_wsgi_application()
