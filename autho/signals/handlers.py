from django.dispatch import receiver
from django.db.models.signals import post_save

from autho.models import User

from common.utils import enqueue_email, get_project_name


@receiver(post_save, sender=User)
def send_welcome_email_to_new_user(sender, instance, created, **kwargs):
    user = instance
    if created:
        enqueue_email.delay(
            subject=f"Welcome to {get_project_name()}",
            email=user.email,
            message="hello",
        )
