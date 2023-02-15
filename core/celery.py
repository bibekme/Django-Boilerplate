import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    "periodic_run_task": {
        "task": "core.tasks.run_task",
        "schedule": crontab(minute=1),
    },
}

app.autodiscover_tasks()
