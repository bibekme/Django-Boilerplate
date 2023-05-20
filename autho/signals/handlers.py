from django.dispatch import receiver
from django.db.models.signals import post_save

from autho.models import User
from autho.tasks import send_mail_to_new_user


@receiver(post_save, sender=User)
def send_welcome_email_to_new_user(sender, instance, created, **kwargs):
    user = instance
    if created:
        send_mail_to_new_user.delay(user.name, user.email)
