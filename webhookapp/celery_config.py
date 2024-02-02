import os

# celery config file
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webhookapp.settings')

app = Celery('webhookapp')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()