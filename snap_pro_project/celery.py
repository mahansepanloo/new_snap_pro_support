import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'snap_pro_project.settings')

app = Celery('snap_pro_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()