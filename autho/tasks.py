from smtplib import SMTPException

from django.conf import settings

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from celery import shared_task


@shared_task
def send_mail_to_new_user(name, email):
    try:
        subject = "Subject"
        html_message = render_to_string(
            "welcome.html",
            {
                "name": name,
            },
        )
        plain_message = strip_tags(html_message)
        from_email = settings.DEFAULT_FROM_EMAIL
        to = email

        send_mail(subject, plain_message, from_email, [to], html_message=html_message)
    except SMTPException as e:
        print("There was an error sending an email: ", e)
