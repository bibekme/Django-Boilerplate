from smtplib import SMTPException

from django.conf import settings
from django.core.mail import send_mail
from celery import shared_task


@shared_task
def send_mail_to_new_user(name, email):
    try:
        send_mail(
            subject="Welcome to our app",
            message=f"Hello {name} welcome to our app. Enjoy",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
        )
    except SMTPException as e:
        print("There was an error sending an email: ", e)
