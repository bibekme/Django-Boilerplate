import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "periodic_run_task": {
        "task": "core.tasks.run_task",
        "schedule": 10.0,
    },
}

app.conf.timezone = "UTC"
