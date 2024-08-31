from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'investsphere_api.settings.prod')

app = Celery('investsphere_api')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'test_task': {
        'task': 'app_users.tasks.test_task',
        'schedule': crontab(minute='*/5'),   
        'args': (), 
    },
}