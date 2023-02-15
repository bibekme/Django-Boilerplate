from time import sleep

from celery import shared_task


@shared_task
def run_task():
    sleep(5)
    print("Scheduled task run successful")
