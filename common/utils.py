import traceback
import os


from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.core.mail import mail_admins

from celery import shared_task
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@shared_task
def custom_mail_admins(subject, message):
    mail_admins(subject, message, fail_silently=True)
    return True


@shared_task
def enqueue_email(
    email,
    subject,
    message="",
    cc=[],
    bcc=[],
    subtype="text",
    fileobj=None,
    remove_file=True,
    from_email=None,
    html_data=None,
):
    try:
        if not isinstance(email, list):
            email = [email]

        if not from_email:
            from_email = settings.DEFAULT_FROM_EMAIL

        emailmessage = EmailMultiAlternatives(
            subject, message, from_email, email, cc=cc, bcc=bcc
        )

        if subtype == "html":
            emailmessage.content_subtype = "html"

        if html_data:
            emailmessage.attach_alternative(html_data, "text/html")

        if fileobj:
            if not isinstance(fileobj, list):
                fileobj = [fileobj]
            for obj in fileobj:
                fobj = open(obj["filepath"], "rb")
                emailmessage.attach(
                    obj["filename"], fobj.read(), obj.get("mimetype", "")
                )
                if remove_file:
                    os.remove(obj["filepath"])

        emailmessage.send()

    except Exception:
        admin_msg = "Subject: {}\nTo: {}\nFrom: {}\n{}".format(
            subject, email, from_email, traceback.format_exc()
        )
        custom_mail_admins.delay("Error Email Enqueue", admin_msg)
    return True


def get_project_name():
    return f"{settings.SITE_DISPLAY_SETTINGS.get('PROJECT_NAME')}"
