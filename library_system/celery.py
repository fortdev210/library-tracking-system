import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_system.settings')

app = Celery('library_system')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
# Celery Beat: Periodic Task Scheduler
app.conf.beat_scheduler = 'django_celery_beat.schedulers:DatabaseScheduler'