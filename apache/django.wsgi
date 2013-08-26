import os
import sys
import olac

os.environ['PYTHON_EGG_CACHE'] = olac.olacvar('python/egg_cache/wsgi')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

sys.path.append('/olac/language-commons')
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

