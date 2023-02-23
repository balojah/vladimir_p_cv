import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_cv.settings')
app = Celery('my_cv')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
