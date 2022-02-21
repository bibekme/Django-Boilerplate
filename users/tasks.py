from django.core.mail import BadHeaderError, send_mail
from templated_mail.mail import BaseEmailMessage
from celery import shared_task


@shared_task
def send_welcome_email(email_address, name):
    print(email_address)
    try:
        message = BaseEmailMessage(
            template_name="emails/welcome.html",
            context={
                "name": name,
            },
        )
        message.send([email_address])
    except BadHeaderError:
        pass


@shared_task
def say_hello(message):
    print("Hey")
