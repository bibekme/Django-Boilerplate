from celery import shared_task


@shared_task
def run_task():
    print("Scheduled task run successful")
